"""
This is a Flask app that lets you do an emotion analysis of an input text string.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Returns an emotion analysis of input string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return_string = "Invalid text! Please try again!"
    else:
        return_string = "For the given statement, the system response is "+\
            f"'anger': {result['anger']}, "+\
            f"'disgust': {result['disgust']}, "+\
            f"'fear': {result['fear']}, "+\
            f"'joy': {result['joy']} and "+\
            f"'sadness': {result['sadness']}. "+\
            f"The dominant emotion is {result['dominant_emotion']}."

    return return_string

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
