import joblib

def load_model_and_vectorizer(model_path='models/fake_news_model.joblib', vectorizer_path='models/tfidf_vectorizer.joblib'):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

def predict_news(text, model, vectorizer):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    return 'REAL' if prediction == 1 else 'FAKE'
