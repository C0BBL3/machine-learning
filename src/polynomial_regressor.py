import random
#import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator
from matrix_class import Matrix


class PolynomialRegressor:
    def __init__(self, degree):
        self.degree = degree
        self.default_guess = []
        self.coefficients = []
        self.data = []
        for _ in range(0, self.degree):
            self.default_guess.append(0)

    def ingest_data(self, data):
        self.data = data

    def solve_coefficients(self):
        X_data = []
        y_data = []
        polynomial_function = []  # error stems
        for i, j in self.data:  # from here
            polynomial_function = []
            for k in range(0, self.degree + 1):  # for the
                polynomial_function.append(i ** k)  # PolynomialRegressor tests
            X_data.append(polynomial_function)
            y_data.append([j])
        X_matrix = Matrix(elements=X_data)
        print('X_matrix.elements', X_matrix.elements)
        Y_matrix = Matrix(elements=y_data)
        print('Y_matrix.elements', Y_matrix.elements)
        X_transpose = X_matrix.transpose()  # xT
        X_transpose_times_X = X_transpose @ X_matrix  # xT * x
        result = X_transpose_times_X.inverse() @ X_transpose @ Y_matrix
        print(result.elements)
        for i in range(0, self.degree + 1):
            # (xT * x)^-1 * xT * y
            self.coefficients.append(result.elements[i][0])

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
