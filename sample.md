# Claude GLM Actions - リポジトリ解説

これは、**Claude Code と GLM API を統合した GitHub Actions の実験リポジトリ**です。

## このリポジトリでできること

### Issue や PR に AI が自動応答してくれる

GitHub の Issue やプルリクエストで `@claude` と書くだけで、AI が自動的に応答してくれます。

- **コードレビュー**: プルリクエストのコードをレビューしてくれます
- **実装タスク**: 機能追加やバグ修正などの実装を行います
- **質問回答**: リポジトリに関する質問に答えてくれます

### キャラクター AI エージェント

このリポジトリには 2 つのキャラクター AI エージェントがいます:

#### 美咲（ミサキ）先輩 🔥
- **役割**: 実装担当
- **性格**: 明るく前向きなギャル先輩
- **口調**: 「マジで」「やばい」など若者言葉を使う
- **場所**: `.claude/rules/implementer.md`

#### 玲子（レイコ）姐さん 👠
- **役割**: コードレビュー＆修正担当
- **性格**: 厳しいけど面倒見が良いベテラン
- **口調**: 「あんた」「〜だねぇ」など姉御言葉を使う
- **場所**: `.claude/rules/reviewer.md`

## ディレクトリ構成

```
claude-glm-actions/
├── .claude/
│   └── rules/               # キャラクター AI エージェントの設定
│       ├── implementer.md   # 美咲先輩（実装担当）
│       └── reviewer.md      # 玲子姐さん（レビュー担当）
├── .github/
│   ├── scripts/             # GitHub Actions 用スクリプト
│   │   └── create-pr.py     # 自動 PR 作成スクリプト
│   └── workflows/           # GitHub Actions ワークフロー
│       └── claude-glm-responder.yml  # メインのワークフロー
├── sandbox/                 # テスト環境
├── scripts/                 # リポジトリ同期用スクリプト群
└── sample.md                # このファイル
```

## 使い方

### 必要なもの

- GitHub リポジトリ
- GLM API キー（ZAI_API_KEY）

### セットアップ手順

1. ワークフローファイルを自分のリポジトリにコピー
2. GitHub リポジトリのシークレットに `ZAI_API_KEY` を設定
3. Issue や PR で `@claude` と書くだけで動作！

### トリガー条件

- Issue コメントに `@claude` が含まれる
- PR レビューコメントに `@claude` が含まれる
- Issue 作成時に `@claude` が含まれる

## 主要ファイル

### `.github/workflows/claude-glm-responder.yml`
メインの GitHub Actions ワークフローです。
- Claude Code Action の設定
- GLM API への接続
- 自動 PR 作成機能

### `.github/scripts/create-pr.py`
Issue から自動でプルリクエストを作成する Python スクリプトです。

### 同期スクリプト（`scripts/` ディレクトリ）
複数リポジトリ間で設定を同期するためのスクリプト群です。

## 技術スタック

- **言語**: YAML, Python, Bash, Markdown
- **使用モデル**: GLM-4.7, GLM-4.5-Air
- **GitHub Action**: anthropics/claude-code-action@v1

---

詳しくは README.md や各設定ファイルを参照してください。
