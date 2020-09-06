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

df2 = df1
df2.filter_columns(['Sara', 'Pete'])
print("    Testing DataFrame 2's filter_columns")
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]], "DataFrame 2's filter_columns were not right, they should be [[3, 1], [1, 0], [4, 1], [0, 0]], but were {}".format(df2.to_array())
print("    DataFrame 2's filter_columns Passed!!!\n")

print("    Testing DataFrame 2's columns")
assert df2.columns == ['Sara', 'Pete'], "DataFrame 2's columns were not right, they should be ['Sara', 'Pete'], but were {}".format(df2.columns)
print("    DataFrame 2's columns Passed!!!\n")

print('\n--------------------------------\n')

def multiply_by_4(x):
    return 4 * x

df3 = DataFrame(data_dict, column_order=['Pete', 'John', 'Sara'])
df3.apply('John', multiply_by_4)
print("    Testing DataFrame 3's apply()")
assert df3.to_array() == [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]], "DataFrame 2's apply() was not right, it should be [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]], but was {}".format(df2.to_array())
print("    DataFrame 2's apply() Passed!!!\n")

df4 = DataFrame(data_dict, column_order=['Pete', 'John', 'Sara'])
df4.to_array()
df4.append_pairwise_interactions()
print("    Testing DataFrame 4's columns")
assert df4.columns == ['Pete', 'John', 'Sara', 'Pete_John', 'Pete_Sara', 'John_Sara'], "DataFrame 4's columns were not right, they should be ['Pete', 'John', 'Sara', 'Pete_John', 'Pete_Sara', 'John_Sara'], but were {}".format(df4.columns)
print("    DataFrame 4's columns Passed!!!\n")

print("    Testing DataFrame 4's to_array()")
assert df4.to_array() == [[1, 2, 3, 2, 3, 6], [0, 1, 1, 0, 0, 1], [1, 0, 4, 0, 4, 0], [0, 2, 0, 0, 0, 0]], "DataFrame 4's to_array() was not right, it should be [[1, 2, 3, 2, 3, 6], [0, 1, 1, 0, 0, 1], [1, 0, 4, 0, 4, 0], [0, 2, 0, 0, 0, 0]], but was {}".format(df4.to_array())
print("    DataFrame 4's to_array() Passed!!!\n")

print('\n--------------------------------\n')

data_dict_2 = {
    'id': [1, 2, 3, 4],
    'color': ['blue', 'yellow', 'green', 'yellow']
}

df5 = DataFrame(data_dict_2, column_order=['id', 'color'])
df5.create_dummy_variables('color')
print("    Testing DataFrame 5's create_dummy_variables()")
assert df5.columns == ['id', 'color_blue', 'color_yellow', 'color_green'], "DataFrame 5's columns were not right, they should be ['id', 'color_blue', 'color_yellow', 'color_green'], but were {}".format(df5.columns)
print("    DataFrame 5's create_dummy_variables() Passed!!!\n")

df5.remove_columns(['id', 'color_yellow'])
print("    Testing DataFrame 5's remove_columns()")
assert df5.columns == ['color_blue', 'color_green'], "DataFrame 5's columns were not right, they should be ['color_blue', 'color_green'], but were {}".format(df5.columns)
print("    DataFrame 5's remove_columns() Passed!!!\n")

df5.append_columns({
    'name': ['Anna', 'Bill', 'Cayden', 'Daphnie'],
    'letter': ['a', 'b', 'c', 'd']
})
print("    Testing DataFrame 5's append_columns()")
assert df5.columns == ['color_blue', 'color_green', 'name', 'letter'], "DataFrame 5's columns were not right, they should be ['color_blue', 'color_green', 'name', 'letter'], but were {}".format(df5.columns)
print("    DataFrame 5's append_columns() Passed!!!\n")


print("    Testing DataFrame 5's to_array()")
assert df5.to_array() == [[1, 0, 'Anna', 'a'], [0, 0, 'Bill', 'b'], [0, 1, 'Cayden', 'c'], [0, 0, 'Daphnie', 'd']], "DataFrame 5's to_array() was not right, it should be [[1, 0, 'Annna', 'a'], [0, 0, 'Bill', 'b'], [0, 1, 'Cayden', 'c'], [0, 0, 'Daphnie', 'd']], but was {}".format(df5.to_array())
print("    DataFrame 5's to_array() Passed!!!\n")


print('ALL TESTS PASS!!!!!')
