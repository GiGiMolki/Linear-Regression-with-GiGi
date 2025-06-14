from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('slr_model.pkl')  # Make sure this path is correct

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        income = float(request.form['income'])
        prediction = model.predict(np.array([[income]]))[0]
        return render_template('index.html', prediction=prediction, income=income)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=5001)