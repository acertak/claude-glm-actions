<img src="https://raw.githubusercontent.com/Sunwood-AI-OSS-Hub/claude-glm-actions-lab/main/assets/release-header-v1.0.0.svg" alt="v1.0.0 Release"/>

# v1.0.0 - Initial Release / 初回リリース

**リリース日 / Release Date:** 2026-01-19

---

## 日本語 / Japanese

### 概要

**Claude GLM Actions Lab** の初回リリースです！🎉

このプロジェクトは、Claude Code と Z AI の GLM-4 モデルを統合し、GitHub Actions で自動化された Pull Request レビューとレスポンスを実現する実験的ラボ環境です。

### 新機能 ✨

- **GitHub Actions ワークフロー統合**
  - `claude-glm-responder.yml`: Claude コメントに応答して GLM-4 で PR レビューを生成
  - `CLAUDE_GLM_DEV.yml`: 開発・テスト用ワークフロー
  - `.claude/` ディレクトリ構造のサポート

- **GLM-4 モデル設定**
  - Z AI の API キー設定（`ZAI_API_KEY`）
  - モデルパラメータの最適化

- **PR 自動化スクリプト**
  - Create PR URL からのタイトル・本文抽出
  - Claude コメントからの PR コンテキスト取得
  - 自動 PR 作成機能

- **CI/CD テスト環境**
  - サンドボックス環境でのテスト実行
  - GitHub Actions 統合テスト

- **キャラクターシステム**
  - ギャル先輩インプリメーター（美咲先輩）
  - 姐さんレビュアー（玲子姐さん）
  - 無重 星来（Agent ZERO アシスタント）

### バグ修正 🐛

- API キー環境変数名の修正（`ZAI_API_KEY`）
- PR 作成時の PAT 認証対応（`GH_PAT_ONIZUKA`）
- コミットメッセージ全体を PR 本文に使用する修正
- Claude bot ユーザー名の修正

### ドキュメント 📚

- README.md の多言語対応（日本語・英語）
- ヘッダー画像のアニメーション追加
- HTML5 準拠の構造調整
- ライセンスファイル（MIT License）追加

### リファクタリング 🔄

- 古いエージェントファイルの削除
- 古いワークフローの整理
- PR 作成スクリプトの Python 実装への書き直し

---

## English

### Overview

First release of **Claude GLM Actions Lab**! 🎉

This is an experimental lab environment that integrates Claude Code with Z AI's GLM-4 model, enabling automated Pull Request reviews and responses through GitHub Actions.

### What's New ✨

- **GitHub Actions Workflow Integration**
  - `claude-glm-responder.yml`: GLM-4 powered PR review responses to Claude comments
  - `CLAUDE_GLM_DEV.yml`: Development and testing workflow
  - `.claude/` directory structure support

- **GLM-4 Model Configuration**
  - Z AI API key setup (`ZAI_API_KEY`)
  - Optimized model parameters

- **PR Automation Scripts**
  - Extract title and body from Create PR URLs
  - Fetch PR context from Claude comments
  - Automated PR creation functionality

- **CI/CD Testing Environment**
  - Sandbox environment testing
  - GitHub Actions integration tests

- **Character System**
  - Gal Senior Implementer (Misaki-senpai)
  - Sister Reviewer (Reiko-neesan)
  - Seira Muju (Agent ZERO Assistant)

### Bug Fixes 🐛

- Fixed API key environment variable name (`ZAI_API_KEY`)
- PAT authentication for PR creation (`GH_PAT_ONIZUKA`)
- Fixed using full commit message in PR body
- Fixed Claude bot username

### Documentation 📚

- README.md multilingual support (Japanese/English)
- Added header image animations
- HTML5-compliant structure adjustments
- License file (MIT License) added

### Refactoring 🔄

- Removed old agent files
- Cleaned up old workflows
- Rewrote PR creation script in Python

---

## インストール方法 / Installation

```bash
# Clone the repository
git clone https://github.com/Sunwood-AI-OSS-Hub/claude-glm-actions-lab.git
cd claude-glm-actions-lab

# Set up required secrets in GitHub
# - ZAI_API_KEY: Your Z AI API key
# - GH_PAT_ONIZUKA: GitHub Personal Access Token for PR creation
```

---

## 使用方法 / Usage

1. **Secrets の設定**:
   - GitHub リポジトリの Settings → Secrets and variables → Actions
   - `ZAI_API_KEY`: Z AI から取得した API キー
   - `GH_PAT_ONIZUKA`: PR 作成用 GitHub PAT

2. **Pull Request 作成時の自動レビュー**:
   - PR で `@claude` への返信を含むコメントを作成
   - GitHub Actions が自動的に GLM-4 でレビューを生成

---

## コントリビューター / Contributors

@Sunwood-AI-OSS-Hub

---

## ライセンス / License

MIT License

---

## 次のリリース予定 / Upcoming

- より高度なレビュー機能
- 追加のキャラクターモード
- パフォーマンスの最適化
- テストカバレッジの向上
