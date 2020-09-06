import requests
import os
from dotenv import load_dotenv
import base64

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



def analyze_wav(audio_base64):
    url = 'https://api.webempath.net/v2/analyzeWav'

    apikey = os.getenv("API_KEY")
    payload = {'apikey': apikey}

    # wav = "./audio/happy-sample.wav"
    # data = open(wav, 'rb')

    data = base64.b64decode(audio_base64.encode('utf-8'))
    audioFile = {'wav' : data}

    return requests.post(url, params=payload, files=audioFile)

# with open('./audio/happy-sample.txt', 'rb') as fp:
#     output = analyze_wav(fp.read().decode('utf-8'))

# print(output.status_code)
# print(output.content)

# For happy:
# {'error': 0, 'calm': 17, 'anger': 30, 'joy': 1, 'sorrow': 0, 'energy': 31}
# Angry:
# {'error': 0, 'calm': 33, 'anger': 13, 'joy': 0, 'sorrow': 3, 'energy': 10}
# Sad
# {'error': 0, 'calm': 38, 'anger': 4, 'joy': 7, 'sorrow': 0, 'energy': 11}