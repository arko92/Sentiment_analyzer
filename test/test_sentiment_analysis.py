from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        
        self.assertEqual(sentiment_analysis('I love working with Python'),'SENT_POSITIVE')
        self.assertEqual(sentiment_analysis('I hate working with Python'),'SENT_NEGATIVE')
        self.assertEqual(sentiment_analysis('I am neutral on Python'),'SENT_NEUTRAL')


unittest.main()