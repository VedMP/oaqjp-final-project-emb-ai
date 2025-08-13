"""
This Module is responsible for understanding the emotion of the text the user provide
"""
import requests
import json
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
    emotionPredictions = json.loads(response.text) #Turn the response text into a json file.

    #Get the scores of the emotions using
    # emotionPredictions['emotionPredictions'][0]['emotion']['emotion_name'].
    anger_score = emotionPredictions['emotionPredictions'][0]['emotion']['anger'] 
    disgust_score = emotionPredictions['emotionPredictions'][0]['emotion']['disgust']
    fear_score = emotionPredictions['emotionPredictions'][0]['emotion']['fear']
    joy_score = emotionPredictions['emotionPredictions'][0]['emotion']['joy']
    sadness_score = emotionPredictions['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = ""
    high_score =0
    return_dict =  {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,'joy': joy_score,'sadness': sadness_score}

    # Finds dominant emotion using comparison to find the emotion with the highest 
    # score and set it dominant emotion in 'return_dict'
    for emotion in return_dict.keys():
        if high_score < return_dict[emotion]:
            high_score = return_dict[emotion]
            dominant_emotion = emotion 
    return_dict['dominant_emotion'] = dominant_emotion
    return return_dict