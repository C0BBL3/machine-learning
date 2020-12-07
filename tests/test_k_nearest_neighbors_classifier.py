import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier
from dataframe import DataFrame

print('\nTesting...\n')

df = DataFrame.from_array(
    [['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
    ['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
    ['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
    ['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
    ['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
    ['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
    ['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
    ['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
    ['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
    ['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
    ['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
    ['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
    ['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ]],
    columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )
knn = KNearestNeighborsClassifier(k=5)
knn.fit(df, 'Cookie Type')
observation = {
    'Portion Eggs': 0.10,
    'Portion Butter': 0.15,
    'Portion Sugar': 0.30,
    'Portion Flour': 0.45
}
print("    Testing KNearestNeighborsClassifier's compute_distances()")
assert knn.compute_distances(observation) == [[0.04690415759823429, 'Shortbread'], [0.037416573867739396, 'Shortbread'], [0.061644140029689765, 'Shortbread'], [0.1224744871391589, 'Shortbread'], [0.15811388300841897, 'Sugar'], [0.158113883008419, 'Sugar'], [0.08831760866327845, 'Sugar'], [0.24494897427831783, 'Sugar'], [0.21213203435596428, 'Fortune'], [0.18708286933869708, 'Fortune'], [0.3959797974644666, 'Fortune'], [0.17320508075688776, 'Fortune'], [0.22759613353482086, 'Fortune']], "KNearestNeighborsClassifier's compute_distances() was not right, it should be [[0.04690415759823429, 'Shortbread'], [0.037416573867739396, 'Shortbread'], [0.061644140029689765, 'Shortbread'], [0.1224744871391589, 'Shortbread'], [0.15811388300841897, 'Sugar'], [0.158113883008419, 'Sugar'], [0.08831760866327845, 'Sugar'], [0.24494897427831783, 'Sugar'], [0.21213203435596428, 'Fortune'], [0.18708286933869708, 'Fortune'], [0.3959797974644666, 'Fortune'], [0.17320508075688776, 'Fortune'], [0.22759613353482086, 'Fortune']], but was {}".format(knn.compute_distances(observation))
print("    KNearestNeighborsClassifier's compute_distances() Passed!!!\n")

print("    Testing KNearestNeighborsClassifier's nearest_neighbors()")
assert knn.nearest_neighbors(observation) == [[0.037416573867739396, 'Shortbread'], [0.04690415759823429, 'Shortbread'], [0.061644140029689765, 'Shortbread'], [0.08831760866327845, 'Sugar'], [0.1224744871391589, 'Shortbread'], [0.15811388300841897, 'Sugar'], [0.158113883008419, 'Sugar'], [0.17320508075688776, 'Fortune'], [0.18708286933869708, 'Fortune'], [0.21213203435596428, 'Fortune'], [0.22759613353482086, 'Fortune'], [0.24494897427831783, 'Sugar'], [0.3959797974644666, 'Fortune']], "KNearestNeighborsClassifier's nearest_neighbors() was not right, it should be [[0.037416573867739396, 'Shortbread'], [0.04690415759823429, 'Shortbread'], [0.061644140029689765, 'Shortbread'], [0.08831760866327845, 'Sugar'], [0.1224744871391589, 'Shortbread'], [0.15811388300841897, 'Sugar'], [0.158113883008419, 'Sugar'], [0.17320508075688776, 'Fortune'], [0.18708286933869708, 'Fortune'], [0.21213203435596428, 'Fortune'], [0.22759613353482086, 'Fortune'], [0.24494897427831783, 'Sugar'], [0.3959797974644666, 'Fortune']], but was {}".format(knn.nearest_neighbors(observation))
print("    KNearestNeighborsClassifier's nearest_neighbors() Passed!!!\n")

print("    Testing KNearestNeighborsClassifier's compute_average_distances()")
assert knn.compute_average_distances(observation) == {'Shortbread': 0.0671098396587056, 'Sugar': 0.16237358723960857, 'Fortune': 0.23919918309016733}, "KNearestNeighborsClassifier's compute_average_distances() was not right, it should be {'Shortbread': 0.0671098396587056, 'Sugar': 0.16237358723960857, 'Fortune': 0.23919918309016733}, but was {}".format(knn.compute_average_distances(observation))
print("    KNearestNeighborsClassifier's compute_average_distances() Passed!!!\n")

print("    Testing KNearestNeighborsClassifier's classify()")
assert knn.classify(observation) == 'Shortbread', "KNearestNeighborsClassifier's classify() was not right, it should be Shortbread, but was {}".format(knn.classify(observation))
print("    KNearestNeighborsClassifier's classify() Passed!!!\n")