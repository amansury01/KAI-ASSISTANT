from transformers import pipeline

# Load once and reuse
sentiment_analyzer = pipeline("sentiment-analysis")

def detect_sentiment(text):
    result = sentiment_analyzer(text)[0]
    label = result['label']
    score = result['score']
    
    print(f"🎭 Sentiment: {label} ({round(score, 2)})")
    return label
