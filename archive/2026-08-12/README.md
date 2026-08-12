# UFO / UAP 每日归档 · 2026-08-12 (UTC)

抓取窗口：2026-08-12 UTC 00:00 ～ 01:12
共 0 篇 · **本次运行未能抓取任何稿件**。

## 运行说明

本次 Routine 由 scheduler 触发后正常启动，但环境的网络出口策略（egress proxy）拒绝了对 `sources.md` 中**全部**白名单源的直接访问：

- `defense.gov` / `aaro.mil` / `nasa.gov` / `dni.gov` / `congress.gov` / `oversight.house.gov` / `intelligence.senate.gov` — WebFetch 与 `curl` 均返回 `403 Forbidden`（CONNECT tunnel failed）。
- `bloomberg.com` / `thedebrief.org` / `liberationtimes.com` — 同样被出口策略拦截。
- `nytimes.com` / `washingtonpost.com` / `wsj.com` / `reuters.com` / `apnews.com` / `bbc.com` / `theguardian.com` — WebSearch 返回 `400: domains not accessible to our user agent`。

WebSearch 尚可访问部分 `.gov` 域名的搜索索引（返回标题 + 链接 + 摘要），但**无法**拿到全文；按 `CLAUDE.md` 要求，正文需逐段翻译原文，不能靠摘要拼凑，因此本次不产出任何单篇归档。

## 需要人工处理

请为本仓库的 Claude Code on the Web 环境放行以下出口域名，以恢复日常抓取能力：

```
defense.gov aaro.mil nasa.gov dni.gov congress.gov
oversight.house.gov intelligence.senate.gov
bloomberg.com thedebrief.org liberationtimes.com
nytimes.com washingtonpost.com wsj.com reuters.com apnews.com
bbc.com theguardian.com
```

网络策略调整方式见 https://code.claude.com/docs/en/claude-code-on-the-web 。放行后下一次 Routine（14:00 UTC）将自动恢复。
