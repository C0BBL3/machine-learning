from dataframe import DataFrame
import random


class DecisionTree:
    def __init__(self, dataframe, split_metric='gini'):
        self.dataframe = dataframe
        self.root = DecisionTreeNode(dataframe, split_metric)

    def split(self):
        self.root.split(self.root)

    def fit(self):
        self.root.fit(self.root)

    def classify(self, coords):
        return self.root.classify(coords)


class DecisionTreeNode:
    def __init__(self, dataframe, split_metric):
        self.dataframe = dataframe
        self.split_metric = split_metric
        self.row_indices = self.dataframe.data_dict['indices']
        self.class_count = {}
        for indice_class in dataframe.data_dict['class']:
            if indice_class not in self.class_count.keys():
                self.class_count[indice_class] = 1
            else:
                self.class_count[indice_class] += 1
        self.impurity = self.impurity_function()
        self.possible_splits = self.possible_splits_function()
        self.low, self.high = None, None
        self.split_bool = False

    def classify(self, coords, current_node=None):
        if current_node == None:
            current_node = self
        if current_node.impurity != 0:
            best_split_var = current_node.best_gini_split()
            if best_split_var is not None:
                if coords[best_split_var[0]] < best_split_var[1]:
                    return current_node.classify(coords, current_node=current_node.low)
                elif coords[best_split_var[0]] >= best_split_var[1]:
                    return current_node.classify(coords, current_node=current_node.high)
            else:
                return current_node.dataframe.data_dict['class'][0]
        else:
            return current_node.dataframe.data_dict['class'][0]

    def fit(self, current_node=None):
        if current_node.low is None and current_node.high is None and current_node.impurity != 0:
            current_node.split(current_node)
        if current_node.low is not None and current_node.low.impurity != 0:
            current_node.fit(current_node.low)
        if current_node.high is not None and current_node.high.impurity != 0:
            current_node.fit(current_node.high)

    def split(self, current_node):
        current_node.split_bool = True
        current_node_needs_splitting = current_node.low is None and current_node.high is None and current_node.impurity != 0
        current_node_low_needs_splitting = current_node.low is not None and current_node.low.impurity != 0
        current_node_high_needs_splitting = current_node.high is not None and current_node.high.impurity != 0
        if current_node_needs_splitting:
            if self.split_metric == 'gini':
                split = current_node.best_gini_split()
            elif self.split_metric == 'random':
                split = current_node.random_split()
            if split[0] == 'x':
                current_node.low = current_node.get_low_split(x=split[1])
                current_node.high = current_node.get_high_split(x=split[1])
            if split[0] == 'y':
                current_node.low = current_node.get_low_split(y=split[1])
                current_node.high = current_node.get_high_split(y=split[1])
        elif current_node_low_needs_splitting:
            self.split(current_node.low)
        elif current_node_high_needs_splitting:
            self.split(current_node.high)

    def random_split(self):
        array = self.possible_splits.to_array()
        return array[random.randint(0, len(array))]

    def best_gini_split(self):
        max(self.possible_splits.to_array(), key=lambda split: split[2])

    def impurity_function(self):
        impurity = 0
        total_indices = len(self.row_indices)
        for indice_class_count in self.class_count.values():
            impurity += indice_class_count/total_indices * \
                (1 - indice_class_count/total_indices)
        return impurity

    def goodness_of_split_function(self, x=None, y=None):
        if y == None:
            x_low_split = self.get_low_split(x=x)
            x_high_split = self.get_high_split(x=x)
            return self.impurity - len(x_low_split.row_indices) / len(self.row_indices) * x_low_split.impurity - len(x_high_split.row_indices) / len(self.row_indices) * x_high_split.impurity
        if x == None:
            y_low_split = self.get_low_split(y=y)
            y_high_split = self.get_high_split(y=y)
            return self.impurity - len(y_low_split.row_indices) / len(self.row_indices) * y_low_split.impurity - len(y_high_split.row_indices) / len(self.row_indices) * y_high_split.impurity

    def get_high_split(self, x=None, y=None):
        if y == None and self.dataframe.select_rows_where(lambda row: row['x'] >= x) != None:
            return DecisionTreeNode(self.dataframe.select_rows_where(lambda row: row['x'] >= x), self.split_metric)
        if x == None and self.dataframe.select_rows_where(lambda row: row['y'] >= y) != None:
            return DecisionTreeNode(self.dataframe.select_rows_where(lambda row: row['y'] >= y), self.split_metric)

    def get_low_split(self, x=None, y=None):
        if y == None and self.dataframe.select_rows_where(lambda row: row['x'] < x) != None:
            return DecisionTreeNode(self.dataframe.select_rows_where(lambda row: row['x'] < x), self.split_metric)
        if x == None and self.dataframe.select_rows_where(lambda row: row['y'] < y) != None:
            return DecisionTreeNode(self.dataframe.select_rows_where(lambda row: row['y'] < y), self.split_metric)

    def possible_splits_function(self):
        if self.impurity != 0:
            unique_xs = []
            for x in self.dataframe.data_dict['x']:
                if x not in unique_xs:
                    unique_xs.append(x)
            unique_xs.sort()
            split_xs = [(unique_xs[i] + unique_xs
                         [i+1]) / 2 for i in range(0, len(unique_xs) - 1)]
            unique_ys = []
            for y in self.dataframe.data_dict['y']:
                if y not in unique_ys:
                    unique_ys.append(y)
            unique_ys.sort()
            split_ys = []
            for i in range(0, len(unique_ys) - 1):
                split_ys.append((unique_ys[i] + unique_ys
                                 [i+1]) / 2)
            possible_splits = []
            for x in split_xs:
                possible_splits.append(
                    ['x', x, self.goodness_of_split_function(x=x)])
            for y in split_ys:
                possible_splits.append(
                    ['y', y, self.goodness_of_split_function(y=y)])
            return DataFrame.from_array(possible_splits, ['feature', 'value', 'goodness of split'])
        else:
            return None
