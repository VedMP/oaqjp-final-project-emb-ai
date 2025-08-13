"""
This Module is responsible for understanding the emotion of the text the user provide
"""
import requests

# Function that given 'text_to_analyze' gets the emotions using Watson NLP
# libaray's emotion Predict function via an API call.
def emotion_detector(text_to_analyze):
    """
    This module uses the url for Watson NLP's Emotion Predict, its corresponding headers,
    and json object containing the text to be analyze the emotion of the text.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_object = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json = my_object, headers=headers)
    return response.text
