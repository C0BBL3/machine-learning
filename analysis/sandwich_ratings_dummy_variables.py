import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor

# [[0, 0, 0, 0],                  [[1]
#  [0, 0, 1, 0],                   [1]
#  [0, 0, 0, 1],                   [4]
#  [0, 0, 1, 1],     [[beta_1],    [0]
#  [5, 0, 0, 0],     [beta_2],     [4]
#  [5, 0, 1, 0],     [beta_3],     [8]
#  [5, 0, 0, 1],     [beta_4],     [1]
#  [5, 0, 1, 1],     [beta_5],     [0]
#  [0, 5, 0, 0],     [beta_6], =   [5]
#  [0, 5, 1, 0],     [beta_7],     [0]
#  [0, 5, 0, 1],     [beta_8],     [9]
#  [0, 5, 1, 1],     [beta_9],     [0]
#  [5, 5, 0, 0],     [beta_10]]    [0]
#  [5, 5, 1, 0],                   [0]
#  [5, 5, 0, 1],                   [0]
#  [5, 5, 1, 1]]                   [0]]

bad_sandwich_1 = [[1, 0, 0, 0, 0, 1],
                  [1, 0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 1, 4],
                  [1, 0, 0, 1, 1, 0],
                  [1, 5, 0, 0, 0, 4],
                  [1, 5, 0, 1, 0, 8],
                  [1, 5, 0, 0, 1, 1],
                  [1, 5, 0, 1, 1, 0],
                  [1, 0, 5, 0, 0, 5],
                  [1, 0, 5, 1, 0, 0],
                  [1, 0, 5, 0, 1, 9],
                  [1, 0, 5, 1, 1, 0],
                  [1, 5, 5, 0, 0, 0],
                  [1, 5, 5, 1, 0, 0],
                  [1, 5, 5, 0, 1, 0],
                  [1, 5, 5, 1, 1, 0]]

poly_regress_3 = PolynomialRegressor()
poly_regress_3.ingest_data(bad_sandwich_1)
poly_regress_3.solve_coefficients()
print('COEFFICIENTS')
print('    bias term:', poly_regress_3.coefficients[0])
print('    beef:', poly_regress_3.coefficients[1])
print('    peanut butter:', poly_regress_3.coefficients[2])
print('    mayo', poly_regress_3.coefficients[3])
print('    jelly:', poly_regress_3.coefficients[4])
print('    beef & peanut butter:', poly_regress_3.coefficients[1] * poly_regress_3.coefficients[2])
print('    beef & mayo:', poly_regress_3.coefficients[1] * poly_regress_3.coefficients[3])
print('    beef & jelly:', poly_regress_3.coefficients[1] * poly_regress_3.coefficients[4])
print('    peanut butter & mayo:', poly_regress_3.coefficients[2] * poly_regress_3.coefficients[3])
print('    peanut butter & jelly:', poly_regress_3.coefficients[2] * poly_regress_3.coefficients[4])
print('    mayo & jelly:', poly_regress_3.coefficients[3]*poly_regress_3.coefficients[4])

print('PREDICTED RATINGS')
print('    2 slices beef + mayo:', 2 * poly_regress_3.coefficients[1] + poly_regress_3.coefficients[3])
print('    2 slices beef + jelly:', 2 * poly_regress_3.coefficients[1] + poly_regress_3.coefficients[4])
print('    3 tbsp peanut butter + jelly:', 3 * poly_regress_3.coefficients[2] + poly_regress_3.coefficients[4])
print('    3 tbsp peanut butter + jelly + mayo:', 3 * poly_regress_3.coefficients[2] + poly_regress_3.coefficients[3] + poly_regress_3.coefficients[4])
print('    2 slices beef + 3 tbsp peanut butter + jelly + mayo:', 2 * poly_regress_3.coefficients[1] + 3 * poly_regress_3.coefficients[2] + poly_regress_3.coefficients[3] + poly_regress_3.coefficients[4])


def transform_matrix(array):
    for nested_arr in array:
        rating = nested_arr[-1]
        nested_arr.pop(0)
        nested_arr.pop(-1)
        combos = [nested_arr[0] * nested_arr[1], nested_arr[0] * nested_arr[2], nested_arr[0] * nested_arr[3], nested_arr[1] * nested_arr[2], nested_arr[1] * nested_arr[3], nested_arr[2] * nested_arr[3]]
        for combo in combos:
            
            nested_arr.append(combo)
        
        nested_arr.append(rating)

    return array

print('Transformed Matrix')
transformed_matrix = transform_matrix(bad_sandwich_1)
print(transformed_matrix)

summ = sum([sum(nested_arr) for nested_arr in transformed_matrix])
assert summ == 313, 'Transformed Matrix is wrong, the sum isnt 313 but was {}'.format(summ)
