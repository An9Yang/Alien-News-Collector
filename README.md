# Alien News Collector

一个云端 Routine 任务，每天自动抓取、翻译并归档美国官方与权威媒体发布的 UFO / UAP / 外星人相关报道。

## 工作方式

1. **Claude Code Routine**（claude.com/code）按日程触发，连接到本仓库。
2. 每次触发时 Claude 会：
   - 读取 [`sources.md`](./sources.md) 中的白名单源；
   - 搜索过去 24 小时内的 UFO / UAP / extraterrestrial 相关内容；
   - 抓取原文、下载图片、翻译为简体中文；
   - 按当天日期写入 `archive/YYYY-MM-DD/` 目录；
   - 更新当日索引、提交并推送。
3. 你后续在 GitHub 或本地 `git pull` 即可查看。

## 仓库结构

```
.
├── README.md                  # 你正在看的这份
├── CLAUDE.md                  # 仓库内常驻的 Claude 行为规范
├── sources.md                 # 监控源白名单（按类别）
├── .claude/
│   └── routine-prompt.md      # 粘贴到 Routine 配置里的 prompt
├── templates/
│   └── article.md             # 单篇双语稿模板
├── scripts/
│   └── download_media.py      # 图片/媒体下载小工具
└── archive/
    └── YYYY-MM-DD/
        ├── README.md          # 当日索引（中英双语标题列表）
        ├── NN-<source>-<slug>.md
        └── assets/
            └── NN-img-1.jpg
```

## 配置 Routine（一次性）

1. 把本仓库推送到 GitHub（参考下方命令）。
2. 打开 https://claude.com/code ，进入 **Routines**。
3. 点击 **New Routine**：
   - **Repository**：连接到 `An9Yang/Alien-News-Collector`，分支 `main`（合并后）。
   - **Schedule**：`0 14 * * *`（每天 UTC 14:00，约北京时间 22:00 / 美东上午 9-10 点）。
   - **Prompt**：复制 [`.claude/routine-prompt.md`](./.claude/routine-prompt.md) 全文粘贴。
   - **Permissions**：允许 `Bash(git push)`、`WebFetch`、`WebSearch`、`Write`、`Edit`。
4. 保存即生效。也可以点 **Run now** 立刻试跑一次。

## 修改频率或来源

- 改时间 → Routine 配置里改 cron。
- 改来源 → 编辑 `sources.md` 后 commit；下次 Routine 自动用新清单。
- 加字段 / 调模板 → 改 `templates/article.md` 与 `CLAUDE.md` 中的"产出格式"小节。

## 本地查看

```bash
git pull origin main
ls archive/
```

每个 `archive/YYYY-MM-DD/README.md` 都列出当天抓到的所有报道及其分类，逐篇 Markdown 都包含原文链接、英文原文、简体中文译稿和本地图片。

## License

仅供个人研究/存档使用。所有抓取的原文版权归原媒体所有，本仓库仅做引用与翻译。
