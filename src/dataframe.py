from matrix_class import Matrix

class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = {}
        self.columns = column_order
        for person in self.columns:
            self.data_dict[person] = data_dict[person]

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
        new_cols = [key_1 + '_' + key_2 for j, (key_2, col_2) in enumerate(self.data_dict.items()) for i, (key_1, col_1) in enumerate(self.data_dict.items()) if j > i]
        new_cols_in_matrix = [[col_1[i] * col_2[i] for i in range(0, len(col_1))] for j, (key_2, col_2) in enumerate(self.data_dict.items()) for i, (key_1, col_1) in enumerate(self.data_dict.items()) if j > i]
        self.columns += new_cols
        for i, col in enumerate(new_cols_in_matrix): self.data_dict[self.columns[i + length_of_old_cols]] = col
        self.array = self.to_array()
        



