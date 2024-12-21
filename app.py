from flask import Flask, render_template, session , request ,redirect
import random
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret-key')

TruthQ = [
    "What's your biggest fear?",
    "Have you ever lied to a close friend?",
    "What's the most embarrassing thing you've ever done?",
    "Have you ever had a crush on a teacher?",
    "What's a secret you've never told anyone?",
    "If you could change one thing about yourself, what would it be?",
    "Have you ever cheated on a test?",
    "What's the most trouble you've gotten into at school?",
    "Who was your first crush?",
    "Have you ever pretended to like a gift you actually hated?",
    "What's the weirdest dream you've ever had?",
    "Have you ever stolen something?",
    "Who is your favorite family member?",
    "What's a lie you've told that you still feel guilty about?",
    "Have you ever had a crush on your best friend's partner?",
    "What's the most childish thing you still do?",
    "Have you ever blamed someone else for something you did?",
    "What's the worst grade you've ever received?",
    "Have you ever faked being sick to skip school or work?",
    "What's your most embarrassing habit?",
    "What's a secret you've kept from your parents?",
    "Have you ever eavesdropped on someone?",
    "What's the most awkward moment you've experienced?",
    "Have you ever ghosted someone?",
    "What's your most irrational fear?",
    "Have you ever been caught talking to yourself?",
    "What's the worst gift you've ever received?",
    "Have you ever peeked at someone else's phone without their permission?",
    "What's the most money you've ever spent on something silly?",
    "Have you ever cried during a movie? Which one?",
    "What's the worst lie you've ever told?",
    "Have you ever cheated in a game?",
    "What's your biggest insecurity?",
    "Have you ever had a crush on a fictional character?",
    "What's the weirdest thing you've ever eaten?",
    "Have you ever laughed at a joke you didn't understand?",
    "Have you ever been rejected by someone you liked?",
    "What's the silliest thing you've argued about?",
    "Have you ever lied about your age?",
    "What's the most embarrassing thing you've posted online?",
    "Have you ever been jealous of a friend?",
    "Have you ever broken a promise?",
    "What's the most scared you've ever been?",
    "Have you ever lied about your accomplishments?",
    "What's your guilty pleasure?",
    "Have you ever been caught singing in the shower?",
    "What's the worst advice you've ever given?",
    "Have you ever copied someone else's homework?",
    "What's the weirdest thing you've done in front of a mirror?",
    "Have you ever snooped through someone's things?",
    "Have you ever had a wardrobe malfunction?",
    "What's the worst thing you've ever smelled?",
    "Have you ever forgotten someone's name right after meeting them?",
    "What's the most awkward text you've sent to the wrong person?",
    "Have you ever fallen asleep in class or at work?",
    "Have you ever lied to get out of trouble?",
    "What's the most embarrassing thing you've Googled?",
    "Have you ever lied about liking a meal someone cooked for you?",
    "What's the strangest rumor you've heard about yourself?",
    "Have you ever exaggerated a story to make it sound better?",
    "What's the most awkward conversation you've ever had?",
    "Have you ever kept a diary or journal?",
    "What's the worst haircut you've ever had?",
    "Have you ever pretended to know something when you didn't?",
    "What's the grossest thing you've ever done?",
    "Have you ever had a crush on a friend's sibling?",
    "What's the most embarrassing nickname you've ever had?",
    "Have you ever been caught in a lie?",
    "What's the most annoying habit you have?",
    "Have you ever laughed so hard you cried?",
    "Have you ever stalked someone on social media?",
    "What's the most ridiculous thing you've been upset about?",
    "Have you ever fallen in public?",
    "What's the strangest thing you've ever collected?",
    "Have you ever broken something and blamed it on someone else?",
    "What's the most random thing in your room?",
    "Have you ever been scared of the dark?",
    "What's the worst movie you've ever watched?",
    "Have you ever kept a secret for someone and regretted it?",
    "What's the funniest misunderstanding you've had?",
    "Have you ever forgotten a special occasion like a birthday?",
    "What's the most awkward thing you've said on a date?",
    "Have you ever re-gifted something you received?",
    "What's the longest you've gone without showering?",
    "Have you ever pretended to like a TV show or movie to impress someone?",
    "What's the weirdest compliment you've ever received?",
    "Have you ever been caught daydreaming?",
    "What's the most unusual thing you've done out of boredom?",
    "Have you ever avoided someone because you didn't want to talk to them?",
    "What's the worst text message you've ever sent?",
    "Have you ever pretended to be asleep to avoid a conversation?",
    "What's the silliest thing you've cried over?",
    "Have you ever been caught dancing when you thought no one was watching?",
    "What's the most embarrassing thing that's happened to you in public?"
]

DareQ = [
    "Do 10 push-ups right now.",
    "Sing your favorite song out loud.",
    "Do an impression of someone in the room.",
    "Run around the outside of the house three times.",
    "Let the person next to you post something on your social media.",
    "Eat a spoonful of hot sauce.",
    "Talk in an accent for the next 3 rounds.",
    "Do your best dance move for a minute.",
    "Wear socks on your hands for the next 5 minutes.",
    "Call a random person and sing 'Happy Birthday' to them.",
    "Let someone draw on your face with a marker.",
    "Do your best animal impression.",
    "Hold your breath for 30 seconds.",
    "Do 20 jumping jacks.",
    "Speak in a whisper until your next turn.",
    "Let someone tickle you for 30 seconds.",
    "Try to lick your elbow.",
    "Act like a chicken until your next turn.",
    "Let someone give you a temporary tattoo with a pen.",
    "Do 15 squats.",
    "Pretend to be a statue for 2 minutes.",
    "Do your best impression of a celebrity.",
    "Eat a raw onion slice.",
    "Let someone style your hair in a silly way.",
    "Do the worm dance.",
    "Try to juggle 3 items of your choice.",
    "Run in place for a minute.",
    "Walk across the room like a crab.",
    "Say everything in a rhyme until your next turn.",
    "Do your best fake cry.",
    "Let someone write a funny word on your forehead.",
    "Try to stand on one foot for 60 seconds.",
    "Put an ice cube down your shirt and let it melt.",
    "Talk without moving your lips until your next turn.",
    "Eat a spoonful of mustard.",
    "Let someone give you a new hairstyle.",
    "Pretend to be a waiter and serve drinks to everyone.",
    "Do a cartwheel (or try to).",
    "Let someone else redo your profile picture on social media.",
    "Talk like a robot until your next turn.",
    "Wear a funny hat for the next 3 rounds.",
    "Do 20 sit-ups.",
    "Pretend to be a monkey until your next turn.",
    "Make the funniest face you can and hold it for 30 seconds.",
    "Try to lick your nose.",
    "Let someone pour water on your head.",
    "Spin around 10 times and try to walk straight.",
    "Do your best stand-up comedy routine for 1 minute.",
    "Try to do a handstand.",
    "Let someone choose an item of clothing for you to wear.",
    "Do your best karate move.",
    "Speak in gibberish for 2 minutes.",
    "Let someone else paint your nails any color they choose.",
    "Try to hop on one foot for 30 seconds.",
    "Put your socks on your hands until your next turn.",
    "Do your best impression of a baby crying.",
    "Balance a book on your head and walk across the room.",
    "Let someone tickle your feet for 30 seconds.",
    "Dance like no one's watching for 1 minute.",
    "Try to moonwalk across the room.",
    "Say the alphabet backward as fast as you can.",
    "Pretend to be a cat and meow for the next minute.",
    "Do your best runway model walk.",
    "Let someone put makeup on you.",
    "Do a plank for 1 minute.",
    "Talk like a pirate until your next turn.",
    "Hold a funny face for the next 2 minutes.",
    "Do your best slow-motion action scene.",
    "Let someone tie your shoes together.",
    "Try to do a backbend (or attempt one).",
    "Do 10 burpees.",
    "Act like your favorite superhero for 1 minute.",
    "Let someone mess up your hair.",
    "Pretend to be a dog and fetch something.",
    "Sing the chorus of a random song in a high-pitched voice.",
    "Do your best evil laugh.",
    "Try to balance on one leg with your eyes closed for 30 seconds.",
    "Do an interpretive dance to a random song.",
    "Let someone draw something on your arm.",
    "Run around the room flapping your arms like a bird.",
    "Do your best impression of a fish out of water.",
    "Pretend to be a waiter and take everyone's food orders.",
    "Let someone redo your hairstyle.",
    "Do your best zombie walk.",
    "Do 15 push-ups while counting out loud.",
    "Let someone give you a new nickname and call you that for the next 3 rounds.",
    "Pretend you're a superhero and save the day.",
    "Wear a towel like a cape for the next 3 turns.",
    "Let someone write something embarrassing on your hand.",
    "Speak in a made-up language for 1 minute.",
    "Pretend to be an alien trying to communicate with humans.",
    "Wear your shirt backward for the next 3 rounds.",
    "Pretend you're underwater for 1 minute.",
    "Spin around 5 times and then try to walk in a straight line.",
    "Balance a spoon on your nose for 30 seconds.",
    "Do your best dance while sitting in a chair.",
    "Pretend to be a character from your favorite movie."
]


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
        return render_template('gamemode.html', players=players)
    
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