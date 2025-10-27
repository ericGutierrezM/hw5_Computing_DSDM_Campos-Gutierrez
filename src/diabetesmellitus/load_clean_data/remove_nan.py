import pandas as pd

class RemoveNaN:
   def __init__(self, data):
      self.data = data
   
   def remove_nan(self):
      return self.data.dropna(subset=['age', 'gender', 'ethnicity'])