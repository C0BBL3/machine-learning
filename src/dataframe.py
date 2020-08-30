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
        



