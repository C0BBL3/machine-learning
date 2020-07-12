import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matrix_class import Matrix


class PolynomialRegressor:
    def __init__(self, degree):
        self.degree = degree
        self.default_guess = [0]
        self.coefficients = [0]
        self.data = []
        for i in range(0, self.degree):
            self.default_guess.append(0)
            self.coefficients.append(0)

    def ingest_data(self, data):
        self.data = data

    def solve_coefficients(self):
        X_data = []
        y_data = []
        for i, j in self.data:
            X_data.append([1, i, i ** 2])
            y_data.append([j])
        X_matrix = Matrix(elements=X_data)
        y_matrix = Matrix(elements=y_data)
        X_transpose = X_matrix.transpose()  # xT
        X_transpose_times_X = X_transpose @ X_matrix  # xT * x
        result = X_transpose_times_X.inverse() @ X_transpose @ y_matrix
        for i in result.elements:
            index = result.elements.index(i)
            self.coefficients[index] = i[0]  # (xT * x)^-1 * xT * y

    def sum_squared_error(self):
        return sum([(self.evaluate(x) - y)**2 for x, y in self.data])

    def evaluate(self, x):
        if self.coefficients == []:
            return sum([self.default_guess[i] * x ** (i + 1) for i in range(0, self.degree)])
        else:
            return sum([self.coefficients[i] * x ** (i + 1) for i in range(0, self.degree)])

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
