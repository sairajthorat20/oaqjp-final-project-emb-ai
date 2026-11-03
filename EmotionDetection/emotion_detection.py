"""
Emotion Detection Module using IBM Watson NLP EmotionPredict Service.
"""
import json
import requests


def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP EmotionPredict service and extracts emotion scores
    along with the dominant emotion.

    Args:
        text_to_analyze (str): The input text to analyze.

    Returns:
        dict: A dictionary containing anger, disgust, fear, joy, sadness,
              and dominant_emotion. Returns None for all keys if the input
              is blank or if the API returns status code 400.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    # Handle blank or whitespace-only input before calling the API
    if not text_to_analyze or not str(text_to_analyze).strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )
    except requests.exceptions.RequestException:
        # Gracefully handle connection issues or timeouts
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Handle HTTP 400 or other client/server errors
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
