# Git / PR ワークフロー

このプロジェクトのブランチ戦略と PR 運用ルールです。Git 操作を行う際は必ず従ってください。

## ブランチ戦略

- 統合ブランチは `main`。`main` への直接プッシュは原則行わず、作業はブランチを切って PR 経由でマージする。
  - 例外: `README.md` や `.gitignore` などのドキュメント・設定整備は、過去に `main` へ直接コミットした実績あり。ただし基本は PR 経由を推奨。
- ブランチ命名の例:
  - 機能・動作確認用: `feature/pr-test`
  - コラボレータ作業用: `ariki-tomono_work` / `ariki-tomono_work_02`
- コラボレータ（`ariki-tomono`）は fork 不要。同一リポジトリ内に直接ブランチを作成できる。

## 同一リポジトリ内ブランチ方式での PR 手順

```bash
# 1. main を最新化
git checkout main
git pull --ff-only

# 2. 作業用ブランチを作成
git checkout -b feature/pr-test

# 3. 変更をコミット（フォーマッタ差分に注意。commit-guidelines.md 参照）
git add .
git commit -m "変更内容の説明"

# 4. リモートにプッシュ
git push -u origin feature/pr-test

# 5. プルリクエストを作成（GitHub CLI を利用）
gh pr create --base main --head feature/pr-test --title "タイトル" --body "説明"

# 6. オーナー ariki4160 側でレビュー・マージ（マージコミット方式 + ブランチ削除）
gh pr merge --merge --delete-branch

# 7. ローカルの main に反映
git checkout main
git pull origin main
```

## マージ方式

- **マージコミット方式**（`gh pr merge --merge`）を標準とする。
- マージ後は `--delete-branch` で作業ブランチを削除する。

## レビュー・マージの役割分担

- 変更・コミット・プッシュ・PR 作成: 作業者（オーナーまたはコラボレータ）
- レビュー（Approve）・マージ: オーナー `ariki4160`

## コラボレータ（ariki-tomono）名義で PR を出す場合

- `gh` はアカウント追加（`gh auth login`）または切替（`gh auth switch`）で `ariki-tomono` に切り替える。
  またはブラウザセッションから PR を作成する。
- コミットは `ariki-tomono` 名義（`user.name` / `user.email`）に合わせる。メール設定は commit-guidelines.md を参照。

## 便利な gh / git コマンド

```bash
gh auth status                 # ログイン中のアカウント確認
gh auth switch                 # 複数ログイン時のアカウント切替
gh pr list                     # PR一覧
gh pr view <番号>              # PRの詳細
gh pr view <番号> --web        # PRをブラウザで開く
git log --oneline --graph      # コミット履歴をグラフ表示
git config user.email          # コミット用メール確認
```
