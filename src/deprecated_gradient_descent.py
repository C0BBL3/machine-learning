class GradientDescent:
    def __init__(self, f):
        self.function = f
        self.num_vars = f.__code__.co_argcount
        self.minimum = [0 for _ in range(0, self.num_vars)]
        


    def grid_search(self, data):
        cartesian_product_of_data = self.cartesian_product(data)
        self.minimum = cartesian_product_of_data[0]
        if len(cartesian_product_of_data) > 1:
            for i in range(1, len(cartesian_product_of_data)):
                if self.function(cartesian_product_of_data[i]) < self.function(self.minimum):
                    self.minimum = cartesian_product_of_data[i]

        return self.minimum

    def next_set_of_combos(self, arr_1, arr_2):
        result = []

        for i in range(0, len(arr_1)):

            for j in range(0, len(arr_2)):

                temp = [num for num in arr_1[i]]
                temp.append(arr_2[j])
                result.append(temp)

        return result

    def cartesian_product(self, arrays):
        result = []
        temp = arrays[0]
        result = [temp]

        for i in range(1, len(arrays)):
            temp = self.next_set_of_combos(temp, arrays[i])
            result.append(temp)

        return result[-1]

    def compute_gradient(self, delta=0.001):
        return [self.tangent_slope_at_point(delta, i) for i in range(0, self.num_vars)]

    def descend(self, scaling_factor=0.001, delta=0.001, num_steps=4, logging=True):
        self.minimum = self.gradient_descent(
            num_steps=num_steps, delta=delta, alpha=scaling_factor)

        print('descending function: y = {}'.format(*[str(round(minimum, 5)) + 'x^' + str(self.minimum.index(minimum) + 1) + ' + ' for minimum in self.minimum]))

        return self.minimum

    def gradient_descent(self, prev_terms=None, num_steps=1, step=0, logging=False, alpha=0.001, delta=0.001, precision=0.001):
        if step < num_steps:
            value_nots = self.minimum
            self.minimum_gradient = self.compute_gradient()
            for i in range(0, len(self.minimum)):
                self.minimum[i] -= alpha * self.minimum_gradient[i]

            if logging: #<--- is commented out because i dont want 100 lines of numbers
                print('y = {}'.format(*[str(round(minimum, 5)) + 'x^' + str(self.minimum.index(minimum) + 1) + ' + ' for minimum in self.minimum]))

            step += 1
            return self.gradient_descent(prev_terms=value_nots, num_steps=num_steps, step=step)

        else:
            return self.minimum

    def tangent_slope_at_point(self, h, derivative):
        positive_delta_args = [self.minimum[i] if i !=
                          derivative else self.minimum[i] + h for i in range(0, self.num_vars)]
        negative_delta_args = [self.minimum[i] if i !=
                          derivative else self.minimum[i] - h for i in range(0, self.num_vars)]
        return (self.function(*positive_delta_args) - self.function(*negative_delta_args)) / (2 * h)
