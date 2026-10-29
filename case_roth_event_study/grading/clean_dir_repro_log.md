# README 复现日志(案例 A,with-Skill)

约束:只使用 /tmp/bohr_v11/clean-repro 内文件,不联网。Python 解释器:`/Users/zjlinnn/.workbuddy/binaries/python/envs/default/bin/python`(3.13.12,PyMuPDF 1.28.0)。

## ④ 时间
- 开始:2026-10-28 17:13:27
- 结束:约 2026-10-28 17:16:23 之后(这是最后一次成功执行 `date '+%F %T'` 的时间,此时产物已全部生成;随后写 repro_log.md 时 Bash 工具报 "session already exists" 无法再取时间,所以没有精确的结束时刻)

## ① 按 README 执行的步骤、命令、结果

### 步骤 0:读 README
`cat pkg/README.md`。关键两节:"3. 如何调用"和"5. 复现一次 A 对照"。

### 步骤 1:按 README §5 建工作目录并放入 PDF / 任务 / skill
README 原命令(假定当前目录下有 `../materials`、`../cases`、`../skill`):
```bash
mkdir r && cd r && mkdir input out && cp ../materials/A/roth_2401.12309v2.pdf input/ && cp ../cases/A_task.md task.md && cp -R ../skill skill
```
- 第一次:在 `clean-repro/run/` 下原样执行,**失败**:`cp: ../materials/A/roth_2401.12309v2.pdf: No such file or directory`(exit=1)。原因见缺口 1。
- 补救:删除失败留下的 `run/r/`,改为以 `run/` 本身作为干净工作目录,把 `../` 换成 `../pkg/`:
```bash
cd /tmp/bohr_v11/clean-repro/run && mkdir input out \
 && cp ../pkg/materials/A/roth_2401.12309v2.pdf input/ \
 && cp ../pkg/cases/A_task.md task.md && cp -R ../pkg/skill skill
```
- 结果:`run/` 下有 `input/ out/ skill/ task.md`,成功。

### 步骤 2:读 skill/SKILL.md,按 Step 0–7 执行
- Step 0:根据 `task.md` 写出 question、my_setting(已知项/缺项),缺项(did 版本、control_group、置信区间宽度等)在 claims.json 中列出。
- Step 1(README §3 第 2 条命令):
```bash
python skill/scripts/extract_pages.py input/roth_2401.12309v2.pdf --out out/work/ --render 5
```
  README 的 `paper.pdf`/`<图表页>` 为占位符,我替换了实际文件名;`--render 5` 是我随手试的(缺口 4)。输出:`n_pages=15`,`text_layer_ok=true`,`pages_figure_like=[4,6]`,退出码 0。随后重跑 `--render 4,6`,得到 `page_4.png`、`page_6.png`(并保留了 `page_5.png`),目视读取图 1、图 2。
- Step 2–4:通读 `out/work/pages.txt`(全部 15 页),手写 `out/claims.json`:23 条 fact、5 条 inference、5 条 unknown。
- Step 5(README §3 第 2 条命令第三行):
```bash
python skill/scripts/verify_quotes.py out/claims.json out/work/pages.json --out out/verify_report.json
```
  输出 `{"total": 33, "pass": 33, "fail": 0, ...}`,退出码 0(一次通过,无需修引文)。
- Step 6–7:写 `out/report.md`(按 SKILL.md 第 6 节结构并含自检清单)。

### 步骤 3:README §3 第 3 条
verify 退出码 0,符合"所有引文逐字出现在所标页"。

## ⑤ 最终产物位置
`/tmp/bohr_v11/clean-repro/run/out/`:
- `report.md`、`claims.json`、`verify_report.json`
- `work/`:`pages.json`、`pages.txt`、`extract_report.json`、`page_4.png`、`page_5.png`、`page_6.png`
- 工作目录其余:`run/input/`、`run/skill/`、`run/task.md`

结论:能按 README + SKILL.md 跑通到 verify 全 PASS,但需要自己补做/猜测下列事项。

## ② README 没写清楚、我不得不自己猜或补做的步骤(最重要)

1. **命令的执行目录没写。** §5 的 `cp ../materials/...` 只有在"当前目录就是 `materials/`、`cases/`、`skill/` 的同级目录"时才成立。README 没说这个前提;包解开后 `README.md` 与这三者同在 `pkg/` 下,我在 `run/` 下执行会失败,必须自己改成 `../pkg/...` 或先 cd 到 `pkg/`。此外,用户要求"在 run/ 下建新目录",而 README 的 `mkdir r && cd r` 会把 `r` 建在包目录里,与"另建干净目录"的意图有冲突,要自己决定放哪。
2. **`--render <图表页>` 没说怎么知道页码。** README 没说先不带 render 跑一次看 `extract_report.json` 的 `pages_figure_like` 再选页,我是试错后才知道应渲染 4、6 页(第一次随手填的 5 页并不是图页)。
3. **`paper.pdf` 与实际文件名 / 路径对不上。** §3 命令写 `paper.pdf`,而 §5 把 PDF 放在 `input/roth_2401.12309v2.pdf`,两节的路径约定不一致,我自己替换。
4. **question / my_setting 放哪、怎么写没说。** §3 第 1 步说"写下 question、my_setting",§5 却只是把 `A_task.md` 拷成 `task.md`,没说是否要另写文件、claims.json 的 `question`/`my_setting` 字段怎么从 task.md 里提。我自行把 task.md 内容整理进 claims.json。
5. **"让 Agent 读取 SKILL.md 并按其 Step 0–7 执行"过于笼统。** README 没给 claims.json 的格式、`report.md` 的结构、fact/inference/unknown 的规则,全靠读 SKILL.md(SKILL.md 里有,但 README 没指路到具体章节);"Agent 阅读全文并写 claims.json"这一步没有任何可执行命令,是整个流程的主要人工/Agent 工作量,README 没说明。
6. **Python 解释器与依赖。** README 命令用 `python`,没说 `python` 指哪个、如何确认已装 PyMuPDF(只在 §2 提了 `pip install pymupdf`);本次由任务给定解释器,我把 `python` 手动替换成绝对路径。
7. **验收步骤缺材料。** §5 说"按 `cases/A_acceptance.md` 逐项评分",但 `pkg/cases/` 里只有 `A_task.md`、`B_task.md`、`C_task.md`,**没有任何 acceptance 文件**,所以无法自评是否"跑对"。README 也没给"跑通"的客观判据,我只能用"脚本 fail=0 且产物齐全"自行定义。
8. **"锁定版本 v1.0.0、哈希前 12 位 ba27d1047953"无法核对。** README 没说哈希算法、对哪些文件/怎么拼接。我试了 sha256/sha1/md5 对"排序后各文件 cat 拼接"以及"各文件哈希再哈希",得到 `d36d008e…`、`460bfd00…`、`578ce6c1…`、`1d5b753f…`、`c427d89…`(pkg 内)等,**均不以 `ba27d1047953` 开头**。我无法验证字节一致声明。
9. **输出目录 `out/` 的预创建。** README §5 创建了 `out/`,§3 又让脚本写 `out/work/`;脚本会自动建目录,但 README 没说 `report.md`/`claims.json` 应放 `out/` 还是别处,我按 SKILL.md 第 3 节放 `out/`。
10. **`materials/A/*.pages.txt` 的用途没说。** README 只说是"带页码文本",没说复现时是否使用、能否替代 extract_pages.py。我没有使用它做证据(只在末尾比对了开头几行,与我生成的 pages.txt 开头一致)。
11. **耗时记录。** SKILL.md 报告第 7 节要求写"耗时/人工介入",README 说耗时见 `report.md` 第 5 节,但包里没有那个 `report.md`,我只能在本日志里写时间。
12. **如何判断"做对了"/评分基线缺失**:没有 with / without 的对照、没有冻结验收标准可对,复现只能验证"流程能跑通",不能验证"结果质量"。

## ③ README 写错 / 对不上的地方
1. **§4 目录结构与实际包不符。** 列出 `report.md manifest.json review.json`、`runs/<run-id>/`、`grading/`,以及 `cases/` 下"运行前冻结的验收标准"。实际 `pkg/` 只有 `README.md`、`skill/`、`materials/`、`cases/`(其中仅 `*_task.md`);上述其余项均不存在。`§5` 引用的 `cases/A_acceptance.md` 也不存在。
2. **§5 的相对路径 `../materials/...` 在包的实际布局下不成立**(见缺口 1,实测报错)。
3. **版本号不一致。** README 标题与"锁定版本"为 `v1.0.0`;`skill/SKILL.md` frontmatter 为 `version: 1.1.0`,`verify_quotes.py` 文档串也写"规范化(v1.1)"。README 却声称"全部 with-Skill 运行均用此版本"。
4. **哈希值对不上**(见缺口 8,无法复现 `ba27d1047953`)。
5. **§3 的命令 `python skill/scripts/…` 与 SKILL.md Step 1/5 的 `python scripts/…` 写法不同**,后者要求在 `skill/` 目录内执行;两处路径约定不一致(我按 README 的写法在工作目录根下执行,可用)。
6. §3 中 `paper.pdf` 与 §5 `input/roth_2401.12309v2.pdf` 对不上(见缺口 3)。
7. README 称"Python 3.13.12";本机恰为 3.13.12,这一条是对得上的。

## 备注(执行者自述的局限)
- report.md 的 statement 由我自己读,无第三方复核;脚本只验证引文逐字存在。
- F20 原句跨 p.12–13,仅引 p.12 内的连续片段。
- 论文外文献(Liu 2025 等)未读,报告中均按 unknown/查找建议处理。
