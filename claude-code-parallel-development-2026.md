# 【2026年最新】Claude Code作者が実践する「超並列駆動」開発術がエンジニアの常識を破壊していた

> 原文: https://qiita.com/ot12/items/66e7c07c459e3bb7082d

Claude Codeの開発者である Boris Cherny氏 (@bcherny) が公開した「2026年の開発セットアップ」が、Claude Codeを使う全人類が読むべき内容でした

彼が実践しているのは、単なるツールの使いこなしではありません。 __人間自身のCPUをマルチスレッド化する__という、エンジニアリングの極致です。

そこで、この記事では彼が明かした驚異のワークフローを解剖し、我々が今すぐ取り入れるべき__次世代の開発思想__を深掘りします。

Claude Codeでどんなことできるかは、以下の記事も参考にしてみてください！

## 1. ターミナルとWebで「多重影分身」

まず度肝を抜かれるのが、同時に稼働させているClaudeの数です。 「AIの回答待ちにスマホを見る」。そんな無駄な時間は、彼の辞書にはありません。

彼は、常時10〜15体ものClaudeインスタンスを並列で従えています。 ここまでくると「一人の開発者」ではありません。AIエージェントたちを統率する、AI部隊の「司令官」です。

では、その「15人の部下」たちはどこにいるのか？ __彼は戦力を「ローカル」と「Web」に分散配備__しています。

## 🖥️ Terminal (Local)

![Terminal screenshot showing multiple Claude sessions](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2F7ebad351-7d36-429e-9bce-48cd440821f2.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=787d0abe561e4384dc0c4430ef689ca8)

まず精鋭の5部隊をローカルに配置しています

ターミナルのタブを 1 〜 5 番に固定し、常に5セッションを常駐し、 それぞれのタブに明確な役割（人格）を与えます。

例えば、以下のようにです

- Tab 1: 新機能の実装（Thinking中...）
- Tab 2: バグの原因調査（ログ解析中...）
- Tab 3: コードのリファクタリング（修正案作成中...）

## ☁️ Web (Cloud)

![Web interface showing multiple browser sessions](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2Fb1f8a17b-f055-40f2-9b85-9cc36a05b05c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b813f5af45c8edbb7634b81e4de67884)

そして、ローカルだけでは手が足りない時は、ブラウザ（claude.ai/code）を開放しら、さらに5〜10セッションを立ち上げ、負荷をオフロードしながら思考の幅を広げます。

## なぜ脳がパンクしないのか？（iTerm2のハック）

「15個も画面を見ていたら、切り替えだけで日が暮れるのでは？」 そう思いますよね。

そこで彼が使っているのが__OSレベルの割り込み処理（Interrupt）です。__

彼は Terminalのシステム通知 をハックし、以下のループを回しています。

1. Claudeに重いタスクを投げる（Thinking開始）。
2. 人間は即座に別のタブへ移動し、別の仕事をする。
3. Claudeの思考が完了し、入力を求めてくると...
4. OSから通知が飛ぶ。
5. 通知を見て、完了したタブにスイッチする。
6. 人間自身が「非同期I/O」になる

これはまさに、OSのタスクスケジューリングを人間が実行している状態です。

AIがコードを書いている数分間、カーソルが点滅するのを眺めるのはブロッキング処理（同期処理）であり、リソースの浪費です。

彼は「待ち時間（I/O Wait）」を極限までゼロにし、CPU（自分の脳）を常にフル稼働させています。

💡 シングルタスクでAIの出力を眺めるのは2025年まで。 2026年は、通知をトリガーに「AIの群れ」を指揮する時代です。

## 2. 「Opus 4.5」一択の経済合理性

![Model selection screenshot showing Opus 4.5 preference](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2Fcb73f59a-6d0c-4f75-9354-d546ea9e9364.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=60f127e2a4ccee598902a068bf7cf6c4)

__「コーディングには軽量で高速なモデル（HaikuやSonnet）が良い」__ そんな定説を、彼は真っ向から否定しました。

彼は、あらゆるタスクにおいて__最も重厚で最も賢いモデル 「Opus 4.5 with thinking」 を採用__しています。

一見、生成の遅いモデルを使うのは非効率に見えるかもしれません。しかし彼はこう断言します。

「__OpusはSonnetより巨大で遅い。だが、『操舵（Steering）』の手間が圧倒的に少ないんだ__」

軽量モデルではコード生成自体は一瞬で終わります。

しかし、指示を微妙に誤解したり、複雑な依存関係を見落としたりしがちです。その結果、人間が「違う、そうじゃない」と何度も修正指示を出すことになり、かえって時間を浪費します。

逆に賢いモデルでは思考時間はかかります。しかし、精度が高く、複雑な要件でも一発で正解を導き出します。

つまり、開発において最も高くつくコストは、AIの待ち時間ではなく、__人間による修正（手戻り）の時間__です。

💡 確実に一発で仕留めてくれるモデルを使うことが、トータルで見れば最速の選択なのです。

## 3. チームの脳を育てる「複利エンジニアリング」

![CLAUDE.md example screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2Fb47e769e-fead-44ae-98fc-26fc4be0e318.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5dc3d45008ef6ca40f4175a621a5f912)

これが最も真似すべきプラクティスです。彼はチーム全員で CLAUDE.md を育てています。

CLAUDE.md とは__AIのための攻略本__です。 リポジトリのルートでGit管理され、コード規約や過去の失敗を記述します。

![CLAUDE.md content screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2F36b32838-3fda-4a68-b9aa-fe39e53db5a6.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=754c0c59e8727432518c99d65694631d)

Boris氏のチームでは、PRレビュー中にGitHub Actionを使ってこれを更新します。

1. AIがミスをする（例：古いライブラリを使った）。
2. 人間がPRで指摘。
3. Botを召喚：@claude add rule to CLAUDE.md とコメント。
4. 永続化：知識が共有され、次回のセッションから全チームメンバーのAIがそのミスをしなくなる。

彼はこれを 「複利エンジニアリング（Compounding Engineering）」 と呼んでいます。

## 4. 「Plan Mode」で一撃必殺を狙う

![Plan Mode screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2F3e14eac7-84fc-4018-b294-03c1c35ba0d3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7a60706a55ec787ef65857db7698f48f)

彼が実際のコーディング（特にPR作成などのまとまったタスク）で最も時間を割いているのが、__計画__のフェーズです。

彼は多くのセッションを、まず Plan Mode（Shift+Tab 2回押し）から開始します。いきなりコードを書かせることはしません。

- 徹底的な議論（Discussion）: Claudeと「どう実装すべきか」を納得いくまで話し合います。
- 合意形成（Agreement）: 人間が「そのプランで完璧だ」とGoサインを出すまで、1行もコードは書かせません。
- モード切替（Switch）: プランが固まった瞬間、"Auto-accept edits mode" に切り替えます。
- 一撃完遂（One-Shot）: 迷いのなくなったClaudeは、驚くべきことに、そのタスクを__One-Shot__で実装し切ります。

「とりあえず書いてみて」と見切り発車するのではなく、「完璧な設計図を作ってから、一気に建設する」。 これこそが、手戻りをゼロにする究極の時短術です。

## 5. 「スラッシュコマンド」でルーチンを自動化

![Slash commands screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2F4b9a12c8-76d8-470d-9bbc-3a164f1ee8c7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9faa4d04188275ff64b1d9c9e3f81670)

彼は、1日に何度も繰り返す「インナーループ（定型作業）」を、全て スラッシュコマンド化して効率化しています。

スラッシュコマンド化するメリットは、単に人間が「長いプロンプトを打つ手間」が省けるだけではありません。

コマンド化して定義することで、__Claude自身もそのワークフローをツールとして認識・実行できる__ようになります。

これは、いわば、自分だけでなくAIにも「業務遂行のためのショートカットキー」を配布するようなものです。

「スラッシュコマンド」を使うことで、属人化しがちな「熟練の手順」が誰もが（そしてAI自身さえも）迷わず実行できる標準機能へと昇華されるのです。

## 6.サブエージェントで「PRワークフロー」を自動化

![Sub-agent screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2F44e6de27-2c8b-499e-a62a-f6c3c724a79f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8b6cc656192c54d25b631670d73c755c)

彼はClaude単体で全てを完結させるのではなく、__特定のタスクに特化したサブエージェント__を使い分けています。

彼はサブエージェントを__スラッシュコマンドの延長線上__にあるものとして捉えており、スラッシュコマンドが「一連の操作のショートカット」なら、サブエージェントは__PR作成における定型ワークフローそのものの自身__と言っています

彼は、ほとんどのPR（プルリクエスト）で発生する「いつもの作業」を、専用のエージェントに任せています。

- code-simplifier (掃除係): Claudeが機能実装を終えた後に起動。コードを整理し、よりシンプルで読みやすい形にリファクタリングします。
- verify-app (検証係): アプリケーションのE2Eテスト（エンドツーエンドテスト）の詳細な手順を熟知しており、動作確認を専門に行います。

人間がやるべきは「創造的な実装」だけ。 「コードの清書」や「テスト手順の実行」といったルーチンワークは、それぞれの専門家に丸投げする。これが2026年流の分業スタイルです。

## 7.Hooksで「最後の10%」を埋める

![Hooks configuration screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2Fc647705a-07ca-4b8e-bbd6-af5d95b64945.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=456c006a08eccaa268033e0bacec8e66)

さらに彼は、PostToolUse フック を活用し、Claudeがコードを書くたびにフォーマッターを自動実行させています。

Boris氏はこう語ります。

「Claudeは通常、そのままでも素晴らしいコードを書く。だが、このフックが__最後の10%を処理する__ことで、CIでのフォーマットエラーを回避するんだ」

AIの生成コードは「ほぼ完璧」ですが、機械的な厳密さ（Lint/Format）は専用ツールに任せるのが確実です。

このフックにより、人間が細かいインデントやスペースを直す時間をゼロにし、「CIが通らない！」という些細なストレスを未然に防いでいます。

## 8.権限管理：スピードと安全の両立

![Permissions configuration screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2Fba36fa84-7bd9-4e6f-96d2-3e76f3d33bc8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a41193e3a5276f9c72134fc968bec44c)

開発速度を優先するあまり、つい --dangerously-skip-permissions（全許可フラグ）を使いたくなりますが、彼はこれを明確に避けています。

代わりに彼は /permissions コマンド を徹底活用しています。

具体的には、ls や git status など、環境に対して無害であることが明白なコマンドだけを「事前許可リスト」に追加します。

そして、 この設定は.claude/settings.json に保存され、チーム全体で共有（Git管理）されます。

これにより、セキュリティリスクを冒すことなく、AIからの「このコマンドを実行してもいいですか？」という不要な確認プロンプトを排除しています。

「全許可」か「毎回確認」かの二択ではなく、「安全なものはスルー」という現実的な解です。

## 9.ツール統合 (MCP) で「エディタの外」も支配する

![MCP tools screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2F1edb5424-fea0-4412-a7dc-b947afe0f087.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9cf13c6576a5bf7cc5c35b844d356fe3)

Claudeの仕事場は、エディタの中だけではありません。 Boris氏は、MCP やCLIツールを通じて、開発に必要なあらゆる外部ツールをClaudeに操作させています。

具体的には、以下のような操作をClaude自身が自律的に行います。

- Slack (via MCP): 過去のログを検索したり、進捗をチームチャンネルに投稿したりする。
- BigQuery (via CLI): データ分析の疑問に答えるため、bq コマンドを叩いてクエリを実行する。
- Sentry: エラーログを直接取得し、解析する。

ここでも徹底されているのが「共有」です。 Slack MCPなどの設定は .mcp.json に記述され、Gitリポジトリでチーム共有されています。

これにより、チームの誰もが（そして彼らのClaudeが）、最初から全てのツールを使いこなせる状態で開発をスタートできるのです。

## 10.最も重要な「検証ループ」

![Verification loop screenshot](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3356814%2F0aa4f262-64d7-4023-9a78-fb800a60494d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=285b56f16dc2429a4f8be3361160c23e)

最後に、Boris氏が**最高の結果を得るために、恐らくこれが一番大事だ（probably the most important thing）**と力説したの「書きっぱなし」にしないことです。

「Claudeにコードを書かせて終わり」では片手落ちです。 Claude自身に、自分の仕事を検証させる手段を与えなければなりません。

彼は Claude Chrome Extension を使い、以下のループを回しています。

1. Claudeがコードを書く。
2. Claude自身がブラウザを開く。
3. 実際にUIを操作し、表示崩れや動作を確認する。
4. 「UXが良い感じ（UX feels good）」になるまで、自律的に修正を繰り返す。
5. 「フィードバックループがあれば、最終的な品質は 2〜3倍 に跳ね上がる」

人間がデバッグするのではなく、「AIが自分で書いて、自分で動かして、自分で直す」環境を用意する。これこそが品質向上の鍵です。

検証方法はプロジェクトごとに違います（bashコマンド、テストコード、ブラウザ、スマホシミュレータなど）。重要なのは、その環境構築にしっかりと投資することです。

## まとめ：2026年の開発者像

Boris氏のセットアップは、「コードを速く書く」ことから__AI部隊を設計・運用する__ことへと、開発者の役割が完全にシフトした未来を映し出しています。

1. 並列化せよ（15並列・通知活用で待ち時間ゼロ）
2. 賢さに投資せよ（Opus 4.5で手戻りゼロ）
3. 知識を蓄積せよ（CLAUDE.mdで複利効果）
4. 検証を自動化せよ（自律ループで品質2倍）

2026年の常識は、今日からでも少しずつ取り入れられます。 さあ、iTermのタブを増やし、CLAUDE.md を作り、あなたの専属AIチームを結成しましょう！

Claude Codeでどんなことできるかは、以下の記事も参考にしてみてください！

---

*Saved from: https://qiita.com/ot12/items/66e7c07c459e3bb7082d*