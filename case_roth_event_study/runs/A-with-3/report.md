# 阅读报告:Roth (2026) 对"did 默认事件研究图 + 前期系数≈0"的含义

论文:Roth, *Interpreting Event-Studies from Recent Difference-in-Differences Methods*, arXiv:2401.12309v2(共15页,页码为 PDF 页序,与打印页码一致)。

## 1. 一句话结论
**不能**据此写"平行趋势得到验证、DID 设定有效"(有条件结论,强度:较确定的否定,但属推断)。论文说明 did 默认图的前期系数是短差分、后期是长差分,二者不对称,不能用 TWFE 式目视推断;论文建议改用对称基期(`base_period="universal"`)画图用于评估平行趋势,并补充分队列均值图、考虑平衡化与敏感性分析。(I1,F1,F9,F12,F15)

## 2. 适用性对照表
| 设定项 | 论文设定 | 我的设定 | 判断 | 依据 |
|---|---|---|---|---|
| 估计量/软件 | CS,R did 默认设置 | CS,R did 默认 | 一致 | F3,F6 |
| 处理时点 | 共同处理时点(非交错),仿真与推导均如此 | 三批交错进入 | 部分一致(机制可迁移,数值结论不可直接迁移) | F8,F23,I2,I3 |
| 对照组 | 从未处理(p.3 正文:Units are either treated ... or never-treated,未单列为 claim) | 从未处理 | 一致(仅限论文的简单仿真) | F8 |
| 证据类型/规模 | 一个简单DGP的推导 + 单次仿真抽样(100单位) | 真实A股面板,约280处理企业 | 论文未覆盖真实数据与该样本规模 | F7,U2 |
| 违背平行趋势形态 | 线性趋势违背、无处理效应 | 未知 | 论文未覆盖(用户形态未知) | I2,U4 |
| 基期设置 | 默认=前期短差分/后期长差分;可改 universal | 默认,未调 | 一致(用户处于论文所批评的默认情形) | F3,F4,F12 |
| 队列构成汇报 | 建议分队列均值图/平衡化 | 未做 | 论文有建议,用户缺项 | F17-F19,I5 |
| HonestDiD 类敏感性 | 提到 Rambachan–Roth;默认图上做可能误导 | 未做 | 部分覆盖;CS交错+universal+HonestDiD 的具体做法论文未覆盖 | F11,I4,U3 |
| 事件研究是否可证明"有效" | 称其提供"证据" | 想写"验证" | 论文未直接评论该措辞 | F2,I1,U6 |

## 3. 原文事实

**F1** · PDF p.2

> should not be interpreted in the same way as traditional dynamic TWFE

论文主旨:对若干流行新方法(含CS),软件默认事件研究图在用于评估平行趋势违背时,不应像传统动态TWFE那样解读。

**F2** · PDF p.2

> provide evidence about the validity of the research design

事件研究图的第二个用途是为研究设计的有效性提供'证据'(而非证明)。

**F3** · PDF p.7

> by default, the construction is asymmetric across the pre-treatment and post-treatment periods

CS 默认构造在处理前与处理后阶段是不对称的(论文在共同处理时点的设定下推导)。

**F4** · PDF p.8

> we compare outcomes in consecutive periods

共同处理时点设定下:CS 处理前系数比较相邻期(短差分),处理后系数比较更长跨度(相对基期0的长差分)。

**F5** · PDF p.8

> show a kink at zero if

在论文仿真DGP(线性违背平行趋势、无处理效应)下,CS 事件研究的总体系数在 0 处出现拐点(kink)。

**F6** · PDF p.5

> treatment coefficients and then exhibits a kink at the time of the treatment

仿真(无处理效应、线性违背平行趋势,did 包默认设置):CS 图的处理前系数相对平坦,处理时点出现拐点并向上倾斜。

**F7** · PDF p.3

> single simulation draw from this DGP

图1的证据来自对该DGP的单次仿真抽样(100个单位,一半被处理)。

**F8** · PDF p.3

> some newer methods with a simulation of an extremely simple non-staggered DiD setting

论文的仿真设定是'极其简单的非交错(non-staggered)DiD设定'。

**F9** · PDF p.9

> a kink or jump in the plot may arise even if there is no treatment effect and parallel trends is equally violated in all periods

即使没有处理效应、且平行趋势在所有期同等程度被违背,这些方法的图仍可能出现拐点/跳跃。

**F10** · PDF p.9

> One should therefore not apply the typical heuristics for visual inference

因此不应套用 TWFE 图的目视推断习惯(如找处理时点的不连续/拐点)。

**F11** · PDF p.9

> may likewise yield misleading conclusions given the asymmetric

比较处理前后系数的敏感性分析(如 Rambachan and Roth 2023,即HonestDiD)在这些不对称构造的默认图上可能得出误导性结论。

**F12** · PDF p.10

> period before treatment as the baseline

论文对CS的修改建议:处理前系数也用长差分,即始终以处理前一期为基准(did 包中通过 base_period 选项 universal 实现)。

**F13** · PDF p.10

> the event-study estimates are numerically equivalent to the dynamic TWFE specification in the non-staggered setting considered here

使用上述设置后,在(论文考察的)非交错设定下,CS 事件研究估计与动态TWFE数值等价。

**F14** · PDF p.10

> using short-differences may make it easier to detect violations of the no anticipation assumption

脚注9转述 Callaway(2021) 博文:短差分(varying base)可能更便于发现'无预期'假设违背;长期违背更易在 universal base 下可视化。此为被引博文的观点,非论文自身检验。

**F15** · PDF p.12

> to visually evaluate the plausibility of the parallel trends assumption

论文建议:用对称处理各期的方法(如按上述选项设置的 did 包)报告事件研究,以目视评估平行趋势的合理性。

**F16** · PDF p.12

> does not threaten the validity of the post-treatment event-study estimates for recent methods if the

论文强调:这一问题不威胁处理后估计的有效性,前提是相应的平行趋势假设成立。

**F17** · PDF p.12

> the composition of units that contribute to an event-study

交错处理下,参与各相对期系数的样本构成通常随相对期而变(引Liu 2025)。

**F18** · PDF p.12

> it will often be useful to supplement aggregated event-studies with plots of the time series of the mean outcome by adoption cohort

论文建议用按队列(adoption cohort)的结果均值时间序列图补充汇总的事件研究图。

**F19** · PDF p.12

> studies that enforce some balancing criteria

论文还建议可报告施加平衡性准则的汇总事件研究;其举例(限定在处理前后至少观测3期的单位)的后半句在p.13首行续写。

**F20** · PDF p.12

> may arise when interpreting these results in staggered settings

论文指出:在交错设定下,即使方法在非交错设定下能匹配TWFE图,解读时仍可能有额外复杂性。

**F21** · PDF p.11

> regarding pitfalls of simply looking at the significance of

脚注14:只看处理前系数是否显著存在陷阱(参见 Roth 2022; Bilinski and Hatfield 2018)。

**F22** · PDF p.12

> magnitudes of the pre-trends estimates and their confidence intervals

脚注14续:应同时看预趋势估计的量级及置信区间;若处理前后系数构造不对称,评估预趋势潜在偏误的量级很困难。

**F23** · PDF p.8

> Formally, in our setting with common treatment timing

CS 系数的形式推导是在'共同处理时点'(common treatment timing)的设定下给出的。


**关于图(未经文本核验)**:p.4 图1、p.6 图2 为图像页,已用脚本渲染为 work/page_4.png、page_6.png 并调用读图工具,但工具返回仅为图像引用提示,我无法确认自己逐点目视读取了图形细节。因此本报告**不包含任何来自图的目视数值或形状判断**;对图1形态的描述一律以 p.5 正文文字(F6)为准。


## 4. 推断

**I1**(基于 F1, F2, F9, F10, F22):不能直接写'平行趋势得到验证、DID设定有效'。论文没有直接评论这句话,但从其框架可推:(a)事件研究只提供'证据'(F2);(b)默认CS图的处理前/后系数构造不对称,'前期近0、后期显著'这一形态与'无效应+线性违背平行趋势'的仿真结果可并存(F9,F10);(c)评估预趋势应看量级与置信区间,而非仅看是否显著(F22)。可写的措辞是'未发现与平行趋势相矛盾的证据/预趋势检验未拒绝',并说明所用基期设置。

**I2**(基于 F3, F4, F5, F6, F7, F23):用户的形态(默认设置下前4期贴近0、后期t+4/t+5显著)与论文仿真中'无处理效应但存在线性违背'时CS默认图的形态(前期平坦、处理后拐点上升)在定性上类似,因此该图本身无法区分'真实动态效应'与'平行趋势被线性/累积性违背'。可能出错处:论文仅为共同处理时点+单次仿真,用户是三队列交错+真实数据;此处是定性类比而非定量结论。

**I3**(基于 F3, F12, F23):论文推导限于共同处理时点,但同时指出 did 包的默认就是前短差分/后长差分并给出 base_period=universal 的修改办法(F3,F12);因此可合理推断用户在交错设定下使用默认选项时,同样是前期系数为短差分。可能出错处:交错设定下的具体聚合权重和 did 包版本差异论文未逐一展开(见U1,U5)。

**I4**(基于 F11, F12, F13, F15):若要做 HonestDiD 类敏感性分析,应在对称构造(base_period=universal)的CS事件研究上做,而不是在默认图上做。论文对此给出的是'默认图上做可能误导'(F11)和'用对称方法评估平行趋势'(F15)的相邻建议,并未明说'CS universal + HonestDiD'的组合;在交错设定下该组合是否合适属于推断(见U3)。

**I5**(基于 F17, F18, F19, F20):用户未汇报队列构成,这在交错设定下是实质缺口:论文只说构成会随相对期变化并建议分队列作图/平衡化(F17-F19)。按用户面板(2010-2024,队列2017/2020/2022)我自行推算:t+4可由2017、2020队列贡献,t+5仅2017队列能贡献(2020+5=2025超出面板),2022队列最多观测到t+2。故t+4、t+5显著可能主要由最早队列驱动。该推算是我的算术,论文未给出;若用户面板't=0'定义不同则需重算。

**I6**(基于 F14, F15):稳妥的报告方式是把两种基期的图都放出来(默认/varying 与 universal),并解释二者含义不同:varying 更适合观察逐期变化/无预期,universal 更适合与TWFE式目视推断可比。依据:F15的对称图建议与F14的Callaway转述;'同时报告两种'本身是我的建议,并非论文明文要求。


## 5. 未知与后续阅读

**U1**:论文没有在交错处理(三批队列)+从未处理对照组的设定下给出CS事件研究的数值/仿真结果,只在共同处理时点下推导并仿真。
- 缺口:交错设定下默认图与universal图的差异大小、队列加权的影响。
- 后续阅读:论文参考文献中的 Callaway and Sant'Anna (2021, J. of Econometrics) 与 Liu (2025, arXiv:2509.01829) ;以及 Callaway (2021) 博文(均出现在论文参考文献中)。

**U2**:论文没有评估在'处理组约280家、仅4个处理前期'的样本规模下预趋势检验的功效,也没给出系数多接近0才算'可以接受'的标准。
- 缺口:预趋势检验功效与可检出的违背幅度。
- 后续阅读:论文参考文献中的 Roth (2022, AER: Insights) 和 Bilinski and Hatfield (2018)。

**U3**:论文没有给出如何在CS(did)的交错结果上具体实施 HonestDiD(如选择平滑度M、相对量级Mbar)。仅指出可参考 Rambachan and Roth (2023) 以及 Liu (2025) 在交错设定下的做法(后者针对插补估计量)。
- 缺口:CS+universal base 下 HonestDiD 的具体操作与参数选取。
- 后续阅读:Rambachan and Roth (2023, REStud) 及其软件文档(查找建议,未在本论文中确认其细节);Liu (2025)。

**U4**:改用 base_period=universal 后,用户的t+4、t+5显著性及处理前系数会如何变化,论文无法回答,需用用户数据重跑。
- 缺口:用户数据上的实际结果。
- 后续阅读:无需读文献;重跑 att_gt(base_period="universal") 并比较。本次未重跑。

**U5**:用户所用 did 包版本、control_group(nevertreated/notyettreated)、anticipation 等选项未知;论文仅说明所测版本(参考文献列 did 2.1.2,并称 2025年10月重装最新版)及'默认'行为,未覆盖用户可能的其它选项组合。
- 缺口:用户包版本与选项;论文所述默认行为是否与用户版本一致。
- 后续阅读:核对用户本机 packageVersion("did") 与 ?att_gt 文档的 base_period 默认值(查找建议,未在本论文中确认)。

**U6**:论文没有讨论'处理前系数近0'是否足以支持写成因果识别成立的措辞,也没有给出推荐的论文表述模板。
- 缺口:期刊/学位论文写作中对平行趋势措辞的惯例。
- 后续阅读:查找建议,未确认存在:Roth et al. (2023, J. Econometrics) 综述(出现在论文参考文献中)可作为起点。


## 6. 下一步操作
1. **(论文建议,F12/F15)** 重跑 `att_gt(..., base_period = "universal")`,再 `aggte(type="dynamic")` 作图,用这张对称图评估平行趋势;保留默认图作附录对照。
2. **(论文建议,F18/F19)** 汇报各队列(2017/2020/2022)的样本量,并画分队列结果均值时间序列图;考虑只用处理前后均观测满若干期的单位做平衡化事件研究。
3. **(论文相关提示 F11,F22 + 我的建议 I4)** 在对称构造的结果上做 HonestDiD 敏感性分析,同时报告前期系数的量级与置信区间,而不只看"不显著"。
4. **(我的建议,I1/U6)** 措辞改为"未发现与平行趋势相矛盾的证据/预趋势检验结果与平行趋势假设相容",并注明基期设置;避免"验证""证明有效"。
5. **(我的推断,I5)** 核查 t+4、t+5 系数是否主要由 2017 队列驱动(2022 队列最多观测到 t+2),必要时汇报分队列估计。

## 7. 核验记录
- `verify_quotes.py`:**total=35, pass=35, fail=0**(fact 23 / inference 6 / unknown 6)。
- 过程:第一次调用脚本时 claims.json 尚未写入(我把写文件与跑脚本并行发出),报 FileNotFoundError,属操作失误,非引文失败;文件写入后第一次核验即 35/35 通过。随后修改了 F19 与 I5 的 statement(未改引文),并再次核验仍 35/35。无 WRONG_PAGE/NOT_FOUND。
- 限制:脚本只核验引文逐字存在,不核验概括是否忠实,statement 由我阅读核对。F6、F14、F19 的 statement 已标注语境(仿真、被引博文观点、跨页)。
- 图:未写入任何来自图的内容(见第3节说明)。I5 的队列覆盖推算是我自己的算术,基于用户 t=0 为首次处理年的假定。
- 未做:未用用户数据重跑 did(U4);未读论文外文献。

## 8. 自检清单
- [x] 结论段回答了 question 本身
- [x] 每条 fact 有页码+逐字引文且全部 PASS
- [x] 未把论文设定外结论写成 fact(交错设定、HonestDiD+CS 均放入 I/U)
- [x] 限定词(仅仿真/默认设置/共同处理时点/被引博文)保留在 statement
- [x] 未使用图中数值/形状;图相关表述以正文为准并已说明
- [x] 每条 unknown 有 gap 与 next_reading;后续阅读限于论文参考文献或标明查找建议
- [x] 区分论文建议与我的建议
- [x] 核验记录如实写了失败与重试
