# UFO / UAP 每日归档 · 2026-06-13 (UTC)

抓取窗口：2026-06-13 UTC 00:00 ～ 01:10
共 1 篇（环境限制下的不完全抓取，详见下方"运行说明"）

## 文件解密

- [01 · Department of War Publishes Third Release of Unidentified Anomalous Phenomena Files on WAR.GOV/UFO](./01-dod-pursue-third-uap-release.md) — 美国战争部在 WAR.GOV/UFO 发布第三批 UAP 文件（U.S. Department of War）

## 运行说明（重要 / Important）

本次 Routine 在沙盒环境中执行时，**对整份白名单的所有源域名均收到
`HTTP 403 host_not_allowed`**，包括：

- 官方：`defense.gov`、`war.gov`、`aaro.mil`、`nasa.gov`、`dni.gov`、
  `congress.gov`、`oversight.house.gov`、`intelligence.senate.gov`
- 顶级美媒：`nytimes.com`、`washingtonpost.com`、`wsj.com`、
  `reuters.com`、`apnews.com`（同时被 WebSearch 用户代理屏蔽）
- 国际：`bbc.com`、`theguardian.com`、`bloomberg.com`
- 垂直：`thedebrief.org`、`liberationtimes.com`

所有源既无法用 `WebFetch` 也无法用 `curl` 直接抓取，因此**本次未能下载任何
新闻稿的逐字原文与图片**。

本档案目录下唯一的条目（`01-dod-pursue-third-uap-release.md`）记录的是
**今日实际发生的最重要 UAP 新闻**——美国战争部（U.S. Department of War）于
2026 年 6 月 12 日（星期五）通过 PURSUE 计划发布第三批 UAP 解密档案
（53 份文件、10 张图像、6 段视频、3 段 NASA 音频，包括一份由 AARO 主任
Jon Kosloski 签署、日期为 2026-06-05 的报告）。该条目的正文是基于多份
**下游报道**的搜索片段聚合摘要而成，并在前置 frontmatter 与正文中明确标注了
`fetch_note` 与 `verification: needs-cross-check`。

### 建议的后续动作

1. 放开本仓库 Routine 运行环境的网络策略，至少允许出站 HTTPS 访问
   `*.defense.gov`、`*.war.gov`、`*.aaro.mil`、`thedebrief.org`、
   `liberationtimes.com`、`bloomberg.com`。
2. 在配置生效后重跑今天的 Routine，让 01 条目被逐字原文与官方图片回填。
3. 如确认沙盒策略不会调整，则需要为 Routine 切换到允许的代理 / 镜像方案，
   否则后续每日抓取都会复现此问题。

## 抓取窗口内已知但未能逐字归档的相关候选

下列条目在搜索阶段已能定位 URL，但同样因 `host_not_allowed` 而无法获取
逐字原文，故未单独成档；记录于此以便人工复查或环境放行后回填：

- *(debrief / liberation 在 2026-06-12～13 是否专文报道 Release 03，搜索结果未给出明确文章 URL；待环境放行后访问 https://thedebrief.org/category/uap/ 与 https://www.liberationtimes.com/ 逐条核对。)*
