# 阅读报告:Roth (2024/2026) 对“CS 默认事件研究图处理前系数≈0 能否证明平行趋势”的回答

论文:Roth, *Interpreting Event-Studies from Recent Difference-in-Differences Methods*, arXiv:2401.12309v2(PDF 共 15 页;页码均为 PDF 页序,与论文打印页码一致)。

## 1. 一句话结论

**不能(有条件、较确定)。** 论文的核心点是:R `did` 默认的事件研究图,处理前系数(相邻期短差分)与处理后系数(相对基期长差分)构造不对称,不能按 TWFE 的目视经验解读,所以“处理前≈0”不足以写成“平行趋势得到验证、DID 设定有效”;论文建议改用 `base_period="universal"` 重画,并配合按队列的均值图、平衡样本和敏感性分析(推断 I1、事实 F6/F19/F26)。注意论文只在非交错、单次仿真中论证,交错设定需用户自行重跑(U1/U4)。

## 2. 适用性对照表

| 设定项 | 论文设定 | 我的设定 | 判断 | 依据 |
|---|---|---|---|---|
| 处理时点 | 共同(非交错)时点:所有处理单位 t=1 起处理(第 3 页、第 6–7 页) | 三批进入(2017/2020/2022) | 部分一致:论文明说结论在非交错设定下推出,交错情形仅有一般提示(构成变化) | F7,F12,F29,U1,I3 |
| 对照组 | 从未处理组(仿真中) | 从未处理组 | 一致(但论文未讨论 control_group 选项) | F8,U3 |
| 估计量/软件 | CS,R `did` 默认设置 | CS,R `did` 默认(版本未知) | 一致(版本/选项未知) | F10,F32,U3 |
| 证据类型与规模 | 一次仿真抽样 + 代数推导,100 个单位 | 约 280 处理 + 数千对照,真实数据 | 部分一致:仿真是例证,代数部分(共同时点)是一般性的,但不是在用户设定下验证 | F7,F13,F15 |
| 违反形态 | 线性趋势违反、无处理效应 | 违反形态未知 | 论文未覆盖(仅例子) | F8,I2 |
| 处理前系数构造 | 默认:相邻期短差分 | 默认选项,未调 base period | 一致 | F12,F13,F19 |
| 事件研究图用途 | 可作为研究设计有效性证据,但默认图不应按 TWFE 方式解读 | 想据此宣称“验证”平行趋势 | 不一致(论文提示不能这样解读) | F4,F6,F16,F17,I1 |
| 队列构成与构成变化 | 指出交错设定下构成随相对时期变化 | 未汇报队列构成 | 论文提示相关(论文给了建议,未对本样本计算) | F29,F30,F31,I4 |
| 敏感性分析 | Rambachan–Roth 类分析在默认不对称图上可能误导 | 未做 HonestDiD | 部分一致:论文给出方向,无 CS 交错步骤 | F18,F27,I5 |

## 3. 原文事实(F*)

**F1**(第 1 页)

> …the default plots produced by software for several of the most popular recent methods do not match those of traditional two-way fixed effects…

含义:摘要:若干主流新方法(含 CS)的软件默认事件研究图与传统 TWFE 事件研究图不一致(论文以非交错处理时点的简单设定论证)。

**F2**(第 1 页)

> …may show a kink or jump at the time of treatment even when the TWFE event-study shows a straight line…

含义:摘要:新方法的图可能在处理时点出现拐点/跳变,即使 TWFE 事件研究是一条直线。

**F3**(第 1 页)

> …visual heuristics for evaluating violations of parallel trends using TWFE event-study plots…

含义:摘要:原因是新方法对处理前系数与处理后系数的构造不对称;因此评估平行趋势违反的 TWFE 目视经验不应直接套用。

**F4**(第 2 页)

> …provide evidence about the validity of the research design…

含义:论文所说的事件研究图第二个用途:为研究设计的有效性提供证据,让读者做“目视推断”。

**F5**(第 2 页)

> …with the coefficient for the period directly before treatment typically normalized to zero…

含义:传统 TWFE 事件研究中,处理前一期的系数通常被标准化为零。

**F6**(第 2 页)

> …should not be interpreted in the same way as traditional dynamic TWFE…

含义:论文的核心论点:为评估平行趋势违反的目的,若干主流新方法的软件默认事件研究图不应按传统动态 TWFE 的方式解读。

**F7**(第 3 页)

> …Figure 1 shows event-studies for a single simulation draw from this DGP when there are 100 total units and half of them are treated…

含义:仿真设定:单次仿真抽样,100 个单位、一半被处理(Figure 1 的证据规模)。

**F8**(第 2 页)

> …there is no effect of the treatment but parallel trends is violated…

含义:仿真 DGP 中处理无效应但平行趋势被违反(处理组相对对照组线性上升)。

**F9**(第 3 页)

> …shows a clear kink at the treatment date…

含义:在该仿真(非交错设定)中,R 包 CS 的事件研究图在处理时点出现明显拐点。

**F10**(第 5 页)

> …using the default settings in the did package in R…

含义:Figure 1(b) 的 CS 结果使用 R did 包的默认设置。

**F11**(第 5 页)

> …the CS event-study plot has relatively flat pre-treatment coefficients and then exhibits a kink at the time of the treatment…

含义:在仿真中 CS 图处理前系数相对平坦,处理时点后出现拐点并向上倾斜(而 TWFE 图是一条连续的线性趋势)。

**F12**(第 7 页)

> …However, by default, the construction is asymmetric across the pre-treatment and post-treatment periods…

含义:第 3.2 节:CS 默认构造在处理前/后不对称(此处推导设定为共同处理时点)。

**F13**(第 8 页)

> …we compare outcomes in consecutive periods…

含义:CS 处理前系数比较相邻期(短差分),处理后系数比较相对处理前一期的长差分(共同处理时点设定)。

**F14**(第 8 页,公式,不手抄;同页锚点句:“Note that for pre-treatment coefficients…”):公式位置:共同处理时点下 CS 系数的分段定义(r<0 用相邻期差,r>=0 用相对基期差)。

**F15**(第 8 页)

> …so the population version of the CS event-study coefficients show a kink at zero…

含义:在仿真 DGP(线性违反)下,CS 系数的总体版本在零点处有拐点。

**F16**(第 9 页)

> …a kink or jump in the plot may arise even if there is no treatment effect and parallel trends is equally violated in all periods…

含义:论文的实践结论:拐点或跳变可能出现在无处理效应、且各期平行趋势违反程度相同的情形中。

**F17**(第 9 页)

> …One should therefore not apply the typical heuristics for visual inference…

含义:因此不应套用 TWFE 事件研究的通常目视经验(找处理时点的不连续/拐点)。

**F18**(第 9 页)

> …may likewise yield misleading conclusions given the asymmetric construction of the pre- and post-treatment coefficients…

含义:对这些事件研究系数比较处理前后系数的敏感性分析(如 Rambachan & Roth 2023)可能因不对称构造而得出误导结论。

**F19**(第 10 页)

> …always use the period before treatment as the baseline…

含义:论文对 CS 的修正建议:处理前系数也用长差分(始终以处理前一期为基期);did 包用 base_period="universal"。

**F20**(第 10 页)

> …in the did R and csdid Stata packages using the options base_period…

含义:did 包与 csdid(Stata)中实现该选项的方式(did: base_period 选项)。

**F21**(第 10 页)

> …the event-study estimates are numerically equivalent to the dynamic TWFE specification in the non-staggered setting considered here…

含义:使用该设置后,在论文考察的非交错设定中,CS 估计与动态 TWFE 数值等价。

**F22**(第 10 页)

> …long-run violations of parallel trends are easier to visualize using the universal-base option…

含义:脚注 9 转述 Callaway(2021)博文:长期平行趋势违反用 universal base 更易看出,但短差分可能更易发现预期效应(no anticipation)违反。

**F23**(第 10 页)

> …using short-differences may make it easier to detect violations of the no anticipation assumption…

含义:脚注 9 续:短差分可能更易发现违反无预期假设。

**F24**(第 11 页)

> …regarding pitfalls of simply looking at the significance of…

含义:脚注 14:Roth(2022)、Bilinski & Hatfield(2018) 讨论了仅看处理前系数显著性的陷阱。

**F25**(第 12 页)

> …researchers should ideally also look at the magnitudes of the pre-trends estimates and their confidence intervals…

含义:脚注 14 续:研究者还应看处理前趋势估计的大小及置信区间;但若处理前后系数构造不对称,评估潜在偏误的大小很困难。

**F26**(第 12 页)

> …report an event-study for a method that treats the periods completely symmetrically…

含义:论文建议:用对称处理各期的方法(如 did 包加上述选项)画图以目视评估平行趋势的合理性。

**F27**(第 12 页)

> …sensitivity analysis for these post-treatment estimates directly using the approach in Rambachan and Roth (2023)…

含义:论文提到可用 Rambachan & Roth (2023) 的方法对处理后估计量直接做敏感性分析;在交错设定下与插补估计量结合的做法见 Liu (2025)。

**F28**(第 12 页)

> …the discussion here does not threaten the validity of the post-treatment event-study estimates for recent methods…

含义:论文强调:新方法的处理后估计量在相应平行趋势假设成立时仍可解释;问题在于难以目视判断处理后系数能否由平行趋势违反解释。

**F29**(第 12 页)

> …the composition of units that contribute to an event-study coefficient will often change across different relative time periods…

含义:交错设定下,贡献于某相对时期系数的单位构成通常随相对时期变化。

**F30**(第 12 页)

> …supplement aggregated event-studies with plots of the time series of the mean outcome by adoption cohort…

含义:论文建议用按队列(adoption cohort)的结果均值时间序列图补充汇总事件研究图,以评估构成变化的重要性。

**F31**(第 13 页)

> …to units who are observed at least 3 periods before and after treatment…

含义:论文建议还可报告施加平衡性条件的汇总事件研究(如仅限处理前后至少各观测 3 期的单位)。

**F32**(第 5 页)

> …All packages were re-installed using the latest versions as of October 31, 2025…

含义:论文引用的软件版本:所有包使用截至 2025-10-31 的最新版本重装;用户的 did 版本未知。

## 4. 推断(I*)

**I1**(基于 F8, F11, F12, F13, F16, F17, F24):处理前系数贴近 0 不足以支撑“平行趋势得到验证、DID 设定有效”的写法。理由:(a) 论文说明默认 CS 图的处理前系数是相邻期短差分,处理后是长差分(F12,F13),并给出一个平行趋势明确被违反、处理无效应的仿真,其中 CS 处理前系数仍相对平坦(F8,F11);(b) 论文指出拐点/跳变可能由不对称构造产生,不应套用常规目视经验(F16,F17);(c) 论文引用的文献指出仅看处理前系数显著性有陷阱(F24)。注意:论文本身没有写“不能用‘验证’一词”或“平行趋势不可验证”,这一措辞建议是读者推断。

**I2**(基于 F7, F11, F13, F15):机制层面的解释(推断):默认 varying base 下,用户的处理前系数“≈0”只说明相邻两期之间处理组与对照组的差异变化很小;若存在每期很小的累积漂移 γ,处理前系数会是接近 γ 的平坦小值(可能被置信区间覆盖 0),而处理后长差分系数在论文的 DGP 中按 γ(r+1) 增长(F15)。因此 t+4、t+5 的显著性有可能部分来自累积漂移,单凭当前图无法排除。第 4 页 Figure 1(b) 的目视近似:Figure 1(b) 处理前系数多在约 0.5 附近、大多数置信区间覆盖或接近 0(目视近似,第 4 页,未经文本核验)。可能出错之处:论文是单次仿真(F7),共同处理时点,线性违反;用户的违反形态未知。

**I3**(基于 F12, F19, F21):论文推导与仿真均为共同(非交错)处理时点,论文对 CS 写“by default ... asymmetric”并指出 did 包可用 universal base(F12,F19),推断该非对称性在用户的三批交错设定中同样存在,但论文没有对交错情形做推导或仿真。对用户:需要用 base_period="universal" 重新估计才能得到可与 TWFE 式目视经验对照的图(F19,F21;F21 仅在非交错设定下证明了与 TWFE 等价)。

**I4**(基于 F29, F30, F31):用户设定的队列构成(推断):面板 2010–2024、三批 2017/2020/2022,若把进入年记作 t=0,则 t+5 只有 2017 队列能观测到(2020 队列最多到 t+4,2022 队列最多到 t+2)。因此用户图中 t+5 的系数只来自 2017 队列,t+4 只来自 2017 与 2020 两个队列,与 t=0~2(三个队列均贡献)的构成不同。论文说明构成会随相对时期变化并建议按队列画图和做平衡样本(F29,F30,F31),但没有针对本样本算过。前提:用户“进入年份”即首次处理年,且面板未因退市等缺失。

**I5**(基于 F18, F26, F27):HonestDiD 一类分析的使用方式(推断):论文提示对“默认不对称构造”的处理前/后系数直接做处理前后比较的敏感性分析可能误导(F18),并建议基于对称构造的图评估(F26)、对处理后估计量做敏感性分析(F27)。故若用户补做 HonestDiD,应基于 universal base 的 CS 结果,而不是默认图的系数。论文未给出针对 CS 交错设定的具体操作步骤。

可能出错之处汇总:所有推断都来自论文的共同时点推导/单次仿真外推;I4 的队列时间计算依赖“进入年=首次处理年”和面板无缺失;I2 里图中数值为目视近似,未经文本核验。论文未直接说这些,故不是事实。

## 5. 未知与后续阅读(U*)

**U1** 论文未对交错处理时点(用户为三批进入)推导或仿真 CS 默认图的不对称性具体如何影响处理前系数。
- 缺什么:论文推导与仿真均为共同处理时点;未涉及三批队列、从未处理对照组、数千家对照企业的规模
- 去哪查:Callaway and Sant'Anna (2021) (论文参考文献,第 13 页);Liu (2025) "Cohort-Anchored Robust Inference for Event-Study with Staggered Adoption"(论文参考文献,第 14 页)

**U2** 论文没有给出“处理前系数接近 0”在什么条件下足以支持平行趋势的检验功效或阈值标准。
- 缺什么:论文只说看处理前系数大小及置信区间(F25),未量化功效或可接受的偏误大小
- 去哪查:Roth (2022) "Pre-test with Caution"、Bilinski and Hatfield (2018)、Rambachan and Roth (2023)(均在论文参考文献,第 13–14 页)

**U3** 用户的 did 包版本、control_group(nevertreated/notyettreated)、anticipation 选项未知;论文第 7 页把 CS 描述为聚合“treated and not-yet-treated”比较,论文未讨论使用从未处理组作为对照时默认图是否有差异。
- 缺什么:论文引用 did 版本 2.1.2(第 13 页);未说明各版本默认选项是否改变;用户的版本和选项缺失
- 去哪查:Callaway (2021) 博文 "Universal vs. Varying Base Period in Event Studies"(论文参考文献,第 13 页);以及用户本机 did 包的帮助文档(查找建议,未确认内容)

**U4** 用户数据下改用 universal base 后处理前系数是否仍接近 0、t+4/t+5 是否仍显著,论文无法回答。
- 缺什么:需要用户用其数据重跑;论文只在 100 个单位的仿真中演示
- 去哪查:用户自行重跑 att_gt(base_period="universal") + aggte(type="dynamic");敏感性分析参考 Rambachan and Roth (2023)

**U5** 短差分图是否更有助于检验用户设定下的预期效应(no anticipation),论文仅转述 Callaway 的观点。
- 缺什么:论文未独立论证;用户的政策是否可能被预期未说明
- 去哪查:Callaway (2021) 博文(论文参考文献,第 13 页)

## 6. 下一步操作

1. (论文建议,F19/F20/F26)用 `att_gt(..., base_period="universal")` + `aggte(type="dynamic")` 重新估计并重画事件研究图;处理前系数以处理前一期为基准,作为评估平行趋势的图。注意 F21 的“与 TWFE 数值等价”只在论文的非交错设定下成立,你的交错设定下不能直接引用。
2. (论文建议,F30/F31)按队列(2017/2020/2022)画结果均值时间序列图,并报告施加平衡性条件的事件研究(例如只保留处理前后至少各观测 3 期的单位)。我的补充(I4):t+5 只有 2017 队列、t+4 只有 2017+2020 队列,需要在文中说明。
3. (论文提示,F18/F27;具体用法为我的建议 I5)补做 HonestDiD 敏感性分析,并基于 universal base 的结果做,而不是基于默认图系数;论文建议参考 Rambachan & Roth (2023) 与 Liu (2025) 对交错设定的做法(U1)。
4. (我的建议,I1)论文表述上不要写“验证了平行趋势/DID 有效”,改成“处理前系数未显示显著偏离,与平行趋势一致;敏感性分析表明…”,并同时报告处理前系数的大小和置信区间(F24/F25),而不是只看显著性。
5. (论文转述,F22/F23)若担心预期效应,可另外保留默认的短差分图作为补充,而不是替代;论文只转述了 Callaway 的看法(U5)。同时在文中写明 did 包版本与 control_group、anticipation 等选项(U3)。

## 7. 核验记录

- 脚本:`verify_quotes.py` 最终结果 total=42, pass=42, fail=0(fact 32、inference 5、unknown 5)。详见 `verify_report.json`。
- 修正:首次核验即全部通过;之后只改了 I2/I4 的措辞(I2 的“图 4”改为“第 4 页 Figure 1(b)”;I4 改为更准确的队列表述),并重跑,结果仍 42/42。
- 局限:脚本只核验引文逐字存在,不核验概括是否忠实;F1 引文因 PDF 断行,statement 为我对摘要的概括;图中数值只作目视近似(第 4、6 页已渲染并目视检查);论文版本日期为 2026-01-21(v2),本报告未联网核查更新。
- 本次未跑用户数据,未声称已重跑;用户 did 版本、control_group 选项未知,故结论对“默认选项”成立,选项不同时需复查(U3)。

## 8. 自检清单

- [x] 结论段回答了 question 本身。
- [x] 每条 fact 有页码+逐字引文(F14 为公式,给页码+锚点),verify_quotes.py 全部 PASS。
- [x] 没有把论文设定外的结论写成 fact。
- [x] 论文限定词(非交错、仿真、默认设置)已写入 statement 或适用性表。
- [x] 来自图的数字标了“目视近似”(I2)。
- [x] 每条 unknown 有 gap 与 next_reading;后续阅读仅指向论文参考文献条目或明示查找建议。
- [x] 区分了“论文建议”与“我的建议”。
- [x] 核验记录如实写了失败与重试(本次无 FAIL)。
