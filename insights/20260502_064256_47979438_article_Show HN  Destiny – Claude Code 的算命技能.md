# 洞察报告

## 基本信息

| 项目 | 内容 |
|------|------|
| **仓库链接** | https://github.com/xodn348/destiny |
| **作者** | xodn348 |
| **项目名称** | destiny |
| **版本** | 0.7.0 |
| **许可证** | MIT |
| **Star数** | 27 |
| **Fork数** | 1 |
| **主要语言** | Python 75.7% / HTML 24.3% |

## 项目概述

**destiny** 是一个为 [Claude Code](https://claude.com/claude-code) 设计的算命插件，不是简单的星座生成器——数字是计算出来的，只有解读部分是生成式的。

## 核心功能

运行 `/destiny` 会产生两部分解读：

- **今日运势** — 根据您的出生星盘解读今天的简短散文，包括五星分类评分（整体、爱情、财运、事业、健康）、为当前时刻抽取的六爻卦象，以及幸运数字/颜色/方向。
- **人生解读** — 性格、人生轨迹概述以及您当前10年周期所处的阶段。

## 技术原理

该插件使用三个古典东亚玄学术数，每个都根据出生日期和时间确定性计算：

1. **四柱（八字）** — 出生年月日时的天干地支组合，描述五行（木、火、土、金、水）的分布特征
2. **万年历引擎** — 使用 `lunar-python` 处理节气转换、真太阳时校正和韩国夏令时
3. **易经（Book of Changes）** — 使用宋代邵雍的梅花易数时点法，根据当前农历日期和时辰推导卦象

## 安装方式

```bash
/plugin marketplace add xodn348/destiny
/plugin install destiny@destiny-marketplace
/destiny
```

## 附加命令

- `/destiny today` — 仅今日运势
- `/destiny life` — 仅人生解读
- `/destiny reset` — 删除保存的资料重新开始
- `/destiny compat <伴侣出生> <城市> <m|f>` — 合盘解读
- `/destiny hook on/off` — 开启/关闭会话启动时自动运行

## 依赖技术

- Python 3.10+
- [lunar-python](https://github.com/6tail/lunar-python)（MIT）— 纯Python万年历
- 易经：King Wen排序 + Legge（1899年）公共领域译本

## 重要声明

**仅供娱乐。没有科学依据，不构成任何建议。** 本软件按"原样"提供，不提供任何明示或暗示的保证。作者和贡献者不对因使用本工具而产生的任何直接、间接、附带、后果性或其他损害负有任何责任。