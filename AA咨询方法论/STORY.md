# AA咨询方法论 · 30 页结构规划

> 独立成册的 AA（应用架构）方法论专册，内容依据《华为数据之道》业务/数据架构向应用层的传导逻辑 + 4A 贯通 + 企业架构治理通则
> 定位：硕磐咨询交付件 · 纯硕磐橙红体系 · 方法 8 / 内容 10 / 模板 12

## 承接口径
本册沿用主文档 `EA企业架构咨询方法论.pptx` 的 AA 骨架（能力映射 → 应用盘点 → 热力图评估 → 组合决策），
在此之上展开为 30 页完整专册，补齐四组内容：

- **应用架构的定位与治理模型**（主册缺失：应用架构到底管什么）
- **集成架构**（主册只在集成关系图里提了一句，没有方法与模板）
- **数据流与事件流**（DA 到 AA 的传导界面）
- **安全合规与架构治理机制**（谁维护、怎么评审、怎么退）

AA 的核心命题：**应用架构回答「用什么系统承载业务能力」**，
它是 BA 的能力与 DA 的数据之间的承载层，也是企业技术债的主要来源。

## 30 页结构

| # | 页码 | 类型 | 标题 | 归属 | 说明 |
|:-|:-|:-|:-|:-|:-|
| 01 | cover | hero | AA 应用架构咨询方法论 | — | 封面 |
| 02 | catalog | supporting | 本册七个部分 | — | 目录（7 条） |
| 03 | content | hero | 应用架构回答「用什么系统承载能力」 | 序 | AA 定位 + 4A 关系 |
| 04 | section | transition | PART 01 应用架构总论 | 总论 | 章节扉页 |
| 05 | content | supporting | 应用架构的三层结构骨架 | 总论 | 展现层 / 支撑层 / 数据访问层 |
| 06 | content | supporting | 五条应用架构原则 | 总论 | 原则清单（含对应代价） |
| 07 | content | supporting | 能力→应用→功能的传导模型 | 总论 | BA 到 AA 的映射链 |
| 08 | section | transition | PART 02 应用组合盘点 | 组件一 | 章节扉页 |
| 09 | content | supporting | 之方法：能力映射四问法 | 组件一 | METHOD |
| 10 | content | supporting | 之内容：应用全景清单与九类资产 | 组件一 | CONTENT |
| 11 | content | template | 之模板：应用卡片 | 组件一 | TEMPLATE |
| 12 | section | transition | PART 03 集成架构 | 组件二 | 章节扉页 |
| 13 | content | supporting | 之方法：集成四问法与四种集成模式 | 组件二 | METHOD |
| 14 | content | supporting | 之内容：集成清单、总线与接口标准 | 组件二 | CONTENT |
| 15 | content | template | 之模板：API 台账 + 集成契约卡 | 组件二 | TEMPLATE |
| 16 | section | transition | PART 04 组合评估与四态决策 | 组件三 | 章节扉页 |
| 17 | content | supporting | 之方法：价值×健康度二维评估 | 组件三 | METHOD |
| 18 | content | supporting | 之内容：建买集成退役四态判定 | 组件三 | CONTENT |
| 19 | content | template | 之模板：应用热力图 + 决策表 | 组件三 | TEMPLATE |
| 20 | section | transition | PART 05 数据流与事件流 | 组件四 | 章节扉页 |
| 21 | content | supporting | 之方法：数据消费识别法 | 组件四 | METHOD |
| 22 | content | supporting | 之内容：数据服务化与事件契约 | 组件四 | CONTENT |
| 23 | content | template | 之模板：数据服务目录 + 事件契约 | 组件四 | TEMPLATE |
| 24 | section | transition | PART 06 安全合规与架构治理 | 组件五 | 章节扉页 |
| 25 | content | supporting | 之方法：应用减法三步法 | 组件五 | METHOD |
| 26 | content | supporting | 之内容：治理机制、评审门与合规红线 | 组件五 | CONTENT |
| 27 | content | template | 之模板：应用退役清单 + 评审检查表 | 组件五 | TEMPLATE |
| 28 | content | supporting | 架构确定性：把技术不确定性关在笼子里 | 收口 | 整体收束 |
| 29 | content | supporting | 常见误区：五个把应用架构做砸的做法 | 收口 | 反面清单 |
| 30 | ending | hero | 结语：让应用承载能力，而不是承载历史 | — | 结束页 |

## 三段配比核对
- **方法页（METHOD）= 09, 13, 17, 21, 25** → 5 页（+ 总论 05/06/07 = 8）
- **内容页（CONTENT）= 03, 10, 14, 18, 22, 26, 28, 29** → 8 页（+ 目录 02 = 10）
- **模板页（TEMPLATE）= 11, 15, 19, 23, 27** → 5 页（+ 封面/章节/结束 = 12）

## 视觉规范
与 DA / BA 专册完全一致：
- 主色 #FA4F24 / 辅色 #F87D2F / 文字 #0F1423 / 底色 #FFFFFF
- 画布 1280×720，三区母版 A(0-120) / B(120-660) / C(660-720)
- 字体 微软雅黑 + Arial
- 页脚：`硕磐机密 · AA应用架构咨询方法论` + `NN / 30`

## 编译命令（shim 不可用，必须直调引擎）
```bash
NODE="C:/Users/gfjia/.workbuddy/binaries/node/versions/22.22.2-6/node.exe"
CLI="C:/Users/gfjia/.workbuddy/binaries/node/versions/22.22.2-6/lib/node_modules/@tencent/slidep/dist/index.js"
$NODE $CLI lint AA业务架构咨询方法论.pptx --dsl-file slides/NN.slide
$NODE $CLI create AA业务架构咨询方法论.pptx
$NODE $CLI upsert-dsl AA业务架构咨询方法论.pptx --dsl-file slides/NN.slide
```
## 备注写入（重要）
一律用 `slide_add_notes`，**不要**用 `slide_set_notes_text`（新文件备注页不存在，会报 SlideEditor::SetNo...）。