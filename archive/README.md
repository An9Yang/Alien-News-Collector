# Archive

每个子目录是一个 UTC 日期，由 Routine 自动生成。

```
archive/
└── 2026-05-09/
    ├── README.md            # 当日索引（按分类）
    ├── 01-aaro-...md        # 单篇双语稿（带 frontmatter）
    ├── 02-nyt-...md
    └── assets/
        ├── 01-img-1.jpg
        └── 02-img-1.png
```

## 怎么读

1. 打开当日 `README.md` 看摘要与分类。
2. 点进具体文章，frontmatter 给出 source / url / published_at / category。
3. 正文先英文原文，后简体中文译稿。
4. 图片走 `assets/` 相对引用，离线也能看。

## 找历史

- 按日期：直接进对应目录。
- 按主题：在仓库根 `git grep "<keyword>" archive/`。
- 按来源：`grep -lr "^source: nyt" archive/`。
