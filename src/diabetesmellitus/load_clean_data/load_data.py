import pandas as pd
from sklearn.model_selection import train_test_split

class LoadData:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        self.data = pd.read_csv(self.path, sep=',')
        self.y = self.data['diabetes_mellitus']
        self.X = self.data.drop(['diabetes_mellitus'], axis=1)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
        self.X, self.y, test_size=0.2, random_state=23, stratify=self.y)

        self.df_train = self.X_train.join(self.y_train).reset_index()
        self.df_test = self.X_test.join(self.y_test).reset_index()

        return self.df_train, self.df_test