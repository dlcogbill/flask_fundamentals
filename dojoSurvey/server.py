from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['user_name'] = request.form['name']
    session['user_location'] = request.form['location']
    session['user_favorite_language'] = request.form['favorite_language']
    session['user_platform'] = request.form['platform']
    session['user_comment'] = request.form['comment']
    session['reasons'] = request.form.getlist('reason')
    for i in session['reasons']:
        print(i)
    print(session)
    return render_template('results.html')

@app.route('/results', methods=['POST'])
def results():
    print(session)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)