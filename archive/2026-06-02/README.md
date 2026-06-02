# UFO / UAP 每日归档 · 2026-06-02 (UTC)

抓取窗口：2026-06-02 UTC 00:00 ～ 01:10
共 0 篇 · 今日白名单源未发现过去 24 小时内发布的相关内容。

## 运行说明

- 已对白名单（DoD / AARO / NASA / ODNI / Congress / House Oversight / Senate Intel /
  NYT / WaPo / WSJ / Reuters / AP / BBC / Guardian / Bloomberg /
  The Debrief / Liberation Times）执行 WebSearch 关键词组合：
  `UAP`、`UFO`、`unidentified anomalous phenomena`、`AARO`、`Pentagon UAP`、
  `NASA UAP`、`PURSUE`、`congressional UAP hearing`。
- 搜索片段中可见的最新一批新闻仍聚集在 2026 年 5 月初的 PURSUE 首轮释出
  和 2026 年 3 月 31 日 Luna 议员致 Hegseth 部长的 46 段视频请求信，
  没有发现明确署期为 2026-06-01 或 2026-06-02 的新条目。
- 本次容器的出站网络策略对所有白名单 host 返回 `403 host_not_allowed`，
  WebFetch 无法拉取全文以核验发布时间或生成英中对照译稿。
  Routine 因此无法完成"抓取 → 翻译 → 归档"的全流程。
- 如需在后续 Routine 中正常归档，请在环境的 network policy 中放行
  `sources.md` 中列出的官方与媒体域名（至少包含 `aaro.mil`、`defense.gov`、
  `nasa.gov`、`dni.gov`、`congress.gov`、`oversight.house.gov`、
  `intelligence.senate.gov`、`thedebrief.org`、`liberationtimes.com`、
  `bloomberg.com`）。
