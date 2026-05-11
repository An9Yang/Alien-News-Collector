# 仓库说明（给 Claude）

这个仓库是一个**自动化新闻归档器**，专门收集美国官方与权威媒体发布的 UFO / UAP / 外星人相关报道。每天由一个 Routine 触发，由你（Claude）执行抓取、翻译、归档、提交。

如果你看到这个文件，说明你正运行在本仓库的 Claude Code 会话里。请遵守以下规范。

## 任务来源

- **Routine prompt** 位于 `.claude/routine-prompt.md`，那是日常运行时的入口指令。
- **来源白名单** 位于 `sources.md`，**只**抓里面列出的源；不要使用 Reddit、Twitter、阴谋论站点。
- **单篇模板**位于 `templates/article.md`。

## 归档约定

### 目录结构

```
archive/
└── YYYY-MM-DD/                  # UTC 日期，仅在当日有内容时创建
    ├── README.md                # 当日索引
    ├── 01-<source>-<slug>.md    # 第一篇
    ├── 02-<source>-<slug>.md
    └── assets/
        ├── 01-img-1.jpg
        └── 02-img-1.png
```

**空白日（0 篇）不创建目录、不写文件、不提交。运行记录看 Routine 详情页即可。**

### 文件命名

- `<source>` 用短标签：`dod`, `aaro`, `nasa`, `odni`, `nyt`, `wapo`, `wsj`, `reuters`, `ap`, `bbc`, `guardian`, `bloomberg`, `debrief`, `liberation`, `congress`。
- `<slug>` 用英文标题前 4-6 个实词的 kebab-case，例如 `pentagon-uap-historical-record`。
- 序号 `NN` 从 `01` 开始，按发现顺序递增。

### 单篇文件格式

严格按 `templates/article.md` 输出，前置 YAML frontmatter 包含：

```yaml
---
title_en: <英文原标题>
title_zh: <简体中文译标题>
source: <短标签，如 nyt>
source_name: <The New York Times>
url: <原文链接>
published_at: <ISO 8601，原文发布时间，UTC>
fetched_at: <ISO 8601，本次抓取的 UTC 时间>
category: <见下方分类>
authors:
  - <作者 1>
tags:
  - UAP
  - <其他>
images:
  - assets/01-img-1.jpg
fetch_status: ok            # 被 403 时用 blocked-by-source
verification: standard      # 垂直源 / 合成稿用 needs-cross-check
---
```

正文部分按模板分两栏：先英文原文，再"## 简体中文译稿"。译稿要求：

- 信达雅，不要直译生硬；专有名词首次出现保留英文原名（括号里）。
- 数字、日期、人名职衔尽量与英文原文对齐。
- 不要漏段、不要总结代替翻译。

### 分类（category 字段使用英文 slug，索引页展示中文）

| slug | 中文 | 说明 |
|---|---|---|
| `official-statement` | 官方声明 | DoD/DoW/AARO/NASA/ODNI 的新闻稿、声明、报告发布 |
| `congressional-hearing` | 国会听证 | 国会听证会、证词、议员声明 |
| `document-disclosure` | 文件解密 | FOIA 解密、官方档案公开（如 PURSUE 计划批次） |
| `news-report` | 新闻报道 | 媒体的事件性报道 |
| `investigative-report` | 深度调查 | 长篇调查、独家爆料 |
| `sighting-event` | 目击事件 | 具体目击案例的报道 |
| `analysis-opinion` | 分析评论 | 分析、评论、社论（仅在内容含实质信息时收录） |

### 图片处理

- 每篇文章里的图片用 `scripts/download_media.py <url> <dest_path>` 下载到 `archive/YYYY-MM-DD/assets/`。
- 命名 `NN-img-1.<ext>`，`NN` 与文章序号一致，`<ext>` 由 Content-Type 决定。
- 在 Markdown 里用相对路径引用：`![caption](assets/01-img-1.jpg)`。
- 如果原页面图片下载失败，记录原图 URL 但不要让整篇失败。

### 当日索引 `archive/YYYY-MM-DD/README.md`

仅在当天至少抓到 1 篇时才写：

```markdown
# UFO / UAP 每日归档 · YYYY-MM-DD (UTC)

抓取窗口：YYYY-MM-DD UTC 00:00 ～ HH:MM
共 N 篇

## 官方声明
- [01 · 英文标题](./01-aaro-...md) — 中文标题（Source）

## 新闻报道
- ...
```

## 去重

写入前快速检查 `archive/<前 2 天>/README.md` 与今天的 README 是否已有同一 URL。已抓过就跳过。

## 提交规范

- **有抓到稿子才提交**：
  - Commit message：`archive: YYYY-MM-DD · N items`。
  - Commit body 列出每条 URL，方便回溯。
- **0 篇的日子不创建目录、不提交**。运行记录看 Routine 详情页即可，避免仓库被空的 day stub 污染。
- **Push 到 `main`**，使用 `git push origin HEAD:main`。Routine 会话本身在自动生成的 `claude/<random>` 会话分支上，但归档**统一进 main**。
- 如果 push 因冲突失败：`git fetch origin main && git rebase origin/main && git push origin HEAD:main`。

## 安全与版权

- 只抓白名单内源；不抓需要登录的私域内容；遇到付费墙就只抓摘要并标注 `paywalled: true`。
- 翻译稿仅供个人研究/存档；不公开发布或商业使用。
