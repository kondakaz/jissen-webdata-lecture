# 練習サイト

授業用の架空サイトで、指定ページのデータ収集と授業内での保存を許可する。

- `campus/index.html` と `campus/news/page1.html`～`page3.html`：第９・10回のタグ、class、id、階層、カード、表とページ送り。
- `stock/index.html` と `stock/S001/page1.html` など：第11回の架空３社の月次株価。
- `robots-guide.html`：第９回の robots.txt の説明。`private/` は拒否例で、機密情報を置かない。

## ビルド

Python 3 でリポジトリのルートから `python tools/build_site.py` を実行する。乱数シードは22で固定している。生成されたHTMLやCSSを手で編集せず、生成スクリプトを変更して再実行する。

## 公開手順

GitHub Pages で公開する際は、ホスト側リポジトリの robots.txt も併せて確認する。公開後に実際の URL と `bow()` の動作を確認する。

検索クローラーが `noindex` を読み取れるよう、robots.txt に検索クローラー向けの一律拒否は追加しない。
