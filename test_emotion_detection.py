import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(sentiment_analyzer('I am glad this happened')['label'], 'SENT_POSITIVE')
        self.assertEqual(sentiment_analyzer('I hate working with Pyhton')['label'], 'SENT_NEGATIVE')
        self.assertEqual(sentiment_analyzer('I am neutral on Python')['label'], 'SENT_NEUTRAL')

unittest.main()
