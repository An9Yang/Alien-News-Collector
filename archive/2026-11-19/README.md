# UFO / UAP 每日归档 · 2026-11-19 (UTC)

抓取窗口：2026-11-19 UTC 00:00 ～ 01:02
共 0 篇 · 今日白名单源未发布相关内容。

## 运行备注

- 官方源（defense.gov / aaro.mil / nasa.gov / dni.gov / congress.gov / oversight.house.gov / intelligence.senate.gov）：WebSearch 覆盖，过去 24 小时未命中 UAP 新发稿。AARO PURSUE 最新公开批次停留在 10 月 23 日（Department of War 第七批），11 月未见新条目。
- 顶级美媒（nytimes.com / washingtonpost.com / wsj.com / reuters.com / apnews.com）与 bbc.com / theguardian.com / bloomberg.com：**WebSearch 用户代理被拒**（HTTP 400），本次 Routine 无法覆盖。详见下方"已知限制"。
- 垂直源（thedebrief.org / liberationtimes.com）：WebSearch 覆盖，最新一篇为 Liberation Times 2026-11-17《Behind the White House's UFO Silence》，位于 24 小时窗口外。
- 全部白名单域名在本会话内 WebFetch 均返回 `ENOTFOUND`（DNS 未解析），说明云环境出口未对这些域名放行，无法做"按主页/栏目页回看"的二次确认。

## 已知限制（需人工介入）

1. **顶级美媒 WebSearch 封禁**：Anthropic WebSearch user-agent 当前被 NYT / WaPo / Reuters / AP / BBC / Guardian / WSJ / Bloomberg 拒绝，Routine 覆盖范围实际收窄到官方源 + 垂直源。
2. **WebFetch 域名未放行**：本会话 Agent Proxy 未放行白名单任何域名，无法抓取原文正文。即便搜索命中条目，当前流程也无法完成 3.1 节"抓原文"。
3. 建议在 Environment 的 network policy 里显式放行 `defense.gov`、`aaro.mil`、`nasa.gov`、`dni.gov`、`congress.gov`、`oversight.house.gov`、`intelligence.senate.gov`、`thedebrief.org`、`liberationtimes.com`；并为顶级美媒配置替代抓取路径（RSS、官方 feed 或 MCP 代理）。
