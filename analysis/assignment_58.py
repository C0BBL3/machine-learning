#import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator
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

def percent_correct(k):
    correct_observations = 0
    for i in range(len(data_set)):
        observation = {
        'Cookie Type': data_set[i][0],
        'Portion Eggs': data_set[i][1],
        'Portion Butter': data_set[i][2],
        'Portion Sugar': data_set[i][3],
        'Portion Flour': data_set[i][4]
        }
        data_set_without_i = data_set[:i] + data_set[i+1:]
        df = DataFrame.from_array(data_set_without_i, 
        columns = ['Cookie Type', 'Portion Eggs', 'Portion Butter', 'Portion Sugar', 'Portion Flour']
        )
        knn = KNearestNeighborsClassifier(df, prediction_column = 'Cookie Type')
        #print('observation["Cookie Type"]', observation["Cookie Type"])
        print('knn.classify(observation, k=k)', knn.classify(observation, k=k))
        #print('knn.classify(observation, k=k) == data_set[k][0]', knn.classify(observation, k=k) == observation["Cookie Type"])
        if knn.classify(observation, k=k) == observation["Cookie Type"]:
            correct_observations += 1
    #print('correct_observations', correct_observations)
    #print('len(data_set)', len(data_set))
    return correct_observations/len(data_set)


y_values = []
for k in range(2, len(data_set)):
    print('k, data_set[k]', k, data_set[k])
    y_values.append(percent_correct(k))
    print('y_values', y_values)


#plt.plot([x for x in range(1, len(data_set)+1)],y_values)
#plt.savefig('plot.png')
#plt.show()