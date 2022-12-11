# This is the text to speech module
# It will use the uberduck api to connvert text to speech. 
# The text is coming from Replicate api as a description of a given scene.

import requests


def text_to_speech(speech_text):

    url = "https://api.uberduck.ai/speak"
    speech = speech_text

    print(speech)

    payload = {
        "voice": "lj",
        "pace": 1,
        "speech": speech
    }
    headers = {
        "accept": "application/json",
        "uberduck-id": "anonymous",
        "content-type": "application/json",
        "authorization": "Basic cHViX2loeWJpYnJldHhleGl4cHR5Zzpwa19hOGQ5ZDQ3OC04ZTE5LTQxNDktODlmYy04NjU5ZjU2MzRjZDg="
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text