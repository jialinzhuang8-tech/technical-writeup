#!/usr/bin/env python3
"""verify_quotes.py - 校验"论点-证据台账"(claims.json)里的每条原文引文是否真的出现在所标页码上。

用法:
  python verify_quotes.py claims.json pages.json [--out verify_report.json]

claims.json 结构见 SKILL.md。本脚本检查:
  * label=fact       : 必须有 page(int) 和 quote(>=12字符); quote 经规范化后须逐字出现在该页文本中。
                       若只出现在别的页, 报 WRONG_PAGE 并给出实际页码。公式类用 quote_type="formula" + anchor
                       (anchor 是同页紧邻公式的散文句, 同样须逐字出现)。
  * label=inference  : 必须有 based_on(引用已存在的 fact id) 且不能自带 quote。
  * label=unknown    : 必须有 gap(缺什么) 和 next_reading(去哪里核查; 未确认存在的材料要写成'查找建议')。
  * 所有 id 唯一; fact 的 page 不超范围。
退出码: 0 全部通过; 1 存在失败(未通过的论点不得写进结论)。
规范化(v1.1): NFKC + 统一引号 + 去断行连字符 + 压缩空白; 比较时两侧同时去掉全部连字符并转小写(只对连字符放宽,不做词序容错)。
"""
import argparse
import difflib
import json
import re
import sys
import unicodedata


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    s = re.sub(r"-\s*\n\s*", "", s)          # 行末断词连字符
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def cmp_key(s: str) -> str:
    """比较用键(v1.1)。页面文本与引文两侧使用同一规则: 去掉所有连字符/破折号并转小写。
    原因: PDF 常把 pre-treatment 断成 pre-/treatment, 提取后成 pretreatment; 引文若保留原连字符
    会被误判为 NOT_FOUND。两侧同规则后, 只在连字符上放宽, 其余字符仍须逐字一致。"""
    s = norm(s).lower()
    return re.sub(r"[-\u2010-\u2015\u2212]", "", s)


def near(quote_n: str, page_n: str):
    """给修正用的最近似片段(仅提示, 不算通过)。"""
    if not page_n:
        return None
    m = difflib.SequenceMatcher(None, quote_n[:200], page_n, autojunk=False)
    b = m.find_longest_match(0, min(len(quote_n), 200), 0, len(page_n))
    if b.size < 12:
        return None
    s = max(0, b.b - 20)
    return page_n[s:s + min(len(quote_n) + 40, 240)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("claims")
    ap.add_argument("pages")
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    data = json.load(open(a.claims, encoding="utf-8"))
    pages = json.load(open(a.pages, encoding="utf-8"))
    pn = {p["page"]: cmp_key(p["text"]) for p in pages}
    n_pages = len(pages)
    claims = data.get("claims", data) if isinstance(data, dict) else data

    results, ids, fact_ids = [], set(), set()
    for c in claims:
        if c.get("label") == "fact" and c.get("id"):
            fact_ids.add(c["id"])

    for c in claims:
        cid, label = c.get("id"), c.get("label")
        r = {"id": cid, "label": label, "status": "PASS", "problems": []}
        if not cid or cid in ids:
            r["problems"].append("id 缺失或重复")
        ids.add(cid)
        if label not in ("fact", "inference", "unknown"):
            r["problems"].append("label 必须是 fact/inference/unknown")
        if not str(c.get("statement", "")).strip():
            r["problems"].append("statement 为空")

        if label == "fact":
            page = c.get("page")
            if not isinstance(page, int) or not 1 <= page <= n_pages:
                r["problems"].append(f"page 非法: {page!r} (范围 1..{n_pages})")
            else:
                is_formula = c.get("quote_type") == "formula"
                text = c.get("anchor") if is_formula else c.get("quote")
                if not text or len(norm(text)) < 12:
                    r["problems"].append("quote(或公式的 anchor)缺失或少于12字符")
                else:
                    q = cmp_key(text)
                    if q in pn[page]:
                        r["verified_on_page"] = page
                    else:
                        other = [k for k, v in pn.items() if q in v]
                        if other:
                            r["problems"].append(f"WRONG_PAGE: 引文实际在 p.{other}, 而非 p.{page}")
                        else:
                            r["problems"].append("NOT_FOUND: 引文未逐字出现在任何页")
                            hint = near(q, pn[page])
                            if hint:
                                r["nearest_on_cited_page"] = hint
        elif label == "inference":
            based = c.get("based_on")
            if not based or not isinstance(based, list):
                r["problems"].append("inference 必须列出 based_on(fact id 列表)")
            else:
                miss = [b for b in based if b not in fact_ids]
                if miss:
                    r["problems"].append(f"based_on 引用了不存在的 fact: {miss}")
            if c.get("quote"):
                r["problems"].append("inference 不得自带 quote(推断不是原文)")
        elif label == "unknown":
            if not str(c.get("gap", "")).strip():
                r["problems"].append("unknown 必须写 gap(缺什么信息)")
            if not str(c.get("next_reading", "")).strip():
                r["problems"].append("unknown 必须写 next_reading(去哪里核查; 未确认存在的材料写成查找建议)")

        if r["problems"]:
            r["status"] = "FAIL"
        results.append(r)

    summary = {
        "total": len(results),
        "pass": sum(r["status"] == "PASS" for r in results),
        "fail": sum(r["status"] == "FAIL" for r in results),
        "by_label": {k: sum(1 for r in results if r["label"] == k) for k in ("fact", "inference", "unknown")},
    }
    report = {"summary": summary, "results": results}
    if a.out:
        json.dump(report, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False))
    for r in results:
        if r["status"] == "FAIL":
            print(f"[FAIL] {r['id']}: " + "; ".join(r["problems"]))
            if r.get("nearest_on_cited_page"):
                print(f"       最近似原文: {r['nearest_on_cited_page']}")
    sys.exit(0 if summary["fail"] == 0 else 1)


if __name__ == "__main__":
    main()
