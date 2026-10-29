# 阅读报告:默认 did 事件研究图处理前系数≈0,能否写"平行趋势得到验证"?

论文:Roth, J., *Interpreting Event-Studies from Recent Difference-in-Differences Methods*, arXiv:2401.12309v2(版本日期 2026-01-21)。页码均为 PDF 页序(与打印页码一致,共15页)。

## 1. 一句话结论

**不能。**(有条件强度)论文显示,默认设置的 CS 事件研究图处理前系数是相邻期短差分、处理后是长差分,二者构造不对称,处理前"平坦"不能当作平行趋势成立的证据(F5、F7、I1);建议改用 `base_period="universal"` 重画,并补充分队列均值图与构成检验(F10、F15、F17)。论文只在非交错、单次仿真下证明这点,用户的交错设定属推断(I3)。

## 2. 适用性对照表

| 设定项 | 论文设定 | 我的设定 | 判断 | 依据 |
| --- | --- | --- | --- | --- |
| 处理时点 | 仿真与推导均为非交错(common timing),处理从 t=1 开始 | 3 批交错进入(2017/2020/2022) | 部分一致(机制可迁移,数值性质未证) | F1, F2, F5, F12, I3, U1 |
| 对照组 | 从不处理组(仿真);CS 描述为处理组与 not-yet-treated 比较 | 从未处理组数千家 | 部分一致 | F23, U5 |
| 估计量/软件 | CS,R `did` 默认设置 | CS,R `did` 默认设置 | 一致(版本需核对) | F4, F5, F25, U5 |
| 默认图构造 | 处理前短差分、处理后长差分 | 用户未改 base period,即默认 | 一致 | F5, F6 |
| 趋势违反形态 | 线性趋势违反,无处理效应(单次仿真,100 单位) | 未知;真实数据的违反形式未知 | 论文未覆盖 | F1, F2, F3, I2 |
| 图形症状 | 处理前相对平坦,处理时点出现拐折,此后上升 | 处理前4期≈0,t+4、t+5 显著 | 定性相容,不能互证 | F4, F26, I2 |
| 样本规模 | 100 单位,一半处理 | 约280处理 + 数千对照 | 论文未覆盖(功效问题) | F2, U4 |
| 队列构成 | 单一队列 | 三批队列,构成未汇报 | 部分一致(论文提示构成会随相对时间变化) | F16, F17, I4, U3 |
| 敏感性分析 | 提及 Rambachan-Roth;对默认不对称图可能误导 | 未做 HonestDiD | 论文未覆盖 CS 交错的具体做法 | F9, F22, F24, I5, U2 |

## 3. 原文事实(F*)

**F1**(PDF p.3)
> However, parallel trends is violated: the treated group's outcome increases linearly relative to the control group's outcome in all periods

含义:论文的核心仿真设定(单次仿真抽样、非交错处理时点):处理组结果相对对照组线性上升,即平行趋势被违反。

**F2**(PDF p.3)
> Figure 1 shows event-studies for a single simulation draw from this DGP when there are 100 total units and half of them are treated.

含义:图1对应的仿真规模:单次仿真抽样,100个单位、一半为处理组;处理时点非交错。

**F3**(PDF p.2)
> there is no effect of the treatment but parallel trends is violated

含义:在该仿真中处理无效应但平行趋势被违反。

**F4**(PDF p.5)
> then exhibits a kink at the time of the treatment, sloping upwards afterwards.

含义:在上述仿真中,使用 R did 包默认设置的 CS 事件研究图(图1b):处理前系数相对平坦,处理时点出现拐折(kink),此后向上倾斜。

**F5**(PDF p.7)
> the pre-treatment coefficients are "short-differences", i.e. comparisons of consecutive periods, whereas the post-treatment coefficients are "long-differences", i.e. comparisons relative to the period before treatment.

含义:CS 默认构造在处理前与处理后是不对称的:处理前系数是相邻期的短差分(short-differences),处理后系数是相对处理前一期的长差分(long-differences)。(论文第3.2节,非交错时点设定下的推导)

**F6**(PDF p.8)
> [公式] 锚点句: so the population version of the CS event-study coefficients show a kink at zero

含义:在论文仿真 DGP 下 CS 总体事件研究系数的公式:r<0 时为常数 gamma,r>=0 时为 gamma*(r+1),故若 gamma 不为 0 则在 0 处出现拐折。(公式不手抄,见同页 anchor)

**F7**(PDF p.9)
> a kink or jump in the plot may arise even if there is no treatment effect and parallel trends is equally violated in all periods

含义:论文的实践结论:由于处理前/后系数构造不对称,即使无处理效应且平行趋势在所有期被同等程度违反,图上也可能出现拐折或跳变。(针对 CS、BJS 等默认事件研究图)

**F8**(PDF p.9)
> One should therefore not apply the typical heuristics for visual inference

含义:论文主张不应对这些方法的默认图套用 TWFE 事件研究的常见目视判断(如找处理时点的断点/拐折)。

**F9**(PDF p.9)
> Sensitivity analyses that compare the pre-treatment and post-treatment coefficients from these event-studies (e.g. Manski and Pepper, 2018; Rambachan and Roth, 2023) may likewise yield misleading conclusions

含义:论文指出:比较这类事件研究图处理前与处理后系数的敏感性分析(如 Rambachan and Roth, 2023)在处理前/后系数构造不对称时,可能得出误导性结论。

**F10**(PDF p.10)
> always use the period before treatment as the baseline

含义:论文对 CS 的修正建议:处理前系数也使用长差分,即始终以处理前一期为基准。

**F11**(PDF p.10)
> This can be implemented, for example, in the did R and csdid Stata packages using the options base_period

含义:该修正在 did(R) 中通过 base_period 选项(论文写作 base_period = "universal")实现;在 csdid(Stata) 中用 long2。

**F12**(PDF p.10)
> Using these settings, the event-study estimates are numerically equivalent to the dynamic TWFE specification in the non-staggered setting considered here.

含义:论文称:使用这些设置后,CS 事件研究估计在论文所考虑的非交错时点设定下与动态 TWFE 数值等价(论文未对交错设定做此断言)。

**F13**(PDF p.10)
> he concludes that long-run violations of parallel trends are easier to visualize using the universal-base option

含义:脚注9转述 Callaway(2021) 博客:用 universal 基期更易可视化长期平行趋势违反;用短差分可能更易发现无预期假设的违反。

**F14**(PDF p.12)
> the discussion here does not threaten the validity of the post-treatment event-study estimates for recent methods if the appropriate parallel trends assumption holds

含义:论文强调上述讨论不威胁处理后事件研究估计的有效性——前提是相应的平行趋势假设成立。

**F15**(PDF p.12)
> report an event-study for a method that treats the periods completely symmetrically (e.g. using the did package with the options described above) to visually evaluate the plausibility of the parallel trends assumption

含义:论文建议:用对处理前后期完全对称处理的方法(如按上述选项设置的 did 包)报告事件研究,以目视评估平行趋势的"合理性(plausibility)"。

**F16**(PDF p.12)
> the composition of units that contribute to an event-study coefficient will often change across different relative time periods

含义:论文指出在交错设定中,对事件研究系数有贡献的单位构成通常随相对时间变化。

**F17**(PDF p.12)
> it will often be useful to supplement aggregated event-studies with plots of the time series of the mean outcome by adoption cohort

含义:论文建议用各采纳队列(adoption cohort)的结果均值时间序列图来补充汇总的事件研究图。

**F18**(PDF p.12)
> studies that enforce some balancing criteria

含义:论文还建议报告施加平衡性标准的汇总事件研究(示例:限定为处理前后至少观察3期的单位;该示例句跨 p.12-13,此处引文取 p.12 部分)。

**F19**(PDF p.2)
> provide evidence about the validity of the research design

含义:事件研究图的第二个用途是提供关于研究设计有效性的"证据"(evidence),并非证明。

**F20**(PDF p.12)
> researchers should ideally also look at the magnitudes of the pre-trends estimates and their confidence intervals

含义:脚注14(跨页,此为 p.12 部分):论文称研究者最好还应查看处理前趋势估计的量级及其置信区间。

**F21**(PDF p.11)
> Roth (2022) and Bilinski and Hatfield (2018) regarding pitfalls of simply looking at the significance of

含义:脚注14(p.11 部分)指向 Roth(2022) 与 Bilinski and Hatfield(2018),讨论仅看处理前系数显著性(的陷阱)。

**F22**(PDF p.12)
> evaluating the magnitudes of potential bias from pre-trends is challenging if the pre-treatment and post-treatment coefficients are not constructed symmetrically

含义:脚注14(p.12 部分):处理前、后系数构造不对称时,评估由处理前趋势带来的潜在偏误的量级是困难的。

**F23**(PDF p.7)
> CS constructs event-studies by aggregating DiD comparisons of treated and not-yet-treated units

含义:论文说明其 CS 比较是处理组与尚未处理(not-yet-treated)单位的汇总(第3.2节描述)。

**F24**(PDF p.12)
> One can also conduct sensitivity analysis for these post-treatment estimates directly using the approach in Rambachan and Roth (2023)

含义:论文对 BJS 类估计量指出:可对处理后估计直接做 Rambachan-Roth 敏感性分析,交错设定下的实施见 Liu (2025)(该句语境是 BJS 等插补估计量,不是 CS)。

**F26**(PDF p.5)
> the CS event-study plot has relatively flat

含义:F4 的前半句:在上述单次仿真(非交错、无处理效应、线性趋势违反)中,默认 CS 事件研究图的处理前系数"相对平坦"(引文截止于断行连字符前,因 PDF 在 pre-/treatment 处断行,脚本会去掉连字符导致整句无法匹配)。

**F25**(PDF p.5)
> All packages were re-installed using the latest versions as of October 31, 2025.

含义:论文结果对应的软件版本:所有包均重新安装为截至 2025-10-31 的最新版(参考文献列 did 2.1.2)。

## 4. 推断(I*)

以下均为由 F* 推出、论文没有明说的内容,不含引文。

**I1**(依据:F1, F2, F4, F26, F5, F6, F7)

处理前系数贴近 0 不能作为"平行趋势得到验证"的依据。默认 CS 的处理前系数是相邻期短差分(F5),在论文的线性违反仿真中仍呈"相对平坦"(F4、F6),而图上拐折可在平行趋势被违反时出现(F7)。因此默认图的"处理前平坦+处理后上升"形态,不能与"线性漂移(趋势违反)"区分开。可能出错处:该结论的直接证据只来自论文的一次仿真(F2)与一个线性DGP(F1),用户真实数据的违反形式(非线性、仅在某些队列)可能不同。

**I2**(依据:F3, F4, F26, F6)

用户的图(处理前4期近0、t+4/t+5显著)与论文 CS 仿真中"线性趋势违反而无处理效应"产生的形态在定性上相容(F3、F4、F6):在论文DGP中处理后系数为 gamma*(r+1),随 r 增大而变大,故晚期系数最易显著。这只说明用户的图无法排除该解释,并不说明用户数据确有趋势违反。

**I3**(依据:F5, F6, F10, F11, F12)

论文推荐的改图办法(universal 基期、处理前同样用长差分,F10-F11)会使处理前系数与处理后系数同口径地相对 t-1 比较;若存在线性漂移,处理前系数应呈现斜率而不是平坦(由F5、F6的差分构造反推)。因此建议用 base_period="universal" 重画并与默认图并列。可能出错处:论文只在非交错设定下证明与 TWFE 数值等价(F12),用户的3批交错+从未处理设定下的性质论文没有给出。

**I4**(依据:F16, F17, F18)

按用户设定(面板至2024年、队列为2017/2020/2022,假设为年度数据且进入年即首个处理年),相对时间 t+4 仅能由2017与2020队列贡献,t+5 仅由2017队列贡献,2022队列最多观察到 t+2;处理前4期则三批队列均可贡献。依据论文关于构成随相对时间变化的提示(F16),用户图上晚期显著的系数很可能主要由最早进入的队列驱动,与处理前系数的样本构成不同。这是由用户设定算出的推断,论文本身没有讨论用户的数据。年份推算依赖用户的数据频率与进入年定义。

**I5**(依据:F9, F22, F24, F10)

论文警告对默认的不对称图做"前后系数比较型"敏感性分析可能误导(F9、F22),并只明确建议在 BJS 类估计量下对处理后估计做 Rambachan-Roth 分析(F24)。因此用户若补做 HonestDiD 类分析,不应直接基于默认 CS 事件研究的处理前系数;宜先改为 universal 基期再做,并核实其对 CS 交错设定的适用实现。论文未就 CS 交错设定给出具体做法。

**I6**(依据:F15, F19, F20, F21)

写作措辞:论文把事件研究图定位为"证据"(F19),把处理前图用于评估平行趋势的"合理性"(F15),并提醒不能只看处理前系数显著性、应看量级与置信区间(F20、F21)。据此,"平行趋势假设得到验证、DID设定有效"属于过强表述;更稳妥的说法是"与平行趋势相容/未发现明显违反的证据,并经敏感性与构成检验"。这是对论文立场的措辞性延伸,论文本身没有给出推荐用语。

**I7**(依据:F7, F14)

论文区分两件事:处理后估计在平行趋势成立时仍可解释(F14),而问题在于难以判断它是否可由趋势违反解释(F7)。因此用户的 DID 结果并非被论文否定,只是"用默认图的处理前平坦来背书"这一论证不成立;结论强度是'有条件'。

## 5. 未知与后续阅读(U*)

**U1** 论文没有在含从未处理组的多队列(3批)交错设定下,实际演示或推导 universal 基期 CS 事件研究的行为(图和推导均为非交错时点)。
- 缺什么/为何影响决策:交错+从未处理对照下,universal 基期图是否足以辨别趋势违反、与默认图差异多大,论文未给出。
- 去哪里查:论文参考文献中的 Callaway (2021) 博客 'Universal vs. Varying Base Period in Event Studies'(p.10 脚注9、p.13 参考文献,论文自己引用)。

**U2** 论文没有给出 CS 估计量在交错设定下做 HonestDiD/Rambachan-Roth 敏感性分析的具体步骤或阈值;只在 BJS 类估计量处指向 Liu (2025)。
- 缺什么/为何影响决策:用户应对 CS(universal 基期)的哪些系数、以何种约束(如相对违反幅度 M)做敏感性分析,论文没有覆盖。
- 去哪里查:Rambachan and Roth (2023) 与 Liu (2025),均在论文参考文献中(p.14);具体 R 实现(例如 HonestDiD 软件包)不在本文参考文献中,属'查找建议,未确认存在于本论文参考文献'。

**U3** 用户未汇报各队列样本构成及各队列在各相对时间的观测数,论文无法替用户判断哪个队列驱动 t+4/t+5。
- 缺什么/为何影响决策:每个队列(2017/2020/2022)的企业数、可观测的相对期范围、分队列事件研究系数。
- 去哪里查:用户自己的数据;方法层面见 Liu (2025)(p.14 参考文献,论文 p.11-12 引用其队列与构成讨论)。

**U4** 论文没有量化:在约280家处理企业、数千家从未处理企业的样本规模下,处理前系数近0在统计功效上能排除多大的趋势违反。
- 缺什么/为何影响决策:处理前系数置信区间宽度与可排除的趋势斜率大小;论文只说应看量级与置信区间(F20)。
- 去哪里查:Roth (2022) 'Pre-test with Caution'、Bilinski and Hatfield (2018),均在论文参考文献中(p.13-14)。

**U5** 用户所用 did 包版本、对照组设定(never-treated 与 not-yet-treated)、是否含协变量、是否存在预期效应,论文没有讨论;论文的默认行为描述对应其所用软件版本(F25),用户版本可能不同。
- 缺什么/为何影响决策:用户的 att_gt 具体参数;论文只描述了默认处理前系数为短差分(F5)但未讨论对照组选择如何改变图形。
- 去哪里查:查找建议,未确认存在:所用 did 包版本自带的帮助文档/更新日志中关于基期默认值的说明;论文参考文献列出 did 包 (Callaway and Sant'Anna 2022, R package version 2.1.2)。

**U6** 论文没有回答"怎样的处理前证据足以在论文里写成平行趋势成立";论文只讨论图的解读,并未提供可直接引用的措辞标准,也没有讨论平行趋势在处理后期的不可检验性。
- 缺什么/为何影响决策:投稿/答辩层面的汇报规范。
- 去哪里查:查找建议,未确认存在:Rambachan and Roth (2023)(在论文参考文献中)的汇报建议部分;其余需用户导师/期刊惯例。

## 6. 下一步操作(按优先级)

1. **改图(论文建议 F10、F11)**:用 `att_gt(..., base_period = "universal")` 重估,再用 `aggte(type = "dynamic")` 画图,与默认图并列放入论文或附录。观察处理前系数是否仍贴近 0、是否出现斜率或系统性漂移。(注:`universal` 的具体参数写法以论文 p.10 为准;用户版本的参数名需自查,见 U5。)
2. **分队列报告(论文建议 F16、F17、F18)**:汇报 2017/2020/2022 三批队列的企业数、各队列在各相对期的观测数;画各队列结果均值的时间序列图;并给出限定"处理前后至少观察 k 期"的平衡样本事件研究。重点检查 t+4、t+5 是否仅由 2017(及 2020)队列驱动(I4,我的推断,需用你的数据核实)。
3. **同时看量级与置信区间(论文建议 F20、F21、F22)**:不要只用"处理前系数不显著/接近0"作结论;报告处理前系数的点估计与置信区间,并说明置信区间能排除多大的趋势违反(功效见 U4)。
4. **敏感性分析(部分来自论文 F9、F24,多数为我的建议 I5)**:在 universal 基期的事件研究基础上做 Rambachan-Roth/HonestDiD 类分析;不要直接基于默认(不对称)图的处理前系数。具体实现论文未给出(U2),需另行查找。
5. **改写措辞(我的建议 I6、I7)**:不写"平行趋势得到验证、DID 设定有效",改为类似"处理前事件研究系数与平行趋势相容,未发现明显违反的证据(基期统一的事件研究图、分队列检查及敏感性分析均如此)",并如实说明平行趋势的处理后部分不可检验。

## 7. 核验记录

- 脚本:`skill/scripts/extract_pages.py`(15页,文本层可用,无无文本页,`pages_figure_like`=[4,6],已渲染 `out/work/page_4.png`、`page_6.png` 并目视)、`skill/scripts/verify_quotes.py`。
- **最终结果:total=39,pass=39,fail=0**(fact 26 / inference 7 / unknown 6)。
- **第1轮:total=38,pass=37,fail=1。** F4 的整句引文 NOT_FOUND:原文在 p.5 的 "pre-/treatment" 处断行,PDF 文本为 "pretreatment",而我摘录时写了带连字符的 "pre-treatment"。副作用是引文被缩短。第1轮报告保存于 `work/verify_report_round1.json`。
- **修正1:** 将 F4 的引文截短为 "then exhibits a kink at the time of the treatment, sloping upwards afterwards."(逐字);为保留"处理前相对平坦"这一限定信息,新增 F26("the CS event-study plot has relatively flat"),I1、I2 的 based_on 同步加入 F26。第2轮(仅修正F4后)结果保存于 `work/verify_report_round2.json`(38/38);加入 F26 后重跑得最终 39/39。共迭代2次修改,未超过3轮上限,无被删除论点。
- 图的处理:Figure 1/2 的图形内容只依据论文正文对图的文字描述(F4 等),我没有从图中读取任何数值写入结论。
- 仍存的限制:(1) 论文证据仅为一次仿真(100 单位)+ 非交错时点下的解析推导,未做交错设定的仿真;(2) F18 的示例句("restricted to units who are observed at least 3 periods before and after treatment")跨 p.12-13,引文仅取 p.12 部分;脚注14(F20-F22)跨 p.11-12,按页分别引用;(3) F11 引文在 "base_period" 处截止,论文原文该处为 `base_period = "universal"`(含 PDF 中的下划线/引号排版),引号内容见 p.10;(4) 全文公式未手抄。
- 人工介入:无。

## 8. 自检清单

- [x] 结论段回答了 question 本身。
- [x] 每条 fact 有页码+逐字引文(或公式锚点),verify_quotes 全部 PASS。
- [x] 没有把论文设定外的结论写成 fact(交错设定、用户数据相关内容均在 I*/U*)。
- [x] 论文限定词(单次仿真、非交错、默认设置、"if the appropriate parallel trends assumption holds")保留在 statement 中。
- [x] 来自图的数字标了目视近似:未使用图中数值。
- [x] 每条 unknown 有 gap 与 next_reading;后续阅读仅指向论文参考文献或标注"查找建议,未确认存在"。
- [x] 区分了论文建议(F*)与我的建议(I*/经验)。
- [x] 核验记录里如实写了失败、重试和未完成项。
