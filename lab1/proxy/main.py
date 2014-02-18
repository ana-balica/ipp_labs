import time
from urlparse import urljoin
from flask import Flask, render_template, request, flash, session

from download import Downloader, ProxyDownloader


app = Flask(__name__)
app.secret_key = 'some_secret_key_whatever'
media = {"WGS.115": "http://ocw.mit.edu/ans15436/ZipForEndUsers/WGS/wgs-115-spring-2013/wgs-115-spring-2013.zip",
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
        title = request.form["ocw"]
        long_title = media[title].split('/')[-1]
        filepath = urljoin("downloads/", long_title)
        downloader = Downloader()
        downloader.get(media[title], filepath)
        flash('Successfully downloaded {0}'.format(long_title))
    return render_template('proxy.html', page_title="No proxy", action="no_proxy")


@app.route('/simple-proxy/', methods=['GET', 'POST'])
def simple_proxy():
    if request.method == 'POST':
        if 'request_count' not in session:
            session['request_count'] = 1
        else:
            session['request_count'] += 1
        title = request.form["ocw"]
        long_title = media[title].split('/')[-1]
        filepath = urljoin("downloads/", long_title)
        downloader = Downloader()
        proxy = ProxyDownloader(downloader, session['request_count'])
        download_data = proxy.get(media[title], filepath)
        if download_data:
            session['request_count'] = 0
            for data in download_data:
                flash('Successfully downloaded {0}'.format(data[1].split('/')[-1]))
    return render_template('proxy.html', page_title="Simple proxy", action="simple_proxy")    


@app.route('/caching-proxy/')
def caching_proxy():
    pass


if __name__ == "__main__":
    app.debug = True
    app.run()