import urllib
from urlparse import urljoin
from flask import Flask, render_template, request


app = Flask(__name__)
books = {"head_first_web_design": "http://it-ebooks.info/go.php?id=378-1392675790-f597a7940b48b95cb72f848efad42016",
         "head_first_design_patterns": "http://it-ebooks.info/go.php?id=252-1392675832-83f522728f81e90f89ed476ff9c95e55",
         "head_first_data_analysis": "http://it-ebooks.info/go.php?id=250-1392675874-42981d0d415bf9387170465f29d5116c",
         "head_first_rails": "http://it-ebooks.info/go.php?id=374-1392678356-5810778fb9f821ec03ace650664cd30d",
         "head_first_wordpress": "http://it-ebooks.info/go.php?id=379-1392678394-f9ed6d1e4fdefb737c271a08b7310af7"}


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/no-proxy/', methods=['GET', 'POST'])
def no_proxy():
    if request.method == 'POST':
        title = request.form["book"]
        filepath = urljoin("downloads/", title + '.pdf')
        urllib.urlretrieve(books[title], filepath)
    return render_template('proxy.html', page_title="No proxy")


@app.route('/simple-proxy/')
def simple_proxy():
    pass


@app.route('/caching-proxy/')
def caching_proxy():
    pass


if __name__ == "__main__":
    app.debug = True
    app.run()