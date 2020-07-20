from gradient_descent import GradientDescent

data = [(0, 1), (1, 2), (2, 4), (3, 10)]


def sum_squared_error(beta_0, beta_1, beta_2):
    squared_errors = []
    for (x, y) in data:
        estimation = beta_0 + beta_1*x + beta_2*(x**2)
        error = estimation - y
        squared_errors.append(error**2)
    return sum(squared_errors)


minimizer = GradientDescent(sum_squared_error)
minimizer.descend(scaling_factor=0.001, delta=0.01,
                  num_steps=100, logging=True)
minimizer.minimum
# you can ignore this error cause im passing all betas into the function
sum_squared_error(*minimizer.minimum)
