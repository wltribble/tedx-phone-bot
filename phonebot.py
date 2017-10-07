from flask import Flask, request, redirect
from twilio.twiml.voice_response import Play, VoiceResponse


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    response.play('', digits='wwww#')

    return str(response)

if __name__ == "__main__":
    app.run(debug=False)
