import urllib
from urlparse import urljoin
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = 'some_secret_key_whatever'
books = {"WGS.115": "http://ocw.mit.edu/ans15436/ZipForEndUsers/WGS/wgs-115-spring-2013/wgs-115-spring-2013.zip",
         "6.046J": "http://ocw.mit.edu/ans15436/ZipForEndUsers/6/6-046j-spring-2012/6-046j-spring-2012.zip",
         "ES.S60": "http://ocw.mit.edu/ans15436/ZipForEndUsers/ES/es-s60-spring-2013/es-s60-spring-2013.zip",
         "18.353J": "http://ocw.mit.edu/ans15436/ZipForEndUsers/18/18-353j-fall-2012/18-353j-fall-2012.zip",
         "24.118": "http://ocw.mit.edu/ans15436/ZipForEndUsers/24/24-118-spring-2013/24-118-spring-2013.zip"}


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/no-proxy/', methods=['GET', 'POST'])
def no_proxy():
    if request.method == 'POST':
        title = request.form["book"]
        filepath = urljoin("downloads/", title + '.zip')
        urllib.urlretrieve(books[title], filepath)
        flash('Successfully downloaded {0}'.format(title))
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