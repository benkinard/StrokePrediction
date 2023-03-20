import dill
import pandas as pd
from pathlib import Path
from person import Person


class StrokePredictor:
    def __init__(self):
        abs_path = Path(__file__).resolve().parent.parent
        with open(abs_path / "Data/model.pkl", "rb") as f:
            self.model = dill.load(f)
        self.data = {'gender': None, 'age': None, 'hypertension': None, 'heart_disease': None, 'ever_married': None,
                     'work_type': None, 'residence_type': None, 'avg_glucose_level': None, 'bmi': None,
                     'smoking_status': None}

    def format_data(self, person: Person) -> pd.DataFrame:
        # TODO: Read Person attributes into self.data
        return pd.DataFrame(self.data)

    def make_prediction(self, person: Person) -> bool:
        X = self.format_data(person)
        return self.model.predict(X)


if __name__ == '__main__':
    StrokePredictor()
