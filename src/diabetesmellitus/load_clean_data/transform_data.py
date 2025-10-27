import pandas as pd
from abc import ABCMeta, abstractmethod

class TransformParent(metaclass=ABCMeta):
    @abstractmethod
    def transform(self):
        return NotImplementedError


class TransformGender(TransformParent):
    def __init__(self, data):
        self.data = data
    
    def transform(self):
        self.data['gender'] = self.data["gender"].map({"M": 1, "F": 0})
        return self.data

class TransformEthnicity(TransformParent):
    def __init__(self, data):
        self.data = data
    
    def transform(self):
        self.data = pd.get_dummies(self.data, columns=['ethnicity'], dtype=int)
        return self.data
        
