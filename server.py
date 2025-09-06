'''Analyse emotions from the text'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """return analysed emotions from the given text"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']

    return f"For the given statement, the system response is \
     'anger': {anger_score}, \
     'disgust': {disgust_score}, \
     'fear': {fear_score}, \
     'joy': {joy_score} and \
     'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."


@app.route("/")
def index():
    """return page index.html"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
