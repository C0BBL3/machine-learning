from gradient_descent import GradientDescent
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


[print('Gradient')]
print('    1 Variable Function')
minimizer = GradientDescent(single_variable_function)

gradient = minimizer.compute_gradient(delta=0.01)

assert gradient == [
    -2.0000000000000018], 'Gradient should be [-2.0000000000000018] but was actually {}'.format(gradient)


print('    2 Variable Function')
minimizer = GradientDescent(two_variable_function)

gradient = minimizer.compute_gradient(delta=0.01)

assert minimizer.minimum == [-2.0000000000000018,
                             3.0001000000000055], 'Gradient should be [-2.0000000000000018, 3.0001000000000055] but was actually {}'.format(gradient)


print('    3 Variable Function')
minimizer = GradientDescent(three_variable_function)

gradient = minimizer.compute_gradient(delta=0.01)

assert minimizer.minimum == [-2.0000000000000018, 3.0001000000000055, -
                             4.0004000000000035], 'Gradient should be [-2.0000000000000018, 3.0001000000000055, -4.0004000000000035] but was actually {}'.format(gradient)


print('    6 Variable Function')
minimizer = GradientDescent(six_variable_function)

gradient = minimizer.compute_gradient(delta=0.01)

assert minimizer.minimum == [-2.0000000000000018, 3.0001000000000055, -4.0004000000000035, 1.0000000000000009, 2.0000000000000018,
                             3.0000000000000027], 'Gradient should be [-2.0000000000000018, 3.0001000000000055, -4.0004000000000035, 1.0000000000000009, 2.0000000000000018, 3.0000000000000027] but was actually {}'.format(gradient)


print('Descend')
print('    1 Variable Function')
minimizer = GradientDescent(single_variable_function)

gradient = minimizer.compute_gradient(delta=0.01)

descent = minimizer.descend(
    scaling_factor=0.001, delta=0.01, num_steps=1, logging=True)

assert minimizer.minimum == [
    0.0020000000000000018], 'Descent should be [0.0020000000000000018] but was actually {}'.format(descent)


print('    2 Variable Function')
minimizer = GradientDescent(two_variable_function)

descent = minimizer.descend(
    scaling_factor=0.001, delta=0.01, num_steps=1, logging=True)

assert minimizer.minimum == [0.0020000000000000018, -
                             0.0030001000000000055], 'Descent should be [0.0020000000000000018, -0.0030001000000000055] but was actually {}'.format(descent)


print('    3 Variable Function')
minimizer = GradientDescent(three_variable_function)

descent = minimizer.descend(
    scaling_factor=0.001, delta=0.01, num_steps=1, logging=True)

assert minimizer.minimum == [0.0020000000000000018, -0.0030001000000000055,
                             0.004000400000000004], 'Descent should be [0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004] but was actually {}'.format(descent)


print('    6 Variable Function')
minimizer = GradientDescent(six_variable_function)

descent = minimizer.descend(
    scaling_factor=0.001, delta=0.01, num_steps=1, logging=True)

assert minimizer.minimum == [0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004, -0.0010000000000000009, -0.0020000000000000018, -
                             0.0030000000000000027], 'Descent should be [0.0020000000000000018, -0.0030001000000000055, 0.004000400000000004, -0.0010000000000000009, -0.0020000000000000018, -0.0030000000000000027] but was actually {}'.format(descent)


print('Grid Search')
print('    Two Variable Function')
minimizer = GradientDescent(single_variable_function)

minimizer.grid_search([[0, 0.25, 0.75]])

grid_search = minimizer.minimum

assert minimizer.minimum == [
    0.75], 'Grid Search should be [0.75] but was {}'.format(grid_search)


print('    2 Variable Function')
minimizer = GradientDescent(two_variable_function)

minimizer.grid_search([[0, 0.25, 0.75], [0.9, 1, 1.1]])

grid_search = minimizer.minimum

assert minimizer.minimum == [
    0.75, 0.9], 'Grid Search should be [0.75, 0.9] but was {}'.format(grid_search)


print('    3 Variable Function')
minimizer = GradientDescent(three_variable_function)

minimizer.grid_search(
    [[0, 0.25, 0.75], [0.9, 1, 1.1], [0, 1, 2, 3]])

grid_search = minimizer.minimum

assert minimizer.minimum == [
    0.75, 0.9, 1], 'Grid Search should be [0.75, 0.9, 1] but was {}'.format(grid_search)


print('    6 Variable Function')
minimizer = GradientDescent(six_variable_function)

minimizer.grid_search([[0, 0.25, 0.75], [0.9, 1, 1.1], [0, 1, 2, 3],
                       [-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2]])

grid_search = minimizer.minimum

assert minimizer.minimum == [
    0.75, 0.9, 1, -2, -2, -2], 'Grid Search should be [0.75, 0.9, 1, -2, -2, -2] but was {}'.format(grid_search)


print('All Tests Passed!! 😊')
