from GradientDescent import GradientDescent

def single_variable_function(x):
    return (x-1)**2
def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3
def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4
def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6
 
minimizer = GradientDescent(single_variable_function)
print(minimizer.minimum)

print(minimizer.compute_gradient(delta=0.01))

print(minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True))

 
minimizer = GradientDescent(two_variable_function)
print(minimizer.minimum)

print(minimizer.compute_gradient(delta=0.01))

print(minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True))

 
minimizer = GradientDescent(three_variable_function)
print(minimizer.minimum)

print(minimizer.compute_gradient(delta=0.01))

print(minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True))

 
minimizer = GradientDescent(six_variable_function)
print(minimizer.minimum)

print(minimizer.compute_gradient(delta=0.01))

print(minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=1, logging=True))
