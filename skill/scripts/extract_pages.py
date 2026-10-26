#!/usr/bin/env python3
"""extract_pages.py - 把论文 PDF 拆成"带页码的文本"，并诊断哪些页的内容不在文本里。

用法:
  python extract_pages.py paper.pdf --out work/ [--render 3,4] [--dpi 110]

产物(都写在 --out 下):
  pages.json          [{"page":1,"text":"...","n_chars":N,"n_images":K}, ...]  (页码 = PDF 页序, 从1开始)
  pages.txt           人读版, 每页以 =====[PDF page N]===== 开头
  extract_report.json 诊断: 无文本页 / 疑似图表页 / 乱码比例 / 打印页码与PDF页序的差异线索
  page_N.png          仅在 --render 指定时生成, 供目视读图

退出码: 0 = 文本层可用; 3 = 整篇没有可用文本层(扫描件/图片PDF), 此时不得声称"已逐字核验"。
依赖: PyMuPDF (pip install pymupdf)。
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

try:
    import pymupdf  # PyMuPDF >= 1.24
except ImportError:  # 旧版导入名
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit("需要 PyMuPDF: pip install pymupdf")

FIG_HINT = re.compile(r"^\s*(Figure|Fig\.|Table)\s*[A-Z]?\d+", re.I | re.M)


def garble_ratio(text: str) -> float:
    """非字母数字/常见标点的字符占比, 用于识别乱码或公式碎片。"""
    if not text:
        return 1.0
    bad = 0
    for ch in text:
        cat = unicodedata.category(ch)
        if ch.isspace() or cat[0] in "LN" or ch in ".,;:()[]{}%-–—'\"“”‘’/&+=<>*?!":
            continue
        bad += 1
    return bad / len(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out", required=True)
    ap.add_argument("--render", default="", help="逗号分隔的PDF页序, 渲染成PNG")
    ap.add_argument("--dpi", type=int, default=110)
    a = ap.parse_args()

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(a.pdf)
    pages, no_text, figure_like, garbled = [], [], [], []
    for i, pg in enumerate(doc):
        text = pg.get_text()
        n_img = len(pg.get_images())
        pages.append({"page": i + 1, "text": text, "n_chars": len(text), "n_images": n_img})
        if len(text.strip()) < 30:
            no_text.append(i + 1)
        if n_img > 0 and len(text.strip()) < 400:
            figure_like.append(i + 1)
        elif FIG_HINT.search(text) and n_img > 0:
            figure_like.append(i + 1)
        if text.strip() and garble_ratio(text) > 0.35:
            garbled.append(i + 1)

    (out / "pages.json").write_text(json.dumps(pages, ensure_ascii=False), encoding="utf-8")
    (out / "pages.txt").write_text(
        "".join(f"\n\n=====[PDF page {p['page']}]=====\n{p['text']}" for p in pages), encoding="utf-8")

    n = len(pages)
    usable = n - len(no_text)
    report = {
        "pdf": str(a.pdf),
        "n_pages": n,
        "pages_without_text": no_text,
        "pages_figure_like": sorted(set(figure_like)),
        "pages_garbled": garbled,
        "text_layer_ok": usable >= max(1, int(0.5 * n)),
        "notes": [
            "pages_figure_like 的图内容不在文本里: 图上的数值/形状只能目视读取, 且必须标注为'目视近似, 未经文本核验'。",
            "公式区域常被拆成逐字符行, 无法逐字引用: 公式只给页码+邻近散文锚点, 不要手抄公式当原文引文。",
            "页码以 PDF 页序为准; 若与论文打印页码不同, 在报告中同时注明。",
        ],
    }
    (out / "extract_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    for tok in [t for t in a.render.split(",") if t.strip()]:
        k = int(tok)
        if 1 <= k <= n:
            doc[k - 1].get_pixmap(dpi=a.dpi).save(str(out / f"page_{k}.png"))

    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report["text_layer_ok"] else 3)


if __name__ == "__main__":
    main()
