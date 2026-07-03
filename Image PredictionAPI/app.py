from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No image uploaded"

    image = request.files['image']

    # Dummy prediction
    prediction = "Cat"
    confidence = "95%"

    return f"""
    <h2>Prediction Result</h2>
    <p><b>File:</b> {image.filename}</p>
    <p><b>Prediction:</b> {prediction}</p>
    <p><b>Confidence:</b> {confidence}</p>
    <br>
    <a href="/">Try Another Image</a>
    """

if __name__ == '__main__':
    app.run(debug=True)