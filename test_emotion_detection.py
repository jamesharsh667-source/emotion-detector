"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test formatted emotion output and dominant emotion detection."""

    def test_emotion_detector_returns_formatted_output(self):
        mock_response = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.95,
                        "sadness": 0.04
                    }
                }
            ]
        }

        with patch("EmotionDetection.emotion_detection.requests.post") as mock_post:
            mock_post.return_value.json.return_value = mock_response
            result = emotion_detector("I am happy today")

        expected_output = {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.95,
            "sadness": 0.04,
            "dominant_emotion": "joy"
        }
        self.assertEqual(result, expected_output)

    def test_dominant_emotion_is_highest_score(self):
        mock_response = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.87,
                        "disgust": 0.05,
                        "fear": 0.10,
                        "joy": 0.01,
                        "sadness": 0.15
                    }
                }
            ]
        }

        with patch("EmotionDetection.emotion_detection.requests.post") as mock_post:
            mock_post.return_value.json.return_value = mock_response
            result = emotion_detector("I am very angry")

        self.assertEqual(result["dominant_emotion"], "anger")

    def test_status_code_400_returns_none_values(self):
        with patch("EmotionDetection.emotion_detection.requests.post") as mock_post:
            mock_post.return_value.status_code = 400
            result = emotion_detector("")

        expected_output = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
