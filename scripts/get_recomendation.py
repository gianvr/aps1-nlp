import pandas as pd
from scripts.get_data import get_data
from sklearn.feature_extraction.text import TfidfVectorizer


def get_recommendation(query, threshold=0.1):
    df = get_data()
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["OriginalTweet"])

    query_vector = vectorizer.transform([query])

    R = X.dot(query_vector.T)
    R = R.todense()
    R = pd.DataFrame(R, columns=["Relevance"])
    R["OriginalTweet"] = df["OriginalTweet"]
    R = R.sort_values("Relevance", ascending=False)
    R = R[R["Relevance"] > threshold]
    
    return R
