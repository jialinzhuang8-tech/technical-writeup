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
