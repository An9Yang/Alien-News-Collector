# UFO / UAP 每日归档 · 2026-05-24 (UTC)

抓取窗口：2026-05-24 UTC 00:00 ～ 01:15
共 1 篇

> 备注：本仓库 Routine 首次跑批。当前 24 小时窗口内的主导新闻是
> **5 月 22 日（星期五）美国战争部 PURSUE 第二批 UAP 档案发布**，相关后续报道
> 与官方页面更新持续到 5 月 23 日。本次归档纳入这份官方稿作为基准件；其他白名单
> 媒体（NYT/WaPo/WSJ/Reuters/AP/BBC/Guardian 等）在本沙箱环境下被搜索代理
> 拒绝（"domain not accessible to our user agent"），未能纳入；垂直源 The Debrief
> 与 Liberation Times 的相关稿件均在 5 月 21 日及更早，超出 24 小时窗口，未纳入。

## 官方声明
- [01 · Department of War Publishes Second Release of Unidentified Anomalous Phenomena Files on WAR.GOV/UFO](./01-dod-pursue-second-uap-release.md) — 美国战争部发布第二批不明异常现象（UAP）档案，登录 WAR.GOV/UFO（U.S. Department of War）

## 运行环境注记

- **网络**：沙箱出站走白名单代理，war.gov / aaro.mil / thedebrief.org / liberationtimes.com / bloomberg.com 等域名的 `WebFetch`、`curl`、`urllib` 均返回 `HTTP 403 / Host not in allowlist`。
- **可用工具**：仅 `WebSearch`（且 nytimes/wapo/wsj/reuters/apnews/bbc/guardian 等域名被搜索 user-agent 屏蔽）。
- **影响**：
  - 文章正文无法以"逐段 verbatim"方式取得，已基于多源 `WebSearch` 摘要交叉核对重建，直接引语已多家媒体复核；转述/概述段在正文里已明确标注。
  - 图片无法落盘，候选 URL 写在 `assets/01-img-1-unavailable.txt`，留待可联网环境补抓。
- **下一次 Routine**：建议在 cloud 环境的 network policy 中把以下域名加入出站白名单，可显著改善抓取完整度：
  - `war.gov`, `defense.gov`, `aaro.mil`, `nasa.gov`, `dni.gov`, `congress.gov`, `oversight.house.gov`, `intelligence.senate.gov`
  - `thedebrief.org`, `liberationtimes.com`, `bloomberg.com`
  - （nytimes/wapo/wsj/reuters/apnews/bbc/guardian 即使加白名单，WebSearch 仍会拒绝；考虑改用付费 API 或客户端抓取）
