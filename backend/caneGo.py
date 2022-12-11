# caneGo main file

from caption import caption
from speech import text_to_speech
from get_audio import get_audio
from playwav import playaudio

import json
 

# generate caption for the scene:
model_type = "j-min/clip-caption-reward"
m_version = "de37751f75135f7ebbe62548e27d6740d5155dfefdf6447db35c9865253d7e06"
image_path = "https://images.pexels.com/photos/13876637/pexels-photo-13876637.jpeg"
get_description = caption(model_type, m_version, image_path)

# request text to speech for the captoin:
result = text_to_speech(get_description)
result = json.loads(result)

audio_uuid = result.get('uuid')
print(audio_uuid)
audio = get_audio(audio_uuid)

print("finnal result : audio file wav format ")
print (audio)

playaudio(audio)

print("cycle done")

