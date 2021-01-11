import sys
sys.path.append('src')
from dataframe import DataFrame

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sara': [3, 1, 4, 0]
}

print('\nTesting...\n')

print('----------------------------------------------------------------\n')

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

print('----------------------------------------------------------------\n')

df2 = df1
df2.filter_columns(['Sara', 'Pete'])
print("    Testing DataFrame 2's filter_columns")
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]], "DataFrame 2's filter_columns were not right, they should be [[3, 1], [1, 0], [4, 1], [0, 0]], but were {}".format(df2.to_array())
print("    DataFrame 2's filter_columns Passed!!!\n")

print("    Testing DataFrame 2's columns")
assert df2.columns == ['Sara', 'Pete'], "DataFrame 2's columns were not right, they should be ['Sara', 'Pete'], but were {}".format(df2.columns)
print("    DataFrame 2's columns Passed!!!\n")

print('----------------------------------------------------------------\n')

def multiply_by_4(x):
    return 4 * x

df3 = DataFrame(data_dict, column_order=['Pete', 'John', 'Sara'])
df3.apply('John', multiply_by_4)
print("    Testing DataFrame 3's apply()")
assert df3.to_array() == [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]], "DataFrame 2's apply() was not right, it should be [[1, 8, 3], [0, 4, 1], [1, 0, 4], [0, 8, 0]], but was {}".format(df2.to_array())
print("    DataFrame 3's apply() Passed!!!\n")

print('----------------------------------------------------------------\n')

df4 = DataFrame(data_dict, column_order=['Pete', 'John', 'Sara'])
df4.to_array()
df4.append_pairwise_interactions()
print("    Testing DataFrame 4's columns")
assert df4.columns == ['Pete', 'John', 'Sara', 'Pete_John', 'Pete_Sara', 'John_Sara'], "DataFrame 4's columns were not right, they should be ['Pete', 'John', 'Sara', 'Pete_John', 'Pete_Sara', 'John_Sara'], but were {}".format(df4.columns)
print("    DataFrame 4's columns Passed!!!\n")

print("    Testing DataFrame 4's to_array()")
assert df4.to_array() == [[1, 2, 3, 2, 3, 6], [0, 1, 1, 0, 0, 1], [1, 0, 4, 0, 4, 0], [0, 2, 0, 0, 0, 0]], "DataFrame 4's to_array() was not right, it should be [[1, 2, 3, 2, 3, 6], [0, 1, 1, 0, 0, 1], [1, 0, 4, 0, 4, 0], [0, 2, 0, 0, 0, 0]], but was {}".format(df4.to_array())
print("    DataFrame 4's to_array() Passed!!!\n")

print('----------------------------------------------------------------\n')

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

print('----------------------------------------------------------------\n')

data_dict_3 = {
    'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
    'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
    'condiments': [[], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly'],
                   [], ['mayo'], ['jelly'], ['mayo', 'jelly']],
    'rating': [1, 1, 4, 0, 4, 8, 1, 0, 5, 0, 9, 0, 0, 0, 0, 0]
}
df6 = DataFrame(data_dict_3, column_order=['beef', 'pb', 'condiments'])
print("    Testing DataFrame 6's columns")
assert df6.columns == ['beef', 'pb', 'condiments'], "DataFrame 6's columns were not right, they should be ['color_blue', 'color_green', 'name', 'letter'], but were {}".format(df6.columns)
print("    DataFrame 6's append_columns() Passed!!!\n")

print("    Testing DataFrame 6's to_array()")
assert df6.to_array() == [[0,  0,  []], [0,  0,  ['mayo']], [0,  0,  ['jelly']], [0,  0,  ['mayo', 'jelly']], [5,  0,  []], [5,  0,  ['mayo']], [5,  0,  ['jelly']], [5,  0,  ['mayo', 'jelly']], [0,  5,  []], [0,  5,  ['mayo']], [0,  5,  ['jelly']], [0,  5,  ['mayo', 'jelly']], [5,  5,  []], [5,  5,  ['mayo']], [5,  5,  ['jelly']], [5, 5, ['mayo', 'jelly']]], "DataFrame 6's to_array() was not right, it should be [[0,  0,  []], [0,  0,  ['mayo']], [0,  0,  ['jelly']], [0,  0,  ['mayo', 'jelly']], [5,  0,  []], [5,  0,  ['mayo']], [5,  0,  ['jelly']], [5,  0,  ['mayo', 'jelly']], [0,  5,  []], [0,  5,  ['mayo']], [0,  5,  ['jelly']], [0,  5,  ['mayo', 'jelly']], [5,  5,  []], [5,  5,  ['mayo']], [5,  5,  ['jelly']], [5, 5, ['mayo', 'jelly']]], but was {}".format(df6.to_array())
print("    DataFrame 6's to_array() Passed!!!\n")

df6.create_dummy_variables('condiments')
print("    Testing DataFrame 6's create_dummy_variables()")
assert df6.columns == ['beef', 'pb', 'mayo', 'jelly'], "DataFrame 6's columns were not right, they should be ['beef', 'pb', 'mayo', 'jelly'], but were {}".format(df6.columns)
assert df6.to_array() == [[0,  0,  0,  0], [0,  0,  1,  0], [0,  0,  0,  1], [0,  0,  1,  1], [5,  0,  0,  0], [5,  0,  1,  0], [5,  0,  0,  1], [5,  0,  1,  1], [0,  5,  0,  0], [0,  5,  1,  0], [0,  5,  0,  1], [0,  5,  1,  1], [5,  5,  0,  0], [5,  5,  1,  0], [5,  5,  0,  1], [5,  5,  1,  1]], "DataFrame 6's to_array() was not right, it should be [[0,  0,  0,  0], [0,  0,  1,  0], [0,  0,  0,  1], [0,  0,  1,  1], [5,  0,  0,  0], [5,  0,  1,  0], [5,  0,  0,  1], [5,  0,  1,  1], [0,  5,  0,  0], [0,  5,  1,  0], [0,  5,  0,  1], [0,  5,  1,  1], [5,  5,  0,  0], [5,  5,  1,  0], [5,  5,  0,  1], [5,  5,  1,  1]], but was {}".format(df6.to_array())
print("    DataFrame 6's create_dummy_variables() Passed!!!\n")

df6.append_pairwise_interactions()
print("    Testing DataFrame 6's append_pairwise_interactions()")
assert df6.columns == ['beef', 'pb', 'mayo', 'jelly', 'beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly'], "DataFrame 6's columns were not right, they should be ['beef', 'pb', 'mayo', 'jelly', 'beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly'], but were {}".format(df6.columns)
assert df6.to_array() == [[0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [0,  0,  1,  0,  0,  0,  0,  0,  0,  0], [0,  0,  0,  1,  0,  0,  0,  0,  0,  0], [0,  0,  1,  1,  0,  0,  0,  0,  0,  1], [5,  0,  0,  0,  0,  0,  0,  0,  0,  0], [5,  0,  1,  0,  0,  5,  0,  0,  0,  0], [5,  0,  0,  1,  0,  0,  5,  0,  0,  0], [5,  0,  1,  1,  0,  5,  5,  0,  0,  1], [0,  5,  0,  0,  0,  0,  0,  0,  0,  0], [0,  5,  1,  0,  0,  0,  0,  5,  0,  0], [0,  5,  0,  1,  0,  0,  0,  0,  5,  0], [0,  5,  1,  1,  0,  0,  0,  5,  5,  1], [5,  5,  0,  0, 25,  0,  0,  0,  0,  0], [5,  5,  1,  0, 25,  5,  0,  5,  0,  0], [5,  5,  0,  1, 25,  0,  5,  0,  5,  0], [5,  5,  1,  1, 25,  5,  5,  5,  5,  1]], "DataFrame 6's to_array() was not right, it should be [[0,  0,  0,  0,  0,  0,  0,  0,  0,  0], [0,  0,  1,  0,  0,  0,  0,  0,  0,  0], [0,  0,  0,  1,  0,  0,  0,  0,  0,  0], [0,  0,  1,  1,  0,  0,  0,  0,  0,  1], [5,  0,  0,  0,  0,  0,  0,  0,  0,  0], [5,  0,  1,  0,  0,  5,  0,  0,  0,  0], [5,  0,  0,  1,  0,  0,  5,  0,  0,  0], [5,  0,  1,  1,  0,  5,  5,  0,  0,  1], [0,  5,  0,  0,  0,  0,  0,  0,  0,  0], [0,  5,  1,  0,  0,  0,  0,  5,  0,  0], [0,  5,  0,  1,  0,  0,  0,  0,  5,  0], [0,  5,  1,  1,  0,  0,  0,  5,  5,  1], [5,  5,  0,  0, 25,  0,  0,  0,  0,  0], [5,  5,  1,  0, 25,  5,  0,  5,  0,  0], [5,  5,  0,  1, 25,  0,  5,  0,  5,  0], [5,  5,  1,  1, 25,  5,  5,  5,  5,  1]], but was {}".format(df6.to_array())
print("    DataFrame 6's append_pairwise_interactions() Passed!!!\n")

df6.append_columns({'constant': [1 for _ in range(len(data_dict_3['rating']))],'rating': data_dict_3['rating']})
print("    Testing DataFrame 6's columns")
assert df6.columns == ['beef', 'pb', 'mayo', 'jelly', 'beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly', 'constant', 'rating'], "DataFrame 6's columns were not right, they should be ['constant', 'beef', 'pb', 'mayo', 'jelly', 'beef_pb', 'beef_mayo', 'beef_jelly', 'pb_mayo', 'pb_jelly', 'mayo_jelly', 'rating'], but were {}".format(df6.columns)
print("    DataFrame 6's columns Passed!!!\n")

print("    Testing DataFrame 6's to_array()")
assert df6.to_array() == [[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1], [0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  1], [0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  1,  4], [0,  0,  1,  1,  0,  0,  0,  0,  0,  1,  1,  0], [5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  4], [5,  0,  1,  0,  0,  5,  0,  0,  0,  0,  1,  8], [5,  0,  0,  1,  0,  0,  5,  0,  0,  0,  1,  1], [5,  0,  1,  1,  0,  5,  5,  0,  0,  1,  1,  0], [0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  1,  5], [0,  5,  1,  0,  0,  0,  0,  5,  0,  0,  1,  0], [0,  5,  0,  1,  0,  0,  0,  0,  5,  0,  1,  9], [0,  5,  1,  1,  0,  0,  0,  5,  5,  1,  1,  0], [5,  5,  0,  0, 25,  0,  0,  0,  0,  0,  1,  0], [5,  5,  1,  0, 25,  5,  0,  5,  0,  0,  1,  0], [5,  5,  0,  1, 25,  0,  5,  0,  5,  0,  1,  0], [5,  5,  1,  1, 25,  5,  5,  5,  5,  1,  1,  0]], "DataFrame 6's to_array() was not right, it should be [[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1], [0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  1], [0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  1,  4], [0,  0,  1,  1,  0,  0,  0,  0,  0,  1,  1,  0], [5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  4], [5,  0,  1,  0,  0,  5,  0,  0,  0,  0,  1,  8], [5,  0,  0,  1,  0,  0,  5,  0,  0,  0,  1,  1], [5,  0,  1,  1,  0,  5,  5,  0,  0,  1,  1,  0], [0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  1,  5], [0,  5,  1,  0,  0,  0,  0,  5,  0,  0,  1,  0], [0,  5,  0,  1,  0,  0,  0,  0,  5,  0,  1,  9], [0,  5,  1,  1,  0,  0,  0,  5,  5,  1,  1,  0], [5,  5,  0,  0, 25,  0,  0,  0,  0,  0,  1,  0], [5,  5,  1,  0, 25,  5,  0,  5,  0,  0,  1,  0], [5,  5,  0,  1, 25,  0,  5,  0,  5,  0,  1,  0], [5,  5,  1,  1, 25,  5,  5,  5,  5,  1,  1,  0]], but was {}".format(df6.to_array())
print("    DataFrame 6's to_array() Passed!!!\n")

print('----------------------------------------------------------------\n')

columns = ['firstname', 'lastname', 'age']
arr = [['Kevin', 'Fray', 5],
           ['Charles', 'Trapp', 17],
           ['Anna', 'Smith', 13],
           ['Sylvia', 'Mendez', 9]]

df7 = DataFrame.from_array(arr, columns)
print("    Testing DataFrame 7's from_array()")
assert df7.data_dict == {'firstname': ['Kevin', 'Charles', 'Anna', 'Sylvia'], 'lastname': ['Fray', 'Trapp', 'Smith', 'Mendez'], 'age':[5, 17, 13, 9]}, "DataFrame 7's from_array() was not right, it should be {'firstname': ['Kevin', 'Charles', 'Anna', 'Sylvia'], 'lastname': ['Fray', 'Trapp', 'Smith', 'Mendez'], 'age':[5, 17, 13, 9]}, but was {}".format(df7.data_dict)
print("    DataFrame 7's from_array() Passed!!!\n")

print("    Testing DataFrame 7's select_columns()")
assert df7.select_columns(['firstname','age']).to_array() == [['Kevin', 5], ['Charles', 17], ['Anna', 13], ['Sylvia', 9]], "DataFrame 7's select_columns() was not right, it should be [['Kevin', 5], ['Charles', 17], ['Anna', 13], ['Sylvia', 9]], but was {}".format(df7.array)
print("    DataFrame 7's select_columns() Passed!!!\n")

print("    Testing DataFrame 7's select_rows()")
assert df7.select_rows([1,3]).to_array() == [['Charles', 'Trapp', 17], ['Sylvia', 'Mendez', 9]], "DataFrame 7's select_columns() was not right, it should be [['Charles', 'Trapp', 17],['Sylvia', 'Mendez', 9]], but was {}".format(df7.select_rows([1,3]).to_array())
print("    DataFrame 7's select_columns() Passed!!!\n")

print("    Testing DataFrame 7's select_rows_where()")
assert df7.select_rows_where(lambda row: len(row['firstname']) >= len(row['lastname']) and row['age'] > 10).to_array() == [['Charles', 'Trapp', 17]], "DataFrame 7's select_columns_where() was not right, it should be [['Charles', 'Trapp', 17]], but was {}".format(df7.select_rows_where(lambda row: len(row['firstname']) >= len(row['lastname']) and row['age'] > 10).to_array())
print("    DataFrame 7's select_rows_where() Passed!!!\n")

print("    Testing DataFrame 7's order_by()")
assert df7.order_by('age', True).to_array() == [['Kevin', 'Fray', 5], ['Sylvia', 'Mendez', 9], ['Anna', 'Smith', 13], ['Charles', 'Trapp', 17]], "DataFrame 7's order_by() was not right, it should be [['Kevin', 'Fray', 5], ['Sylvia', 'Mendez', 9], ['Anna', 'Smith', 13], ['Charles', 'Trapp', 17]], but was {}".format(df7.order_by('age', True).to_array())
print("    DataFrame 7's order_by() Passed!!!\n")

print("    Testing DataFrame 7's order_by()")
assert df7.order_by('firstname', False).to_array() == [['Sylvia', 'Mendez', 9], ['Kevin', 'Fray', 5], ['Charles', 'Trapp', 17], ['Anna', 'Smith', 13]], "DataFrame 7's order_by() was not right, it should be [['Sylvia', 'Mendez', 9], ['Kevin', 'Fray', 5], ['Charles', 'Trapp', 17], ['Anna', 'Smith', 13]], but was {}".format(df7.order_by('firstname', False).to_array())
print("    DataFrame 7's order_by() Passed!!!\n")

print('----------------------------------------------------------------\n')

path_to_datasets = 'C:/Users/colbi/VSCode/Computational Math/machine-learning/datasets/'
filename = 'airtravel.csv' 
filepath = path_to_datasets + filename
df8 = DataFrame.from_csv(filepath, header=True)

print("    Testing DataFrame 8's to_array()")
assert df8.to_array() == [['"JAN"', '340', '360', '417'], ['"FEB"', '318', '342', '391'], ['"MAR"', '362', '406', '419'], ['"APR"', '348', '396', '461'], ['"MAY"', '363', '420', '472'], ['"JUN"', '435', '472', '535'], ['"JUL"', '491', '548', '622'], ['"AUG"', '505', '559', '606'], ['"SEP"', '404', '463', '508'], ['"OCT"', '359', '407', '461'], ['"NOV"', '310', '362', '390'], ['"DEC"', '337', '405', '432']], "DataFrame 8's to_array() was not right, it should be [['Month', '1958', '1959', '1960'],['JAN',  '340',  '360',  '417'],['FEB',  '318',  '342',  '391'],['MAR',  '362',  '406',  '419'],['APR',  '348',  '396',  '461'],['MAY',  '363',  '420',  '472'],['JUN',  '435',  '472',  '535'],['JUL',  '491',  '548',  '622'],['AUG',  '505',  '559',  '606'],['SEP',  '404',  '463',  '508'],['OCT',  '359',  '407',  '461'],['NOV',  '310',  '362',  '390'],['DEC',  '337',  '405',  '432']], but was {}".format(df8.to_array())
print("    DataFrame 8's to_array() Passed!!!\n")

print('----------------------------------------------------------------\n')

path_to_datasets = 'C:/Users/colbi/VSCode/Computational Math/machine-learning/datasets/'
filename = 'freshman_lbs.csv' 
filepath = path_to_datasets + filename
df9 = DataFrame.from_csv(filepath, header=True)

print("    Testing DataFrame 9's to_array()")
assert df9.to_array() ==  [['"M"', '159', '130', '22.02', '18.14'], ['"M"', '214', '190', '19.70', '17.44'], ['"M"', '163', '152', '24.09', '22.43'], ['"M"', '205', '194', '26.97', '25.57'], ['"F"', '150', '141', '21.51', '20.10'], ['"M"', '130', '121', '18.69', '17.40'], ['"F"', '141', '132', '24.24', '22.88'], ['"F"', '123', '117', '21.23', '20.23'], ['"F"', '154', '150', '30.26', '29.24'], ['"F"', '128', '123', '21.88', '21.02'], ['"F"', '110', '104', '17.63', '16.89'], ['"M"', '156', '152', '24.57', '23.85'], ['"M"', '148', '145', '20.68', '20.15'], ['"F"', '123', '121', '20.97', '20.36'], ['"F"', '154', '150', '27.30', '26.73'], ['"F"', '134', '132', '23.30', '22.88'], ['"F"', '117', '115', '19.48', '19.24'], ['"M"', '203', '203', '24.74', '24.69'], ['"F"', '126', '128', '20.69', '20.79'], ['"M"', '148', '148', '20.49', '20.60'], ['"F"', '128', '128', '21.09', '21.24'], ['"F"', '108', '110', '18.37', '18.53'], ['"M"', '150', '150', '22.40', '22.61'], ['"F"', '152', '152', '28.17', '28.43'], ['"M"', '192', '194', '23.60', '23.81'], ['"M"', '179', '181', '26.52', '26.78'], ['"M"', '132', '134', '18.89', '19.27'], ['"F"', '115', '117', '19.31', '19.75'], ['"M"', '154', '156', '20.96', '21.32'], ['"F"', '139', '141', '21.78', '22.22'], ['"F"', '123', '126', '19.78', '20.23'], ['"M"', '150', '152', '22.40', '22.82'], ['"M"', '150', '152', '22.76', '23.19'], ['"F"', '119', '123', '20.15', '20.69'], ['"M"', '176', '181', '22.14', '22.57'], ['"M"', '141', '145', '20.27', '20.76'], ['"F"', '126', '130', '22.15', '22.93'], ['"F"', '139', '143', '23.87', '24.67'], ['"F"', '119', '123', '18.61', '19.34'], ['"F"', '123', '128', '21.73', '22.58'], ['"M"', '119', '123', '18.93', '19.72'], ['"M"', '161', '165', '25.88', '26.72'], ['"M"', '170', '174', '28.59', '29.53'], ['"F"', '139', '145', '21.89', '22.79'], ['"F"', '112', '119', '18.31', '19.28'], ['"F"', '130', '137', '19.64', '20.63'], ['"F"', '143', '150', '23.02', '24.10'], ['"F"', '117', '123', '20.63', '21.91'], ['"F"', '137', '143', '22.61', '23.81'], ['"F"', '121', '128', '22.03', '23.42'], ['"M"', '163', '170', '20.31', '21.34'], ['"M"', '163', '172', '20.31', '21.36'], ['"M"', '141', '150', '19.59', '20.77'], ['"M"', '141', '150', '21.05', '22.31'], ['"F"', '126', '134', '23.47', '25.11'], ['"F"', '141', '150', '22.84', '24.29'], ['"F"', '132', '141', '19.50', '20.90'], ['"M"', '141', '150', '18.51', '19.83'], ['"M"', '145', '156', '21.40', '22.97'], ['"F"', '115', '126', '17.72', '19.42'], ['"M"', '156', '170', '22.26', '23.87'], ['"F"', '121', '132', '21.64', '23.81'], ['"M"', '143', '156', '22.51', '24.45'], ['"M"', '165', '181', '23.69', '25.80'], ['"F"', '93', '108', '15.08', '17.74'], ['"M"', '163', '181', '22.64', '25.33'], ['"M"', '207', '231', '36.57', '40.86']], "DataFrame 9's to_array() was not right, it should be [['M', '159', '130', '22.02', '18.14'], ['M', '214', '190', '19.70', '17.44'], ['M', '163', '152', '24.09', '22.43'], ['M', '205', '194', '26.97', '25.57'], ['F', '150', '141', '21.51', '20.10'], ['M', '130', '121', '18.69', '17.40'], ['F', '141', '132', '24.24', '22.88'], ['F', '123', '117', '21.23', '20.23'], ['F', '154', '150', '30.26', '29.24'], ['F', '128', '123', '21.88', '21.02'], ['F', '110', '104', '17.63', '16.89'], ['M', '156', '152', '24.57', '23.85'], ['M', '148', '145', '20.68', '20.15'], ['F', '123', '121', '20.97', '20.36'], ['F', '154', '150', '27.30', '26.73'], ['F', '134', '132', '23.30', '22.88'], ['F', '117', '115', '19.48', '19.24'], ['M', '203', '203', '24.74', '24.69'], ['F', '126', '128', '20.69', '20.79'], ['M', '148', '148', '20.49', '20.60'], ['F', '128', '128', '21.09', '21.24'], ['F', '108', '110', '18.37', '18.53'], ['M', '150', '150', '22.40', '22.61'], ['F', '152', '152', '28.17', '28.43'], ['M', '192', '194', '23.60', '23.81'], ['M', '179', '181', '26.52', '26.78'], ['M', '132', '134', '18.89', '19.27'], ['F', '115', '117', '19.31', '19.75'], ['M', '154', '156', '20.96', '21.32'], ['F', '139', '141', '21.78', '22.22'], ['F', '123', '126', '19.78', '20.23'], ['M', '150', '152', '22.40', '22.82'], ['M', '150', '152', '22.76', '23.19'], ['F', '119', '123', '20.15', '20.69'], ['M', '176', '181', '22.14', '22.57'], ['M', '141', '145', '20.27', '20.76'], ['F', '126', '130', '22.15', '22.93'], ['F', '139', '143', '23.87', '24.67'], ['F', '119', '123', '18.61', '19.34'], ['F', '123', '128', '21.73', '22.58'], ['M', '119', '123', '18.93', '19.72'], ['M', '161', '165', '25.88', '26.72'], ['M', '170', '174', '28.59', '29.53'], ['F', '139', '145', '21.89', '22.79'], ['F', '112', '119', '18.31', '19.28'], ['F', '130', '137', '19.64', '20.63'], ['F', '143', '150', '23.02', '24.10'], ['F', '117', '123', '20.63', '21.91'], ['F', '137', '143', '22.61', '23.81'], ['F', '121', '128', '22.03', '23.42'], ['M', '163', '170', '20.31', '21.34'], ['M', '163', '172', '20.31', '21.36'], ['M', '141', '150', '19.59', '20.77'], ['M', '141', '150', '21.05', '22.31'], ['F', '126', '134', '23.47', '25.11'], ['F', '141', '150', '22.84', '24.29'], ['F', '132', '141', '19.50', '20.90'], ['M', '141', '150', '18.51', '19.83'], ['M', '145', '156', '21.40', '22.97'], ['F', '115', '126', '17.72', '19.42'], ['M', '156', '170', '22.26', '23.87'], ['F', '121', '132', '21.64', '23.81'], ['M', '143', '156', '22.51', '24.45'], ['M', '165', '181', '23.69', '25.80'], ['F', '93', '108', '15.08', '17.74'], ['M', '163', '181', '22.64', '25.33'], ['M', '207', '231', '36.57', '40.86']], but was {}".format(df9.to_array())
print("    DataFrame 9's to_array() Passed!!!\n")

print('----------------------------------------------------------------\n')

print('ALL TESTS PASS!!!!!')
