from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
from nltk.corpus import stopwords
import nltk

# Ensure that stopwords are downloaded (run once)
nltk.download('stopwords')

# Define the English stop words
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Preprocess the text by:
    - Lowercasing
    - Removing HTML tags
    - Removing punctuation and numbers (keeping only alphabets and spaces)
    - Tokenizing the text and removing English stop words
    """
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    filtered_tokens = [token for token in tokens if token not in stop_words]
    cleaned_text = ' '.join(filtered_tokens)
    return cleaned_text

# Load the saved vectorizer and model from your pickle file.
with open('sentiment_model.pkl', 'rb') as file:
    vectorizer, model = pickle.load(file)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Ensure the JSON payload contains the required 'review' key.
    if not data or 'review' not in data:
        return jsonify({'error': 'No review provided'}), 400

    review = data['review']
    # Apply the cleaning function on the incoming review.
    cleaned_review = clean_text(review)

    print("Original Review: ", review)  # Debugging line
    print(f"Cleaned Review: {cleaned_review}")  # Debugging line
    # Vectorize the cleaned review.
    review_vectorized = vectorizer.transform([cleaned_review])
    prediction = model.predict(review_vectorized)

    # Assuming your label mapping: 0 = negative, 1 = positive.
    result = 'positive' if prediction[0] == 1 else 'negative'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
