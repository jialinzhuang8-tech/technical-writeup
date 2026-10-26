# 案例 A 评分结果

按 A_acceptance.md 逐项评分,总分 30。引文核对以 paper_pages.txt 为准。

| 报告 | 总分 | R1-R6 | Q1-Q4 | G1-G3 | U1-U2 | 引文(逐字/总数) | 硬性扣分 |
|---|---|---|---|---|---|---|---|
| R1 | 28 | 2/2/2/2/2/1 | 2/2/2/2 | 2/2/1 | 2/2 | 24/24 | 无 |
| R2 | 29 | 2/2/2/2/2/2 | 2/2/2/2 | 2/2/1 | 2/2 | 26/26 | 无 |
| R3 | 24 | 2/2/2/2/2/2 | 2/1/1/1 | 1/2/1 | 1/2 | 12/14 | X1(混写): 第1节将自己的措辞建议归入'论文建议的做法' -> Q3、U1 上限 1 |
| R4 | 29 | 2/2/2/2/2/2 | 2/2/1/2 | 2/2/2 | 2/2 | 12/13 | X1(轻度): 【原文】栏内夹带解读与未标注推断 -> Q3 上限 1 |

## R1(总分 28)

**逐项依据**

- R1=2:F2/I1 明确'默认图处理前是短差分、处理后是长差分,不对称(p.7)',结论'不能…前期贴近0不能证明平行趋势'。
- R2=2:F4(p.2)'no effect of the treatment but parallel trends is violated…linear'+F6(p.5)CS 处理前平坦、处理时点 kink+F3 公式(p.8);明确是仿真/单次抽样(F5)。缺:未提 γ=0.5 与 TWFE 图呈直线的对照。
- R3=2:F11/F12(p.10)base_period="universal"/long2;F13 明确'仅在非 staggered 设定下'数值等价。
- R4=2:表格'论文非 staggered vs 用户 staggered'、F8(p.1)、F18/F19/F20(p.12)、U2 明确 F13 不外推到交错。
- R5=2:F16(p.12)'makes it challenging to visualize whether…'及含义'不否定适当平行趋势成立时处理后估计的有效性';I5 也区分。引文只截后半句,'does not threaten'未逐字引,但含义准确。
- R6=1:F17+I2 提到脚注14引 Roth 2022/Bilinski&Hatfield,并说'不要只看是否显著/接近0',但引文页码标 p.12(引用在 p.11),且没有明说'论文只是引用、未展开'。
- Q1=2:抽查 p.2/3/5/7/9/10/12/13 均与 PDF 页序一致,无错页。
- Q2=2:24 条英文引文全部逐字存在(含跨页 F21+F22 'restricted…to units…')。
- Q3=2:F/I/U 三分,每条 I 标依据与可能出错处;下一步逐条标【论文建议】/【我的建议】。
- Q4=2:p.4/p.6 图读数明确写'目视近似,未经文本核验,未用作 fact',并在 I2 重复标注。
- G1=2:适用性对照表覆盖估计量/软件选项/处理时点/对照组/违背形态/规模/修复/队列/敏感性。
- G2=2:U1/U3/I4:未知 base period 与版本、未报队列构成(含 t+4/t+5 构成推算)、未做 HonestDiD;U3 说明论文只指向 Rambachan-Roth 与 Liu(2025)。
- G3=1:后续阅读限于论文参考文献(CS2021、Liu2025、R&R2023、Roth2022、Bilinski、Callaway 博客),HonestDiD 包标'查找建议,未确认';但未明说'这些文献我未读过',未提 Li&Strezhnev。
- U1=2:6 步动作,逐条标【论文建议 F*】/【我的建议 I*】(universal 重画、措辞、队列均值图、HonestDiD)。
- U2=2:结论'有条件的确定';反复声明单次仿真、非 staggered、用户数据违背形态未知,不对用户图下定论。

**引文核对**:英文引文 24 条,逐字 24 条;未通过:无

抽查引文:
- 引文'by default, the construction is asymmetric…short-differences…long-differences' 在 p.7 找到
- 引文'a kink or jump in the plot may arise even if there is no treatment effect…' 在 p.9 找到
- 引文'always use the period before treatment as the baseline' 在 p.10 找到
- 引文'does not…'(F16 'makes it challenging to visualize…') 在 p.12 找到
- 引文'To assess the importance of changing composition…by adoption cohort' 在 p.12 找到
- 引文'to units who are observed at least 3 periods before and after treatment' 在 p.13 找到(F21 的前半在 p.12)
- 引文'Liu (2025) also discusses how these block biases…' 在 p.11 脚注11 找到

抽查页码:F2 p.7 ✓;F5 p.3 ✓;F6 p.5 ✓;F1 p.2 ✓;F8 p.1 ✓;参考文献 did 2.1.2 p.13 ✓;GitHub 代码脚注 p.3 ✓

**主要优点**
- 全文 24 条引文均逐字、页码全对;引文/推断/未知分类严格
- 对照表完整,队列构成 t+4/t+5 推算清楚
- 图读数明确标'目视近似,未经文本核验'

**主要缺陷**
- R6 未显式说明脚注14 仅为引用、未展开,页码标 p.12
- G3 未声明'未读过所引文献'
- R2 未提 γ=0.5 与 TWFE 直线对照

备注:R6 唯一扣分:未显式说明脚注14 仅引用而未展开,且页码标 p.12 而 Roth/Bilinski 引用在 p.11。未触发 X1–X4。

## R2(总分 29)

**逐项依据**

- R1=2:F5(p.7)+一句话结论'默认…处理前是相邻期短差分、处理后是长差分…处理前平坦不能当作平行趋势成立的证据'。
- R2=2:F3(p.2)'no effect of the treatment but parallel trends is violated'、F1(p.3)、F4(p.5)kink、F6(p.8)公式;反复标明'单次仿真'。缺:未提 γ=0.5 数值和 TWFE 直线对照。
- R3=2:F10/F11/F12(p.10):always use the period before treatment、base_period、非交错下与动态 TWFE 数值等价,并注明'论文未对交错设定做此断言'。
- R4=2:对照表 + I3:'论文只在非交错设定下证明与 TWFE 数值等价…用户的3批交错…论文没有给出';F16-F18(p.12)队列构成与分队列均值图。
- R5=2:F14(p.12)逐字'does not threaten the validity of the post-treatment…if the appropriate parallel trends assumption holds'+I7 区分。
- R6=2:F21(p.11)逐字引脚注14'Roth (2022) and Bilinski and Hatfield (2018) regarding pitfalls of simply looking at the significance of';F20/I6 说应看量级与置信区间;未编造其展开内容(但未明说'未展开')。
- Q1=2:抽查 p.2/3/5/7/10/11/12 均正确;脚注14 跨 p.11-12 按页分别引用,正确。
- Q2=2:26 条英文引文全部逐字(跨页处理为截断,F4 因连字符断行如实说明并改引)。
- Q3=2:F/I/U 三类;每条 I 写依据与'可能出错处';行动逐条标 论文建议 / 我的建议。
- Q4=2:明确'我没有从图中读取任何数值写入结论',图形仅引正文文字描述。
- G1=2:对照表 9 行(时点/对照组/估计量/默认图/违背形态/症状/样本规模/队列/敏感性)。
- G2=2:U1-U5/I4/I5:未调 base period(默认)、未报队列构成、未做敏感性;U2 明确论文仅在 BJS 处指向 Liu(2025)、R&R,没给 CS 做法。
- G3=1:后续阅读仅指向论文参考文献(Callaway 博客、R&R、Liu、Roth 2022、Bilinski),HonestDiD 包标为'查找建议,未确认存在';但未明说'这些文献未读过',未提 Li&Strezhnev。
- U1=2:5 步动作,逐条标注来源(论文建议 F10/F11、部分来自论文多数为我的建议 I5、我的建议 I6/I7)。
- U2=2:'有条件强度',所有论文证据标注为单次仿真+线性DGP,I2 明言'并不说明用户数据确有趋势违反'。

**引文核对**:英文引文 26 条,逐字 26 条;未通过:无

抽查引文:
- 引文'the pre-treatment coefficients are "short-differences"…' 在 p.7 找到
- 引文'One should therefore not apply the typical heuristics for visual inference' 在 p.9 找到
- 引文'Roth (2022) and Bilinski and Hatfield (2018) regarding pitfalls…' 在 p.11 找到
- 引文'evaluating the magnitudes of potential bias from pre-trends is challenging…' 在 p.12 找到
- 引文'All packages were re-installed using the latest versions as of October 31, 2025.' 在 p.5 找到
- 引文'provide evidence about the validity of the research design' 在 p.2 找到(跨 p.1-2 起句)

抽查页码:F1 p.3 ✓;F3 p.2 ✓;F6 p.8 ✓;F21 p.11 ✓;F25 p.5 ✓;Rambachan/Liu 参考文献 p.14 ✓;Callaway 博客脚注9 p.10 ✓

**主要优点**
- 26 条引文全逐字,页码全对,连字符断行问题如实处理
- 对照表 + 每条 I 注明'可能出错处'
- R6 引 p.11 脚注14 原文,行动逐条区分论文建议/我的建议

**主要缺陷**
- G3 未声明未读过所引文献
- R2 未提 γ=0.5 与 TWFE 直线对照
- 报告较长,但无加分

备注:总分最高(并列)。未触发 X1–X4。R2 的 TWFE 直线对照未写,影响不大。

## R3(总分 24)

**逐项依据**

- R1=2:第1节 + 表 C(p.7–8):处理前短差分、处理后长差分,默认设置下不能用 TWFE 方式'看'。
- R2=2:表 D:'真实处理效应为零,但…线性上升的趋势违背(γ=0.5)',CS 'relatively flat…kink'(p.5)、p.8 公式;表 A 提 TWFE 直线;明确是模拟。
- R3=2:表 F(p.10)universal + 非交错下与动态 TWFE 数值等价。
- R4=2:推断1:'论文只证明了非交错情形…我把 p.7–8 机制外推到交错…p.12 additional complications may arise'。
- R5=2:表 H(p.12)'does not threaten the validity of the post-treatment…'+说明问题在于难以判断。
- R6=2:结论2 + 表 G:脚注14 引 Roth 2022/Bilinski 指出'只看显著性有陷阱',应看量级和CI;未编造展开(未明说'未展开')。
- Q1=2:抽查 p.1/3/5/7/8/9/10/12-13 均正确。
- Q2=1:14 条英文引文中 2 条非逐字:(i)'do not match those of traditional TWFE event-studies' 原文为'traditional two-way fixed effects (TWFE) event-studies'(p.1),被改写后仍入引号;(ii)p.12 的'composition changes'为改写词而非原文用语。
- Q3=1:有'论文明确支持/我的推断/论文没覆盖'三节,但第1节把'措辞上改成…'列在'论文建议的做法'下,而第5节才承认措辞是自己建议;属 X1 混写,Q3 上限 1。
- Q4=1:'我也查看了 p.4 的图片:前期点平坦且在 0.5 上下'——有读图来源,但数值'0.5'以事实口吻给出,未标'目视近似'。
- G1=1:指出了非交错 vs 交错(推断1)与对照组类型(推断4),但没有逐项对照表;估计量/默认设置的一致性未单独检查。
- G2=2:'论文没覆盖'列出 HonestDiD 在交错 CS 上的操作、功效;推断 3 队列构成;默认 base period;并说明论文只指向 R&R2023 与 Liu2025。
- G3=1:只指向 Liu (2025)'需要读该文献',文献均真实,但未声明'未读过、待核实';未提 Li&Strezhnev、Callaway 博客作为阅读项(仅在正文提脚注9)。
- U1=1:动作具体(universal 重画、队列均值图、平衡版、HonestDiD、看CI),但第1节标题'论文建议的做法'混入自己的措辞建议、未逐条标来源,受 X1 影响上限 1。
- U2=2:第6节局限:单一 DGP、非交错,不应过度推广;'我无法确认用户数据就是这种情形'。

**引文核对**:英文引文 14 条,逐字 12 条;未通过:["'…do not match those of traditional TWFE event-studies'(原文含 two-way fixed effects (TWFE))", "'composition changes'(原文无此措辞)"]

抽查引文:
- 引文'construct the pre-treatment coefficients asymmetrically from the post-treatment coefficients' 在 p.1 找到
- 引文'typical heuristics for visual inference developed based on dynamic TWFE specifications will be misleading…' 在 p.3 找到
- 引文'researchers should ideally also look at the magnitudes…' 在 p.12 找到(页码标 p.11–12 合理)
- 引文'restricted to units who are observed at least 3 periods before and after treatment' 跨 p.12-13 找到
- 引文'do not match those of traditional TWFE event-studies' 未逐字找到
- 引文'composition changes' 未找到(改写)

抽查页码:B p.3 ✓;C p.7–8 ✓;E p.9 ✓;F p.10 ✓;I p.12–13 ✓;SA/Wooldridge p.5 ✓

**主要优点**
- 核心结论 R1–R6 均正确并带页码
- 明确区分'推断/论文没覆盖'并指出交错外推
- 给出措辞建议并声明为自己的

**主要缺陷**
- 'composition changes'及改写的摘要句仍放入引号
- 第1节把自己的措辞建议列在'论文建议的做法'下(混写)
- G1 无逐项对照,图读数'0.5 上下'未标目视近似,G3 未声明未读文献

备注:核心结论与 R1–R6 正确;失分来自引文改写、混写与对比/文献声明不足。

## R4(总分 29)

**逐项依据**

- R1=2:结论1:默认 CS 处理前短差分/处理后长差分不对称(p.7-8),不能按 TWFE 方式解读。
- R2=2:结论1 与表:'无处理效应…γ=0.5…处理前一条平的线…kink'(p.2-3,p.5,p.8);并说明 TWFE Fig.1a 是直线;标明是模拟。
- R3=2:表(p.10)universal + '非交错下数值等价';推断1 不外推。
- R4=2:推断1 + 未覆盖:'论文的数学与模拟都限定在非交错…推广到用户是我的推断';p.12 additional complications。
- R5=2:结论末段引 p.12 'does not threaten the validity of the post-treatment…if the appropriate parallel trends assumption holds'。
- R6=2:结论3:脚注14(p.11-12)指向 Roth 2022/Bilinski&Hatfield,'论文自己只给了这一条指引,没有展开'——明确诚实。
- Q1=2:抽查 p.2-3/5/7-8/9/10/12-13 均正确;'脚注11 在 p.12'为略模糊表述但文意不误。
- Q2=2:13 条英文引文12 条逐字;1 条把 'packages using' 缩写为 'package using'(省略号内的单复数微调),不算明显改写。
- Q3=1:有【原文】【推断】【未覆盖】标签,但【原文】栏内混入解读('看起来像一个真实的动态处理效应'、'弱证据'),表中'这意味着不能把默认 CS 图系数直接喂给 HonestDiD'亦为未标注推断;行动 1 把 universal 在交错下'和 TWFE 读法一致'写成无标注结论。按 X1 上限 1。
- Q4=2:'我看了图:约在0.5附近…'、'目视核对了 Fig.1',以'约'表述并声明为目视;边界情形。
- G1=2:推断1/3/5 分别对照交错 vs 非交错、默认设置、对照组(never vs not-yet),估计量一致隐含。
- G2=2:推断3(未调 base period)、推断4(队列构成,算出 t+4/t+5 贡献队列)、未覆盖(HonestDiD 操作,论文只指向 R&R2023 与 Liu2025)。
- G3=2:局限明示'未读被引文献(Liu 2025、Li & Strezhnev 2025、Rambachan & Roth 2023等),相关内容仅转述论文'。
- U1=2:6 步动作 + 页码;措辞明标'我的建议,非原文';来源区分基本清晰。
- U2=2:明说论文没说用户结果不对,不下定论;t+4/t+5 为'需重点排查';局限段说明仅单次模拟。

**引文核对**:英文引文 13 条,逐字 12 条;未通过:["'in the did R … package using the options base_period' 原文为 'packages using'(单复数微调,轻微)"]

抽查引文:
- 引文'a kink or jump in the plot may arise even if…' 在 p.9 找到
- 引文'Sensitivity analyses that compare the pre-treatment and post-treatment coefficients…' 在 p.9 找到
- 引文'event-study estimates are numerically equivalent to the dynamic TWFE specification in the non-staggered setting' 在 p.10 找到
- 引文'completely separate the testing and estimation steps' 在 p.11 找到
- 引文'supplement aggregated event-studies with plots of the time series of the mean outcome by adoption cohort…' 在 p.12-13 找到
- 引文'additional complications may arise' 在 p.12 找到

抽查页码:§3.2 not-yet-treated p.7 ✓;公式 p.8 ✓;脚注9 p.10 ✓;did 2.1.2 p.13 ✓;Fig.1(b) p.4 ✓

**主要优点**
- 有【原文】/【推断】/【未覆盖】标签,明确声明未读被引文献
- R6 明说脚注14 论文只给指引、未展开
- 队列贡献 t+4/t+5 的推算正确且标注为推断

**主要缺陷**
- 【原文】栏内夹带解读(如'看起来像真实动态效应'、'弱证据')及未标注推断
- 行动1 把 universal 在交错下'读法一致'写成无标注结论
- 1 条引文微改单复数

备注:与 R2 同为 29。若对 R4 的 Q3 不扣 X1 则为 30。

## 说明
- 引文核对采用归一化(去引号样式/断行连字符/空白)后的字符串匹配,并人工复查失败项(跨页续句如 'restricted… to units' 视为逐字)。
- 图读数(0.5 等)无法在文本中核实,仅按报告是否标注为目视读取评分。
- 边界判断:R4 的 Q3(X1 轻度)、Q4;R1/R2 的 G3 与 R3/R4 的差别。