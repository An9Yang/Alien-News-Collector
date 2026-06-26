# UFO / UAP 每日归档 · 2026-06-26 (UTC)

抓取窗口：2026-06-26 UTC 00:00 ～ 01:05
共 0 篇 · 抓取受阻：执行环境出站策略拦截全部白名单源。

## 运行状况

WebSearch 仍可返回标题与摘要，但 WebFetch / curl 对以下白名单域名一律被 egress 代理在 CONNECT 阶段以 HTTP 403 拒绝（`gateway answered 403 to CONNECT (policy denial or upstream failure)`）：

- `defense.gov`, `www.defense.gov`
- `www.aaro.mil`
- `www.nasa.gov`
- `www.dni.gov`
- `www.congress.gov`
- `oversight.house.gov`
- `www.intelligence.senate.gov`
- `www.bloomberg.com`
- `thedebrief.org`
- `www.liberationtimes.com`

顶级美媒 (`nytimes.com` / `washingtonpost.com` / `wsj.com` / `reuters.com` / `apnews.com`) 与 BBC、Guardian 同时被 WebSearch 的 user-agent 策略屏蔽 (`400: domains not accessible to our user agent`)。

由于无法获取任一原文正文，本次未生成任何篇章；按归档约定写入空索引以证明 Routine 已执行。

## 待处理

请运维方在该会话的 egress policy 中放行 `sources.md` 白名单域名（至少 `defense.gov` / `aaro.mil` / `nasa.gov` / `dni.gov` / `congress.gov` / `oversight.house.gov` / `intelligence.senate.gov` / `thedebrief.org` / `liberationtimes.com` / `bloomberg.com`），否则后续日常 Routine 同样无法落稿。
