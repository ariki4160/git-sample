# git-sample

GitHub の基本的な機能を確認するための練習用プロジェクトです。実際のアプリ開発ではなく、ブランチ運用・コミット・プルリクエスト・マージといった一連の Git/GitHub ワークフローの動作確認を目的としています。

## 目的

- ブランチの作成と切り替え
- コミットとプッシュ
- プルリクエスト（PR）の作成・レビュー・マージ
- コラボレータを含む複数アカウントでの共同作業の確認

## ファイル構成

| ファイル     | 内容                                                              |
| ------------ | ----------------------------------------------------------------- |
| `index.html` | メッセージを追記しながらコミット履歴を確認するためのサンプル HTML |
| `test.html`  | プルリクエストの動作確認に使うサンプル HTML                       |
| `code1.py`   | 日付の上旬・中旬・下旬を判定して出力する簡単な Python スクリプト  |

## 使い方

### code1.py の実行

現在の日付が上旬・中旬・下旬のどれかを判定して出力します。

```bash
python3 code1.py
```

実行例:

```
中旬です
```

### HTML の確認

`index.html` や `test.html` はブラウザで開くだけで表示を確認できます。

## リポジトリ情報

- オーナー: [ariki4160](https://github.com/ariki4160)
- コラボレータ: [ariki-tomono](https://github.com/ariki-tomono)

## Git/GitHub 操作の例

同一リポジトリ内でブランチを切ってプルリクエストを作成し、マージするまでの基本的な流れです。

```bash
# 作業用ブランチを作成
git checkout -b feature/pr-test

# 変更をコミット
git add .
git commit -m "変更内容の説明"

# リモートにプッシュ
git push -u origin feature/pr-test

# プルリクエストを作成（GitHub CLI を利用）
gh pr create --base main --head feature/pr-test --title "タイトル" --body "説明"

# マージコミット方式でマージし、ブランチを削除
gh pr merge --merge --delete-branch
```
