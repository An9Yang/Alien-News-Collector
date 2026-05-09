# 监控源白名单

Routine 仅抓取本文件列出的源。新增 / 删除源 → 改本文件 → commit；下次 Routine 自动生效。

短标签（`source` 字段）出现在文件名和 frontmatter 里。

## 1. 美国官方 (Official)

| 短标签 | 名称 | 主要入口 | 备注 |
|---|---|---|---|
| `dod` | U.S. Department of Defense | https://www.defense.gov/News/Releases/ | 五角大楼新闻稿 |
| `aaro` | All-domain Anomaly Resolution Office | https://www.aaro.mil/News/ | UAP 主管机构 |
| `aaro-cases` | AARO Case Resolution Reports | https://www.aaro.mil/Resolved-Cases/ | 已结案目击 |
| `nasa` | NASA UAP | https://science.nasa.gov/uap/ | NASA 独立研究小组 |
| `odni` | Office of the Director of National Intelligence | https://www.dni.gov/index.php/newsroom | 含 UAP 年度报告 |
| `congress` | U.S. Congress hearings | https://www.congress.gov/ | UAP 听证会、议案 |
| `house-oversight` | House Oversight Committee | https://oversight.house.gov/ | 历次 UAP 听证主办方之一 |
| `senate-intel` | Senate Select Committee on Intelligence | https://www.intelligence.senate.gov/ | 情报委员会相关动向 |

**搜索关键词建议**：`UAP`, `unidentified anomalous phenomena`, `unidentified aerial phenomena`, `AARO`, `anomaly resolution`.

## 2. 顶级美媒 (Top US Media)

| 短标签 | 名称 | 入口 |
|---|---|---|
| `nyt` | The New York Times | https://www.nytimes.com/section/us |
| `wapo` | The Washington Post | https://www.washingtonpost.com/national-security/ |
| `wsj` | The Wall Street Journal | https://www.wsj.com/news/politics |
| `reuters` | Reuters | https://www.reuters.com/world/us/ |
| `ap` | Associated Press | https://apnews.com/hub/us-news |

## 3. 国际权威 (International)

| 短标签 | 名称 | 入口 |
|---|---|---|
| `bbc` | BBC News | https://www.bbc.com/news/world/us_and_canada |
| `guardian` | The Guardian | https://www.theguardian.com/world/uap |
| `bloomberg` | Bloomberg | https://www.bloomberg.com/politics |

## 4. UAP 垂直 (Vertical)

> 这两家独家爆料较多，但需要人工核实。Routine 抓取时在 frontmatter 里加 `verification: needs-cross-check`。

| 短标签 | 名称 | 入口 |
|---|---|---|
| `debrief` | The Debrief | https://thedebrief.org/category/the-intelligence-brief/ |
| `liberation` | Liberation Times | https://www.liberationtimes.com/ |

## 抓取关键词

英文（任一命中即视为相关）：

- `UFO`, `UAP`, `unidentified aerial phenomena`, `unidentified anomalous phenomena`
- `extraterrestrial`, `alien` (排除明显的 sci-fi / immigration 上下文)
- `AARO`, `All-domain Anomaly Resolution Office`
- `Pentagon UAP`, `NASA UAP`, `congressional UAP hearing`
- `Tic Tac` (经典案例代名词), `Nimitz incident`, `Roosevelt UAP`

中文同义（用于检索国际中文版时使用）：不明飞行物、不明空中现象、外星人、外星生命、五角大楼 UAP。
