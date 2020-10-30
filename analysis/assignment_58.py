import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier
from dataframe import DataFrame

data_set = [['Shortbread', 0.14, 0.14, 0.28, 0.44],
            ['Shortbread', 0.10, 0.18, 0.28, 0.44],
            ['Shortbread', 0.12, 0.10, 0.33, 0.45],
            ['Shortbread', 0.10, 0.25, 0.25, 0.40],
            ['Sugar', 0.00, 0.10, 0.40, 0.50],
            ['Sugar', 0.00, 0.20, 0.40, 0.40],
            ['Sugar', 0.02, 0.08, 0.45, 0.45],
            ['Sugar', 0.10, 0.15, 0.35, 0.40],
            ['Sugar', 0.10, 0.08, 0.35, 0.47],
            ['Sugar', 0.00, 0.05, 0.30, 0.65],
            ['Fortune', 0.20, 0.00, 0.40, 0.40],
            ['Fortune', 0.25, 0.10, 0.30, 0.35],
            ['Fortune', 0.22, 0.15, 0.50, 0.13],
            ['Fortune', 0.15, 0.20, 0.35, 0.30],
            ['Fortune', 0.22, 0.00, 0.40, 0.38],
            ['Shortbread', 0.05, 0.12, 0.28, 0.55],
            ['Shortbread', 0.14, 0.27, 0.31, 0.28],
            ['Shortbread', 0.15, 0.23, 0.30, 0.32],
            ['Shortbread', 0.20, 0.10, 0.30, 0.40]]

y_values = []
for k in range(0, len(data_set)):
    df = DataFrame.from_array(data_set[:k] + data_set[k+1:], 
    columns = ['Cookie Type', 
    'Portion Eggs', 
    'Portion Butter', 
    'Portion Sugar', 
    'Portion Flour']
    )
    knn = KNearestNeighborsClassifier(df, prediction_column = 'Cookie Type')
    y_values.append(percent_correct(k, knn, df))

def percent_correct(k, knn, df):
    data_set_without_k = data_set[:k] + data_set[k+1:]
    observation = {
    'Portion Eggs': data_set[k][0],
    'Portion Butter': data_set[k][1],
    'Portion Sugar': data_set[k][2],
    'Portion Flour': data_set[k][3]
    }
    for i in range(0, len(data_set) - 1):
        correct_observations = 0
        if knn.classify(observation, k=k) == data_set_without_k[i][0]:
            correct_observations += 1
    return correct_observations/(len(data_set)-1)

plt.plot([x for x in range(1, len(data_set))],y_values,)
plt.savefig('plot.png')