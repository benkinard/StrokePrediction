import dill
import uuid
from flask import Flask, flash, redirect, render_template, request, url_for
from person import Person

# TODO: Handle wait time for prediction to load
# TODO: Create template HTML file for prediction landing page
# Configure app
app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    # Confirm all required fields are not empty
    if request.form['age'] == '':
        flash("Please fill out \"Age\" field", "error")
        return redirect(url_for('index'))

    required_drop_down_fields = {'sex': 'Sex', 'work': 'Work Type', 'residence': 'Residence Type',
                                 'smoking': 'Smoking Status'}
    expected_fields_in_actual = [expected in request.form.keys() for expected in required_drop_down_fields.keys()]
    if not all(expected_fields_in_actual):
        missing_field = list(required_drop_down_fields.keys())[expected_fields_in_actual.index(False)]
        flash(f"Please fill out \"{required_drop_down_fields[missing_field]}\" field", "error")

        return redirect(url_for('index'))

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

    # Load model
    with open('static/model.pkl', 'rb') as pickle:
        model = dill.load(pickle)
    # Make prediction
    X = person.get_info()
    is_stroke_likely = model.predict(X)[0]

    return f"<h1>Prediction Landing Page</h1>\n<p>Likely to have a stroke: {'Yes' if is_stroke_likely else 'No'}"


if __name__ == "__main__":
    app.run(debug=True)
