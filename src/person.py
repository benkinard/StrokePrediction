class Person:
    def __init__(self, age: int, sex: str, is_married: bool, has_heart_disease: bool, has_hypertension: bool,
                 work_type: str, residence_type: str, smoking_status: str, avg_glucose_level: float = None,
                 bmi: float = None):
        self.age: int = age
        self.sex: str = sex
        self.is_married: bool = is_married
        self.has_heart_disease: bool = has_heart_disease
        self.has_hypertension: bool = has_hypertension
        self.work_type: str = work_type
        self.residence_type: str = residence_type
        self.avg_glucose_level: float = avg_glucose_level
        self.bmi: float = bmi
        self.smoking_status: str = smoking_status

    def get_info(self):
        # TODO: Write method here
        return
