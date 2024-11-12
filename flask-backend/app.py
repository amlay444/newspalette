from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    Returns 'positive', 'negative', or 'neutral' based on the sentiment score.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def get_article_sentiment(articles):
    """
    Analyze the sentiment of a list of articles.
    Each article should be a dictionary with a 'description' key.
    Returns a list of articles with an added 'sentiment' key.
    """
    for article in articles:
        if 'description' in article:
            article['sentiment'] = analyze_sentiment(article['description'])
    return articles
