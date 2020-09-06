from typing import Optional
from fastapi import FastAPI
from empath import analyze_wav
from Recommendation_system import score,emotion,index
from typing import Dict

import json

# resBody = res.json()

app = FastAPI()

# @app.get("/voice/{voice_type}")
# def read_item(voice_type: str, q: Optional[str] = None):
#     return {
#         "calm": resBody.get('calm'), 
#         "anger": resBody.get('anger'),
#         "joy": resBody.get('joy'),
#         "sorrow": resBody.get('sorrow'), 
#         "energy": resBody.get('energy'),
#         }

# @app.get("/emotion/{emotion_type}")
# def read_item(emotion_type: str, q: Optional[str] = None):
#     return {
#         "scores": score,
#         "emotions": emotion,
#         "dominantEmotion": emotion[index]
#         }

@app.post("/audio")
def process(data: Dict[str,str]):
    # print(data['audio_message'].encode('utf-8'))
    output = analyze_wav(data['audio_message'])
    print(output.status_code)
    print(output.content)
    return data
    
    # return analyze_wav(data['audio_message'])