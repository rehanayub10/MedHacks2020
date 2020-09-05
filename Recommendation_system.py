
import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# All the Backend Stuff
version='2020-09-05'
authenticator = IAMAuthenticator('Koiz6SDn9oG82iXIFi-IimRPcKb0ar302KZ7fnsHRzql')
tone_analyzer = ToneAnalyzerV3(
    version=version,
    authenticator=authenticator
)
tone_analyzer.set_service_url('https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/216cbdf1-ee0e-4eea-90da-592042bf347b')

# Text Input from the aggregate of the UI
text="i am sooo confused"

# Running the tone analysis on the Text Input
tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()

# Parsing the results
score=[];
emotion=[];
for i in tone_analysis["document_tone"]["tones"]:
    score.append(i['score'])
    emotion.append(i['tone_id'])
print(score,emotion)

# Most elicited emotion
if score:
    index=score.index(max(score))
    print("Strongest emotion: %s" %emotion[index])

print(score,emotion)
print(emotion[index])
