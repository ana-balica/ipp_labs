from flask import Flask, render_template, request


app = Flask(__name__)
books = {"head_first_javascript": "http://filepi.com/i/67jRlIk",
		 "head_first_ajax": "http://filepi.com/i/mqjSTFf",
		 "head_first_mobile_web": "http://filepi.com/i/deiTISD",
		 "head_first_python": "http://it-ebooks.info/go.php?id=373-1392673408-99416e0f6a7e26889228df535550c3c5",
		 "head_first_programming": "http://it-ebooks.info/go.php?id=372-1392673452-f82251d58ced6458b12a2f92e0d6d3f8"}


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/no-proxy/', methods=['GET', 'POST'])
def no_proxy():
    if request.method == 'POST':
        print request.form
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