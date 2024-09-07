from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model dari file
model = pickle.load(open('churn_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Ambil data dari request
        features = [
            data['CreditScore'],
            data['Age'],
            data['Balance'],
            data['Has_Credit_Card'],
            data['Is_Active_Member'],
            data['Estimated_Salary'],
            data['geo_France'],
            data['geo_Germany'],
            data['geo_Spain'],
            data['Female'],
            data['Male'],
            data['nop_1'],
            data['nop_2'],
            data['nop_3'],
            data['nop_4'],
            data['Ten_0'],
            data['Ten_1'],
            data['Ten_2'],
            data['Ten_3'],
            data['Ten_4'],
            data['Ten_5'],
            data['Ten_6'],
            data['Ten_7'],
            data['Ten_8'],
            data['Ten_9'],
            data['Ten_10']
        ]
        prediction = model.predict([features])  # Prediksi
        return jsonify({'prediction': prediction.tolist()})  # Return hasil prediksi
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)
