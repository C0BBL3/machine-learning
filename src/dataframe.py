from matrix import Matrix

class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = {}
        self.columns = column_order
        for key in self.columns:
            self.data_dict[key] = data_dict[key]
        self.last_base_column_index = len(column_order)

    def to_array(self):
        return [list(row) for row in zip(*[self.data_dict[col] for col in self.columns])]

    @staticmethod
    def from_array(array, columns): 
        return DataFrame(dict(zip(columns, [[row[i] for row in array] for i, _ in enumerate(array[0])])), columns)

    def filter_columns(self, columns):
        self.data_dict = DataFrame(self.data_dict, columns).data_dict
        self.columns = [key for key, _ in self.data_dict.items()]

    def select_columns(self, columns): 
        return DataFrame(self.data_dict, columns)

    def select_rows(self, indices):
        return self.from_array([DataFrame(self.data_dict, self.columns).to_array()[i] for i in indices], self.columns)

    def select_rows_where(self, lambda_function):
        return self.select_rows([i for i in range(len(self.to_array()[0])) if lambda_function({column: value[i] for column, value in self.data_dict.items()})])

    def order_by(self, column, ascending):
        return self.select_rows(self.get_sorted_indicies(column, ascending))

    def get_sorted_indicies(self, column, ascending):
        return [self.data_dict[column].index(row) for row in self.quick_sort(self.data_dict[column], ascending)]

    def quick_sort(self, arr, ascending):
        copy_arr, sorted_arr = [value for value in arr], []
        while len(copy_arr) > 0:
            sorted_arr.append(min(copy_arr))
            copy_arr.remove(min(copy_arr))
        if ascending: return sorted_arr
        else: return sorted_arr[::-1]

    def apply(self, column, function): 
        self.data_dict[column] = [function(value) for value in self.data_dict[column]]

    def append_pairwise_interactions(self):
        new_cols, new_cols_in_matrix, length_of_old_cols = [], [], len(self.columns)
        cartesian = self.cartesian_product([self.columns, self.columns])
        for keys in cartesian:
            new_cols.append('_'.join(keys))
            new_cols_in_matrix.append([value_1 * value_2 for value_1, value_2 in zip(self.data_dict[keys[0]], self.data_dict[keys[1]])])
        self.columns += new_cols
        for i, col in enumerate(new_cols_in_matrix): self.data_dict[self.columns[i + length_of_old_cols]] = col
        self.array = self.to_array()

    def next_set_of_combos(self, current_arr, next_arr): #ex current_arr = [a] next_arr = [1,2,3] then next_set_of_combos(current_arr, next_arr) would return [[a,1], [a,2], [a,3]]
        result = [] 
        for col_1 in current_arr: 
            for col_2 in next_arr:
                if [col_1, col_2] not in result and [col_2, col_1] not in result and col_1 != col_2:
                    result.append([col_1, col_2])
        return result 
  
    def cartesian_product(self, arrays):
        result, current_arr = [arrays[0]], arrays[0]
        for arr in arrays[1:]: 
            current_arr = self.next_set_of_combos(current_arr, arr)
            result.append(current_arr)
        return result[-1]

    def append_columns(self, dictionary):
        for key, values in dictionary.items():
            self.columns.append(key)
            self.data_dict[key] = values

    def remove_columns(self, columns):
        self.columns = [col for col, _ in self.data_dict.items() if col not in columns]
        self.filter_columns(self.columns)

    def create_dummy_variables(self, dumb_column):
        new_cols, rows = self.get_unique_dummy_columns(dumb_column)
        self.remove_columns(dumb_column)
        self.append_columns({col: [row[i] for row in rows] for i, col in enumerate(new_cols)})

    def get_unique_dummy_columns(self, dumb_column):
        new_cols, rows = [], []
        if isinstance(self.data_dict[dumb_column][0], list):
            longest_list = self.get_longest_list(dumb_column)
            for list_1 in longest_list:
                if list_1 != [] and list_1 not in new_cols:
                    new_cols.append(list_1)
            for list_2 in self.data_dict[dumb_column]:
                rows.append([1 if value in list_2 else 0 for value in longest_list])
            return new_cols, rows
        else:
            for value_1 in self.data_dict[dumb_column]:
                if str(dumb_column) + '-' + str(value_1) not in new_cols:
                    new_cols.append(str(dumb_column) + '_' + str(value_1))
                    rows.append([1 if value_1 == value_2  else 0 for value_2 in self.data_dict[dumb_column]])
            return new_cols, rows

    def get_longest_list(self, dumb_column):
        longest_list = []
        for list_1 in self.data_dict[dumb_column]:
            if len(list_1) > len(longest_list):
                longest_list = list_1
        return longest_list

    
