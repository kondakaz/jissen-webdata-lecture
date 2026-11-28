from pathlib import Path
import random
from html import escape
from textwrap import indent

ROOT = Path(__file__).resolve().parent.parent
random.seed(22)

def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8', newline='\n')

def page(title, body, root=''):
    return f'''<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="robots" content="noindex, nofollow">
    <title>{title} | 星野原大学案内</title>
    <link rel="stylesheet" href="{root}assets/style.css">
  </head>
  <body>
    <header>
      <a href="{root}index.html">星野原大学案内</a>
      <nav>
        <a href="{root}campus/index.html">大学案内</a>
        <a href="{root}stock/index.html">架空株価</a>
        <a href="{root}robots-guide.html">robots.txt</a>
      </nav>
    </header>
    <main>
      <h1>{title}</h1>
      <p class="notice">授業用の架空データ。この教材内の指定ページは収集練習可。</p>
{indent(body, '      ')}
    </main>
    <footer>星野原大学は架空の大学である。</footer>
  </body>
</html>
'''

def card(i, prefix=''):
    titles=['学園祭の開催案内','図書館の利用案内','公開講座のお知らせ','サークル交流会','キャンパス見学会','展示会のお知らせ','施設利用のお知らせ','講演会の案内','学習相談会','地域交流イベント','読書週間のお知らせ','研究紹介の案内','音楽会のお知らせ','進学相談会','作品展の案内','施設見学会']
    # 見出しとリンクの間に空白を加えず、そのまま１行に置く。
    return f'''<article class="news-card" data-news-id="N{i:03}">
  <p class="date">2026-10-{i:02}</p>
  <p class="category">{["イベント","案内"][i%2]}</p>
  <h2 class="news-title"><a href="{prefix}n{i:03}.html">{titles[i-1]}</a></h2>
</article>'''


def cards(ids, prefix=''):
    return indent('\n'.join(card(i, prefix) for i in ids), '  ')


def pagination():
    links = '\n'.join(f'  <a href="page{k}.html">{k}ページ</a>' for k in range(1, 4))
    return f'<nav>\n{links}\n</nav>'

def table(headers, rows, ident):
    header_cells = '\n'.join(f'      <th>{escape(header)}</th>' for header in headers)
    body_rows = []
    for row in rows:
        cells = '\n'.join(f'      <td>{escape(str(cell))}</td>' for cell in row)
        body_rows.append(f'    <tr>\n{cells}\n    </tr>')
    body = '\n'.join(body_rows)
    return f'''<table id="{ident}">
  <thead>
    <tr>
{header_cells}
    </tr>
  </thead>
  <tbody>
{body}
  </tbody>
</table>'''

write('assets/style.css','''body{margin:0;font-family:system-ui,sans-serif;color:#26364a;background:#f6f8fa;line-height:1.65}header,footer{background:#18385a;color:white;padding:1rem max(1rem,calc((100% - 1000px)/2))}header a,footer a{color:white}nav a{margin-right:1em}main{max-width:1000px;margin:auto;padding:2rem 1rem}h1{border-left:6px solid #b5863f;padding-left:.6em}h2{font-size:1.2rem}.notice{background:#fff3cf;padding:1em}.news-card{background:white;border:1px solid #d5dce4;border-radius:5px;padding:.5em 1em;margin:.7em 0}table{border-collapse:collapse;background:white}td,th{border:1px solid #aab8c4;padding:.4em .8em}th{background:#e6eef5}a{color:#135382}''')
write('index.html', page('練習サイト', '''<p>大学案内と架空株価のページでHTMLの読み取りを練習する。</p>
<ul>
  <li><a href="campus/index.html">大学案内</a></li>
  <li><a href="stock/index.html">架空株価</a></li>
  <li><a href="robots-guide.html">robots.txtの解説</a></li>
</ul>'''))
events=table(['event_id','date','event','capacity'],[['E001','2026-11-01','公開講座',80],['E002','2026-11-08','見学会',40],['E003','2026-11-15','作品展',60],['E004','2026-11-22','交流会',50]],'events')
facilities = table(['施設', '場所'], [['図書館', '中央棟']], 'facilities')
body = f'''<p id="campus-message">大学生活に関する情報を掲載しています。</p>
<p><a href="news/page1.html">過去のお知らせ</a></p>
<section id="student-news">
  <h2>学生向けお知らせ</h2>
{cards(range(1, 4), 'news/')}
</section>
<section id="public-news">
  <h2>一般向けお知らせ</h2>
{cards(range(4, 7), 'news/')}
</section>
<section id="other-info">
  <h2>その他の案内</h2>
  <p class="date">更新日 2026-10-30</p>
  <div>
    <p>入れ子の案内</p>
  </div>
</section>
<h2>サークル一覧</h2>
<ul id="circles">
  <li>読書会</li>
  <li>写真同好会</li>
  <li>音楽研究会</li>
</ul>
<h2>イベント予定表</h2>
{events}
<h2>施設案内</h2>
{facilities}'''
write('campus/index.html',page('大学案内',body,'../'))
for n, ids in enumerate([range(1,7),range(7,13),range(13,17)],1):
    body = f'''<section id="news-list">
{cards(ids)}
</section>
{pagination()}'''
    write(f'campus/news/page{n}.html', page('過去のお知らせ', body, '../../'))
for i in range(1,17):
    body = f'''<p>お知らせ N{i:03} の教材用本文である。</p>
<p><a href="page1.html">一覧へ</a></p>'''
    write(f'campus/news/n{i:03}.html', page('お知らせ', body, '../../'))
companies=[('S001','桜台フード','食品'),('S002','みどり交通','交通'),('S003','青空通信','通信')]
master = table(['company_code', 'company_name', 'industry'], companies, 'company-master')
company_links = '\n'.join(f'  <li><a href="{code}/page1.html">{name}</a></li>' for code, name, _ in companies)
body = f'''<p>月初の日付は月を表すラベルであり、取引日ではない。価格は教材上の円である。</p>
{master}
<ul>
{company_links}
</ul>'''
write('stock/index.html', page('架空株価', body, '../'))
for j,(code,name,industry) in enumerate(companies):
    for p in range(1,4):
        rows=[]
        for m in range(1,13):
            t=(p-1)*12+m-1
            price=1000+j*350+(t*6 if j==0 else (t%5)*4 if j==1 else -min(t,18)*8+max(0,t-18)*8)+random.randint(-8,8)
            rows.append([f'{2022+p}-{m:02}-01',price,10000+j*1500+random.randint(0,1000)])
        history = table(['date', 'close', 'volume'], rows, 'stock-history')
        body = f'''<p>架空データ。日付は月ラベルであり取引日ではない。</p>
{history}
{pagination()}'''
        write(f'stock/{code}/page{p}.html', page(name + 'の月次株価', body, '../../'))
write('robots-guide.html', page('robots.txtの解説', '''<p>robots.txtは自動アクセスに対する規則であり、利用規約や著作権の許諾そのものではない。</p>
<p>授業で確認するrobots.txt: <a href="https://kondakaz.github.io/jissen-webdata-lecture/robots.txt">https://kondakaz.github.io/jissen-webdata-lecture/robots.txt</a></p>
<p>「User-agent: *」の組は、本教材のprivateディレクトリをDisallowし、Crawl-delayに5秒を指定している。Crawl-delayへの対応はクローラにより異なる。</p>
<p>BadPracticeBotは全体を拒否する例である。自分の名乗りに合う専用の組があるプログラムは、その組に従う。Rではrobotstxtパッケージのpaths_allowed()で判定を確かめられる。</p>
<p><a href="private/index.html">拒否対象の体験ページ</a></p>'''))
write('private/index.html',page('関係者専用の例','<p>robots.txtのDisallowを説明するための架空ページである。機密情報はない。</p>','../'))
write('.nojekyll','')
