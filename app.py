from flask import Flask, render_template, session , request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gameload', methods=['POST', 'GET'])
def gameload():
    if request.method == 'POST':
        Number = request.form.get('Numbers')

    return render_template("gameload.html")


if __name__ == '__main__':
    app.run(debug=True,port=5000)   