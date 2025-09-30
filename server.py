"""
Flask application for Emotion Detection.
Provides endpoints to analyze user text and return emotion scores and dominant emotion.
"""
import json
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def emo_detector():
    """
    Analyze text passed via query parameter 'textToAnalyze' and return emotion results.
    Returns:
        Formatted string with emotion scores and dominant emotion, or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if isinstance(response, str):
        response = json.loads(response)

    dominant = response.get("dominant_emotion")
    if dominant is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
        'anger': {response['anger']}
        'disgust': {response['disgust']}
        'fear': {response['fear']}
        'joy': {response['joy']}
        'sadness': {response['sadness']}
        The dominant emotion is {dominant}"""

@app.route("/")
def render_index_page():
    """
    Render the main index page.
    Returns:
        Rendered HTML page.
    """
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
