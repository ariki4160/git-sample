# コラボレーターによるプルリクエスト検証

## 概要

コラボレーター `ariki-tomono` が変更を加え、オーナー `ariki4160` がレビュー・マージする
一連のワークフローを検証した記録です。

- リポジトリ: https://github.com/ariki4160/git-sample
- オーナー: ariki4160
- コラボレーター: ariki-tomono
- 対象ブランチ: `ariki-tomono_work` → `main`
- マージされたPR: #3

---

## 実施手順

### 1. 作業ブランチで変更・コミット

`ariki-tomono_work` ブランチで `index.html` に1行追加。

```bash
git checkout ariki-tomono_work
# index.html を編集
git add index.html
git commit -m "ariki-tomonoによるプルリク検証用の変更"
```

追加した内容:
```html
<p>ariki-tomonoによるプルリク検証用の変更</p>
```

### 2. リモートにプッシュ

```bash
git push origin ariki-tomono_work
# 6ff7dc6..793829d  ariki-tomono_work -> ariki-tomono_work
```

### 3. プルリクエストを作成（ariki-tomono）

以下のURLをブラウザで開き「Create pull request」をクリック。

```
https://github.com/ariki4160/git-sample/compare/main...ariki-tomono_work
```

- base: `main`
- compare: `ariki-tomono_work`
- PR番号: #3

### 4. レビュー・マージ（ariki4160）

1. https://github.com/ariki4160/git-sample/pulls を ariki4160 アカウントで開く
2. 「Files changed」タブで差分を確認
3. 「Review changes」→「Approve」→「Submit review」
4. 「Merge pull request」→「Confirm merge」

マージコミット: `ab33f9e Merge pull request #3 from ariki4160/ariki-tomono_work`

### 5. ローカルの main に反映

```bash
git checkout main
git pull origin main
# Updating ff8876f..ab33f9e  Fast-forward
```

---

## 検証結果

| 項目 | 結果 |
|------|------|
| コラボレーターによるブランチへのプッシュ | ✅ 成功 |
| プルリクエストの作成 | ✅ 成功 |
| オーナーによるレビュー・承認 | ✅ 成功 |
| マージ | ✅ 成功（マージコミット方式） |
| ローカル main への反映 | ✅ 成功 |

---

## 注意事項

- プッシュ時の認証は HTTPS + Personal Access Token（ariki-tomono アカウント）
- コミットのメールアドレスは GitHub のプライバシー保護のため noreply アドレスを使用
  - ariki-tomono の noreply: `128684460+ariki-tomono@users.noreply.github.com`
- エディタの自動フォーマッタが有効だと余計な差分が入る場合があるため注意

---

## 関連ドキュメント

- [handover.md](../handover.md) - プロジェクト全体の引継ドキュメント
