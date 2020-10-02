class Matrix():

    def __init__(self, elements=None, shape=None, fill=0):
        self.elements = elements
        self.determinant_number = 1
        if self.elements == None and shape != None:
            if fill == 'diag':
                self.elements = self.create_identity_elements(
                    shape[0], shape[1])
            else:
                self.elements = self.create_matrix_elements(
                    shape[0], shape[1], fill)
        else:
            self.elements = elements

        self.cols = len(self.elements[0])
        self.rows = len(self.elements)
        self.shape = shape

    #-------------------------------------------------------Main Functions-------------------------------------------------------

    def rref(self, return_determinant=False):
        self.determinant_number = 1
        copy_matrix = self.copy(self)  # creates a new copy matrix
        for i in range(0, copy_matrix.cols):  # i in range of the columns
            pivot_row = copy_matrix.get_pivot_row(i)
            if pivot_row != None:
                if pivot_row != i:
                    copy_matrix.swap_rows(pivot_row, i)
                    copy_matrix.determinant_number *= -1
                copy_matrix.scale_row(i)
                copy_matrix.determinant_number *= copy_matrix.get_scalar(i)
                if i != copy_matrix.cols - 1:  # if not last row
                    copy_matrix.clear_below(i)
                if i != 0:  # if not first row
                    copy_matrix.clear_above(i)
            else:
                if return_determinant:
                    return 0
        self.determinant_number = copy_matrix.determinant_number
        if return_determinant:
            return self.determinant_number
        return copy_matrix

    def inverse(self):
        copy_matrix = self.copy(self)
        identity_elements = self.create_identity_elements(self.cols, self.rows)
        for i, row in enumerate(copy_matrix.elements):
            for value in identity_elements[i]:
                row.append(value)

        copy_matrix.rows = len(copy_matrix.elements)
        copy_matrix.cols = len(copy_matrix.elements[0])
        solved_aug_matrix = copy_matrix.rref()

        return Matrix(elements=[row[solved_aug_matrix.cols // 2:] for row in solved_aug_matrix.elements])

    def determinant(self):
        if self.rows == self.cols:
            if len(self.elements) == 2:
                return (self.elements[0][0] * self.elements[1][1] - self.elements[0][1] * self.elements[1][0])
            else:
                return self.rref(return_determinant=True)
        else:
            return 'Matrix not square, please give a square matrix'

    #------------------------------------------------------create matrices-------------------------------------------------------

    def create_matrix(self, x, y, fill_value = 0):
        return Matrix(elements=self.create_matrix_elements(x, y, fill_value))

    def create_matrix_elements(self, x, y, fill_value = 0):
        return [[fill_value for j in range(0, y)] for i in range(0, x)]

    def create_identity(self, x, y):  # x is col and y is row
        return Matrix(elements=self.create_identity_elements(x, y))

    def create_identity_elements(self, x, y):
        return [[1 if i == j else 0 for j in range(0, y)] for i in range(0, x)]

    #-----------------------------------------------------Overload functions-----------------------------------------------------

    def __add__(self, second_matrix):
        new_matrix = self.create_matrix(self.rows, self.cols, 0)

        for i in range(0, self.cols):
            for j in range(0, self.rows):
                new_matrix.elements[i][j] = self.elements[i][j] + \
                    second_matrix.elements[i][j]

        return new_matrix

    def __sub__(self, second_matrix):
        new_matrix = self.create_matrix(self.rows, self.cols, 0)

        for i in range(0, self.cols):
            for j in range(0, self.rows):
                new_matrix.elements[i][j] = self.elements[i][j] - \
                    second_matrix.elements[i][j]

        return new_matrix

    def __mul__(self, scalar):
        new_matrix = self.create_matrix(self.rows, self.cols, 0)

        for i in range(0, self.cols):
            for j in range(0, self.rows):
                new_matrix.elements[i][j] = scalar * self.elements[i][j]

        return new_matrix

    def __matmul__(self, second_matrix):
        new_matrix = self.create_matrix(self.rows, second_matrix.cols, 0)

        for i in range(0, self.rows):
            for j in range(0, second_matrix.cols):
                for k in range(0, self.cols):
                    new_matrix.elements[i][j] += self.elements[i][k] * \
                        second_matrix.elements[k][j]

        return new_matrix

    def __eq__(self, second_matrix):
        if self.rows == second_matrix.rows and self.cols == second_matrix.cols:
            for i in range(0, self.cols):
                for j in range(0, self.rows):
                    if self.elements[i][j] != second_matrix.elements[i][j]:
                        return False
            return True
        else:
            return False

    def __getitem__(self, coords):
        row = coords[0]
        col = coords[1]
        if isinstance(coords[0], slice):
            row = []
            for k in range(0, self.cols):
                row.append(self.elements[k][col])
            return row
        elif isinstance(coords[1], slice):
            col = []
            for k in range(0, self.rows):
                col.append(self.elements[row][k])
            return col
        else:
            return self.elements[row][col]

    def __setitem__(self, coords, value):
        row = coords[0]
        col = coords[1]
        if isinstance(coords[0], slice):
            for k in range(0, self.cols):
                self.elements[k][col] = value[k]
            return self
        elif isinstance(coords[1], slice):
            for k in range(0, self.rows):
                self.elements[row][k] = value[k]
            return self
        else:
            self.elements[row][col] = value
            return self

    #------------------------------------------------------Helper Functions------------------------------------------------------

    def check_if_matrix_is_invertable(self):
        self.determinant_number = self.determinant()
        if self.rows != self.cols:
            return False

        elif self.determinant == 0:
            return False

        else:
            return True

    def get(self, row, col):
        return self.elements[row][col]

    def swap_rows(self, row_1_Num, row_2_Num):
        copy_matrix = self.copy(self)
        copy_matrix.elements[row_1_Num], copy_matrix.elements[row_2_Num] = copy_matrix.elements[row_2_Num], copy_matrix.elements[row_1_Num]

        return copy_matrix

    def scale_row(self, row_num):
        scalar_col = self.find_col_num_of_first_nonzero_element_in_row(row_num)

        if scalar_col == None:
            return self
        else:
            scalar = self.get_scalar(row_num)
            for col_num in range(0, self.cols):
                self.elements[row_num][col_num] /= scalar

            return self

    def get_scalar(self, row_num):
        scalar_col = self.find_col_num_of_first_nonzero_element_in_row(row_num)
        return self.elements[row_num][scalar_col]

    def find_col_num_of_first_nonzero_element_in_row(self, row_num):
        for col_num in range(0, self.cols):
            element = self.elements[row_num][col_num]
            if element != 0:
                return col_num

        return None

    def clear_above(self, row_num):
        col_num = self.find_col_num_of_first_nonzero_element_in_row(row_num)
        if col_num == None:
            return self
        else:
            divisor = self.elements[row_num][col_num]
            for i in range(row_num - 1, -1, -1):
                element = self.elements[i][col_num]
                if element != 0:
                    scalar = element / divisor
                    for j in range(col_num, self.cols):
                        self.elements[i][j] -= scalar * \
                            self.elements[row_num][j]

            return self

    def clear_below(self, row_num):
        col_num = self.find_col_num_of_first_nonzero_element_in_row(row_num)
        for i in range(row_num + 1, self.rows):
            if self.elements[i][col_num] != 0:
                scalar = self.elements[i][col_num] / self.elements[row_num][
                    col_num]
                for j in range(col_num, self.cols):
                    self.elements[i][j] -= scalar * \
                        self.elements[row_num][j]

        return self

    def get_pivot_row(self, col_num):
        for i in self.elements:
            j = self.find_col_num_of_first_nonzero_element_in_row(self.elements.index(i))
            if col_num == j:
                return self.elements.index(i)
        return None

    def min(self):
        min_val = self.elements[0][0]
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                if self.elements[i][j] < min_val:
                    min_val = self.elements[i][j]

        return min_val

    def max(self):
        max_val = self.elements[0][0]
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                if self.elements[i][j] > max_val:
                    max_val = self.elements[i][j]

        return max_val

    def transpose(self, arr=None):
        if arr == None:
            return Matrix(elements=[[row[i] for row in self.elements] for i in range(len(self.elements[0]))])
        else:
            return Matrix(elements=[[row[i] for row in arr] for i in range(len(arr[0]))])

    def exponent(self, exp):
        if exp == 0:
            return self.create_identity(self.rows, self.cols)
        else:
            copy_matrix = self.copy(self)
            for _ in range(0, exp - 1):
                copy_matrix @= self

            return copy_matrix

    def show(self):
        for row in self.elements:
            print(row)

    def copy(self, matrix):
        return Matrix(elements=[[value for value in row] for row in self.elements])

    def compute_minor(self, i, j):
        return Matrix(elements=[row[:j] + row[j + 1:] for row in (self.elements[:i] + self.elements[i + 1:])])

    def round(self, num_of_decimals=0):  # for tests
        A = self.copy(self)
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                A.elements[row][col] = int(
                    round(self.elements[row][col], num_of_decimals))

        return A

    #--------------------------------------------------obsolete (slow) functions-------------------------------------------------

    def inverse_with_cofactors(self):  # slow af but accurate
        A = self.copy(self)
        if self.check_if_matrix_is_invertable():
            if len(self.elements) == 2:
                return Matrix(elements=[[self.elements[1][1] / self.determinant_number, -1 * self.elements[0][1] / self.determinant_number],
                                        [-1 * self.elements[1][0] / self.determinant_number, self.elements[0][0] / self.determinant_number]])
            print('2')
            cofactors = []
            for row in range(0, self.rows):
                print('row', row)
                cofactorRow = []
                for col in range(0, self.cols):
                    print('col', col)
                    minor = A.compute_minor(row, col)
                    cofactorRow.append(
                        ((-1) ** (row + col)) * minor.determinant())
                cofactors.append(cofactorRow)
            cofactors = self.transpose(cofactors)
            print('5')
            for row in range(0, cofactors.rows):
                print('5', row)
                for col in range(0, cofactors.cols):
                    print('6', col)
                    cofactors[row, col] /= self.determinant_number
            return cofactors
        else:
            print('ERROR: Matrix is not Invertible. Please give a Invertible matrix')

    def inverse_by_minors(self):  # tiny bit faster but still slow and not 100% accurate
        A = self.copy(self)
        big_matrix = self.copy(self)
        #assert self.cols == self.rows, 'ERROR: Matrix is not Invertible. Please give a Invertible matrix'
        if self.check_if_matrix_is_invertable():
            for i in range(0, A.rows):
                for j in range(0, A.cols):
                    small_matrix = A.compute_minor(i, j)
                    small_matrix.cols = len(small_matrix.elements[0])
                    small_matrix.rows = len(small_matrix.elements)
                    if isinstance(small_matrix.determinant(), str) and isinstance(big_matrix.determinant(), str):
                        A.elements[i][j] = small_matrix.determinant(
                        ) / big_matrix.determinant()
                A.transpose()

            return A
        else:
            print('ERROR: Matrix is not Invertible. Please give a Invertible matrix')

    # slow way of doing a determinant but is accurate
    def recursive_determinant(self, matrix):
        #print('matrix.elements', matrix.elements)
        if matrix.rows == matrix.cols:
            if len(matrix.elements) == 2:
                return (matrix.elements[0][0] * matrix.elements[1][1] - matrix.elements[0][1] * matrix.elements[1][0])
            elif len(matrix.elements) > 2:
                determinant = 0

                for c in range(len(matrix.elements)):
                    determinant += ((-1.0) ** c) * matrix.elements[0][c] * self.recursive_determinant(
                        matrix.compute_minor(0, c))

                return determinant

        else:
            return 'Matrix not square, please give a square matrix'
