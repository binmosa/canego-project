


import requests
import simpleaudio


def playaudio(audio):

    sample_rate = 8000
    num_channels = 2
    bytes_per_sample = 2

    total = sample_rate * num_channels * bytes_per_sample

   # logging.basicConfig(level=logging.INFO)

    audio_url = audio

   # logging.info(f"Downloading audio file from: {audio_url}")
    content = requests.get(audio_url).content

    # Just to ensure that the file does not have extra bytes
    #blocks = len(content) // total
    #content = content[:total * blocks]

    wave = simpleaudio.WaveObject(audio_data=content,
                                sample_rate=sample_rate,
                                num_channels=num_channels,
                                bytes_per_sample=bytes_per_sample)
    control = wave.play()
    control.wait_done()
    return
