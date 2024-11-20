from transformers import pipeline

def analyze_sentiment(news_text):
    try:
        sentiment_analyzer = pipeline("sentiment-analysis")

        result = sentiment_analyzer(news_text)

        positive = sum(1 for r in result if r['label'] == 'POSITIVE')
        negative = sum(1 for r in result if r['label'] == 'NEGATIVE')
        neutral = len(result) - positive - negative

        return {
            "positive": positive,
            "negative": negative,
            "neutral": neutral,
        }

    except Exception as e:
        raise RuntimeError(f"Error in sentiment analysis: {e}")
