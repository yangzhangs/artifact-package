> **🌐 语言 / Language**: [中文](#贡献指南) | [English](#contributing-to-gemini-voyager) | [Español](CONTRIBUTING_ES.md) | [Français](CONTRIBUTING_FR.md) | [日本語](CONTRIBUTING_JA.md)

---

---

# 贡献指南

> [!CAUTION]
> **本项目暂时不接受任何新功能的 PR。** 如果你有一个很想做的功能，请按以下流程操作：
>
> 1. **先开一个 Issue 与维护者讨论**你的想法和方案
> 2. **等待维护者同意，并确定了一个好的实现方案后**，再开始编码并提交 PR
>
> 未经讨论直接提交的新功能 PR 将被直接关闭，不予审核。感谢理解。

> [!IMPORTANT]
> **项目状态：低频维护。** 回复较慢。优先处理带测试的 PR。

感谢你考虑为 Voyager 做出贡献！🚀

本文档提供贡献的指南和说明。我们欢迎错误修复、文档改进和翻译等贡献。关于新功能，请务必先通过 Issue 进行讨论。

---

## 🚫 AI 政策

**本项目拒绝接受任何未经人工复核的 AI 生成的 PR。**

虽然 AI 是很好的辅助工具，但“懒惰”的复制粘贴贡献会浪费维护者的时间。

- **缺乏逻辑解释** 或缺少必要测试的 PR 将将被拒绝。
- 你必须理解并对你提交的每一行代码负责。
- **Git 协作能力**：你应熟悉 GitHub 和 Git 的基本工作流，确保能在 AI Agent 的辅助下正确进行开源协作。如果你对此尚不熟悉，建议先学习相关知识，请保持 PR 中的 Git 历史整洁，避免出现混乱的提交记录。

---

## 目录

- [快速开始](#快速开始)
- [认领 Issue](#认领-issue)
- [开发环境设置](#开发环境设置)
- [进行更改](#进行更改)
- [提交 Pull Request](#提交-pull-request)
- [代码风格](#代码风格)
- [添加 Gem 支持](#添加-gem-支持)
- [许可证](#许可证)

---

---

## 快速开始

---

### 前置要求

- **Bun** 1.0+（必需）
- 用于测试的 Chromium 内核浏览器（Chrome、Edge、Brave 等）
- **Firefox：必须进行测试。**
- **Safari：作为可选项目**。如果有环境请进行测试；或者由 AI/自行判断该功能是否为 Safari 不支持的功能，并请予以标注。

---

### 快速启动

```bash

---

# 克隆仓库
git clone https://github.com/Nagi-ovo/gemini-voyager.git
cd gemini-voyager

---

### 查找 Gem ID

- 打开与该 Gem 的对话
- 检查 URL：`https://gemini.google.com/app/gem/[GEM_ID]/...`
- 在配置中使用 `[GEM_ID]` 部分

---

## 项目范围

Voyager 通过以下功能增强 Gemini AI 聊天体验：

- 时间线导航
- 文件夹组织
- 指令宝库
- 聊天导出
- UI 自定义

> [!NOTE]
> **我们认为 Voyager 的功能已经足够充分且全面。** 引入过多个性化、小众的功能不会让软件更好用，反而会增加维护负担。除非你认为某个功能确实是急需的、大多数用户都会用到的，否则不建议提交 Feature Request。

**不在范围内**：网站爬取、网络拦截、账户自动化。

---

---

## 获取帮助

- 💬 [GitHub Discussions](https://github.com/Nagi-ovo/gemini-voyager/discussions) - 提问
- 🐛 [Issues](https://github.com/Nagi-ovo/gemini-voyager/issues) - 报告错误
- 📖 [文档](https://gemini-voyager.vercel.app/) - 阅读文档

---

---

## 🚫 AI Policy

**We explicitly reject AI-generated PRs that have not been manually verified.**

While AI tools are great assistants, "lazy" copy-paste contributions waste maintainer time.

- **Low-quality AI PRs** will be closed immediately without discussion.
- **PRs without explanation** of the logic or missing necessary tests will be rejected.
- You must understand and take responsibility for every line of code you submit.
- **Workflow Proficiency**: You should be familiar with GitHub and Git workflows and able to collaborate correctly using AI tools. If you are new to this, please learn the basics first to ensure a clean Git history in your PRs.

---

# Clone the repository
git clone https://github.com/Nagi-ovo/gemini-voyager.git
cd gemini-voyager

---

### Finding the Gem ID

- Open a conversation with the Gem
- Check the URL: `https://gemini.google.com/app/gem/[GEM_ID]/...`
- Use the `[GEM_ID]` portion in your configuration

---

## Project Scope

Voyager enhances the Gemini AI chat experience with:

- Timeline navigation
- Folder organization
- Prompt vault
- Chat export
- UI customization

> [!NOTE]
> **We believe Voyager's feature set is already comprehensive and well-rounded.** Adding too many niche or overly personalized features does not make the software better — it only increases the maintenance burden. Unless you believe a feature is truly essential and would benefit the majority of users, please reconsider submitting a Feature Request.

**Out of scope**: Site scraping, network interception, account automation.

---

---

## Getting Help

- 💬 [GitHub Discussions](https://github.com/Nagi-ovo/gemini-voyager/discussions) - Ask questions
- 🐛 [Issues](https://github.com/Nagi-ovo/gemini-voyager/issues) - Report bugs
- 📖 [Documentation](https://gemini-voyager.vercel.app/) - Read the docs

---
