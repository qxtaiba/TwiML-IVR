################################################################## BOILER PLATE ##################################################################

from flask import flash, render_template, redirect, request, session, url_for
from werkzeug.utils import append_slash_redirect
from twilio.twiml.voice_response import VoiceResponse

from ivr_phone_tree_python import app
from ivr_phone_tree_python.view_helpers import twiml

@app.route('/')
@app.route('/ivr')

def home():
    return render_template('index.html')

################################################################## BOILER PLATE ##################################################################

################################################################## WELCOME MENU ##################################################################

@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(num_digits=1, action=url_for('menu'), method="POST") as sreeIVR:
        sreeIVR.say("hello. you have reached tamarbutah's testing studio.")
        sreeIVR.pause(length=1)
        sreeIVR.say("please press 1 for the first sub-menu, press 2 for the second sub-menu, or press 3 to listen to your options again.")
        sreeIVR.pause(length=5)

    return twiml(response)


@app.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = {'1': optionA,
                      '2': optionB,
                      '3': relistenWelcome}

    if selected_option in option_actions:
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)

    return oopsRedirect_Welcome()

@app.route('/ivr/relistenWelcome', methods=['POST'])
def relistenWelcome(response):
    with response.gather(num_digits=1, action=url_for('menu'), method="POST") as sreeIVR:
        sreeIVR.say("please press 1 for the first sub-menu, press 2 for the second sub-menu, or press 3 to listen to your options again.")
        sreeIVR.pause(length=5)

    return twiml(response)

def oopsRedirect_Welcome():
    response = VoiceResponse()
    response.say("oops, you have selected an invalid option. let's try again.")
    response.redirect(url_for('welcome'))

    return twiml(response)

def redirect_welcome():
    response = VoiceResponse()
    response.redirect(url_for('welcome'))

    return twiml(response)


################################################################## WELCOME MENU ##################################################################

################################################################## OPTION A ##################################################################

@app.route('/ivr/optionA', methods=['POST'])
def optionA(response):
    with response.gather(numDigits=1, action=url_for('optionA_Handler'), method="POST") as sreeIVR:
        sreeIVR.say("you have selected the first sub-menu")
        sreeIVR.pause(length=1)
        sreeIVR.say("please press 1 for option 1A, press 2 for option 1B, press 3 for option 1C, press 4 for option 1D, press 5 for option 1E, or press 6 to listen to your options again. to return to the main menu, please press any key")
    return response

@app.route('/ivr/optionA_Handler', methods=['POST'])
def optionA_Handler():
    selected_option = request.form['Digits']
    option_actions = {'1': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                      '2': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                      '3': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
                      '4': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                      '5': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                      '6': relistenOptionA}

    if selected_option == "6":
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)
        
    elif selected_option in option_actions:
        response = VoiceResponse()
        with response.gather(numDigits=1, action=url_for('optionA_EndHandler'), method="POST") as sreeIVR:
            sreeIVR.play(option_actions[selected_option])
            sreeIVR.say("please press 1 to listen to another conversation, or press 2 to return to the main menu")
        return twiml(response)
        
    return redirect_welcome()

@app.route('/ivr/optionA_EndHandler', methods=['POST'])
def optionA_EndHandler():
    selected_option = request.form['Digits']
    option_actions = {'1': relistenOptionA,
                      '2': relistenWelcome}

    if selected_option in option_actions:
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)

    return oopsRedirect_optionA()


@app.route('/ivr/relistenOptionA', methods=['POST'])
def relistenOptionA(response):
    with response.gather(num_digits=1, action=url_for('optionA_Handler'), method="POST") as sreeIVR:
        sreeIVR.say("please press 1 for option 1A, press 2 for option 1B, press 3 for option 1C, press 4 for option 1D, press 5 for option 1E, or press 6 to listen to your options again. to return to the main menu, please press any key")
        sreeIVR.pause(length=5)

    return twiml(response)

def oopsRedirect_optionA():
    response = VoiceResponse()
    response.say("oops, you have selected an invalid option. let's try again.")
    response.redirect(url_for('optionA'))

    return twiml(response)

################################################################## OPTION A ##################################################################

################################################################## OPTION B ##################################################################
@app.route('/ivr/optionB', methods=['POST'])
def optionB(response):
    with response.gather(numDigits=1, action=url_for('optionB_Handler'), method="POST") as sreeIVR:
        sreeIVR.say("you have selected the second sub-menu")
        sreeIVR.pause(length=1)
        sreeIVR.say("please press 1 for option 1A, press 2 for option 1B, press 3 for option 1C, press 4 for option 1D, press 5 for option 1E, or press 6 to listen to your options again. to return to the main menu, please press any key")
    return response

@app.route('/ivr/optionB_Handler', methods=['POST'])
def optionB_Handler():
    selected_option = request.form['Digits']
    option_actions = {'1': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                      '2': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                      '3': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
                      '4': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                      '5': "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                      '6': relistenOptionB}

    if selected_option == "6":
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)
        
    elif selected_option in option_actions:
        response = VoiceResponse()
        with response.gather(numDigits=1, action=url_for('optionB_EndHandler'), method="POST") as sreeIVR:
            sreeIVR.play(option_actions[selected_option])
            sreeIVR.say("please press 1 to hear another musing, or press 2 to return to the main menu")
        return twiml(response)
        
    return redirect_welcome()

@app.route('/ivr/optionB_EndHandler', methods=['POST'])
def optionB_EndHandler():
    selected_option = request.form['Digits']
    option_actions = {'1': relistenOptionA,
                      '2': relistenWelcome}

    if selected_option in option_actions:
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)

    return oopsRedirect_optionB()

@app.route('/ivr/relistenOptionB', methods=['POST'])
def relistenOptionB(response):
    with response.gather(num_digits=1, action=url_for('optionB_Handler'), method="POST") as sreeIVR:
        sreeIVR.say("please press 1 for option 1A, press 2 for option 1B, press 3 for option 1C, press 4 for option 1D, press 5 for option 1E, or press 6 to listen to your options again. to return to the main menu, please press any key")
        sreeIVR.pause(length=5)

    return twiml(response)

def oopsRedirect_optionB():
    response = VoiceResponse()
    response.say("oops, you have selected an invalid option. let's try again.")
    response.redirect(url_for('optionB'))

    return twiml(response)

################################################################## OPTION B ##################################################################