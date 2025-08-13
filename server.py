"""
This module contains the flask server and routes for our web application
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate our Flask object app
app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders 'index.html'.
    """
    return render_template("index.html")
@app.route("/emotionDetector")
def detect_emotion():
    """
    Obtains 'textToAnalyze' gets its results and returns the results in a friendler
    and more informative way.
    """
    text_to_analyze= request.args.get('textToAnalyze')
    result_dict = emotion_detector(text_to_analyze)

    #Cretes a formmated string for giving the user the response in formatted manor
    response = f"""For the given statement, the system reponse is 'anger': {result_dict['anger']},
    'disgust': {result_dict['disgust']}, 'fear' : {result_dict['fear']}, 'joy' : {result_dict['joy']},
    'sadness' : {result_dict['sadness']}. The dominant emotion is
    {result_dict['dominant_emotion']}"""
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
