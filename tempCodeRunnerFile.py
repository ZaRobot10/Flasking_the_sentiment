# Load the saved vectorizer and model
# with open('/Users/ekankaar/Documents/Projects_again/flasking/sentiment_model.pkl', 'rb') as file:
#     vectorizer, model = pickle.load(file)

# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
    
#     # Ensure the JSON payload contains the required 'review' key
#     if not data or 'review' not in data:
#         return jsonify({'error': 'No review provided'}), 400
    
#     review = data['review']
#     review_vectorized = vectorizer.transform([review])
#     prediction = model.predict(review_vectorized)
    
#     # Assuming your label mapping: 0 = negative, 1 = positive
#     result = 'positive' if prediction[0] == 1 else 'negative'
#     return jsonify({'prediction': result})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
