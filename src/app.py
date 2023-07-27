from flask import Flask, flash, render_template, request
from person import Person

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    # Confirm all fields that cannot be empty are not empty
    expected_req_fields_to_ui_map = {'age': 'Age', 'sex': 'Sex', 'work': 'Work Type', 'residence': 'Residence Type',
                                     'smoking': 'Smoking Status'}
    expected_fields_in_actual = [expected in request.form.keys() for expected in expected_req_fields_to_ui_map.keys()]
    if not all(expected_fields_in_actual):
        missing_field = list(expected_req_fields_to_ui_map.keys())[expected_fields_in_actual.index(False)]
        flash(f"Please fill out \"{expected_req_fields_to_ui_map[missing_field]}\" field", "error")

    # Create person object from form data
    age = int(request.form['age'])
    sex = request.form['sex']
    ever_married = 'marital-status' in request.form.keys()
    has_heart_disease = 'heart-disease' in request.form.keys()
    has_hypertension = 'hypertension' in request.form.keys()
    work_type = request.form['work']
    residence_type = request.form['residence']
    avg_glucose_level = None if request.form['glucose'] == '' else float(request.form['glucose'])
    bmi = None if request.form['bmi'] == '' else float(request.form['bmi'])
    smoking_status = request.form['smoking']

    person = Person(age, sex, ever_married, has_heart_disease, has_hypertension, work_type, residence_type,
                    smoking_status, avg_glucose_level, bmi)

    # Make prediction
    X = person.get_info()

    return "<h1>Prediction Landing Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
