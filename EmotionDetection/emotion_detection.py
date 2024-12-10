import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyse):
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json = myobj, headers=HEADERS)

    if response.status_code == 400:
        to_return = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
            }

    elif response.status_code == 200:
        formatted_response = json.loads(response.text)
        to_return = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = ''
        dominant_score = 0
        for emotion, score in to_return.items():
            if score > dominant_score:
                dominant_emotion = emotion
                dominant_score = score
        to_return.update({'dominant_emotion': dominant_emotion})

    return to_return
