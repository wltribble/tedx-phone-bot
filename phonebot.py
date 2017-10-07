from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse, Play


app = Flask(__name__)


@app.route('/', methods=['POST'])
def voice():
    response = VoiceResponse().play('', digits='wwww#')
    return response

if __name__ == "__main__":
    app.run(debug=False)
