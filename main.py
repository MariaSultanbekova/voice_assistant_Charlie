from config import COMMAND_WORD, API_KEY
import time
import openai
import os
from gtts import gTTS


openai.api_key = API_KEY
last_question = ""


def speak(text, lang='ru'):
    """text voiceover"""
    tts = gTTS(text=text, lang=lang)
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")


while True:
    with open('transcriptions/transcript.txt', 'r', encoding='utf') as file:
        recorded_text = file.read()


    # we are looking for a command word that will be the beginning of the request
    match = recorded_text.lower().find(COMMAND_WORD)
    if match and recorded_text:
        query = recorded_text[match:].replace(last_question, '')
        last_question = recorded_text[match:]

        print(query)
        # sending the query
        response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": query}])
        response_text = response['choices'][0]['message']['content']
        print(response_text, '\n\n')

        # voiced
        speak(response_text)
        # take a break, because I do not have access to the paid version))
        time.sleep(15)
