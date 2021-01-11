import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from random_forest import RandomForest

path_to_datasets = 'C:/Users/colbi/VSCode/Computational Math/machine-learning/datasets/'
filename = 'freshman_lbs.csv' 
filepath = path_to_datasets + filename
df = DataFrame.from_csv(filepath, header=True)
df.filter_columns(['"Sex"', '"Weight (Sep)"', '"BMI (Sep)"'])
df.rename_columns(['"Sex"', 'x', 'y']) #x is weight, and y is bmi this is to allow the trees to work
df.apply('x', lambda x: float(x))
df.apply('y', lambda x: float(x))
df.data_dict['indices'] = list(range(0,len(df)))
df.columns.append('indices')

def classifications(decision_tree, dataframe):
    classifications = []
    for index in range(len(dataframe)):
        observation = {'x': dataframe.data_dict['x'][index], 'y': dataframe.data_dict['y'][index]}
        guess = decision_tree.classify(observation) 
        answer = dataframe.data_dict['"Sex"'][index]
        classifications.append(guess == answer)
    return classifications

def combine_lists(lists):
        final_list = []
        for arr in lists:
            final_list += arr
        return final_list

first_20_df = df.split_dataframe(5,0, location_of_splits = None)
last_80_df = df.split_dataframe(2,1, location_of_splits = [0.2])
second_20_df = df.split_dataframe(5,1, location_of_splits = None)
first_20_last_60_df = df.split_dataframe(3,(0,2), location_of_splits = [0.2,0.4])
third_20_df = df.split_dataframe(5,2, location_of_splits = None)
first_40_last_40_df = df.split_dataframe(3,(0,2), location_of_splits =[0.4,0.6])
fourth_20_df = df.split_dataframe(5,3, location_of_splits = None)
first_60_last_20_df = df.split_dataframe(3,(0,2), location_of_splits =[0.6,0.8])
fifth_20_df = df.split_dataframe(5,4, location_of_splits = None)
first_80_df = df.split_dataframe(2,0, location_of_splits =[0.8])

prlast_80_decision_tree = DecisionTree(dataframe = last_80_df, class_name = '"Sex"')
last_80_decision_tree.fit()
first_20_last_60_decision_tree = DecisionTree(dataframe = first_20_last_60_df, class_name = '"Sex"')
first_20_last_60_decision_tree.fit()
first_40_last_40_decision_tree = DecisionTree(dataframe = first_40_last_40_df, class_name = '"Sex"')
first_40_last_40_decision_tree.fit()
first_60_last_20_decision_tree = DecisionTree(dataframe = first_60_last_20_df, class_name = '"Sex"')
first_60_last_20_decision_tree.fit()
first_80_decision_tree = DecisionTree(dataframe = first_80_df, class_name = '"Sex"')
first_80_decision_tree.fit()
gini_first_20_classifications = classifications(last_80_decision_tree, first_20_df)
gini_second_20_classifications = classifications(first_20_last_60_decision_tree, second_20_df)
gini_third_20_classifications = classifications(first_40_last_40_decision_tree, third_20_df)
gini_fourth_20_classifications = classifications(first_60_last_20_decision_tree, fourth_20_df)
gini_fifth_20_classifications = classifications(first_80_decision_tree, fifth_20_df)

gini_classifications = combine_lists([gini_first_20_classifications, gini_second_20_classifications, gini_third_20_classifications, gini_fourth_20_classifications, gini_fifth_20_classifications])
print('gini accuracy', gini_classifications.count(True) / len(gini_classifications))

last_80_random_decision_tree = DecisionTree(last_80_df, split_metric = 'random', class_name = '"Sex"')
last_80_random_decision_tree.fit()
first_20_last_60_random_decision_tree = DecisionTree(dataframe = first_20_last_60_df, split_metric = 'random', class_name = '"Sex"')
first_20_last_60_random_decision_tree.fit()
first_40_last_40_random_decision_tree = DecisionTree(dataframe = first_40_last_40_df, split_metric = 'random', class_name = '"Sex"')
first_40_last_40_random_decision_tree.fit()
first_60_last_20_random_decision_tree = DecisionTree(dataframe = first_60_last_20_df, split_metric = 'random', class_name = '"Sex"')
first_60_last_20_random_decision_tree.fit()
first_80_random_decision_tree = DecisionTree(dataframe = first_80_df, split_metric = 'random', class_name = '"Sex"')
first_80_random_decision_tree.fit()

random_first_20_classifications = classifications(last_80_random_decision_tree, first_20_df)
random_second_20_classifications = classifications(first_20_last_60_random_decision_tree, second_20_df)
random_third_20_classifications = classifications(first_40_last_40_random_decision_tree, third_20_df)
random_fourth_20_classifications = classifications(first_60_last_20_random_decision_tree, fourth_20_df)
random_fifth_20_classifications = classifications(first_80_random_decision_tree, fifth_20_df)

random_classifications = combine_lists([random_first_20_classifications, random_second_20_classifications, random_third_20_classifications, random_fourth_20_classifications, random_fifth_20_classifications])
print('random accuracy', random_classifications.count(True) / len(random_classifications))

last_80_random_forest_10 = RandomForest(10, class_name = '"Sex"')
last_80_random_forest_10.fit(last_80_df)
first_20_last_60_random_forest_10 = RandomForest(10, class_name = '"Sex"')
first_20_last_60_random_forest_10.fit(first_20_last_60_df)
first_40_last_40_random_forest_10 = RandomForest(10, class_name = '"Sex"')
first_40_last_40_random_forest_10.fit(first_40_last_40_df)
first_60_last_20_random_forest_10 = RandomForest(10, class_name = '"Sex"')
first_60_last_20_random_forest_10.fit(first_60_last_20_df)
first_80_random_forest_10 = RandomForest(10, class_name = '"Sex"')
first_80_random_forest_10.fit(first_80_df)

forest_10_first_20_classifications = classifications(last_80_random_forest_10, first_20_df)
forest_10_second_20_classifications = classifications(first_20_last_60_random_forest_10, second_20_df)
forest_10_third_20_classifications = classifications(first_40_last_40_random_forest_10, third_20_df)
forest_10_fourth_20_classifications = classifications(first_60_last_20_random_forest_10, fourth_20_df)
forest_10_fifth_20_classifications = classifications(first_80_random_forest_10, fifth_20_df)

forest_10_classifications = combine_lists([forest_10_first_20_classifications, forest_10_second_20_classifications, forest_10_third_20_classifications, forest_10_fourth_20_classifications, forest_10_fifth_20_classifications])print('forest 10 accuracy', forest_10_classifications.count(True) / len(forest_10_classifications))

last_80_random_forest_100 = RandomForest(100, class_name = '"Sex"')
last_80_random_forest_100.fit(last_80_df)
first_20_last_60_random_forest_100 = RandomForest(100, class_name = '"Sex"')
first_20_last_60_random_forest_100.fit(first_20_last_60_df)
first_40_last_40_random_forest_100 = RandomForest(100, class_name = '"Sex"')
first_40_last_40_random_forest_100.fit(first_40_last_40_df)
first_60_last_20_random_forest_100 = RandomForest(100, class_name = '"Sex"')
first_60_last_20_random_forest_100.fit(first_60_last_20_df)
first_80_random_forest_100 = RandomForest(100, class_name = '"Sex"')
first_80_random_forest_100.fit(first_80_df)

forest_100_first_20_classifications = classifications(last_80_random_forest_100, first_20_df)
forest_100_second_20_classifications = classifications(first_20_last_60_random_forest_100, second_20_df)
forest_100_third_20_classifications = classifications(first_40_last_40_random_forest_100, third_20_df)
forest_100_fourth_20_classifications = classifications(first_60_last_20_random_forest_100, fourth_20_df)
forest_100_fifth_20_classifications = classifications(first_80_random_forest_100, fifth_20_df)

forest_100_classifications = combine_lists([forest_100_first_20_classifications, forest_100_second_20_classifications, forest_100_third_20_classifications, forest_100_fourth_20_classifications, forest_100_fifth_20_classifications])
print('forest 100 accuracy', forest_100_classifications.count(True) / len(forest_100_classifications))

last_80_random_forest_1000 = RandomForest(1000, class_name = '"Sex"')
last_80_random_forest_1000.fit(last_80_df)
first_20_last_60_random_forest_1000 = RandomForest(1000, class_name = '"Sex"')
first_20_last_60_random_forest_1000.fit(first_20_last_60_df)
first_40_last_40_random_forest_1000 = RandomForest(1000, class_name = '"Sex"')
first_40_last_40_random_forest_1000.fit(first_40_last_40_df)
first_60_last_20_random_forest_1000 = RandomForest(1000, class_name = '"Sex"')
first_60_last_20_random_forest_1000.fit(first_60_last_20_df)
first_80_random_forest_1000 = RandomForest(1000, class_name = '"Sex"')
first_80_random_forest_1000.fit(first_80_df)

forest_1000_first_20_classifications = classifications(last_80_random_forest_1000, first_20_df)
forest_1000_second_20_classifications = classifications(first_20_last_60_random_forest_1000, second_20_df)
forest_1000_third_20_classifications = classifications(first_40_last_40_random_forest_1000, third_20_df)
forest_1000_fourth_20_classifications = classifications(first_60_last_20_random_forest_1000, fourth_20_df)
forest_1000_fifth_20_classifications = classifications(first_80_random_forest_1000, fifth_20_df)

forest_1000_classifications = combine_lists([forest_1000_first_20_classifications, forest_1000_second_20_classifications, forest_1000_third_20_classifications, forest_1000_fourth_20_classifications, forest_1000_fifth_20_classifications])
print('forest 1000 accuracy', forest_1000_classifications.count(True) / len(forest_1000_classifications))


