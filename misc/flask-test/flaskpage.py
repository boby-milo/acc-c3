from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/millo')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0')
