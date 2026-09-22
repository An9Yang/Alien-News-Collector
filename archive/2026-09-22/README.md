# UFO / UAP 每日归档 · 2026-09-22 (UTC)

抓取窗口：2026-09-22 UTC 00:00 ～ 01:10
共 0 篇 · 今日 Routine 未能从白名单源抓取任何内容。

## 运行说明

本次 Routine 运行环境的出口网络策略拒绝了 `sources.md` 中**全部**白名单域名的 HTTPS 访问（代理返回 403 CONNECT tunnel failed）。已确认以下域名均不可达：

- 官方：`defense.gov`, `aaro.mil`, `nasa.gov`, `dni.gov`, `congress.gov`, `oversight.house.gov`, `intelligence.senate.gov`
- 顶级美媒：`nytimes.com`, `washingtonpost.com`, `wsj.com`, `reuters.com`, `apnews.com`
- 国际权威：`bbc.com`, `theguardian.com`, `bloomberg.com`
- UAP 垂直：`thedebrief.org`, `liberationtimes.com`

WebSearch 可以返回标题与摘要片段，但 WebFetch 无法拉取原文正文，因此无法按模板完成双语归档与图片下载。

搜索片段中显示，过去 24 小时内可能与 UAP 相关的候选（均非白名单源，未收录）：

- The Gazette (gazette.com) 2026-09-21 · "Feds declassify two more Pikes Peak area UAP sightings"

后续 Routine 需要用户在环境配置里放行上述白名单域名（或调整 `sources.md`）才能恢复正常归档。
