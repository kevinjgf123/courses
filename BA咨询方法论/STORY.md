# BA咨询方法论 · 30 页结构规划

> 独立成册的 BA（业务架构）方法论专册，内容依据《华为数据之道》业务架构章节 + 企业架构 4A 贯通逻辑
> 定位：硕磐咨询交付件 · 纯硕磐橙红体系 · 方法 8 / 内容 10 / 模板 12

## 承接口径
本册沿用主文档 `EA企业架构咨询方法论.pptx` 的 BA 四步法骨架
（价值流分析 → 能力识别 → 能力评估 → 能力地图构建），
在此之上展开为 30 页完整专册，补齐战略解码、组织映射、能力落地三段。

BA 的核心命题：**业务架构回答「做什么业务、凭什么做」**，
它决定了 DA/AA/TA 的共同起点，也是 4A 集成的枢纽。

## 30 页结构

| # | 页码 | 类型 | 标题 | 归属 | 说明 |
|:-|:-|:-|:-|:-|:-|
| 01 | cover | hero | BA 业务架构咨询方法论 | — | 封面 |
| 02 | catalog | supporting | 本册七个部分 | — | 目录（7 条） |
| 03 | content | hero | 业务架构回答「做什么业务、凭什么做」 | 序 | BA 定位 + 4A 关系 |
| 04 | section | transition | PART 01 业务架构总论 | 总论 | 章节扉页 |
| 05 | content | supporting | 业务架构的四层结构骨架 | 总论 | 战略→价值流→能力→组织 |
| 06 | content | supporting | 五条业务架构原则 | 总论 | 原则清单 |
| 07 | content | supporting | BA 与 DA/AA/TA 的贯通关系 | 总论 | 4A 集成链 |
| 08 | section | transition | PART 02 战略解码与价值流 | 组件一 | 章节扉页 |
| 09 | content | supporting | 之方法：战略解码五步法 | 组件一 | METHOD |
| 10 | content | supporting | 之内容：价值流识别与绘制 | 组件一 | CONTENT |
| 11 | content | template | 之模板：价值流图 + 符号规范 | 组件一 | TEMPLATE |
| 12 | section | transition | PART 03 业务能力识别 | 组件二 | 章节扉页 |
| 13 | content | supporting | 之方法：价值流→能力两问法 | 组件二 | METHOD |
| 14 | content | supporting | 之内容：能力域/能力组/能力项三层分解 | 组件二 | CONTENT |
| 15 | content | template | 之模板：业务能力卡片 | 组件二 | TEMPLATE |
| 16 | section | transition | PART 04 能力评估与热力图 | 组件三 | 章节扉页 |
| 17 | content | supporting | 之方法：成熟度×重要度二维评估 | 组件三 | METHOD |
| 18 | content | supporting | 之内容：五级成熟度定义与判断依据 | 组件三 | CONTENT |
| 19 | content | template | 之模板：能力热力图 + 评估打分表 | 组件三 | TEMPLATE |
| 20 | section | transition | PART 05 能力地图与组织映射 | 组件四 | 章节扉页 |
| 21 | content | supporting | 之方法：能力—组织—岗位映射三线法 | 组件四 | METHOD |
| 22 | content | supporting | 之内容：能力地图绘制与缺口识别 | 组件四 | CONTENT |
| 23 | content | template | 之模板：组织映射表 + 能力地图底图 | 组件四 | TEMPLATE |
| 24 | section | transition | PART 06 能力落地与治理 | 组件五 | 章节扉页 |
| 25 | content | supporting | 之方法：能力路线图与变革举措编排 | 组件五 | METHOD |
| 26 | content | supporting | 之内容：能力运营机制与考核指标 | 组件五 | CONTENT |
| 27 | content | template | 之模板：能力路线图 + 运营看板 | 组件五 | TEMPLATE |
| 28 | content | supporting | 四层贯通：战略到能力的因果链 | 收口 | 端到端链路 |
| 29 | content | supporting | 常见误区：五个做砸业务架构的坑 | 收口 | 反面清单 |
| 30 | ending | hero | 结语：业务架构让战略落地有路径 | — | 结束页 |

## 三段配比核对
- **方法页（METHOD）= 09, 13, 17, 21, 25** → 5 页（+ 总论 05/06/07 = 8）
- **内容页（CONTENT）= 03, 10, 14, 18, 22, 26, 28, 29** → 8 页（+ 目录 02 = 10）
- **模板页（TEMPLATE）= 11, 15, 19, 23, 27** → 5 页（+ 封面/章节/结束 = 12）

## 视觉规范
与 DA 专册完全一致：
- 主色 #FA4F24 / 辅色 #F87D2F / 文字 #0F1423 / 底色 #FFFFFF
- 画布 1280×720，三区母版 A(0-120) / B(120-660) / C(660-720)
- 字体 微软雅黑 + Arial
- 页脚：`硕磐机密 · BA业务架构咨询方法论` + `NN / 30`

## 编译命令
```bash
NODE="C:/Users/gfjia/.workbuddy/binaries/node/versions/22.22.2-6/node.exe"
CLI="C:/Users/gfjia/.workbuddy/binaries/node/versions/22.22.2-6/lib/node_modules/@tencent/slidep/dist/index.js"
$NODE $CLI lint   slides/NN.slide
$NODE $CLI create BA业务架构咨询方法论.pptx
$NODE $CLI upsert-dsl BA业务架构咨询方法论.pptx --dsl-file slides/NN.slide
```