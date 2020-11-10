class NaiveBayesClassifier:
    def __init__(self, dataframe, dependent_variable='scam'):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable

    def probability(self, variable, boolean):
        return self.dataframe.data_dict[variable].count(boolean) / len(self.dataframe.data_dict[variable])
    
    def conditional_probability(self, parameter, given=(None, False)):
        conditional_list = []
        for i, boolean in enumerate(self.dataframe.data_dict[parameter[0]]):
            if self.dataframe.data_dict[given[0]][i] == given[1]:
                conditional_list.append(boolean)
        return conditional_list.count(parameter[1]) / len(conditional_list)
    
    def likelihood(self, parameter, observed_features):
        result = self.probability(parameter[0], parameter[1])
        for variable, boolean in observed_features.items():
            result *= self.conditional_probability((variable, boolean), given = parameter)
        return result

    def classify(self, variable, observed_features):
        if self.likelihood((variable, True), observed_features) != self.likelihood((variable, False), observed_features):
            return self.likelihood((variable, True), observed_features) >= self.likelihood((variable, False), observed_features)
        else:
            return 