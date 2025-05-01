# FinBERT financial news sentiment

from transformers import BertTokenizer, BertForSequenceClassification, pipeline

tokenizer = BertTokenizer.from_pretrained("ProsusAI/finbert")
model = BertForSequenceClassification.from_pretrained("ProsusAI/finbert")
finbert_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def analyze_finbert_batch(texts):
    return finbert_pipeline(texts, truncation=True)
