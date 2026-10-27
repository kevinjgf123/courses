# 《管道处理（Pipeline）咨询方法论》· 第八册 STORY

## 一、系列定位（八册）

| 专册 | 核心命题 | 一句话 |
|---|---|---|
| DA | 先有治，才有存 | 数据架构是枢纽 |
| BA | 能力与组织解耦 | 业务架构是基础 |
| AA | 应用数量增长带来技术债 | 应用架构是载体 |
| TA | 不押注单点技术 | 技术架构是底座 |
| Ontology | 语义与动力学合一 | 本体是 4A 的汇流点 |
| Agent | 明确谁来判断、权限多大、何时停手 | Agent 是 4A 的新实践点 |
| 知识库 | 知识要被治理，不只是被存起来 | 知识库是 4A 的新实践点 |
| **管道处理** | **数据进出本体必须可管、可追、可退** | **管道处理是 4A 的新实践点** |

## 二、核心主张

1. **管道处理不是 ETL 的新说法。** ETL 关心「把数据搬到哪」，管道处理关心「哪一版数据、在什么口径下、由谁、经过哪几步、进入了本体的哪个对象类型」。
2. **管道有两个方向，不是一个方向。** 进向是「源系统 → 本体」，出向是「本体 → 调用方」。绝大多数失败都发生在出向：读得进去，出不来；出得来，血缘断了。
3. **管道是业务应用，不是技术组件。** 它有自己的业务责任（谁对口径负责）、数据责任（三层数据）、应用责任（拓扑与编排）、技术责任（运行时与非功能）。
4. **管道的第一属性是「可退」。** 上生产之前必须能回答：这一版怎么来的、回滚到哪一版、谁批准的。
5. **先 batch，后 incremental，最后 streaming。** 反过来做，复杂度会指数上升。
6. **先只读取数，后 Action 写回。** 写回必须由 Logic 执行、且在发起人权限内。

## 三、Palantir 官方核实结论（本册引用依据）

### Data Connection
- 官方定义：以 **dataset transactions** 管理离散版本的数据框架，用于「随时间管理数据」
- 提供跨时间的完整血缘：能追溯哪个 sync task 产生了哪个版本的 dataset
- 支持 batch / streaming / media / CDC sync / virtual tables
- 支持增量同步，避免每次全量
- 细粒度安全：sync 集合甚至单个 sync 可按角色或分类级访问控制
- sync metadata 与 sync definition 分离，支持完整分支（branch），可在沙箱分支中测试新配置

### HyperAuto（SDDI）
- 三大组件：Connectors（双向大规模安全传输）/ Source exploration（引导式发现 + 批量同步）/ Automatic pipeline generation
- 自动生成管道四步：
  1. Source-specific preprocessing → 固定 schema 的元数据集
  2. Cleaning libraries → 标准化清洗
  3. Core generation → 数据富化、列重命名、去重、union
  4. Derived elements → join 表、时序数据集、富化列
- 可从 source 到 Ontology 全链路自动生成，产出人类可读代码（Spark），可 review / modify / test / version control，可 check-in 到 git
- 内置 SAP、Salesforce、NetSuite、HubSpot connector，兼容对象存储、流、JDBC、REST、NoSQL

### Snapshot vs Incremental
- 官方原文：只有当输入数据集通过 APPEND 或不修改既有文件的 UPDATE 事务变更时，增量才生效；把 snapshot 输入标成 incremental 无效
- 限制：join 时增量数据集必须在左侧；两个增量数据集 join 不支持；union 要求所有输入同一计算模式；窗口函数/聚合/pivot 只作用于当前事务；replay 只支持全量重放
- 可开启 **Require incremental execution**，非增量时作业直接失败，防止静默退化为 snapshot

### 管道开发标准流程
1. 设置推荐的 **Project 结构**（从一开始就组织数据安全与治理）
2. 在 Pipeline Builder 或 Code Repositories 创建 **batch pipeline**：处理输入、清洗过滤、join，产出高质量 dataset
3. 将最终 dataset **映射成 object types 与 link types**
4. 设置调度，使数据定期流动
5. 增强项：unit tests、branching and release、health checks

### 选型原则
- 多数情况先 batch，之后引入 incremental 提升性能、降低延迟
- 已知新数据规模极大时可从一开始设计为 incremental，但复杂度显著更高
- 流式管道只会和其最慢组件一样快，必须从设计之初就确保达到目标延迟与吞吐

### 互操作
- 所有数据保持原始格式（CSV / Iceberg / Parquet），通过 REST / JDBC / S3 访问
- **Multimodal Data Plane（MMDP）** + **Virtual Tables**：直接利用 Databricks / Snowflake / BigQuery 等已有资产，避免无谓复制
- Code interoperability：Python / Java / SparkSQL + Spark / Flink / DataFusion / Polars

### Data Health / Data Lineage
- Data Health 按 status / time / size / content / schema 五类维度设检查，可配严重级别与告警
- Data Lineage 可视化数据流动，展示一处健康问题如何影响下游

### Ontology 输出侧
- Data / Logic / Action 三类工具
- 官方原文：LLM 不能直接访问工具，只能请求使用工具，工具调用由 AIP Logic 在发起用户权限内执行
- Ontology 编辑必须从 Action 中执行 Logic 函数才生效
- 行列级访问控制只过滤读入提示词的数据，不覆盖输出与 Apply actions，需配分类级访问控制

## 四、公网管道处理理论（引用依据）

- ETL → ELT 演进：先清洗后入仓 vs 先入仓后建模
- 微批（micro-batch）与流批（stream-batch）混合
- 幂等性与可重放是增量管道两项前提
- 变更数据捕获（CDC）
- 血缘分三层：表级、字段级、任务级
- Data Contract 与 Producer / Consumer 责任划分
- 五类常见失效模式：静默漏数、口径漂移、延迟累积、重复处理、血缘断裂

## 五、30 页结构

| 页 | 标题 | 性质 |
|---|---|---|
| 01 | 封面 | 深色 |
| 02 | 目录 | 浅色 |
| 03 | 序论：为什么 4A 之后还要谈管道处理 | 浅色 |
| 04 | Approach 八阶段（含每阶段产出物） | 浅色 |
| 05 | PART 01 扉页 | 深色 |
| 06 | 管道处理到底是什么：双向两个方向 | 浅色 |
| 07 | Palantir 管道体系全景：源到本体、本体到应用 | 浅色 |
| 08 | Data Connection：把源系统管起来 | 浅色 |
| 09 | HyperAuto / SDDI：让元数据生成管道 | 浅色 |
| 10 | Snapshot vs Incremental：一条决定整条管道命运的选择 | 浅色 |
| 11 | PART 02 扉页 | 深色 |
| 12 | 方向一：数据源 → Ontology 的六道关口 | 浅色 |
| 13 | dataset transactions 与版本血缘 | 浅色 |
| 14 | 管道分支与发布：一次都不许直接改生产 | 浅色 |
| 15 | PART 03 扉页 | 深色 |
| 16 | 方向二：Ontology → 调用的三条出口 | 浅色 |
| 17 | 管道 × 知识库：知识抽取管道的特殊性 | 浅色 |
| 18 | 管道 × Agent：上下文供给与终止控制 | 浅色 |
| 19 | 管道 × Ontology：映射规则与写回边界 | 浅色 |
| 20 | 四者关系总览与三条硬边界 | 浅色 |
| 21 | PART 04 扉页 | 深色 |
| 22 | 管道处理的 4A 映射总览 | 浅色 |
| 23 | BA：管什么、谁负责、什么时候停 | 浅色 |
| 24 | DA：三层数据与十二项必建模元数据 | 浅色 |
| 25 | AA：管道拓扑与调用编排 | 浅色 |
| 26 | TA：运行时、调度与非功能 | 浅色 |
| 27 | 管道五道门 | 浅色 |
| 28 | 五类失败模式 | 浅色 |
| 29 | 上线评审 12 项 + 批→增→流三步演进 | 浅色 |
| 30 | 结语（串联八册主线） | 深色 |

## 六、Approach 八阶段

| # | 阶段 | 性质 | 做什么 | 产出物 |
|---|---|---|---|---|
| 1 | 源系统与场景盘点 | 治理 | 盘点源系统、要支撑的场景 | 源清单 + 场景清单 |
| 2 | 口径与映射设计 | 治理 | 定口径、划边界、设计到本体的映射 | 口径字典 + 本体映射表 |
| 3 | 接入与同步设计 | 设计 | 连接方式、同步频率、批次与事务 | 接入方案 + 同步模式表 |
| 4 | 加工与质量设计 | 设计 | 加工逻辑、清洗规则、质量检查 | 加工逻辑规范 + 质量规则表 |
| 5 | 版本与血缘设计 | 治理 | 版本策略、事务粒度、血缘矩阵 | 版本策略 + 血缘矩阵 |
| 6 | 分支与发布流程 | 工程 | 分支规范、评审、发布与回滚 | 分支规范 + 发布检查表 |
| 7 | 健康度与可观测设计 | 工程 | 五类健康检查、告警、血缘可视 | 健康检查清单 + 告警矩阵 |
| 8 | 演进与退役治理 | 运营 | 从批到增到流、旧管道退役 | 演进路线图 + 退役预案 |

三条硬规则：
- 先 batch 后 incremental 再 streaming
- 先只读取数后 Action 写回
- 先有血缘与健康检查再上生产

## 七、视觉规范

- 画布 1280×720
- 主色 `#FA4F24`，辅色 `#F87D2F`
- 主文字 `#0F1423`，灰辅助 `#F7F7F8` / `#E8E8E8`
- 浅橙提示 `#FFF3EE` + `#FBA15C`
- 章节扉页：深色 `#0F1423` → `#2A1810` 渐变 + 巨字编号
- 三区母版：A 标题 96 / B 内容 479 / C 页脚 58

## 八、备注写入方案

1. `notes.json` 30 条，风格：可直接演讲、不机械复述页面、不含教练话术
2. `write_notes.py` 两阶段：先用 python-pptx 访问 `slide.notes_slide` 触发骨架生成，再用 zipfile 注入 `<p:sp>`
3. 违规关键词检测：讲述要点 / 怎么讲 / 时长 / 本页 / 这页 / 要点一 / 讲稿 / 备注栏
4. 几何自检：形状不得越界（容差 9525 EMU）
