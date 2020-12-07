from dataframe import DataFrame

class LeaveOneOutCrossValidator:
    def __init__(self, knn, dataframe, prediction_column):
        self.knn = knn
        self.dataframe = dataframe
        self.prediction_column = prediction_column

    def accuracy(self):
        correct_observations = []
        temp = []
        for i in range(len(self.dataframe.to_array())):
            observation = {self.dataframe.columns[i]: value for i,value in enumerate(self.dataframe.to_array()[i])}
            dataframe_without_kth_row = self.dataframe.select_rows([j for j in range(len(self.dataframe.to_array())) if i != j])
            self.knn.fit(dataframe_without_kth_row, self.prediction_column)
            correct_observations.append(self.knn.classify(observation,i) == observation[self.prediction_column])
            correct_observation = observation[self.prediction_column]
            classification = self.knn.classify(observation,i)
            temp.append((correct_observation,classification))
        return correct_observations.count(True)/len(correct_observations)