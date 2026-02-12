# Trajectory-aware Academic Paper Recommender  
# 基于研究轨迹的学术论文推荐系统

---

## Overview ｜ 项目简介

This project implements a trajectory-aware academic paper recommender that models research direction evolution rather than simple semantic similarity.

Unlike traditional recommendation systems that rely only on embedding similarity, this system attempts to predict the **evolution of research interests** and guide users along a research trajectory.

本项目实现了一个基于研究轨迹（Research Trajectory）的学术论文推荐系统，通过建模研究方向的演化过程，而不仅依赖语义相似度，实现更连续、更智能的论文发现体验。

---

## Features ｜ 功能特点

- **Direction Field Modeling（方向场建模）**  
  使用多方向表示用户研究兴趣，避免推荐空间塌缩。

- **Momentum Prediction（研究动量预测）**  
  根据历史交互轨迹预测未来研究方向。

- **Intent-aware Ranking（研究意图感知排序）**  
  区分理论、综述、应用等不同研究意图。

- **Anti-collapse Regularization（防塌缩机制）**  
  防止推荐逐渐收缩到过窄领域。

- **Telegram Bot Interface（Telegram Bot交互）**  
  基于聊天界面的论文推荐体验。

---

## Current Support ｜ 当前支持

- arXiv paper source only（目前仅支持 arXiv 数据源）

---

## Requirements ｜ 环境要求

- Python 3.10.19 (recommended)
- macOS / Linux (tested)
- Telegram Bot API

推荐使用：

Python 3.10.19


---

## Installation ｜ 安装依赖

Clone repository:

```bash
git clone https://github.com/NanagasaSuzutsuki/telegrambot.git
cd telegrambot
pip install -r requirements.txt
pip install python-telegram-bot sentence-transformers numpy feedparser requests
```
Configuration ｜ 配置

Create a Telegram bot using @BotFather and obtain a token.

通过 @BotFather 创建 Telegram Bot 并获取 Token。

Edit main.py:

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

Run ｜ 运行

python main.py

Project Goal ｜ 项目目标

This project explores a new paradigm:

Academic Recommendation → Research Navigation

Instead of recommending only similar papers, the system aims to guide users along evolving research directions.

本项目尝试将传统论文推荐升级为研究导航系统，不仅推荐相似论文，更关注研究方向的发展路径。

Development Notes ｜ 开发说明

This project was developed with GPT-assisted programming workflows, focusing on rapid prototyping of research-oriented recommendation systems.

本项目在开发过程中结合 GPT 辅助编程（GPT-assisted development），用于快速构建研究型推荐系统原型。

GPT主要用于：

架构设计探索

推荐算法思路验证

代码结构优化

核心设计与算法逻辑由作者自主规划与实现。

Future Work ｜ 未来计划

Citation-aware ranking

Structural research graph integration

Multi-source paper support

会接入semantic scholar 的api（申请中）进行进一步的更新和申请教程

I will integrate with the Semantic Scholar API (application in progress) for further updates and application tutorials.



