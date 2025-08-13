"""
This module is reponsible for testing the emotion_detector from the EmotionDetection packages
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    This class creates an object from which unit tests for emotion_detector 
    can be run using a function.
    """
    def test_emotion_detection(self):
        """
        This function runs all the tests for emotion_detection using assetEqual
        """
        result1 = emotion_detector('I am glad this happend')['dominant_emotion']
        self.assertEqual(result1, 'joy')
        result2 = emotion_detector('I am really mad about this')['dominant_emotion']
        self.assertEqual(result2, 'anger')
        result3 = emotion_detector('I feel disgusted just hearing about this')['dominant_emotion']
        self.assertEqual(result3, 'disgust')
        result4 = emotion_detector('I am so sad abouth this')['dominant_emotion']
        self.assertEqual(result4, 'sadness')
        result5 = emotion_detector('I am really afraid this will happen')['dominant_emotion']
        self.assertEqual(result5, 'fear')

if __name__ == "__main__":
    unittest.main()