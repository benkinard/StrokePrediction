from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    # TODO: Handle blank form values
    print(f"Age: {request.form['age']}")
    print(f"Sex: {request.form['sex']}")
    print(f"Married: {request.form['marital-status']}")
    print(f"Heart Disease: {request.form['heart-disease']}")
    print(f"Hypertension: {request.form['hypertension']}")
    print(f"Work Status: {request.form['work']}")
    print(f"Residence Type: {request.form['residence']}")
    print(f"Avg Glucose Level: {request.form['glucose']}")
    print(f"BMI: {request.form['bmi']}")
    print(f"Smoking Status: {request.form['smoking']}")
    # TODO: Create person object from form data

    return "<h1>Prediction Landing Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
