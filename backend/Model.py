from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax;

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")

model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")

def scoreOutput(userString) : 
    encoded_text = tokenizer(userString, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    return scores
