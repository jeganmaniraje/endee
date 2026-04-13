from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])

        features = np.array([[area, bedrooms, bathrooms]])
        prediction = model.predict(features)

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f"Estimated Price: ₹ {output}")
    
    except:
        return render_template('index.html', prediction_text="Error in input")

if __name__ == "__main__":
    app.run(debug=True)
