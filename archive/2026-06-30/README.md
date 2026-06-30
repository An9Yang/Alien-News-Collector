# UFO / UAP 每日归档 · 2026-06-30 (UTC)

抓取窗口：2026-06-30 UTC 00:00 ～ 01:15
共 0 篇 · 本次 Routine 未能完成正常抓取。

## 运行说明

本次 Routine 通过 WebSearch 检索了 `sources.md` 中的白名单域名，但所有 WebFetch 与 `curl` 请求被环境出口代理拒绝（CONNECT 403）。被阻断的域名包括：

- `www.war.gov`
- `www.defense.gov`
- `www.aaro.mil`
- `thedebrief.org`
- `www.liberationtimes.com`

由于无法读取任何原文正文，不能生成符合 `templates/article.md` 要求（逐段中英对照）的归档文件，因此今日不落盘任何 `NN-*.md`。

需要管理员检查并放开上述白名单域名的 egress 策略，参考 `/root/.ccr/README.md`。

## 经 WebSearch 浮现的过去 24 小时候选（未抓取，需人工核实）

- **法国国民议会 UAP 公共议会研讨会**（2026-06-29，巴黎，Victor-Hugo Hall）
  - "La recherche sur les phénomènes aérospatiaux non identifiés au-delà des fantasmes"
  - 由 Arnaud Saint-Martin（LFI-NFP，塞纳-马恩省议员）与 Pierre Henriet（Horizons & Indépendants，旺代省议员）联合发起，CNES/GEIPAN 支持
  - 候选英文报道：The Debrief — "Scientists and Government Officials Convene in Paris to Explore UAP Science, Testimonies, and Policy"
    `https://thedebrief.org/scientists-and-government-officials-convene-in-paris-to-explore-uap-science-testimonies-and-policy/`
- **Pentagon PURSUE Release 02 / 后续视频**（仍处预告阶段，最新 PURSUE 第三批发布日期为 2026-06-12，不在 24 小时窗口内）
  - `https://www.war.gov/ufo/`
- **众议院 Federal Secrets 解密专项任务组 UAP 听证（2026-06-25）**：超出 24 小时窗口

## 下次 Routine 建议

1. 优先恢复 `war.gov`、`aaro.mil`、`thedebrief.org`、`liberationtimes.com` 的出口访问；
2. 若仍受限，考虑在 Routine 中加入 fallback 数据源或人工导入流程。
