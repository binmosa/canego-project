
# This is the get audio module
# It will fetch the audio file from uberduck

import requests
import time
import json

def get_audio(code):

    url = "https://api.uberduck.ai/speak-status?uuid={}".format(code)

    # fixing the delay in response (takign time to generate audio)
    # here we could play a sound such : this is the description of the current scene:
    time.sleep(5)
     
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    response = response.json()
    audio_file = response['path']
    
    return audio_file