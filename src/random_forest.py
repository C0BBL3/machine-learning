from decision_tree import DecisionTree

class RandomForest:
    def __init__(self, number_of_random_trees, class_name = 'class', max_depth = 5):
        self.number_of_random_trees = number_of_random_trees
        self.class_name = class_name
        self.max_depth = max_depth

    def fit(self, dataframe):
        self.random_trees = [DecisionTree(dataframe = dataframe, split_metric='random', class_name = self.class_name, max_depth = self.max_depth) for number_of_random_tree in range(self.number_of_random_trees)]
        for tree in self.random_trees: tree.fit()

    def classify(self, observation):
        classifications = [random_tree.classify(observation) for random_tree in self.random_trees]
        votes = [(classification_type, classifications.count(classification_type)) for classification_type in classifications]
        return max(votes, key=lambda vote: vote[1])[0]
