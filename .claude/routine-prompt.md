# Routine Prompt — UFO/UAP 每日归档

> 把本文件**全文**粘贴到 Claude Code Routine 的 prompt 字段。
> 触发频率：daily, 9:00 AM GMT+8 (= 1:00 UTC)。
> 仓库：`An9Yang/Alien-News-Collector`，**push 目标分支：`main`**。
> Routine 会话本身在自动生成的 `claude/<random>` 临时分支上运行，归档统一汇入 main。

---

你是这个仓库的归档器。先读 `CLAUDE.md` 与 `sources.md`，然后按以下流程执行**今天**（UTC）的归档。

## 0. 准备

```bash
TODAY=$(date -u +%Y-%m-%d)
mkdir -p archive/$TODAY/assets
# 当前会话已 base 在 main 最新快照上，不需要 pull。
```

## 1. 搜索（覆盖过去 24 小时）

对 `sources.md` 中**每一类**源执行 WebSearch / WebFetch，关键词组合：

- `UAP OR UFO OR "unidentified anomalous phenomena" OR "unidentified aerial phenomena"`
- `extraterrestrial OR alien` （排除 sci-fi、immigration 语境）
- `AARO OR "All-domain Anomaly Resolution Office"`
- `Pentagon UAP`, `NASA UAP`, `congressional UAP hearing`
- `PURSUE`, `war.gov/UFO`（战争部 2026 启动的 UAP 解密计划）

**用 `allowed_domains`** 把搜索限制到白名单域名，例如：

```
WebSearch(query="UAP Pentagon", allowed_domains=["defense.gov","war.gov","aaro.mil","nasa.gov","dni.gov","congress.gov","oversight.house.gov","intelligence.senate.gov","nytimes.com","washingtonpost.com","wsj.com","reuters.com","apnews.com","bbc.com","theguardian.com","bloomberg.com","thedebrief.org","liberationtimes.com"])
```

只保留**发布时间在过去 24 小时内**且与 UAP/UFO/外星人主题**实质相关**的条目。把候选列表写在 scratch（不要落盘）。

## 2. 去重

对每条候选 URL：

1. `grep -r "<url>"  archive/` 检查近 3 天是否已收录。
2. 若已存在 → 跳过。

## 3. 抓取与处理（对每条新候选执行）

按发现顺序分配序号 `NN = 01, 02, ...`。

### 3.1 抓原文

```
WebFetch(url=<原文链接>, prompt="Return the full article body verbatim, including subheadings, bylines, dateline, and image captions. Preserve paragraph breaks. List every image URL appearing in the article body with its caption.")
```

**WebFetch 被 403 / host_not_allowed 阻挡时**：退而求其次，用 WebSearch 在多个白名单 + 知名媒体域名上交叉检索同一事件，**多源核对事实点合成稿件**；在 frontmatter 标 `fetch_status: blocked-by-source` 与 `verification: needs-cross-check`，正文开头加一段【抓取说明】指明这是合成稿、待后续 Routine 用原文回填。参考实例：`archive/2026-05-09/01-dod-pentagon-uap-pursue-file-release.md`。

**如遇 paywall**：在 frontmatter 标 `paywalled: true`，正文存可获得的摘要并写明"完整原文需登录"。

### 3.2 下载图片

对每张图片：

```bash
python3 scripts/download_media.py "<image_url>" "archive/$TODAY/assets/${NN}-img-${k}"
```

脚本会按 Content-Type 自动加扩展名并打印最终路径。失败就保留 URL，不阻塞。

### 3.3 翻译

把英文原文逐段翻成简体中文。要求：

- 信达雅、不漏段、不总结代替翻译；
- 专有名词首次出现保留英文（中文译名后括号注英文）；
- 数字、日期、职衔尽量与原文对齐。

### 3.4 写文件

文件名 `archive/$TODAY/${NN}-<source>-<slug>.md`，按 `templates/article.md` 输出。frontmatter 字段必须齐全：

```yaml
---
title_en: ...
title_zh: ...
source: <短标签>
source_name: ...
url: ...
published_at: <ISO8601 UTC>
fetched_at: <ISO8601 UTC>
category: <见 CLAUDE.md 表>
authors: [...]
tags: [...]
images:
  - assets/01-img-1.jpg
paywalled: false
verification: standard   # 垂直媒体或合成稿用 needs-cross-check
fetch_status: ok          # 被 403 时用 blocked-by-source
---
```

正文：

```markdown
## Original (English)

<原文逐段，保留小标题、引文、图片插入位置>

## 简体中文译稿

<对应译文>

## 图片

![<caption EN>](assets/NN-img-1.jpg)

## 引用

- 原文链接：<url>
- 抓取时间：<fetched_at> UTC
```

## 4. 写当日索引

写 `archive/$TODAY/README.md`：

```markdown
# UFO / UAP 每日归档 · $TODAY (UTC)

抓取窗口：$TODAY UTC 00:00 ～ <现在 HH:MM>
共 N 篇

## 官方声明
- [01 · <英文标题>](./01-...md) — <中文标题>（<source_name>）

## 国会听证
- ...

## 新闻报道
- ...

（无内容的分类省略）
```

如果今天 0 篇：

```markdown
# UFO / UAP 每日归档 · $TODAY (UTC)

抓取窗口：$TODAY UTC 00:00 ～ <HH:MM>
共 0 篇 · 今日白名单源未发布相关内容。
```

## 5. 提交 → push 到 main

```bash
git add archive/$TODAY
N=$(ls archive/$TODAY/*.md 2>/dev/null | grep -v README.md | wc -l | tr -d ' ')

if [ "$N" -gt 0 ]; then
  MSG="archive: $TODAY · $N items"
else
  MSG="archive: $TODAY · empty day"
fi

git commit -m "$MSG"

# 关键：直接 push 到 main，不要 push 到当前会话分支
git push origin HEAD:main \
  || (git fetch origin main && git rebase origin/main && git push origin HEAD:main)
```

如果 push 仍失败（网络/冲突），最多重试 4 次（间隔 2s/4s/8s/16s）。

## 6. 报告

最后用 1-3 句话告诉用户今天抓了几篇、分别什么主题、是否有需要人工核实的（垂直源 / 合成稿）。**不要**重复正文内容。

---

## 小贴士

- 一篇都没抓到也要写 README 并提交，证明 Routine 跑过了。
- 翻译卡壳的句子用 `[原文]` 标出来不要硬翻。
- 图片下载脚本失败不要让全篇失败 —— 记录 URL，正文继续。
- 时间一律 UTC；用 `date -u` 不要用 local time。
- **Push 必须走 `git push origin HEAD:main`**：会话本身在 `claude/<random>` 临时分支，归档统一进 main，避免每次都新建一条分支。
- WebFetch 被 host_not_allowed 阻挡时，**回落到 WebSearch 多源交叉合成**，并标记 `fetch_status: blocked-by-source`、`verification: needs-cross-check`。
