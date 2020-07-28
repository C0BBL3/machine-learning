import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor

sandwiches_1 = [[1, 0, 0, 1], [1, 1, 0, 2], [1, 2, 0, 4], [1, 4, 0, 8], [1, 6, 0, 9], [
    1, 0, 2, 2], [1, 0, 4, 5], [1, 0, 6, 7], [1, 0, 8, 6],  [1, 2, 2, 0], [1, 3, 4, 0]]

poly_regress_1 = PolynomialRegressor()
poly_regress_1.ingest_data(sandwiches_1)
poly_regress_1.solve_coefficients()

rating = poly_regress_1.coefficients[1] + \
    poly_regress_1.coefficients[2] * 5 + poly_regress_1.coefficients[2] * 5
print('5 roast beef + 5 tbsp of peanut butter = {}'.format(rating))

# rating = 1.1493506493506493 + 1.4220779220779225 * (slices of beef) + 0.7584415584415587 * (tbsp peanut butter)

# Yes, you should belive that 5 roast beef + 5 tbsp of peanut butter has a high rating because computers don't lie and the conputer said it had a high rating

# QUESTION 1
# What is the model?

#    rating = 1.5873900293255128 + 0.8671554252199409 * (slices beef) + 0.42038123167155433 * (tbsp peanut butter)

# QUESTION 2
# What is the predicted rating of a sandwich with 5 slices of roast beef AND
# 5 tablespoons of peanut butter (on the same sandwich)?

#    rating = 5.070967741935485

# QUESTION 3
# How does this prediction compare to that from the previous assignment? Did
# including the additional data make the prediction trustworthy? Why or why not?

#    First assignment = 12.05194  | both rounded to
#    Current Assignment = 5.07097 | 5 decimal places

#    For the Current Assignment the code gave us a lower value, seeing that when peanut butter and roast beef are mixed, it'll be pretty bad, which makes the data more trustworthy

# QUESTION 4
# Fill out the table with the additional interaction term:

# (slices beef) | (tbsp peanut butter) | (slices beef)(tbsp peanut butter) | Rating |
# -----------------------------------------------------------------------------------
#       0       |           0          |                 0                 |    1   |
#       1       |           0          |                 0                 |    2   |
#       2       |           0          |                 0                 |    4   |
#       4       |           0          |                 0                 |    8   |
#       6       |           0          |                 0                 |    9   |
#       0       |           2          |                 0                 |    2   |
#       0       |           4          |                 0                 |    5   |
#       0       |           6          |                 0                 |    7   |
#       0       |           8          |                 0                 |    6   |
#       2       |           2          |                 2                 |    0   | (new data)
#       3       |           4          |                 12                 |    0   | (new data)

# QUESTION 5
# What is the system of equations?

#   1 * beta_0 + 0 * beta_1 + 0 * beta_2 = 1
#   1 * beta_0 + 1 * beta_1 + 0 * beta_2 = 2
#   1 * beta_0 + 2 * beta_1 + 0 * beta_2 = 4
#   1 * beta_0 + 4 * beta_1 + 0 * beta_2 = 8
#   1 * beta_0 + 6 * beta_1 + 0 * beta_2 = 9
#   1 * beta_0 + 0 * beta_1 + 2 * beta_2 = 2
#   1 * beta_0 + 0 * beta_1 + 4 * beta_2 = 5
#   1 * beta_0 + 0 * beta_1 + 6 * beta_2 = 7
#   1 * beta_0 + 0 * beta_1 + 8 * beta_2 = 6
#   1 * beta_0 + 2 * beta_1 + 2 * beta_2 = 0
#   1 * beta_0 + 3 * beta_1 + 4 * beta_2 = 0

# QUESTION 6
# What is the matrix equation?

#   [[1, 0, 0, 0],                   [[1],
#    [1, 1, 0, 0],                    [2],
#    [1, 2, 0, 0],                    [4],
#    [1, 4, 0, 0],    [[beta_0],      [8],
#    [1, 6, 0, 0],     [beta_1],  =   [9],
#    [1, 0, 2, 0],     [beta_2]]      [2],
#    [1, 0, 4, 0],                    [5],
#    [1, 0, 6, 0],                    [7],
#    [1, 0, 8, 0]]                    [6]]
#    [1, 2, 2, 4],                    [0],
#    [1, 3, 4, 12]]                    [0]]

sandwiches_2 = [[1, 0, 0, 0, 1], [1, 1, 0, 0, 2], [1, 2, 0, 0, 4], [1, 4, 0, 0, 8], [1, 6, 0, 0, 9], [
    1, 0, 2, 0, 2], [1, 0, 4, 0, 5], [1, 0, 6, 0, 7], [1, 0, 8, 0, 6],  [1, 2, 2, 4, 0], [1, 3, 4, 12, 0]]

poly_regress_2 = PolynomialRegressor()
poly_regress_2.ingest_data(sandwiches_2)
poly_regress_2.solve_coefficients()

rating = poly_regress_2.coefficients[1] + poly_regress_2.coefficients[2] * 5 + poly_regress_2.coefficients[2] * 5 + poly_regress_2.coefficients[3]
print('5 roast beef + 5 tbsp of peanut butter + roast beef * peanut butter = {}'.format(rating))

# QUESTION 7
# What is the model?

#    rating = 0.8707473221980557 + 1.4452948660073053 * (slices beef) + 0.792106127139164 * (tbsp peanut butter) + -0.7617679648705216 * (slices beef)(tbsp peanut butter)

# QUESTION 8
# What is the predicted rating of a sandwich with 5 slices of roast beef AND
# 5 tablespoons of peanut butter (on the same sandwich)?

#    rating = 9.366356137398945

# QUESTION 9
# How does this prediction compare to that from the previous assignment? Did
# including interaction term make the prediction trustworthy? Why or why not?

#    First Assignment = 12.05194     | all 3 predictions
#    Current Assignment #1 = 5.07097 | rounded to 5
#    Current Assignment #2 = 8.60458 | decimal places

#    For Current Assignment #1 the code gave us a lower value, seeing that when peanut butter and roast beef are mixed, it'll be pretty bad, which makes the data more trustworthy
#    Later for Current Assignment #2 the code gave us a little higher value because when their together there is another value (slices beef) * (tbsp peanut butter) which inflates the value a little
