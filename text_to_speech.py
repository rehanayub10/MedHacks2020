
import os
from google.cloud import texttospeech
# Add your google api authentication credentials
credential_path="/Users/revanthbn/OneDrive/MentalHealthTracker/My-First-Project-5928deb2c80b.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="I feel like a burden. I feel lonely. I’m not doing very well. I miss my family. ")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-UK", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)
# See if there's a way to integrate the response directly
# The response's audio_content is binary.
with open("alexa1.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
