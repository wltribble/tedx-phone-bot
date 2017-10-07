from flask import Flask, request, redirect, Response
from twilio.twiml.voice_response import VoiceResponse, Play


app = Flask(__name__)


def twiml(resp):
    resp = Response(str(resp))
    resp.headers['Content-Type'] = 'text/xml'
    return resp

@app.route('/', methods=['POST'])
def voice():
    response = VoiceResponse()
    with response as r:
        r.play('', digits='wwww#')
    return twiml(response)

if __name__ == "__main__":
    app.run(debug=False)
