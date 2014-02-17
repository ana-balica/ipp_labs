from flask import Flask, render_template, request
app = Flask(__name__)

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