from flask import Flask, render_template  # added render_template!
app = Flask(__name__)

@app.route('/')
def board1():
    return render_template('index.html', rows = 8, cols = 8, color = "black", alternateColor = "red")

@app.route('/<x>')
def board2(x):
    x = int(x)
    return render_template('index.html', rows = x, cols = 8, color = "black", alternateColor = "red")

@app.route('/<x>/<y>')
def board3(x, y):
    x = int(x)
    y = int(y)
    return render_template('index.html', rows = x, cols = y, color = "black", alternateColor = "red")

@app.route('//<x>/<y>/<color1>/<color2>')
def board4(x, y, color1, color2):
    x = int(x)
    y = int(y)
    return render_template('index.html', rows = x, cols = y, color = color1, alternateColor = color2)

if __name__=="__main__":
    app.run(debug=True)