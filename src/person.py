import pandas as pd
import numpy as np


class Person:
    """Class representing a person and their personal info

    Instance Variables
    ------------------
    age : int
        Age of individual
    sex : str
        Biological sex of individual
    ever_married : bool
        Whether the individual has ever been married
    has_heart_disease : bool
        Whether the individual has a heart disease
    has_hypertension : bool
        Whether the individual suffers form high blood pressure
    work_type : str
        The type of work the individual is involved in
    residence_type : str
        The type of area the individual lives
    avg_glucose_level : float
        The average glucose level of the individual
    bmi : float
        The individual's Body Mass Index
    smoking_status : str
        The individual's relationship with smoking

    Public Methods
    --------------
    get_info() -> pd.DataFrame
        Returns the individual's personal information as a record in a table
    """
    def __init__(self, age: int, sex: str, ever_married: bool, has_heart_disease: bool, has_hypertension: bool,
                 work_type: str, residence_type: str, smoking_status: str, avg_glucose_level: float = None,
                 bmi: float = None):
        self.age: int = age
        self.sex: str = sex
        self.ever_married: bool = ever_married
        self.has_heart_disease: bool = has_heart_disease
        self.has_hypertension: bool = has_hypertension
        self.work_type: str = work_type
        self.residence_type: str = residence_type
        self.avg_glucose_level: float = avg_glucose_level
        self.bmi: float = bmi
        self.smoking_status: str = smoking_status

    def get_info(self) -> pd.DataFrame:
        """Return personal info as a single-row dataframe"""
        return pd.DataFrame({'gender': [self.sex], 'age': [self.age], 'hypertension': [int(self.has_hypertension)],
                             'heart_disease': [int(self.has_heart_disease)],
                             'ever_married': ['Yes' if self.ever_married else 'No'], 'work_type': [self.work_type],
                             'Residence_type': [self.residence_type],
                             'avg_glucose_level': [np.nan if not self.avg_glucose_level else self.avg_glucose_level],
                             'bmi': [np.nan if not self.bmi else self.bmi], 'smoking_status': [self.smoking_status]})
