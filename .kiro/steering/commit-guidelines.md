# コミット時の注意事項

コミット・プッシュを行う際は、以下の設定・注意点を必ず守ってください。
過去のトラブルを踏まえた重要なルールです。

## コミット用メールアドレス（必読）

- このリポジトリの `user.email` は **noreply アドレス** に設定する。
  - オーナー `ariki4160`: `577649+ariki4160@users.noreply.github.com`
  - コラボレータ `ariki-tomono`: `128684460+ariki-tomono@users.noreply.github.com`
- 理由: 実アドレス（例: `ariki1068@gmail.com`）でプッシュすると、GitHub の
  メールプライバシー保護（`GH007: Your push would publish a private email address`）で
  **拒否される**ため。
- **noreply アドレスのまま維持すること。** 実アドレスに戻すとプッシュが再び拒否される。
- 確認コマンド: `git config user.email`
- noreply アドレスは `<ユーザーID>+<ユーザー名>@users.noreply.github.com` の形式。
  ユーザーIDは `gh api users/<ユーザー名> --jq .id` で確認できる。

## フォーマッタによる差分の肥大化に注意

- エディタの自動フォーマッタ（Prettier 等）が働くと、1行追加のつもりでも
  `<!DOCTYPE html>` → `<!doctype html>` やタグの自己終了化など**余計な差分**が入る。
- 最小差分にしたい場合は、ファイルに直接挿入するのが確実。
  - 例: `sed -i 's|</body>|    <p>追加行</p>\n</body>|' test.html`
  - ※ macOS の BSD sed では `sed -i ''` のように空の拡張子引数が必要な場合がある。

## コミットメッセージ

- 変更内容が分かる簡潔な日本語で記述する。
  - 例: `ariki-tomono からの動作確認メッセージ追加`
