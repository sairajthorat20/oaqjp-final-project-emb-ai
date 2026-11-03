"""
Offline Unit Tests with Mocking for Emotion Detection and Error Handling.
"""
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetectionOffline(unittest.TestCase):
    """
    Unit tests verifying payload formatting, response parsing,
    dominant emotion logic, and error handling using mock responses.
    """

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_detection(self, mock_post):
        """Test joy detection with mocked 200 OK response."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''{
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.90,
                        "sadness": 0.04
                    }
                }
            ]
        }'''
        mock_post.return_value = mock_response

        res = emotion_detector("I am glad this happened")
        self.assertEqual(res['dominant_emotion'], 'joy')
        self.assertEqual(res['joy'], 0.90)

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_detection(self, mock_post):
        """Test anger detection with mocked 200 OK response."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''{
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.88,
                        "disgust": 0.03,
                        "fear": 0.02,
                        "joy": 0.01,
                        "sadness": 0.06
                    }
                }
            ]
        }'''
        mock_post.return_value = mock_response

        res = emotion_detector("I am really mad about this")
        self.assertEqual(res['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_detection(self, mock_post):
        """Test disgust detection with mocked 200 OK response."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''{
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.05,
                        "disgust": 0.82,
                        "fear": 0.03,
                        "joy": 0.02,
                        "sadness": 0.08
                    }
                }
            ]
        }'''
        mock_post.return_value = mock_response

        res = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_detection(self, mock_post):
        """Test sadness detection with mocked 200 OK response."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''{
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.02,
                        "disgust": 0.03,
                        "fear": 0.04,
                        "joy": 0.01,
                        "sadness": 0.90
                    }
                }
            ]
        }'''
        mock_post.return_value = mock_response

        res = emotion_detector("I am so sad about this")
        self.assertEqual(res['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_detection(self, mock_post):
        """Test fear detection with mocked 200 OK response."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''{
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.02,
                        "disgust": 0.03,
                        "fear": 0.89,
                        "joy": 0.01,
                        "sadness": 0.05
                    }
                }
            ]
        }'''
        mock_post.return_value = mock_response

        res = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res['dominant_emotion'], 'fear')

    def test_blank_input(self):
        """Test that blank and whitespace-only input returns None for all values."""
        res_empty = emotion_detector("")
        self.assertIsNone(res_empty['dominant_emotion'])
        self.assertIsNone(res_empty['anger'])

        res_space = emotion_detector("   ")
        self.assertIsNone(res_space['dominant_emotion'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_http_400_status(self, mock_post):
        """Test that HTTP 400 error returns None for all dictionary values."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = 'Bad Request'
        mock_post.return_value = mock_response

        res = emotion_detector("Invalid query")
        self.assertIsNone(res['dominant_emotion'])
        self.assertIsNone(res['anger'])
        self.assertIsNone(res['joy'])


if __name__ == '__main__':
    unittest.main()
