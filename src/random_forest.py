from decision_tree import DecisionTree

class RandomForest:
    def __init__(self, number_of_random_trees):
        self.random_trees = [DecisionTree('random') for number_of_random_tree in range(number_of_random_trees)]

    def fit(self, dataframe):
        for random_tree in self.random_trees: random_tree.fit(dataframe)

    def classify(self, observation):
        observations = [random_tree.classify(observation) for random_tree in self.random_trees]
        votes = [(classification_type, observations.count(classification_type)) for classification_type in set(observations)]
        return max(votes, key=lambda vote: vote[1])[0]
