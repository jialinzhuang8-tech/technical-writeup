# 阅读报告:默认 CS 事件研究图能否证明"平行趋势成立"

论文:Roth (2026-01-21 版), *Interpreting Event-Studies from Recent Difference-in-Differences Methods*, arXiv:2401.12309v2。共 15 页,下文页码为 PDF 页码(与页脚印刷页码一致)。
证据标注:【原文】=论文直接陈述;【推断】=我从论文结论外推到用户场景;【未覆盖】=论文没讲。

## 1. 结论

**不能写"平行趋势假设得到验证、DID 设定有效"。** 理由有三层,强度递减:

1. **【原文,核心】默认 CS 图的"处理前贴近 0"不能按传统 TWFE 事件研究的方式解读。** 默认 CS 的处理前系数是"短差分"(相邻两期比较),处理后系数是"长差分"(相对处理前一期比较),两者构造不对称。论文模拟中没有任何处理效应、平行趋势被严重违背(处理组相对对照组线性上升,γ=0.5),默认 CS 图仍呈现处理前一条平的线,在处理时点出现"拐点/kink",之后向上倾斜,看起来像一个真实的动态处理效应(p.2-3, p.5, Fig.1b;p.7-8 公式)。
2. **【原文】** 因此"处理前系数≈0,处理后 t+4、t+5 显著"这类图形,不能用常规"看处理时点有无断点/拐点"的启发式来判断。论文原话:"a kink or jump in the plot may arise even if there is no treatment effect and parallel trends is equally violated in all periods. One should therefore not apply the typical heuristics for visual inference—e.g. looking for a discontinuity or kink at the treatment date"(p.9)。
3. **【原文】** 即使图形没问题,"处理前系数不显著"本身也是弱证据。论文在脚注 14(p.11-12)提醒:仅看处理前系数是否显著有陷阱,应同时看系数大小和置信区间,并指向 Roth (2022) 与 Bilinski & Hatfield (2018)。但论文自己只给了这一条指引,没有展开(见第 4 节)。

论文并没有说用户的结果"不对"。它说的是:这张默认图作为平行趋势证据信息量不足;并且在平行趋势成立时,各新方法的处理后估计仍然有效(p.12:"does not threaten the validity of the post-treatment event-study estimates ... if the appropriate parallel trends assumption holds")。所以用户的处理后结果仍可汇报,但需要换一种方式支撑其可信度。

## 2. 论文位置与原文依据

| 判断 | 位置 | 原文依据 / 说明 |
|---|---|---|
| 默认 CS 的构造不对称 | p.7 §3.2 | "by default, the construction is asymmetric ... pre-treatment coefficients are 'short-differences', i.e. comparisons of consecutive periods, whereas the post-treatment coefficients are 'long-differences', i.e. comparisons relative to the period before treatment." |
| 公式:线性违背下 CS 总体系数 | p.8 | β_r^CS = γ(r<0);= γ·(r+1)(r≥0)。"the population version of the CS event-study coefficients show a kink at zero if γ≠0"。即处理前一条平的常数线(斜率 0),处理后斜线。 |
| 模拟图示 | p.4 Fig.1(b);p.5 文字 | "the CS event-study plot has relatively flat pre-treatment coefficients and then exhibits a kink at the time of the treatment, sloping upwards afterwards"。我看了图:处理前系数约在 0.5 附近且置信区间宽,多数包含 0,处理后系数上升且逐渐显著。 |
| 模拟设定 | p.3 §2 | 无处理效应(Y(1)=Y(0));平行趋势被违背,Y(0)=γ·t+ε,γ=0.5;100 个单位、一半处理。TWFE 版(Fig.1a)是一条直线,能直接看出是趋势。 |
| 不能套用常规视觉启发式 | p.9 §4 | 见上文引用。 |
| 基于处理前/后系数比较的敏感性分析也可能被误导 | p.9 | "Sensitivity analyses that compare the pre-treatment and post-treatment coefficients from these event-studies (e.g. Manski and Pepper, 2018; Rambachan and Roth, 2023) may likewise yield misleading conclusions given the asymmetric construction"。注意:这意味着不能把默认 CS 图的系数直接喂给 HonestDiD。 |
| 改图办法(CS) | p.10 | "use 'long-differences' for the pre-treatment coefficients as well as the post-treatment coefficients (i.e. always use the period before treatment as the baseline). This can be implemented ... in the did R ... package using the options base_period = "universal""。"event-study estimates are numerically equivalent to the dynamic TWFE specification in the non-staggered setting"。 |
| 注意 Callaway 的反方观点 | p.10 脚注 9 | Callaway (2021) 认为 universal base 更易看到长期违背,而短差分更适合检测"无预期"(no anticipation)违背。两种图各有用途。 |
| 分离检验与估计 | p.11-12 | 建议"completely separate the testing and estimation steps":用对称的方法(如 did + universal base)画图判断平行趋势是否可信;再单独报告估计。 |
| 队列构成变化 | p.12 | "the composition of units that contribute to an event-study coefficient will often change across different relative time periods. Indeed, if a panel is balanced in calendar time, then with staggered treatment adoption it is necessarily imbalanced in relative time." |
| 队列构成的汇报办法 | p.12-13 | "supplement aggregated event-studies with plots of the time series of the mean outcome by adoption cohort. It may also be useful to report aggregated event-studies that enforce some balancing criteria—e.g. ... restricted to units who are observed at least 3 periods before and after treatment." |
| 敏感性分析 | p.12 + 脚注 11 | 可用 Rambachan & Roth (2023) 做敏感性分析;交错处理下与估计量结合的做法参见 Liu (2025)(该文被论文引用,我没有读)。 |
| 其他估计量 | p.5-6, p.9-12, p.15 | SA、Wooldridge 在非交错情形与 TWFE 事件研究相同;BJS/Gardner/Liu-Wang-Xu 等插补估计量同样不对称,处理时点会出现跳变。本任务用户用的是 CS,故这些只作背景。 |

## 3. 推断(论文没有直接对用户场景下结论的部分)

1. **论文的数学与模拟都限定在"非交错、单一处理时点"(p.3, p.6-7)。** 把结论推广到用户的三批进入(2017/2020/2022),是我的推断。依据:默认 CS 对处理前用短差分、处理后用长差分这一构造是估计量本身的性质,在交错情形下同样适用;论文也在 p.12 明确说交错时"additional complications may arise"。所以"默认图的处理前系数不能证明平行趋势"这一点应当成立,但具体失真形状在交错时会更复杂,论文没有给出。
2. **用户的 4 个处理前期都贴近 0,与"存在线性趋势"并不矛盾。** 如果有一个每期斜率为 γ 的线性违背,默认 CS 的处理前系数会是常数 γ(不是 0),只要 γ 相对标准误较小,每个系数都"不显著、接近 0",而处理后的长差分会按 γ·(r+1) 累积。这一点是对 p.8 公式的直接代入,数学上是论文结果的应用,但"用户的数据就是这种情形"我无法确认。用户的 t+4、t+5 显著恰好落在这种累积效应最明显的位置,这是需要重点排查的。
3. **用户的默认设置很可能就是论文所说的"短差分"版本。** 论文 p.7 与 p.5 说明"default settings in the did package"产生该不对称构造;用户称没有调过 base period,因此推断其图属此类。论文没有逐一列出 did 包的默认参数名,"universal" 选项见 p.10。建议用户核对自己的 did 版本和 `att_gt(..., base_period=)` 的实际取值(论文引用的版本是 did 2.1.2,p.13)。
4. **队列构成问题落在用户设定上。** 面板 2010–2024,三批进入 2017/2020/2022:
   - 2022 队列最多观察到 t+2,2020 队列最多到 t+4,只有 2017 队列能观察到 t+5(最多 t+7)。
   - 因此 t+4、t+5 的聚合系数可能完全由 1–2 个队列贡献;t+5 可能只来自 2017 队列,而其队列规模占 280 家中的多少用户尚未汇报。
   - 这是我根据用户给的年份算出来的,论文只给出一般性警告(p.12)。具体哪些队列贡献哪些相对期,需要用户用数据确认。
5. **"用户已有从未处理组"这一点论文没有讨论。** 论文的 CS 是"treated and not-yet-treated"比较(p.7),用户的对照组是从未处理企业。我推断构造的不对称性与对照组类型无关(它来自基期选择),但论文没有验证。

## 4. 论文没覆盖的

- 交错处理(多队列)下默认 CS 图失真的具体形状与大小;没有交错情形的模拟。
- 如何在 `did` + HonestDiD 中具体操作(代码/参数/怎样处理 universal base 下的系数矩阵)。论文只指向 Rambachan & Roth (2023) 和 Liu (2025)。
- 处理前期数、检验功效:论文没讨论"4 个处理前期够不够"。
- 对照组数千家 vs 处理组 280 家这类不平衡样本、聚类、多重检验等问题。
- 经济学/金融研究中如何措辞(如"支持""未发现违背"vs"验证")。论文没有给出写作措辞;下面的措辞建议是我的建议,不是论文原文。
- 预期效应(no anticipation)怎么检验:仅在脚注 9 提到 Callaway 认为短差分更适合,未展开。

## 5. 后续动作(给用户的建议)

**画图与估计**
1. 用 `att_gt(..., base_period = "universal")` 重估,再 `aggte(type = "dynamic")` 作图(p.10)。此时 t-1 被归一化为 0,其余处理前系数为相对 t-1 的长差分,线性趋势会显示为一条斜线,和 TWFE 事件研究图的读法一致。
2. 同时保留默认(varying)版本放附录,按 Callaway 的看法它更适合观察"预期效应"(脚注 9, p.10),并向读者说明两版图的区别。
3. 画"按队列分组的结果变量均值时间序列"(2017/2020/2022 三批 vs 从未处理组)(p.12)。
4. 报告各队列的企业数,以及 t+4、t+5 各自由哪些队列贡献(p.12 的思路);另做一版只保留处理前后至少观察若干期的平衡样本事件研究(论文例子是前后各 3 期,p.12-13)。

**稳健性**
5. 做 HonestDiD 敏感性分析(Rambachan & Roth 2023;交错情形参见 Liu 2025,p.12 与脚注 11)。注意:论文 p.9 警告,直接用默认非对称系数做这类敏感性分析可能误导,所以应基于 universal 版本的系数/或按 Liu (2025) 的做法。具体操作细节超出本论文,需要另查文档。
6. 报告处理前系数的大小和置信区间,而不只是"不显著"(脚注 14, p.11-12)。

**论文措辞建议(我的建议,非原文)**
- 不写"平行趋势得到验证"。可写类似:"在处理前 4 期未发现显著的差异性趋势,但这不构成对平行趋势的证明;我们报告了 universal base 事件研究图、分队列均值走势与 HonestDiD 敏感性分析以评估其稳健程度"。
- 说明默认 CS 的处理前系数为相邻期差分,与处理后长差分不可直接比较。
- 对 t+4、t+5 的结论注明样本构成(哪些队列贡献)。

## 6. 说明与局限

- 全部结论仅基于对该 PDF 的阅读(15 页,文字用 PyMuPDF 提取,并目视核对了 Fig.1);未读被引文献(Liu 2025、Li & Strezhnev 2025、Rambachan & Roth 2023 等),相关内容仅转述论文对它们的描述。
- 论文的公式和图形来自 γ=0.5 的单次模拟与总体推导;用户数据中违背是否存在、形状如何,论文无法回答。
- 文本提取时部分公式符号有乱码(如 p.8 的 T̄),公式以我对 PDF 渲染与上下文的理解转述,核心不等式(CS: γ vs γ(r+1))与论文 p.8 文字描述一致。
