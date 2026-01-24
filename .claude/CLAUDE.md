# Claude Code 用リポジトリガイド

## Web記事をMarkdownとして保存する方法

このリポジトリでは、Web上の記事を取得してローカルにMarkdownファイルとして保存する機能がよく使用されます。以下に成功した実装手順を記載します。

### 手順

1. **記事の内容を取得する**
   - `mcp__web_reader__webReader` ツールを使用して、記事URLからMarkdown形式のコンテンツを取得します
   - パラメータ例:
     - `url`: 記事のURL
     - `return_format`: "markdown"
     - `retain_images`: true

2. **画像をダウンロードして保存する**
   - 記事内の画像URLを抽出
   - `articles/images/` ディレクトリを作成
   - 各画像をダウンロードして保存
   - 画像ファイル名は適切にリネーム（例: `hero.png`, `screenshot.png`）

3. **Markdownファイルを作成する**
   - ヘッダー情報を追加（タイトル、元URL、著者、日付など）
   - 画像URLをローカルの相対パス（`images/ファイル名`）に置換
   - `articles/` ディレクトリに保存

4. **コミットしてプッシュする**
   - ファイルをステージング: `git add articles/`
   - コミット: `git commit -m "docs: add article"`
   - プッシュ: `git push origin <branch>`

### 推奨されるディレクトリ構造

```
articles/
├── images/
│   ├── hero.png
│   ├── screenshot1.png
│   └── screenshot2.png
└── article-title.md
```

### 画像埋め込みの注意点

- **NG**: base64エンコードして埋め込む（ファイルサイズが大きくなり、表示されない場合がある）
- **OK**: 画像を別ファイルとして保存し、相対パスで参照する

### Markdownのヘッダー例

```markdown
---
title: 記事タイトル
url: https://example.com/article
author: 著者名
date: 2024-01-24
---

# 記事タイトル

本文...

![画像説明](images/hero.png)
```

## 開発ガイドライン

- シンプルに実装する（過剰な抽象化は避ける）
- コミットメッセージは明確に
- 必要に応じて `.claude/rules/` のキャラクター設定を参考にする
