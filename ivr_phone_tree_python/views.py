from flask import (
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
)
from twilio.twiml.voice_response import VoiceResponse

from ivr_phone_tree_python import app
from ivr_phone_tree_python.view_helpers import twiml


@app.route('/')
@app.route('/ivr')
def home():
    return render_template('index.html')


@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(num_digits=1, action=url_for('menu'), method="POST") as g:
        g.say(message="Hello. You have reached Q's audio test. ")
        g.say(message="Please press 1 for option A, or Press 2 for option B to access hidden options.")
        g.pause(length=5)

    return twiml(response)


@app.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = {'1': optionA,
                      '2': optionB}

    if selected_option in option_actions:
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()


@app.route('/ivr/optionB_Handler', methods=['POST'])
def optionB_Handler():
    selected_option = request.form['Digits']
    option_actions = {'1': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                      '2': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                      '3': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.play(option_actions[selected_option])
        return twiml(response)
        
    return _redirect_welcome()


# private methods
def optionA(response):
    with response.gather(numDigits=1, action=url_for('optionB_Handler'), method="POST") as g:
    # g.play("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        g.say("yoyooyoyoyoyoyo i love q")
        g.say("To return to the main menu, please press the star key")
    return response

@app.route('/ivr/optionB', methods=['POST'])
def optionB(response):
    with response.gather(
        numDigits=1, action=url_for('optionB_Handler'), method="POST"
    ) as g:
        g.say("You have selected option B.")
        g.say("To hear option C press 1, to hear option D press 2, or to hear option E press 3.")
        g.pause(length=5)

    return response


def _redirect_welcome():
    response = VoiceResponse()
    response.say("Let's try again")
    response.redirect(url_for('welcome'))

    return twiml(response)

