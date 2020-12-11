import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree

print('\nTesting...\n')

array = [[1, 11, 'A'], [1, 12, 'A'], [2, 11, 'A'], [1, 13, 'B'], [2, 13, 'B'], [3, 13, 'B'], [3, 11, 'B']]
df = DataFrame.from_array(
    array,
    columns = ['x', 'y', 'class']
)
df.append_columns({'indices': [i for i in range(0, len(array))]})
dt = DecisionTree(df)

print("    Testing Decision Tree's row_indices")
assert dt.root.row_indices == [0, 1, 2, 3, 4, 5, 6], "Decision Tree's row_indices was not right, it should be [0, 1, 2, 3, 4, 5, 6], but was {}".format(dt.root.row_indices)
print("    Decision Tree's row_indices  Passed!!!\n")

print("    Testing Decision Tree's  class_count")
assert dt.root.class_count == {'A': 3,'B': 4}, "Decision Tree's class_count was not right, it should be {'A': 3,'B': 4}, but was {}".format(dt.root.class_count)
print("    Decision Tree's class_count Passed!!!\n")

print("    Testing Decision Tree's impurity")
assert dt.root.impurity == 0.4897959183673469, "Decision Tree's impurity was not right, it should be 0.4897959183673469, but was {}".format(dt.root.impurity)
print("    Decision Tree's  Passed!!!\n")

print("    Testing Decision Tree's possible_splits")
assert dt.root.possible_splits.to_array() == [['x', 1.5, 0.08503401360544219], ['x', 2.5, 0.14693877551020407], ['y', 11.5, 0.08503401360544219], ['y', 12.5, 0.2755102040816326]], "Decision Tree's possible_splits was not right, it should be [['x', 1.5, 0.08503401360544219], ['x', 2.5, 0.14693877551020407], ['y', 11.5, 0.08503401360544219], ['y', 12.5, 0.2755102040816326]], but was {}".format(dt.root.possible_splits.to_array())
print("    Decision Tree's possible_splits Passed!!!\n")

print("    Testing Decision Tree's best_split")
assert dt.root.best_split() == ['y', 12.5, 0.2755102040816326], "Decision Tree's best_split was not right, it should be ['y', 12.5, 0.2755102040816326], but was {}".format(dt.root)
print("    Decision Tree's best_split Passed!!!\n")

dt.split()

print("    Testing Decision Tree's low.row_indices")
assert dt.root.low.row_indices == [0, 1, 2, 6], "Decision Tree's low.row_indices was not right, it should be [0, 1, 2, 6], but was {}".format(dt.root.low.row_indices)
print("    Decision Tree's low.row_indices Passed!!!\n")

print("    Testing Decision Tree's high.row_indices")
assert dt.root.high.row_indices == [3, 4, 5], "Decision Tree's high.row_indices was not right, it should be [3, 4, 5], but was {}".format(dt.root.high.row_indices)
print("    Decision Tree's high.row_indices Passed!!!\n")

print("    Testing Decision Tree's low.impurity")
assert dt.root.low.impurity == 0.375, "Decision Tree's low.impurity was not right, it should be , but was {}".format(dt.root)
print("    Decision Tree's low.impurity Passed!!!\n")

print("    Testing Decision Tree's high.impurity")
assert dt.root.high.impurity == 0.0, "Decision Tree's high.impurity was not right, it should be 0.0, but was {}".format(dt.root.high.impurity)
print("    Decision Tree's high.impurity Passed!!!\n")

print("    Testing Decision Tree's low.possible_splits.to_array()")
assert dt.root.low.possible_splits.to_array() == [['x', 1.5,  0.125], ['x', 2.5,  0.375], ['y', 11.5, 0.04166666666666663]], "Decision Tree's low.possible_splits.to_array() was not right, it should be [['x', 1.5,  0.125], ['x', 2.5,  0.375], ['y', 11.5, 0.042]], but was {}".format(dt.root.low.possible_splits.to_array())
print("    Decision Tree's low.possible_splits.to_array() Passed!!!\n")

print("    Testing Decision Tree's low.best_split")
assert dt.root.low.best_split() == ['x', 2.5,  0.375], "Decision Tree's low.best_split was not right, it should be ['x', 2.5,  0.375], but was {}".format(dt.root)
print("    Decision Tree's low.best_split Passed!!!\n")

dt.split()

print("    Testing Decision Tree's low.low.row_indices")
assert dt.root.low.low.row_indices == [0, 1, 2], "Decision Tree's low.low.row_indices was not right, it should be [0, 1, 2], but was {}".format(dt.root)
print("    Decision Tree's low.low.row_indices Passed!!!\n")

print("    Testing Decision Tree's low.high.row_indices")
assert dt.root.low.high.row_indices == [6], "Decision Tree's low.high.row_indices was not right, it should be [6], but was {}".format(dt.root)
print("    Decision Tree's low.high.row_indices Passed!!!\n")

print("    Testing Decision Tree's low.low.impurity")
assert dt.root.low.low.impurity == 0, "Decision Tree's low.low.impurity was not right, it should be 0, but was {}".format(dt.root)
print("    Decision Tree's low.low.impurity Passed!!!\n")

print("    Testing Decision Tree's low.high.impurity")
assert dt.root.low.high.impurity == 0, "Decision Tree's low.high.impurity was not right, it should be 0, but was {}".format(dt.root)
print("    Decision Tree's low.high.impurity Passed!!!\n")

print('\n--------------------------------\n')

array = [[1, 11, 'A'], [1, 12, 'A'], [2, 11, 'A'], [1, 13, 'B'], [2, 13, 'B'], [3, 13, 'B'], [3, 11, 'B']]
df = DataFrame.from_array(
    array,
    columns = ['x', 'y', 'class']
)
df.append_columns({'indices': [i for i in range(0, len(array))]})
dt = DecisionTree(df)

print("    Testing Decision Tree's row_indices")
assert dt.root.row_indices == [0, 1, 2, 3, 4, 5, 6], "Decision Tree's row_indices was not right, it should be [0, 1, 2, 3, 4, 5, 6], but was {}".format(dt.root.row_indices)
print("    Decision Tree's row_indices  Passed!!!\n")

print("    Testing Decision Tree's  class_count")
assert dt.root.class_count == {'A': 3,'B': 4}, "Decision Tree's class_count was not right, it should be {'A': 3,'B': 4}, but was {}".format(dt.root.class_count)
print("    Decision Tree's class_count Passed!!!\n")

print("    Testing Decision Tree's impurity")
assert dt.root.impurity == 0.4897959183673469, "Decision Tree's impurity was not right, it should be 0.4897959183673469, but was {}".format(dt.root.impurity)
print("    Decision Tree's  Passed!!!\n")

print("    Testing Decision Tree's possible_splits")
assert dt.root.possible_splits.to_array() == [['x', 1.5, 0.08503401360544219], ['x', 2.5, 0.14693877551020407], ['y', 11.5, 0.08503401360544219], ['y', 12.5, 0.2755102040816326]], "Decision Tree's possible_splits was not right, it should be [['x', 1.5, 0.08503401360544219], ['x', 2.5, 0.14693877551020407], ['y', 11.5, 0.08503401360544219], ['y', 12.5, 0.2755102040816326]], but was {}".format(dt.root.possible_splits.to_array())
print("    Decision Tree's possible_splits Passed!!!\n")

print("    Testing Decision Tree's best_split")
assert dt.root.best_split() == ['y', 12.5, 0.2755102040816326], "Decision Tree's best_split was not right, it should be ['y', 12.5, 0.2755102040816326], but was {}".format(dt.root)
print("    Decision Tree's best_split Passed!!!\n")

dt.fit()

print("    Testing Decision Tree's low.row_indices")
assert dt.root.low.row_indices == [0, 1, 2, 6], "Decision Tree's low.row_indices was not right, it should be [0, 1, 2, 6], but was {}".format(dt.root.low.row_indices)
print("    Decision Tree's low.row_indices Passed!!!\n")

print("    Testing Decision Tree's high.row_indices")
assert dt.root.high.row_indices == [3, 4, 5], "Decision Tree's high.row_indices was not right, it should be [3, 4, 5], but was {}".format(dt.root.high.row_indices)
print("    Decision Tree's high.row_indices Passed!!!\n")

print("    Testing Decision Tree's low.impurity")
assert dt.root.low.impurity == 0.375, "Decision Tree's low.impurity was not right, it should be , but was {}".format(dt.root)
print("    Decision Tree's low.impurity Passed!!!\n")

print("    Testing Decision Tree's high.impurity")
assert dt.root.high.impurity == 0.0, "Decision Tree's high.impurity was not right, it should be 0.0, but was {}".format(dt.root.high.impurity)
print("    Decision Tree's high.impurity Passed!!!\n")

print("    Testing Decision Tree's low.possible_splits.to_array()")
assert dt.root.low.possible_splits.to_array() == [['x', 1.5,  0.125], ['x', 2.5,  0.375], ['y', 11.5, 0.04166666666666663]], "Decision Tree's low.possible_splits.to_array() was not right, it should be [['x', 1.5,  0.125], ['x', 2.5,  0.375], ['y', 11.5, 0.042]], but was {}".format(dt.root.low.possible_splits.to_array())
print("    Decision Tree's low.possible_splits.to_array() Passed!!!\n")

print("    Testing Decision Tree's low.best_split")
assert dt.root.low.best_split() == ['x', 2.5,  0.375], "Decision Tree's low.best_split was not right, it should be ['x', 2.5,  0.375], but was {}".format(dt.root)
print("    Decision Tree's low.best_split Passed!!!\n")

print("    Testing Decision Tree's low.low.row_indices")
assert dt.root.low.low.row_indices == [0, 1, 2], "Decision Tree's low.low.row_indices was not right, it should be [0, 1, 2], but was {}".format(dt.root)
print("    Decision Tree's low.low.row_indices Passed!!!\n")

print("    Testing Decision Tree's low.high.row_indices")
assert dt.root.low.high.row_indices == [6], "Decision Tree's low.high.row_indices was not right, it should be [6], but was {}".format(dt.root)
print("    Decision Tree's low.high.row_indices Passed!!!\n")

print("    Testing Decision Tree's low.low.impurity")
assert dt.root.low.low.impurity == 0, "Decision Tree's low.low.impurity was not right, it should be 0, but was {}".format(dt.root)
print("    Decision Tree's low.low.impurity Passed!!!\n")

print("    Testing Decision Tree's low.high.impurity")
assert dt.root.low.high.impurity == 0, "Decision Tree's low.high.impurity was not right, it should be 0, but was {}".format(dt.root)
print("    Decision Tree's low.high.impurity Passed!!!\n")

print('\n--------------------------------\n')

array = [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
    [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
    [2,12,'B'],[2,12,'B'],
    [3,12,'A'],[3,12,'A'],
    [3,11,'A'],[3,11,'A'],
    [3,11.5,'A'],[3,11.5,'A'],
    [4,11,'A'],[4,11,'A'],
    [4,11.5,'A'],[4,11.5,'A'],
    [2,10.5,'A'],[2,10.5,'A'],
    [3,10.5,'B'],
    [4,10.5,'A']]
df = DataFrame.from_array(
    array,
    columns = ['x', 'y', 'class']
)
df.append_columns({'indices': [i for i in range(0, len(array))]})
dt = DecisionTree(df)

dt.fit()

print("    Testing Decision Tree's best_split")
assert dt.root.best_split()[0:2] == ['y', 12.5], "Decision Tree's best_split was not right, it should be ['y', 12.5], but was {}".format(dt.root.best_split()[0:2])
print("    Decision Tree's best_split Passed!!!\n")

print("    Testing Decision Tree's best_split")
assert dt.root.low.best_split()[0:2] == ['x', 2.5], "Decision Tree's best_split was not right, it should be ['x', 2.5], but was {}".format(dt.root.low.best_split()[0:2])
print("    Decision Tree's best_split Passed!!!\n")

print("    Testing Decision Tree's best_split")
assert dt.root.low.low.best_split()[0:2] == ['y', 11.25], "Decision Tree's best_split was not right, it should be ['y', 11.25], but was {}".format(dt.root.low.low.best_split()[0:2])
print("    Decision Tree's best_split Passed!!!\n")

print("    Testing Decision Tree's best_split")
assert dt.root.low.high.best_split()[0:2] == ['y', 10.75], "Decision Tree's best_split was not right, it should be ['y', 11], but was {}".format(dt.root.low.high.best_split()[0:2])
print("    Decision Tree's best_split Passed!!!\n")

print("    Testing Decision Tree's best_split")
assert dt.root.low.high.low.best_split()[0:2] == ['x', 3.5], "Decision Tree's best_split was not right, it should be ['x', 3.5], but was {}".format(dt.root.low.high.low.best_split()[0:2])
print("    Decision Tree's best_split Passed!!!\n")

print("    Testing Decision Tree's classify")
assert dt.classify({'x': 2, 'y': 11.5}) == 'B', "Decision Tree's classify was not right, it should be B, but was {}".format(dt.classify({'x': 2, 'y': 11.5}))
print("    Decision Tree's classify Passed!!!\n")

print("    Testing Decision Tree's classify")
assert dt.classify({'x': 2.5, 'y': 13}) == 'B', "Decision Tree's classify was not right, it should be B, but was {}".format(dt.classify({'x': 2.5, 'y': 13}))
print("    Decision Tree's classify Passed!!!\n")

print("    Testing Decision Tree's classify")
assert dt.classify({'x': 4, 'y': 12}) == 'A', "Decision Tree's classify was not right, it should be A, but was {}".format(dt.classify({'x': 4, 'y': 12}))
print("    Decision Tree's classify Passed!!!\n")

print("    Testing Decision Tree's classify")
assert dt.classify({'x': 3.25, 'y': 10.5}) == 'B', "Decision Tree's classify was not right, it should be B, but was {}".format(dt.classify({'x': 3.25, 'y': 10.5}))
print("    Decision Tree's classify Passed!!!\n")

print("    Testing Decision Tree's classify")
assert dt.classify({'x': 3.75, 'y': 10.5}) == 'A', "Decision Tree's classify was not right, it should be A, but was {}".format(dt.classify({'x': 3.75, 'y': 10.5}))
print("    Decision Tree's classify Passed!!!\n")

print('\nAll Tests Passed\n')