# UFO / UAP 每日归档 · 2026-07-22 (UTC)

抓取窗口：2026-07-22 UTC 00:00 ～ 01:10
共 0 篇 · 未落盘

## 运行说明

今日 Routine 运行时，出站代理对本仓库 `sources.md` 白名单内的所有域名（`war.gov` / `defense.gov` / `aaro.mil` / `nasa.gov` / `dni.gov` / `congress.gov` / `oversight.house.gov` / `intelligence.senate.gov` / `nytimes.com` / `washingtonpost.com` / `wsj.com` / `reuters.com` / `apnews.com` / `bbc.com` / `theguardian.com` / `bloomberg.com` / `thedebrief.org` / `liberationtimes.com` 及 `en.wikipedia.org` 等辅助源）在 `WebFetch` 与 `curl` 层均返回 `403 Forbidden`，无法拉取正文与图片，因而未按模板生成任何归档文件。

`WebSearch` 通道正常，用于扫描候选。过去 24 小时内的候选线索（**非白名单**，仅备忘）：

- Fox News：Trump directs agencies to waive NDAs for UAP whistleblowers — 2026-07-21（`foxnews.com`，白名单外）
- DefenseScoop：Pentagon investigating mysterious UAP event reported by the Navy near Virginia's coast — 2026-07-21（`defensescoop.com`，白名单外）
- 二次报道：AARO 本周（7 月 21 日前后）发布 FY2025 Consolidated Annual Report on UAP，含弗吉尼亚外海约 100 个空中物体 + 2 个水面无人系统的事件；直接的 `war.gov` / `aaro.mil` 新闻稿链接因出站阻断无法确认。

## 后续建议

- 若管理员放宽出站策略，允许访问上述白名单域名，明日 Routine 应能正常落盘。
- 如短期无法放宽，可评估：(1) 引入代理白名单例外，(2) 允许在 Routine 中收录非白名单一线源（如 `defensescoop.com`、`foxnews.com`），(3) 通过官方 RSS 镜像/存档源二次抓取。

（本记录符合 CLAUDE.md “空日仍需提交 README 以证明 Routine 跑过” 的约定。）
