from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Routes for each bot attack
@app.route('/bot1')
def bot1():
    # Execute bot1 attack using Selenium
    # You can call your existing Selenium bot here
    subprocess.run(['python3', 'bot1.py'])
    return redirect(url_for('index'))

@app.route('/bot2')
def bot2():
    # Execute bot2 attack using Selenium
    subprocess.run(['python3', 'bot2.py'])
    return redirect(url_for('index'))

@app.route('/bot3')
def bot3():
    # Execute bot3 attack using Selenium
    subprocess.run(['python3', 'bot3.py'])
    return redirect(url_for('index'))

@app.route('/bot4')
def bot4():
    # Execute bot4 attack using Selenium
    subprocess.run(['python3', 'bot4.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
