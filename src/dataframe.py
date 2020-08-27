from matrix_class import Matrix

class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = {}
        self.columns = column_order
        for person in self.columns:
            self.data_dict[person] = data_dict[person]

    def to_array(self):
        self.array = []
        for _, value in self.data_dict.items():
            self.array.append(value)
        mat = Matrix(elements=self.array)
        self.array = mat.transpose().elements
        return self.array

    def filter_columns(self, columns):
        self.columns = columns
        self.array = []
        data_dict = self.data_dict
        self.data_dict = {}
        for person in columns:
            self.data_dict[person] = data_dict[person]
            self.array.append([self.data_dict[person]])
        mat = Matrix(elements=self.array)
        self.array = mat.transpose().elements



