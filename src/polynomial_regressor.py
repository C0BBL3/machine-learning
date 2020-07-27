import random
#import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator
from matrix_class import Matrix


class PolynomialRegressor:
    def __init__(self, degree = 1):
        self.degree = degree
        self.default_guess = []
        self.coefficients = []
        self.data = []
        for _ in range(0, self.degree):
            self.default_guess.append(0)

    def ingest_data(self, data):
        self.data = data

    def solve_coefficients(self, sandwich_situation = False):
        X_data = []
        Y_data = []
        polynomial_function = []
        for arr in self.data:
            if sandwich_situation:
                X_data.append(arr[:-1])
                Y_data.append([arr[-1]])
            else:
                polynomial_function = []
                if self.degree > 0:
                    for k in range(0, self.degree + 1):
                        polynomial_function.append(arr[0] ** k)
                    X_data.append(polynomial_function)

                else:
                    X_data.append([arr[0]])
                Y_data.append([arr[1]])
        X_matrix = Matrix(elements=X_data)
        print('\nX_matrix.elements', X_matrix.elements, '\n')
        Y_matrix = Matrix(elements=Y_data)
        print('Y_matrix.elements', Y_matrix.elements, '\n')
        X_transpose = X_matrix.transpose()  # xT
        X_transpose_times_X = X_transpose @ X_matrix  # xT * x
        print('X_transpose_times_X.inverse()', X_transpose_times_X.inverse())
        result = X_transpose_times_X.inverse() @ X_transpose @ Y_matrix  # (xT * x)^-1 * xT * y
        for results in result.elements:
            if results != result.elements:
                self.coefficients.append(results[0])

        print('Coeffs', self.coefficients, '\n')
        
    def sum_squared_error(self):
        print('baka')
        return sum([(self.evaluate(x) - y)**2 for x, y in self.data])

    def evaluate(self, x):
        if self.coefficients == []:
            return sum([self.default_guess[i] * (x ** i) for i in range(0, self.degree)])
        else:
            return sum([self.coefficients[i] * (x ** i) for i in range(0, self.degree)])
'''
    def plot(self, padding=5, num_subintervals=50):
        title = 'y = {}x^2 + {}x + {}'.format(round(self.coefficients[0], 2), round(
            self.coefficients[1], 2), round(self.coefficients[2], 2))
        x_coords_data = [point[0] for point in self.data]
        y_coords_data = [point[1] for point in self.data]
        x_min_data, x_max_data = min(x_coords_data), max(x_coords_data)
        y_min_data, y_max_data = min(y_coords_data), max(y_coords_data)

        a, b = x_min_data-padding, x_max_data+padding
        approximation_x_coords = [
            a + (b-a)*(i/num_subintervals) for i in range(num_subintervals+1)]
        approximation_y_coords = [self.evaluate(
            x) for x in approximation_x_coords]

        plt.scatter(x_coords_data, y_coords_data, color='black')
        plt.plot(approximation_x_coords, approximation_y_coords, color='blue')
        plt.xlim(x_min_data-padding, x_max_data+padding)
        plt.ylim(y_min_data-padding, y_max_data+padding)
        plt.title(title)
        plt.show()
'''
