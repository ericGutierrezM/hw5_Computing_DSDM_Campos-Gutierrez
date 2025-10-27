from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class Model:
    def __init__(self, column_list, column_target, penalty, C, solver, max_iter):
        self._column_list = column_list
        self._column_target = column_target
        self._penalty = penalty
        self._C = C
        self._solver = solver
        self._max_iter = max_iter
        self.model = 'LogisticRegression'

    def train(self, data):
        X = data[self._column_list]
        y = data[self._column_target]
        if(self.model=='LogisticRegression'):
            self._sc = StandardScaler()
            X_std = self._sc.fit_transform(X)
            self._modelLogistic = LogisticRegression(penalty=self._penalty, solver=self._solver, max_iter=self._max_iter)
            self._modelLogistic.fit(X_std, y)
        return None

    def predict(self, data):
        X_predict = data[self._column_list]
        X_predict_sc = self._sc.transform(X_predict)
        y_predicted = self._modelLogistic.predict_proba(X_predict_sc)[:, 1]
        return y_predicted

