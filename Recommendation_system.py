
import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# All the Backend Stuff
version='2020-09-05'
authenticator = IAMAuthenticator({api-key})
tone_analyzer = ToneAnalyzerV3(
    version=version,
    authenticator=authenticator
)
tone_analyzer.set_service_url({url})

# Text Input from the aggregate of the UI
text="Hated you"

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
