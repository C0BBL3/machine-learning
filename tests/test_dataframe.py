import sys
sys.path.append('src')
from dataframe import DataFrame

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sara': [3, 1, 4, 0]
}

print('\nTesting...\n')
df1 = DataFrame(data_dict, column_order=['Pete', 'John', 'Sara'])
print("    Testing DataFrame 1's data_dict")
assert df1.data_dict == {'Pete': [1, 0, 1, 0], 'John': [2, 1, 0, 2], 'Sara': [3, 1, 4, 0]}, "DataFrame 1's data_dict was not right, it should be {'Pete': [1, 0, 1, 0], 'John': [2, 1, 0, 2], 'Sara': [3, 1, 4, 0]}, but was {}".format(df1.data_dict)
print("    DataFrame 1's data_dict Passed!!!\n")

print("    Testing DataFrame 1's to_array()")
assert df1.to_array() == [[1, 2, 3], [0, 1, 1], [1, 0, 4], [0, 2, 0]], "DataFrame 1's to_array() was not right, it should be [[1, 2, 3] [0, 1, 1] [1, 0, 4] [0, 2, 0]], but was {}".format(df1.to_array())
print("    DataFrame 1's to_array() Passed!!!\n")

print("    Testing DataFrame 1's columns")
assert df1.columns == ['Pete', 'John', 'Sara'], "DataFrame 1's columns were not right, they should be ['Pete', 'John', 'Sara'], but were {}".format(df1.columns)
print("    DataFrame 1's columns Passed!!!\n")

df1.filter_columns(['Sara', 'Pete'])
df2 = df1
print("    Testing DataFrame 2's filter_columns")
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]], "DataFrame 2's filter_columns were not right, they should be [[3, 1], [1, 0], [4, 1], [0, 0]], but were {}".format(df2.to_array())
print("    DataFrame 2's filter_columns Passed!!!\n")

print("    Testing DataFrame 2's columns")
assert df2.columns == ['Sara', 'Pete'], "DataFrame 2's columns were not right, they should be ['Sara', 'Pete'], but were {}".format(df2.columns)
print("    DataFrame 2's columns Passed!!!\n")

def multiply_by_4(x):
    return 4 * x

df3 = DataFrame(data_dict, column_order=['Pete', 'John', 'Sara'])
df3.apply('John', multiply_by_4)
print("    Testing DataFrame 3's apply()")
assert df3.to_array() == [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]], "DataFrame 2's apply() was not right, it should be [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]], but was {}".format(df2.to_array())
print("    DataFrame 2's apply() Passed!!!\n")

print('ALL TESTS PASS!!!!!')
