from matrix_class import Matrix

class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = {}
        self.columns = column_order
        for key in self.columns:
            self.data_dict[key] = data_dict[key]

    def to_array(self):
        self.array = [value for _, value in self.data_dict.items()]
        self.array = Matrix(elements=[[row[i] for row in self.array] for i, col in enumerate(self.array[0])]).elements
        return self.array

    def filter_columns(self, columns):
        self.data_dict = DataFrame(self.data_dict, columns).data_dict
        self.columns = [key for key, _ in self.data_dict.items()]

    def apply(self, column, function):
        self.data_dict[column] = [function(value) for value in self.data_dict[column]]

    def append_pairwise_interactions(self):
        new_cols, new_cols_in_matrix, length_of_old_cols = [], [], len(self.columns)
        for j, (key_2, col_2) in enumerate(self.data_dict.items()):
            for i, (key_1, col_1) in enumerate(self.data_dict.items()):
                if j > i:
                    new_cols.append(key_1 + '_' + key_2)
                    new_cols_in_matrix.append([col_1[i] * col_2[i] for i in range(0, len(col_1))])
        self.columns += new_cols
        for i, col in enumerate(new_cols_in_matrix): self.data_dict[self.columns[i + length_of_old_cols]] = col
        self.array = self.to_array()

    def append_columns(self, dictionary):
        for col, value in dictionary.items():
            self.columns.append(col)
            self.data_dict[col] = value

    def remove_columns(self, columns):
        self.columns = [col for col, _ in self.data_dict.items() if col not in columns]
        self.filter_columns(self.columns)

    def create_dummy_variables(self, stoopid_column):
        new_cols, rows = self.get_unique_dummy_columns(stoopid_column)
        self.remove_columns(stoopid_column)
        self.append_columns({col: rows[i] for i, col in enumerate(new_cols)})

    def get_unique_dummy_columns(self, stoopid_column):
        new_cols, rows = [], []
        for value_1 in self.data_dict[stoopid_column]:
            if str(stoopid_column) + '-' + str(value_1) not in new_cols:
                new_cols.append(str(stoopid_column) + '_' + str(value_1))
                rows.append([1 if value_1 == value_2  else 0 for value_2 in self.data_dict[stoopid_column]])

        return new_cols, rows




