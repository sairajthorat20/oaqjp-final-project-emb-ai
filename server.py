"""
Emotion Detection Web Application Server using Flask.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def detect_emotion():
    """
    Endpoint to receive text from frontend, analyze emotions via emotion_detector,
    and format response string for display.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response is None or response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant = response["dominant_emotion"]

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant}."
    )


@app.route("/")
def render_index_page():
    """
    Serves the main application page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
