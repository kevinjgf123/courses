# 《知识库咨询方法论》STORY.md

## 一、定位

七册系列第七册。前六册：DA / BA / AA / TA / Ontology / Agent。

| 专册 | 核心命题 | 一句话 |
|---|---|---|
| DA | 先有治，才有存 | 数据架构是枢纽 |
| BA | 能力与组织解耦 | 业务架构是基础 |
| AA | 应用数量增长带来技术债 | 应用架构是载体 |
| TA | 不押注单点技术 | 技术架构是底座 |
| Ontology | 语义与动力学合一 | 本体是 4A 的汇流点 |
| Agent | 明确谁来判断、权限多大、何时停手 | Agent 是 4A 的新实践点 |
| **KB** | **知识要被治理，不只是被存起来** | **知识库是 4A 的新实践点** |

## 二、核心主张

1. 知识库不是向量库，也不是文档门户。它是**有口径、有时效、有权限、有引用的知识供给系统**。
2. 知识库是「上游供给」角色：本体是语义模型，Agent 是消费角色，知识库负责把**非结构化知识变成可被引用的结构化供给**。
3. Palantir 给出的答案是 **OAG（Ontology Augmented Generation）**，不是纯 RAG；检索上下文有三类：Ontology context / Document context / Function-backed context。
4. 一条硬边界：**行列表级访问控制只过滤读进提示词的数据，不延伸到模型输出，也不覆盖 Apply actions 的本体编辑** —— 必须配标记/分类级访问控制。
5. 知识库的第一个死因不是检索不准，是**过期与冲突**：同一口径在三份文档里存在，知识库就废了。
6. 每一条回答必须**指到来源的哪个位置**，无引用的答案不允许出现在对内场景。

## 三、Palantir 官方核实结论（本册引用依据）

- **Ontology context**：从本体对象提供上下文。可给固定 N 个对象，或语义搜索取 K 个最相关对象（要求该对象类型有 vector embedding 属性）。起始对象集可以是 Static input（全量对象类型）或 Variable input（作为应用变量传入的过滤后对象集）。可配置哪些属性打印给模型，默认全选，排除不可打印属性（媒体引用、向量嵌入）。可与应用状态联动：对象集输出变量 + 引用变量输出。
- **Document context**：两种模式 —— Full document text mode（整篇文本）、Relevant chunks mode（语义搜索返回 K 个最相关片段，Beta）。
- **Function-backed context**：用户自写检索。每次查询执行。适合内置检索不满足的场景（如关键词 + 语义混合）。TypeScript v1 函数，实现 `AipAgentsContextRetrieval` 接口，`messages` 为唯一必填入参，返回 `retrievedPrompt` 字符串，会被粘贴进系统提示。可选参数接应用变量（目前仅支持 string 与 object set 类型）。
- **工具三类**：Apply actions（写本体）、Call function（调函数）、Query objects（读对象，可指定属性以省 token）、Calculator tool（精确计算）。
- **工具执行身份**：`LLMs do not have direct access to tools; LLMs can only ask to use tools, and these tool calls are then executed by AIP Logic within the invoking user's permissions.`
- **访问控制传播**：行/列访问控制（restricted views、object security policies、property security policies）过滤读入提示词的数据，**但不延伸到模型输出，也不覆盖 Apply actions 的本体编辑**，需要配合 marking / Classification-based Access Control。
- **Ontology 编辑的必要条件**：`The Ontology will not be edited unless the Logic function is executed from an action`，即 Logic 函数必须从 Action 里执行，写回才生效。
- **AIP Evals**：可从运行历史一键 `Add as test case` 生成评测用例集。
- **AIP Assist 文档库**：每个 markdown 在 `overview.md` 里声明 `@name` / `@description`，供模型判断何时查询该文档库 —— 即「文档的文档」。

## 四、公网知识库理论（引用依据）

- **知识管理经典**：SECI 模型（社会化 / 外化 / 组合化 / 内化）、DIKW 链（数据 → 信息 → 知识 → 洞察）。
- **RAG 工程共识**：切片策略决定语义完整性；纯向量检索在企业场景常需与关键词/元数据过滤混合；引用可溯源是信任前提。
- **企业落地的通病**（贯穿本册五类失败模式）：
  1. 过期与冲突 —— 无人负责知识的生命周期
  2. 孤岛 —— 库与库之间不通，同一问题跨库答不全
  3. 权限泄漏 —— 检索层绕过原有权限模型
  4. 引用幻觉 —— 有引用但引错，或引用与结论无关
  5. 无梯度评测 —— 只有「感觉挺好」，没有可回归的准确率

## 五、知识库的四个关键角色（对应页面 06）

1. **采集者**：谁把非结构化内容变成可索引单元
2. **加工者**：切片、抽取实体与关系、补口径
3. **治理者**：谁负责时效、冲突、权限与下架
4. **服务方**：谁把它以检索上下文的形式供给 Agent 与应用

知识库失败，几乎都出在第 3 个角色上 —— 企业普遍只建了前两个，没设第三个。

## 六、30 页结构

| 页 | 标题 |
|---|---|
| 01 | 封面 |
| 02 | 目录 |
| 03 | 序论：为什么 4A 之后还要谈知识库 |
| 04 | Approach 七阶段 |
| 05 | PART 01 扉页 |
| 06 | 知识库到底是什么：四个角色 |
| 07 | 五个组成部分：采集、加工、索引、检索、治理 |
| 08 | RAG 的三层演进与 OAG |
| 09 | 三类检索上下文对照 |
| 10 | 知识成熟度四级 |
| 11 | 知识库岗位说明书与责任矩阵 |
| 12 | PART 02 扉页 |
| 13 | 知识库 × Ontology × Agent 三者总览 |
| 14 | 知识库与 Ontology 的分工 |
| 15 | 知识库与 Agent 的分工 |
| 16 | 引用与溯源：信任的落点 |
| 17 | 权限传播：最容易被忽略的一条硬边界 |
| 18 | 知识供给链路（从源到上下文） |
| 19 | 知识库 × Action：写回的三种方式 |
| 20 | PART 03 扉页 |
| 21 | 知识库的 4A 映射总览 |
| 22 | BA：知识服务谁、谁不该被知识替代 |
| 23 | DA：切片、实体、口径三层 |
| 24 | AA：检索拓扑与应用编排 |
| 25 | TA：索引、向量库与非功能 |
| 26 | 知识库五道门 |
| 27 | 五类失败模式 |
| 28 | 可信度评测与回归 |
| 29 | 从个人文档到企业知识资产四步 |
| 30 | 结语 |

## 七、Approach 七阶段

| 阶段 | 做什么 | 产出物 |
|---|---|---|
| 1 | 知识资产盘点与场景定义 | 知识资产清单 + 场景清单 |
| 2 | 口径与冲突治理 | 口径字典 + 冲突台账 |
| 3 | 切片与实体设计 | 切片规范 + 抽取规则表 |
| 4 | 权限与时效设计 | 访问矩阵 + 时效台账 |
| 5 | 检索策略与评测集设计 | 检索策略书 + 评测集 |
| 6 | 试运行与调优 | 试运行报告 + 调优记录 |
| 7 | 上线与生命周期治理 | 上线评审表 + 治理运营手册 |

三条硬规则：
- 先治理再建库（口径不清就不要先上向量库）
- 先只读检索后写回引用
- 先有评测集后扩知识域

## 八、视觉规范（沿用前六册）

- 1280×720，硕磐橙红
- 主色 `#FA4F24`，辅色 `#F87D2F`，主文字 `#0F1423`
- 灰底 `#F7F7F8`，浅橙提示 `#FFF3EE` + `#FBA15C`
- 章节扉页：深色渐变 + 巨字编号
- A 标题区 height 96 / B 内容区 height 479 / C 页脚区 height 58

## 九、备注写入方案

`notes.json` 30 条，直接构造 `<p:sp>` 注入 `ppt/notesSlides/notesSlideN.xml`（slidep 生成的 notesSlide 是空壳，python-pptx 的 `notes_text_frame` 取不到）。
