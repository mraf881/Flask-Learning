from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def selamatdatang():
    return render_template('selamatdatang.html')

@app.route('/aplikasisatu')
def aplikasisatu():
    return render_template('aplikasisatu.html')

@app.route('/aplikasidua')
def aplikasidua():
    return render_template('aplikasidua.html')

if __name__ == '__main__':
    app.run(debug=True)