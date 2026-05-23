# UFO / UAP 每日归档 · 2026-05-23 (UTC)

抓取窗口：2026-05-22 UTC 14:00 ～ 2026-05-23 UTC 01:25
共 1 篇

## 官方声明
- [01 · Department of War Publishes Second Release of Unidentified Anomalous Phenomena Files on WAR.GOV/UFO](./01-dod-second-release-uap-files-pursue.md) — 美国战争部在 WAR.GOV/UFO 发布第二批"不明异常现象"档案（U.S. Department of War）

## 运行说明

本次 Routine（cron `0 14 * * *` UTC，触发时间 2026-05-23T01:05Z）运行时，沙箱出向网络对绝大多数白名单域名（war.gov、aaro.mil、nasa.gov、thedebrief.org、liberationtimes.com、bloomberg.com 等）的直连 HTTP 请求返回 **403 Forbidden**，仅 WebSearch 的摘要可用。

- 已检索过去 24 小时窗口内的全部白名单源，并对 WebSearch 返回的 The Debrief / Liberation Times / Bloomberg / 官方域名等候选条目逐一尝试 WebFetch，均失败。
- The Debrief 的 "Pentagon Poised to Release New Batch of UAP Videos Under PURSUE Initiative"（约 5 月 22 日）与本次官方发布同主题，且属于事前预告型报道；因无法取得正文逐字内容，未单独入档以避免"以摘要代替翻译"。
- Liberation Times 当前首页文章 "UFO Transparency Stalls Again" 的发布日期为 **2025 年 12 月 14 日**，不在 24 小时窗口内，跳过。
- 今日唯一确认入档的事件为 **5 月 22 日 PURSUE 第二批档案发布**（官方）。文章正文中的 Hegseth 引语等关键表述在多家二级信源中表述一致，可信度较高，但**未经 war.gov 原页面逐字校对**，frontmatter 标记 `verification: needs-cross-check`。

如沙箱网络策略后续放宽，建议人工/下一轮 Routine 重新抓取 war.gov 原页面与同主题 Debrief / Bloomberg 报道，将 verification 升级为 `standard`，并补抓配图。
