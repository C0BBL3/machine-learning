import matplotlib.pyplot as plt

data = [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
    [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
    [2,12,'B'],[2,12,'B'],
    [3,12,'A'],[3,12,'A'],
    [3,11,'A'],[3,11,'A'],
    [3,11.5,'A'],[3,11.5,'A'],
    [4,11,'A'],[4,11,'A'],
    [4,11.5,'A'],[4,11.5,'A'],
    [2,10.5,'A'],[2,10.5,'A'],
    [3,10.5,'B'],
    [4,10.5,'A']]

a_x,a_y,b_x,b_y=[],[],[],[]

for arr in data:
    if arr[2] == 'A':
        a_x.append(arr[0])
        a_y.append(arr[1])
    if arr[2] == 'B':
        b_x.append(arr[0])
        b_y.append(arr[1])

plt.scatter(x=a_x, y=a_y, c='blue')
plt.scatter(x=b_x, y=b_y, c='red')
plt.show()