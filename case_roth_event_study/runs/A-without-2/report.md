# 阅读报告:默认设置的 CS 事件研究图能否支持"平行趋势得到验证"

论文:Roth (2026-01-21 版), *Interpreting Event-Studies from Recent DiD Methods*, arXiv:2401.12309v2。页码为 PDF 页码,与印刷页码一致(共 15 页)。

## 1. 结论(先看这里)

**不能。** 不要写"平行趋势假设得到验证、DID 设定有效"。理由有两层:

1. **默认设置下的 CS 图,其处理前系数的构造方式与处理后系数不对称,不能用传统 TWFE 事件研究图的方法去"看"。**
   - 默认的处理前系数是"短差分"(相邻两期比较)。
   - 处理后系数是"长差分"(相对处理前一期)。
   - 因此,即使平行趋势被线性违背,处理前系数也可能是一排平的、近似常数的点,到处理日再出现拐点。
   - 所以"处理前贴近 0"几乎不具备论文所说的那种可读性。
2. **"处理前系数不显著或贴近 0"本身就不是"验证"。**
   - 论文脚注 14 引用 Roth (2022) 和 Bilinski & Hatfield (2018),指出只看预趋势显著性有陷阱。
   - 论文要求看预趋势估计值的大小及其置信区间,而且要求处理前与处理后系数以对称方式构造,才能评估潜在偏误的大小。

**论文建议的做法**(详见第 4 节):
- 把 `att_gt` 改为 `base_period = "universal"`,并重画事件研究图。
- 补充各队列(cohort)的结果均值时间序列图。
- 说明各相对期的样本构成,必要时做平衡样本版本。
- 用 Rambachan–Roth 类敏感性分析(HonestDiD)处理后效应。
- 措辞上改成"未发现明显的处理前趋势差异"或"结果对一定程度的平行趋势偏离是否稳健",而不是"验证"。

## 2. 论文依据(可核对)

| # | 判断 | 页码 | 原文依据(英文原话,中文说明) |
|---|---|---|---|
| A | 论文的核心主张 | p.1 摘要, p.2 | "the default plots produced by software for several of the most popular recent methods do not match those of traditional TWFE event-studies"。新方法的默认图"可能在处理时点出现拐点或跳跃,即便 TWFE 事件研究是直线"。原因是"construct the pre-treatment coefficients asymmetrically from the post-treatment coefficients"。 |
| B | 传统 TWFE 图的"目测推断"启发式不能直接套用 | p.2、p.3 | "typical heuristics for visual inference developed based on dynamic TWFE specifications will be misleading when applied to these new estimators"(p.3)。 |
| C | CS 默认构造:处理前短差分、处理后长差分 | p.7–8 | "by default, the construction is asymmetric… the pre-treatment coefficients are 'short-differences'… whereas the post-treatment coefficients are 'long-differences'"(p.7)。p.8 给出公式:r<0 时比较 r+1 与 r 期;r≥0 时比较 r+1 与 0 期。 |
| D | 模拟中 CS 图的表现 | p.3、p.5、p.8;图见 p.4 Fig.1(b) | 模拟设定为真实处理效应为零,但处理组相对对照组有线性上升的趋势违背(γ=0.5)。CS 图中"relatively flat pre-treatment coefficients and then exhibits a kink at the time of the treatment, sloping upwards afterwards"(p.5)。公式上 β^CS_r = γ (r<0),β^CS_r = γ(r+1) (r≥0),"show a kink at zero if γ≠0"(p.8)。我也查看了 p.4 的图片:前期点平坦且在 0.5 上下,处理后斜向上。这就是"前平后翘"的图形,而真实处理效应为零。 |
| E | 这类图的处理前系数不可作常规视觉检验,敏感性分析也可能被误导 | p.9 | "a kink or jump in the plot may arise even if there is no treatment effect and parallel trends is equally violated in all periods. One should therefore not apply the typical heuristics… Sensitivity analyses that compare the pre-treatment and post-treatment coefficients… (e.g. Manski and Pepper, 2018; Rambachan and Roth, 2023) may likewise yield misleading conclusions given the asymmetric construction"。 |
| F | CS 的修正办法 | p.10 及脚注 9 | "use 'long-differences' for the pre-treatment coefficients as well as the post-treatment coefficients (i.e. always use the period before treatment as the baseline). This can be implemented… in the did R… using the options base_period = 'universal'"。在非交错设定下,该设置与动态 TWFE 数值等价。 |
| F' | Callaway 博客的折中看法 | 脚注 9, p.10 | 长期违背用 universal 更易看出;但短差分可能更便于发现"无预期效应"违背。 |
| G | 需看预趋势估计值大小及置信区间,不能只看显著性 | 脚注 14, p.11–12 | "researchers should ideally also look at the magnitudes of the pre-trends estimates and their confidence intervals. However, evaluating the magnitudes of potential bias from pre-trends is challenging if the pre-treatment and post-treatment coefficients are not constructed symmetrically."(p.12 脚注尾部) |
| H | 论文不否定处理后估计量本身 | p.12 | "the discussion here does not threaten the validity of the post-treatment event-study estimates… if the appropriate parallel trends assumption holds"。问题在于难以判断处理后系数是否由平行趋势违背造成,而不是处理效应。 |
| I | 交错处理下的样本构成问题 | p.12–13 | "the composition of units that contribute to an event-study coefficient will often change across different relative time periods… if a panel is balanced in calendar time, then with staggered treatment adoption it is necessarily imbalanced in relative time." 建议"supplement aggregated event-studies with plots of the time series of the mean outcome by adoption cohort",并可做平衡版本,"restricted to units who are observed at least 3 periods before and after treatment"。 |
| J | 敏感性分析的位置 | p.11–12 | 可用 Rambachan & Roth (2023) 对处理后估计做敏感性分析;Liu (2025) 给出在交错设定中配合插补估计量使用的建议。脚注 11 提到 Liu (2025) 的"block bias"。 |
| K | 先检验、再估计分开的思路 | p.11–12 | 用对称构造的方法(如 did 包加上述选项)画图来评估平行趋势是否可信,再另外汇报后续处理后估计。这是针对 BJS 的建议,但论文明确把 did 包的 universal 设置作为"对称图"的示例。 |

## 3. 哪些是论文明确说的,哪些是我的推断,哪些论文没覆盖

### 论文明确支持
- CS 默认图的前后不对称及其后果(C、D、E)。
- 用 `base_period="universal"` 作为对称化修正(F)。
- 单看预趋势显著性的缺陷(G)。
- 交错设定下的样本构成问题及补充图(I)。
- 处理后估计的敏感性分析是推荐方向(J)。

### 我的推断(论文没有直接对用户案例这么说)
1. **"处理前 4 期贴近 0 ≠ 无趋势违背"的具体情形。**
   - 论文的证明基于线性趋势违背的非交错模拟(p.7–8)。
   - 用户是三批交错进入,我把 p.7–8 的机制外推到交错情形。这符合论文的精神,但论文本身只证明了非交错情形。
   - 论文 p.12 明确说在交错设定下"additional complications may arise"。
2. **用户的前 4 期"贴近 0"的含义。**
   - 若真实趋势差是每期 γ 的线性违背,默认图的处理前系数约等于 γ 的常数。
   - 当 γ 小于标准误时,看起来就是"贴近 0"。
   - 这意味着,用户看到的"前期很平"与"真有一个小的持续趋势差"在默认图中分不开。这是推断,不是论文对用户数据的结论。
3. **各队列的 t+4、t+5 来源不同,这是我按用户给定年份算的,不是论文内容。**
   - 面板为 2010–2024 年,队列为 2017/2020/2022。
   - t+5 只有 2017 队列能贡献(2017+5=2022;2020+5=2025 超出样本)。
   - t+4 只有 2017 和 2020 队列能贡献(2020+4=2024;2022+4=2026 超出样本)。
   - 处理后各期的系数是不同队列的不同组合。这正是论文 p.12 所说的"composition changes",所以 t+4、t+5 的显著可能主要由最早队列或少数企业驱动。
4. **默认 `did::att_gt` 的 control group 默认是 never-treated。**
   - 论文 p.7 写 CS "aggregating DiD comparisons of treated and not-yet-treated units",没有说明具体默认值。
   - 用户的设定已经说明对照组是从未处理组,这一点我就按用户的设定处理,不依赖论文。

### 论文没覆盖
- **具体到 3 个队列、280 家处理企业、几千家从未处理企业的情形:** 论文没有任何这样的模拟或经验例子。
- **功效与精度:** 没有讨论在这个样本量下处理前系数的检验功效有多大,或标准误多大才算"足够窄"。
- **HonestDiD 在交错 CS 上的具体操作:** 只提到 Rambachan–Roth (2023) 和 Liu (2025),给出的是原则,而不是代码。论文指出对称构造是前提(p.9 的警告)。
- **"得到验证"的标准措辞:** 论文没有给出论文写作中的推荐话术。下面第 5 节的措辞是我的建议。
- **非线性趋势违背、预期效应的细节:** 只在脚注 9 引 Callaway 博客说短差分便于发现预期效应,没有展开。
- **其他估计量(SA、Wooldridge、dCDH)的具体处理:** 论文说明 SA 和 Wooldridge 在非交错时与 TWFE 一致(p.5),但没有给出它们在交错设定下的完整比较,也没有说哪一个更适合用户。

## 4. 对用户的后续动作

按优先级排列:

1. **重画图:** `att_gt(..., base_period = "universal")`,再 `aggte(type = "dynamic")` 并画图。
   - 论文说明这种设置下处理前系数与处理后系数用同一基期,二者可以直接比较(p.10)。
   - 在 universal 设置下,基期的系数本身被固定为 0(这是该设置的标准性质,论文未明言,属于我的补充)。
   - 对比两张图。若 universal 图中处理前系数呈现趋势性漂移或朝处理期逐步上升,就说明默认图掩盖了问题。
   - 建议两张图都放进论文或附录(Callaway 对两种设置各有优点,见脚注 9)。
2. **补队列构成与时间序列(p.12–13):**
   - 汇报各队列企业数量(2017、2020、2022 各多少家)。
   - 画各队列的结局均值时间序列(与从未处理组的对比)。
   - 说明每个相对期(尤其 t+4、t+5)由哪些队列贡献。
   - 做一个平衡版本(例如只保留处理前后各至少 3 期的企业,如论文 p.13 所示),看结论是否保持。
3. **做敏感性分析:** 在 universal 基期的事件研究系数上做 Rambachan–Roth 类分析,例如 HonestDiD,针对 t+4、t+5 报告在多大程度的平行趋势偏离下结论仍成立(p.11–12)。
   - 论文提醒,在不对称构造的图上做这类分析会误导(p.9),所以必须基于对称图。
   - 如何落实到交错 CS 的具体步骤,论文只指向 Liu (2025),需要读该文献。
4. **看数值和置信区间,而不是只看显著(p.12 脚注 14):**
   - 报告处理前系数的点估计和置信区间。
   - 把处理前置信区间的上下界与处理后效应大小比较,判断"若真有这种大小的预趋势,会不会解释掉处理后效应"。

## 5. 写作建议(措辞为我的建议,不是论文原文)

- **不要写:** "事件研究图显示处理前系数不显著,平行趋势假设得到验证,DID 设定有效。"
- **可以写:**
  - "在采用统一基期(universal base period)的事件研究中,处理前各期系数的点估计较小且置信区间包含 0,未发现明显的预趋势差异;但这并不能证明平行趋势成立。"
  - "我们进一步给出各队列的样本构成与结局均值走势,并用敏感性分析检验处理后效应对平行趋势一定程度偏离的稳健性。"
- 若 universal 图或敏感性分析给出不利信号,要在论文中如实汇报,并把"平行趋势"降为"需要的识别假设",而不是已验证的事实。

## 6. 局限

- 本报告只依据这篇 15 页的论文,并按要求未联网。
- 论文自述是对"可视化解读"的说明性短文,模拟为非交错的单一 DGP;不应把它的结论过度推广为对所有交错设计的定量判断。
- 第 3 节"推断"部分请不要当作论文结论引用。
