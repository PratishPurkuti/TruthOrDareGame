from flask import Flask, render_template, session , request ,redirect


app = Flask(__name__)
app.secret_key = 'kaloseto'

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

@app.route('/playername',methods=['POST','GET'])
def playername():
    if request.method =='POST':
        Number = session.get('Number')
        return render_template('Gamemode.html')
    return render_template('playername.html',Number=Number)

if __name__ == '__main__':
    app.run(debug=True,port=5000)   