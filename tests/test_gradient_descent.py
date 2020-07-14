from gradient_descent import GradientDescent  # halp
import sys
sys.path.append('src')


print('Testing...')


def single_variable_function(x):
    return (x-1)**2


def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3


def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4


def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6


print('Gradient')
print('    1 Variable Function')
minimizer = GradientDescent(single_variable_function)

minimizer.compute_gradient(delta=0.01)
gradient = [round(minimum, 10) for minimum in minimizer.minimum]

assert gradient == [
    -2.0000000000], 'Gradient should be [-2.0000000000] but was actually {}'.format(gradient)


print('    2 Variable Function')
minimizer = GradientDescent(two_variable_function)

minimizer.compute_gradient(delta=0.01)
gradient = [round(minimum, 10) for minimum in minimizer.minimum]

assert gradient == [-2.0000000000,
                             3.0001000000], 'Gradient should be [-2.0000000000, 3.0001000000] but was actually {}'.format(gradient)


print('    3 Variable Function')
minimizer = GradientDescent(three_variable_function)

minimizer.compute_gradient(delta=0.01)
gradient = [round(minimum, 10) for minimum in minimizer.minimum]

assert gradient == [-2.0000000000, 3.0001000000, -
                             4.0004000000], 'Gradient should be [-2.0000000000, 3.0001000000, -4.0004000000] but was actually {}'.format(gradient)


print('    6 Variable Function')
minimizer = GradientDescent(six_variable_function)

minimizer.compute_gradient(delta=0.01)
gradient = [round(minimum, 10) for minimum in minimizer.minimum]

assert gradient == [-2.0000000000, 3.0001000000, -4.0004000000, 1.0000000000, 2.0000000000,
                             3.0000000000], 'Gradient should be [-2.0000000000, 3.0001000000, -4.0004000000, 1.0000000000, 2.0000000000, 3.0000000000] but was actually {}'.format(gradient)


print('Descend')
print('    1 Variable Function')
minimizer = GradientDescent(single_variable_function)

minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True), 10)
descent=[round(minimum, 10) for minimum in minimizer.minimum]


assert descent == [
    0.0020000000], 'Descent should be [0.0020000000] but was actually {}'.format(descent)


print('    2 Variable Function')
minimizer = GradientDescent(two_variable_function)

minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True), 10)
descent=[round(minimum, 10) for minimum in minimizer.minimum]

assert descent == [0.0020000000, -
                             0.0030001000], 'Descent should be [0.0020000000, -0.0030001000] but was actually {}'.format(descent)


print('    3 Variable Function')
minimizer=GradientDescent(three_variable_function)

minimizer.descend(scaling_factor = 0.001, delta = 0.01, num_steps = 1, logging = True), 10)
descent=[round(minimum, 10) for minimum in minimizer.minimum]

assert descent == [0.0020000000, -0.0030001000,
                             0.0040004000], 'Descent should be [0.0020000000, -0.0030001000, 0.0040004000] but was actually {}'.format(descent)


print('    6 Variable Function')
minimizer=GradientDescent(six_variable_function)

minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True), 10)
descent=[round(minimum, 10) for minimum in minimizer.minimum]

assert descent == [0.0020000000, -0.0030001000, 0.0040004000, -0.0010000000, -0.0020000000, -
                             0.0030000000], 'Descent should be [0.0020000000, -0.0030001000, 0.0040004000, -0.0010000000, -0.0020000000, -0.0030000000] but was actually {}'.format(descent)


print('Grid Search')
print('    Two Variable Function')
minimizer=GradientDescent(single_variable_function)

minimizer.grid_search([[0, 0.25, 0.75]])

grid_search=[round(minimum, 10) for minimum in minimizer.minimum]

assert grid_search == [
    0.75], 'Grid Search should be [0.75] but was {}'.format(grid_search)


print('    2 Variable Function')
minimizer=GradientDescent(two_variable_function)

minimizer.grid_search([[0, 0.25, 0.75], [0.9, 1, 1.1]])

grid_search=[round(minimum, 10) for minimum in minimizer.minimum]

assert grid_search == [
    0.75, 0.9], 'Grid Search should be [0.75, 0.9] but was {}'.format(grid_search)


print('    3 Variable Function')
minimizer=GradientDescent(three_variable_function)

minimizer.grid_search(
    [[0, 0.25, 0.75], [0.9, 1, 1.1], [0, 1, 2, 3]])

grid_search=[round(minimum, 10) for minimum in minimizer.minimum]

assert grid_search == [
    0.75, 0.9, 1], 'Grid Search should be [0.75, 0.9, 1] but was {}'.format(grid_search)


print('    6 Variable Function')
minimizer=GradientDescent(six_variable_function)

minimizer.grid_search([[0, 0.25, 0.75], [0.9, 1, 1.1], [0, 1, 2, 3],
                       [-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2]])

grid_search=[round(minimum, 10) for minimum in minimizer.minimum]

assert grid_search == [
    0.75, 0.9, 1, -2, -2, -2], 'Grid Search should be [0.75, 0.9, 1, -2, -2, -2] but was {}'.format(grid_search)


print('All Tests Passed!! 😊')
