from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import pandas as pd
from typing import Tuple

device = "cuda" if torch.cuda.is_available() else "cpu"

tokinizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
labels = ["positive", "negative", "neutral"]

def sentiment_estimate(news):
    if news:
        tokens = tokinizer(news, return_tensors= "pt", padding=True).to(device)
        
        results = model(tokens["input_ids"],attention_mask= tokens["attention_mask"])[
            "logits"]

        results = torch.nn.functional.softmax(torch.sum(results, 0), dim=-1)
        probability = results[results.argmax(results)]
        sentiment = labels[results.argmax(results)]
        return sentiment, probability
    else:
        return 0, labels[-1]
    
if __name__ == "__main__":
    tensor, sentiment = sentiment_estimate(['markets responded negatively to the news!','traders were displeased!'])
    print(f"Sentiment: {tensor}, Probability: {sentiment}")
    print(torch.cuda.is_available())