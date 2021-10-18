import random # import the random module
import time
random.seed(time.process_time())
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    
    if 'attempts' in session:
        print('Keep trying!')
        print(f"Attempts: {session['attempts']}")
    else:
        print("Good luck!")
        session['solution'] = random.randint(1, 100)
        session['attempts'] = 0
        print(f"Attempts: {session['attempts']}")
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['attempts'] += 1
    print(request.form)
    session['user_guess'] = int(request.form['answer'])
    print(f"{session['solution']} {session['user_guess']}")
    print(f"Attempts: {session['attempts']}")
    return redirect('/')

@app.route('/success', methods=['POST'])
def success():
    print(request.form)
    print(f"{session['solution']} {session['user_guess']}")
    print(f"Attempts: {session['attempts']}")
    session['attempts'] = 0
    session['solution'] = random.randint(1, 100)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)