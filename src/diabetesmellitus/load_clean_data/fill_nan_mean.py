import pandas as pd

class FillNaN:
    def __init__(self, data):
        self.data = data
    
    def fill_nan(self):
        self.data[['height','weight']] = self.data[['height','weight']].fillna(self.data[['height','weight']].mean())
        return self.data