from flask import Flask ,  render_template,request
import pickle
import numpy as np
 app = Flask(__name__)

# Load the trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  # Extract features from form input
  int_features = [float(x) for x in request.form.values()]
  final_features = [np.array(init_features)]
  prediction = model.predict(final_features)


  output = 'High Risk of Heart Disease'  if prediction[0] == 1 else 'Low Risk of Heart Disease'

  return render_template('index.html', prediction_text=f'prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)
           
