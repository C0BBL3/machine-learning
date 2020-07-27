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

classes = []

functions = [single_variable_function,
             two_variable_function, three_variable_function,
             six_variable_function]

answers = [[-2.0000000000], [-2.0000000000, 3.0001000000],
           [-2.0000000000, 3.0001000000, -4.0004000000],
           [-2.0000000000, 3.0001000000, -4.0004000000,
             1.0000000000, 2.0000000000, 3.0000000000]]

for i in range(1, 7):
    if i != 4 and i != 5:
        print('    {} Variable Function').format(i)
        classes.append(GradientDescent(functions[i]))
        classes[i].compute_gradient(delta=0.01)
        gradient = [round(minimum, 10) for minimum in classes[i].minimum]

        assert gradient == answers[i], 'Gradient should be ' + str(answers[i]) + ' but was actually {}'.format(gradient)



print('Descend')

classes = []

answers = [[0.0020000000], [0.0020000000, -0.0030001000],
           [0.0020000000, -0.0030001000, 0.0040004000],
           [0.0020000000, -0.0030001000, 0.0040004000,
            -0.0010000000, -0.0020000000, -0.0030000000]]

for i in range(1, 7):
    if i != 4 and i != 5:
        print('    {} Variable Function').format(i)
        functions.append(GradientDescent(functions[i]))
        functions[i].descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True), 10)
        descent=[round(minimum, 10) for minimum in functions[i].minimum]

            assert descent == answers[i], 'Descent should be ' +
            str(answers[i]) + ' but was actually {}'.format(gradient)

print('Grid Search')

classes = []

answers = [[0.75], [0.75, 0.9], [0.75, 0.9, 1], [0.75, 0.9, 1, -2, -2, -2]]

for i in range(1, 7):
    if i != 4 and i != 5:
        print('    {} Variable Function').format(i)
        functions.append(GradientDescent(functions[i]))
        functions[i].descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True), 10)
        grid_search=[round(minimum, 10) for minimum in functions[i].minimum]

        assert grid_search == answers[i], 'Grid Search should be ' + str(answers[i]) + ' but was actually {}'.format(gradient)

print('All Tests Passed!! 😊')
