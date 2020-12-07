import sys
sys.path.append('src')
from dataframe import DataFrame
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier
from leave_one_out_cross_validator import LeaveOneOutCrossValidator


df = DataFrame.from_array(
    [['Shortbread',     0.14,       0.14,      0.28,     0.44],
     ['Shortbread',     0.10,       0.18,      0.28,     0.44],
        ['Shortbread',     0.12,       0.10,      0.33,     0.45],
        ['Shortbread',     0.10,       0.25,      0.25,     0.40],
        ['Sugar',     0.00,       0.10,      0.40,     0.50],
        ['Sugar',     0.00,       0.20,      0.40,     0.40],
        ['Sugar',     0.02,       0.08,      0.45,     0.45],
        ['Sugar',     0.10,       0.15,      0.35,     0.40],
        ['Sugar',     0.10,       0.08,      0.35,     0.47],
        ['Sugar',     0.00,       0.05,      0.30,     0.65],
        ['Fortune',     0.20,       0.00,      0.40,     0.40],
        ['Fortune',     0.25,       0.10,      0.30,     0.35],
        ['Fortune',     0.22,       0.15,      0.50,     0.13],
        ['Fortune',     0.15,       0.20,      0.35,     0.30],
        ['Fortune',     0.22,       0.00,      0.40,     0.38],
        ['Shortbread',     0.05,       0.12,      0.28,     0.55],
        ['Shortbread',     0.14,       0.27,      0.31,     0.28],
        ['Shortbread',     0.15,       0.23,      0.30,     0.32],
        ['Shortbread',     0.20,       0.10,      0.30,     0.40]],
    ['Cookie Type', 'Portion Eggs', 'Portion Butter',
        'Portion Sugar', 'Portion Flour']
)
knn = KNearestNeighborsClassifier(k=5)

cross_validator_1 = LeaveOneOutCrossValidator(knn, df, prediction_column='Cookie Type')

print('\nTesting...\n')

print("    Testing Leave One Out Cross Validator's accuracy()")
assert cross_validator_1.accuracy()==0.7894736842105263, "Leave One Out Cross Validator's accuracy() was not right, it should be 0.6842105263157895, but was {}".format(cross_validator_1.accuracy())
print("    Leave One Out Cross Validator's accuracy() Passed!!!\n")

accuracies = []
for k in range(1,  len(df.to_array())-1):
    knn = KNearestNeighborsClassifier(k)
    cross_validator_2 = LeaveOneOutCrossValidator(knn, df, prediction_column='Cookie Type')
    accuracies.append(cross_validator_2.accuracy())

print("    Testing Leave One Out Cross Validator's accuracies")
assert accuracies==[0.5789473684210527, 0.7368421052631579, 0.5789473684210527, 0.6842105263157895, 0.7894736842105263, 0.7368421052631579, 0.5789473684210527, 0.6842105263157895, 0.631578947368421, 0.5263157894736842, 0.42105263157894735, 0.42105263157894735, 0.3684210526315789, 0.3157894736842105, 0.3684210526315789, 0.3157894736842105, 0.42105263157894735], "Leave One Out Cross Validator's accuracies was not right, it should be [0.5789473684210527, 0.7368421052631579, 0.5789473684210527, 0.6842105263157895, 0.7894736842105263, 0.7368421052631579, 0.5789473684210527, 0.6842105263157895, 0.631578947368421, 0.5263157894736842, 0.42105263157894735, 0.42105263157894735, 0.3684210526315789, 0.3157894736842105, 0.3684210526315789, 0.3157894736842105, 0.42105263157894735], but was {}".format(accuracies)
print("    Leave One Out Cross Validator's accuracies Passed!!!\n")

print('All Tests Passed!!!')

