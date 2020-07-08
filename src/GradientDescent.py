class GradientDescent:
    def __init__(self, f):
        self.function = f
        self.minimum = [0, 0]
        self.num_vars = f.__code__.co_argcount

    def grid_search(self, data):
        for i in data[0]:
            for j in data[1]:
                # dynamic amount of for loops here
                current_index = [i, j]  # [array of i,j,k,...]
                if self.function(*current_index) < self.function(*self.minimum):
                    self.minimum = [i, j]

        return self.minimum

    def compute_gradient(self, delta=0.001):
        return [self.tangent_slope_at_point(delta, i) for i in range(0, self.num_vars)]

    def descend(self, scaling_factor=0.001, delta=0.001, num_steps=4, logging=True):
        self.minimum = self.gradient_descent(
            num_steps=num_steps, delta=delta, alpha=scaling_factor)

        print('descending function: y = {}x + {}'.format(*[str(round(minimum, 5)) + 'x^' + str(self.minimum.index(minimum) + 1) + ' + ' for minimum in self.minimum])

        return self.minimum

    def gradient_descent(self, prev_terms=None, num_steps=1, step=0, logging=False, alpha=0.001, delta=0.001, precision=0.001):
        if step < num_steps:
            value_nots=self.minimum
            self.minimum_gradient=self.compute_gradient()
            for i in range(0, len(self.minimum)):
                self.minimum[i] -= alpha * self.minimum_gradient[i]

            def function(x):
                return sum([self.minimum[i] * x ** (i + 1) for i in range(0, self.minimum)])

            # if logging: #<--- is commented out because i dont want 100 lines of numbers
                # print('y = {}x + {}'.format(round(y1,2), round(x1,2)))

            step += 1
            return self.gradient_descent(prev_terms=value_nots, num_steps=num_steps, step=step)

        else:
            return self.minimum

    def tangent_slope_at_point(self, h, derivative):
        positive_delta=[self.minimum[i] if i !=
            derivative else self.minimum[i] + h for i in range(0, self.num_vars)]
        negative_delta=[self.minimum[i] if i !=
            derivative else self.minimum[i] - h for i in range(0, self.num_vars)]
        return (self.function(*positive_delta) - self.function(*negative_delta)) / (2 * h)
