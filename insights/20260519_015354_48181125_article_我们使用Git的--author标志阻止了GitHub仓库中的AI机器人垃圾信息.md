# 洞察报告：AI垃圾内容对开源生态的威胁

**洞察链接**: https://archestra.ai/blog/only-responsible-ai

**Hacker News讨论**: https://news.ycombinator.com/item?id=48181125

**来源**: Archestra.AI Blog

**发布日期**: 2026年4月17日

**作者**: Ildar Iskhakov (CTO)

---

## 一、问题背景

GitHub近期公布统计数据，庆祝AI在其平台贡献指标上的"巨大贡献"，却完全忽略了贡献质量下降的问题。Archestra团队认为，开源生态正在遭受前所未有的AI垃圾内容（AI Slop）侵袭。

## 二、具体表现

### 2.1 issue被AI机器人轰炸

团队在一个悬900美元赏金的issue上发布"MCP Apps"支持需求，很快收到合法贡献者的关注，但随后AI机器人涌入，将讨论推至**253条评论**，用无意义的"实施计划"甚至对维护者的攻击污染了对话。

### 2.2 PR泛滥成灾

仅添加x.ai提供商支持的issue，就收到**27个Pull Request**，大多数贡献者甚至没有尝试测试代码。

### 2.3 维护成本激增

团队成员每周需花费**半天时间**清理AI垃圾，移除未经测试的PR，关闭虚构的issue。稍有疏忽，仓库就变得对合法贡献者完全不再友好。

## 三、应对措施

### 3.1 建立声誉系统

开发了名为"London-Cat"的小型机器人，基于合并的PR和其他信号计算贡献者声誉。

### 3.2 部署AI sheriff

尝试自动识别AI生成的PR，但不幸误伤了一些合法PR。

### 3.3 最终方案：贡献者 onboarding 机制

采取"核选项"：**阻止未完成 onboarding 的用户创建issue、提交PR或发表评论**。尽管这对于依赖GitHub活动指标获取融资的初创公司而言风险极大，但团队坚持"质量重于数量"的原则。

## 四、技术实现

GitHub提供"限制于先前的贡献者"设置：如果用户之前未在main分支提交过commit，则无法评论issue或PR。利用Git的`--author`参数，可以将commit归属到其他用户：

```bash
gh api users/their-username --jq '.id'

git commit \
  --author="their-username <ID+their-username@users.noreply.github.com>" \
  -m "chore: add their-username to external contributors"
```

完整流程：

1. 用户在官网完成ethical AI规则学习并通过CAPTCHA
2. GitHub Action自动获取用户GitHub ID，将其添加到`EXTERNAL_CONTRIBUTORS.md`
3. 以用户名义推送commit到main
4. 用户获得仓库访问权限

## 五、安全风险

AI垃圾不仅打击合法贡献者的积极性，还带来严重安全隐患。LiteLLM仓库曾遭遇攻击者利用AI机器人引导对话的攻击事件。

## 六、结论

当GitHub报告的漂亮数据背后充斥着AI生成的垃圾内容时，开源项目团队不得不承担起清理AI垃圾的重任，并发明各种变通方案来维护开源社区的合法性。这不仅是质量问题，更是开源生态的生存危机。

**是时候认真对待AI对开源的影响了。**