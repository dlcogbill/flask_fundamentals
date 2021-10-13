from flask import Flask, render_template  # added render_template!
app = Flask(__name__)

@app.route('/play')
def play1():
    return render_template('index.html', x = 3, color = 'cyan')

@app.route('/play/<num>')
def play2(num):
    num = int(num)
    return render_template('index.html', x = num, color = 'cyan')

@app.route('/play/<num>/<col>')
def play3(num, col):
    num = int(num)
    col = str(col)
    return render_template('index.html', x = num, color = col)

if __name__=="__main__":
    app.run(debug=True)