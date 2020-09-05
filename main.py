import requests

url = 'https://api.webempath.net/v2/analyzeWav'

apikey = 'beCDBTXWx4-u4NL_i1PDBrvGyGdzBCwTwAu4w-fxfCk'
payload = {'apikey': apikey}

wav = "./audio/sad-sample.wav"
data = open(wav, 'rb')
audioFile = {'wav' : data}

res = requests.post(url, params=payload, files=audioFile)
print(res.json())

# Results (not very accurate lol):
# For happy:
# {'error': 0, 'calm': 17, 'anger': 30, 'joy': 1, 'sorrow': 0, 'energy': 31}
# Angry:
# {'error': 0, 'calm': 33, 'anger': 13, 'joy': 0, 'sorrow': 3, 'energy': 10}
# Sad
# {'error': 0, 'calm': 38, 'anger': 4, 'joy': 7, 'sorrow': 0, 'energy': 11}