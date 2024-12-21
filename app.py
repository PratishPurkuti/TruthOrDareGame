from flask import Flask, render_template, session , request ,redirect
from truthanddare import TruthQ,DareQ
import random
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret-key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gameload', methods=['POST', 'GET'])
def gameload():
    if request.method == 'POST':
        try:
            Number = int(request.form.get('number'))
        except (ValueError, TypeError):
            # Handle cases where the input is not a valid integer
            return "Invalid input. Please enter a number."
        if 2 <= Number <= 15:
            session['Number'] = Number
            return render_template('playername.html',Number=Number)

    return render_template("gameload.html")
@app.route('/playername', methods=['POST', 'GET'])
def playername():
    if request.method == 'POST':
        Number = session.get('Number')  # Retrieve the number of players from the session
        players = []
        for i in range(1, Number + 1):  # Iterate over a range from 1 to Number (inclusive)
            player_name = request.form.get(f'player{i}')  # Get the player's name from the form
            players.append(player_name)  # Add the name to the list
        session["players"] = players
        # Pass the players list to the next template if needed
        return render_template('Gamemode.html', players=players)
    
    # Handle GET requests
    Number = session.get('Number', 0)
    return render_template('playername.html', Number=Number)

@app.route('/classic', methods=['POST','GET'])
def classic():
    players= session.get('players')
    name = random.choice(players)
    print(name)
    return render_template('classic.html',name = name)
    
@app.route('/truth')
def truth():
    randoms = random.choice(TruthQ)
    return render_template('question.html',randoms = randoms)

@app.route('/dare')
def dare():
    randoms = random.choice(DareQ)
    return render_template('question.html',randoms = randoms)

if __name__ == '__main__':
    app.run()   