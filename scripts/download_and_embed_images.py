#!/usr/bin/env python3
"""
Download images from URLs and embed them as base64 in markdown.
"""
import re
import base64
import urllib.request
from pathlib import Path

# Article content
ARTICLE_CONTENT = '''![Image 1: Claude CodeからCodex CLI・Gemini CLIを使えるようにする](https://images.ctfassets.net/ct0aopd36mqt/3KBTm8tdpO9RJJuaVvVzod/a9964bb03097b448b2327edc6920bf9f/Claude.png?w=3840&fm=webp)

## はじめに

お疲れ様です。あきとです。

最近、Claude Codeを使っていて「他のAIモデルの意見も聞きたいな」と思う場面が増えてきました。OpenAIのCodex CLIやGoogleのGemini CLIをClaude Codeから呼び出せないか調べていたところ、MCP（Model Context Protocol）を使えば実現できるとわかりました。
そのため今回は、Claude CodeにCodex CLIとGemini CLIをMCPを経由して使用する方法を紹介します。

## Codex CLIのMCP追加

### 前提条件

Codex CLIのMCPを追加するには、以下の準備が必要です。

- Codex CLIがインストール済みであること
- OpenAIへのログインが完了していること

### 追加コマンド

以下のコマンドを実行するだけで、Codex CLIをMCPとして追加できます。

```
claude mcp add -s user --transport stdio codex -- codex mcp-server
```

このMCPはOpenAI公式が提供しているため、安心して利用できるのがポイント。公式提供のため、今後Codexがアップデートされた際も、MCP側の更新が期待できます。

## Gemini CLIのMCP追加

### 前提条件

Gemini CLIのMCPを追加するには、以下の準備が必要です。

- Gemini CLIがインストール済みであること
- Googleアカウントへのログインが完了していること

### 追加コマンド

以下のコマンドで、Gemini CLIをMCPとして追加できます。

```
claude mcp add -s user --transport stdio gemini -- npx -y gemini-mcp-tool
```

こちらもユーザー単位でMCPを追加しています。

### 注意点

Gemini CLIのMCPは、gemini-mcp-toolというGitHubリポジトリから提供されています。
公式ではなくサードパーティ製のため、利用は自己責任でお願いします。セキュリティ面やサポート体制を考慮したうえで導入してください。

## Gemini 3 Pro Previewモデルの有効化

現状、`gemini-3-pro-preview`モデルを使用するには、Gemini CLIでの設定変更が必要です。

### 設定手順

1. Gemini CLIで`/settings`コマンドを実行
2. 「Preview Features」の項目を`true`に変更
3. Gemini CLIを再起動

![Image 2: Preview Featuresの設定画面](https://devio2024-2-media.developers.io/upload/6euGKPoI6cFuIYlo9FPIdX/2026-01-21/cAvPh62qdhDy.png)

## 実際に使ってみた

お試しで各AIモデルにコードレビューを依頼してみました。

### サンプルコード

レビュー対象として、フォルダに落ちていた以下のPythonコードを使用しています。

main.py:

```
class TextAnalysisEngine:
    def __init__(self, source_content: str):
        self.source_content = source_content

    def generate_reversed_copy(self) -> str:
        return self.source_content[::-1]

    def convert_to_uppercase(self) -> str:
        return self.source_content.upper()

    def calculate_word_count(self) -> int:
        return len(self.source_content.split())

    def compile_analysis_report(self) -> str:
        return (
            f"Original: {self.source_content}\\n"
            f"Reversed: {self.generate_reversed_copy()}\\n"
            f"Upper: {self.convert_to_uppercase()}\\n"
            f"Word Count: {self.calculate_word_count()}"
        )

def run_demonstration():
    demo_input_string = "Hello from test! This is an expanded python script."
    analysis_engine = TextAnalysisEngine(demo_input_string)

    print("--- Text Analysis Report ---")
    print(analysis_engine.compile_analysis_report())

if __name__ == "__main__":
    run_demonstration()
```

### 各モデルのレビュー結果

各MCPに対してモデルを指定し、以下のような依頼文でレビューをお願いしました。

```
Gemini3ProとGPT5.2とOpus4.5それぞれを使ってmain.pyをレビューして
```

結果がこちらです。

![Image 3: 各AIモデルのレビュー比較結果](https://devio2024-2-media.developers.io/upload/6euGKPoI6cFuIYlo9FPIdX/2026-01-21/ExNUydcrT3uv.png)

モデルによって指摘するポイントはやはり異なるので、複数の視点から一括でレビューを受けられるのは大きなメリットだと感じました。

## まとめ

今回は、Claude CodeにCodex CLIとGemini CLIをMCPとして追加する方法を紹介しました。

Claude Codeでは、SkillsやCommands、Subagentsを作成することで、各モデルの得意分野に合わせた仕事を任せられるようになります。
また、指示する際は使うMCPを明示するのも大事ですが、モデルのバージョンを正確に指定しないと意図しないバージョンのモデルが使われる可能性があるため、指定が必要です。

本ブログが誰かの参考になれば幸いです。

## 参考文献

- Codex Agents SDK Guide | OpenAI
- Get Started with Gemini 3 | Gemini CLI

## クラスメソッドオペレーションズ株式会社について

クラスメソッドグループのオペレーション企業です。

運用・保守開発・サポート・情シス・バックオフィスの専門チームが、IT・AIをフル活用した「しくみ」を通じて、お客様の業務代行から課題解決や高付加価値サービスまでを提供するエキスパート集団です。

当社は様々な職種でメンバーを募集しています。

「オペレーション・エクセレンス」と「らしく働く、らしく生きる」を共に実現するカルチャー・しくみ・働き方にご興味がある方は、クラスメソッドオペレーションズ株式会社 コーポレートサイト をぜひご覧ください。※2026年1月 アノテーション株式会社から社名変更しました
'''

# Image URLs from the article
IMAGE_URLS = [
    ("https://images.ctfassets.net/ct0aopd36mqt/3KBTm8tdpO9RJJuaVvVzod/a9964bb03097b448b2327edc6920bf9f/Claude.png?w=3840&fm=webp", "Image 1: Claude CodeからCodex CLI・Gemini CLIを使えるようにする"),
    ("https://devio2024-2-media.developers.io/upload/6euGKPoI6cFuIYlo9FPIdX/2026-01-21/cAvPh62qdhDy.png", "Image 2: Preview Featuresの設定画面"),
    ("https://devio2024-2-media.developers.io/upload/6euGKPoI6cFuIYlo9FPIdX/2026-01-21/ExNUydcrT3uv.png", "Image 3: 各AIモデルのレビュー比較結果"),
]


def get_mime_type(url: str) -> str:
    """Get MIME type from URL."""
    if url.endswith('.png') or '.png?' in url:
        return 'image/png'
    elif url.endswith('.jpg') or url.endswith('.jpeg') or '.jpg?' in url or '.jpeg?' in url:
        return 'image/jpeg'
    elif url.endswith('.webp') or '.webp?' in url:
        return 'image/webp'
    elif url.endswith('.gif') or '.gif?' in url:
        return 'image/gif'
    elif url.endswith('.svg') or '.svg?' in url:
        return 'image/svg+xml'
    return 'image/png'  # default


def download_and_encode_image(url: str) -> str:
    """Download image and return base64 encoded data URL."""
    print(f"Downloading: {url}")
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            image_data = response.read()
            base64_data = base64.b64encode(image_data).decode('utf-8')
            mime_type = get_mime_type(url)
            return f"data:{mime_type};base64,{base64_data}"
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return url  # Return original URL on error


def process_markdown(content: str) -> str:
    """Replace image URLs with base64 data URLs."""
    result = content
    for url, alt_text in IMAGE_URLS:
        print(f"Processing: {alt_text}")
        data_url = download_and_encode_image(url)
        # Replace the URL in markdown
        old_pattern = f"]({url})"
        new_pattern = f"]({data_url})"
        result = result.replace(old_pattern, new_pattern)
    return result


def main():
    print("Starting image download and embedding...")
    processed_content = process_markdown(ARTICLE_CONTENT)

    # Add header
    header = """# Claude CodeからCodex CLI・Gemini CLIを使えるようにする

**著者:** 山本暁斗
**元URL:** https://dev.classmethod.jp/articles/claude-code-codex-gemini-mcp/
**公開日:** 2026-02-06

---

"""

    final_content = header + processed_content

    # Write to file
    output_path = Path("articles/claude-code-codex-gemini-mcp.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(final_content, encoding='utf-8')
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()
