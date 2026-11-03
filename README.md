# IBM Emotion Detection Web Application

A web-based Emotion Detection application built with Python, Flask, and the IBM Watson NLP EmotionPredict service. This project analyzes the sentiment and emotion behind user-submitted text, returning individual emotion scores for anger, disgust, fear, joy, and sadness, along with the dominant emotion.

This project is developed as the Final Project for the **IBM: Developing AI Applications with Python and Flask** course (part of the IBM DevOps and Software Engineering / Applied AI professional certificates).

---

## Architecture and Project Structure

```text
final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py               # Package initialization exposing emotion_detector
│   └── emotion_detection.py      # Core NLP emotion detection logic & API caller
├── static/
│   └── mywebscript.js            # Frontend JavaScript handling AJAX requests
├── templates/
│   └── index.html                # Web interface template
├── server.py                     # Flask web server routing and response formatting
├── test_emotion_detection.py     # Unit test suite verifying emotion classifications
├── test_offline.py               # Unit tests verifying response handling and edge cases
├── README.md                     # Project documentation
└── .gitignore                    # Git ignore file
```

---

## Features

- **Watson NLP Integration**: Connects to the IBM Watson NLP `EmotionPredict` service using gRPC metadata header `emotion_aggregated-workflow_lang_en_stock`.
- **Emotion Analysis Breakdown**: Formats and returns fine-grained scores for five core emotions:
  - `anger`
  - `disgust`
  - `fear`
  - `joy`
  - `sadness`
- **Dominant Emotion Identification**: Identifies the dominant emotion based on the maximum score among the five emotions.
- **Robust Error Handling**:
  - Rejects empty, whitespace-only, or invalid text.
  - Gracefully handles HTTP 400 Bad Request responses and network timeouts by returning `None` for all emotion scores and notifying the user.
- **Flask Web Deployment**: Serves a responsive web interface on port 5000.
- **PEP 8 / Pylint Compliance**: Passes static code analysis with a perfect **10.00/10** score.

---

## Installation and Setup

### 1. Prerequisites
- Python 3.10+ (tested with Python 3.12)
- Virtual environment (`venv`)

### 2. Create Virtual Environment and Install Dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .\.venv\Scripts\activate
pip install flask requests pylint
```

---

## Running the Application

Start the Flask server:
```bash
python server.py
```
By default, the application runs on `http://localhost:5000` (or `http://0.0.0.0:5000`).

Open your web browser and navigate to `http://localhost:5000`. Enter text in the textarea and click **Run Sentiment Analysis**.

---

## Example Outputs

### Valid Input Example
**Input text:** `"I am glad this happened"`
**Response:**
```text
For the given statement, the system response is 'anger': 0.005, 'disgust': 0.002, 'fear': 0.003, 'joy': 0.968 and 'sadness': 0.045. The dominant emotion is joy.
```

### Invalid / Blank Input Example
**Input text:** `""`
**Response:**
```text
Invalid text! Please try again!
```

---

## Running Unit Tests

Run the test suite using Python's built-in `unittest` runner:
```bash
python -m unittest test_emotion_detection.py
```

To run offline test cases with mock responses:
```bash
python -m unittest test_offline.py
```

---

## Static Code Analysis (Pylint)

Run pylint on the server and emotion detection module:
```bash
pylint server.py EmotionDetection/emotion_detection.py
```
**Score:** `10.00/10`
