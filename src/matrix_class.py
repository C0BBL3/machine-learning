class Matrix():

    def __init__(self, elements=None, shape=None, fill=0):
        self.elements = elements
        self.determinant_number = 1
        self.determinant = 0
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

    def __add__(self, b):
        c = self.create_matrix(self.rows, self.cols, 0)

        for i in range(0, self.cols):
            for j in range(0, self.rows):
                c.elements[i][j] = self.elements[i][j] + b.elements[i][j]

        return c

    def __sub__(self, b):
        c = self.create_matrix(self.rows, self.cols, 0)

        for i in range(0, self.cols):
            for j in range(0, self.rows):
                c.elements[i][j] = self.elements[i][j] - b.elements[i][j]

        return c

    def __mul__(self, k):
        c = self.create_matrix(self.rows, self.cols, 0)

        for i in range(0, self.cols):
            for j in range(0, self.rows):
                c.elements[i][j] = k * self.elements[i][j]

        return c

    def __matmul__(self, matrix):
        c = self.create_matrix(self.rows, matrix.cols, 0)

        for i in range(0, self.rows):
            for j in range(0, matrix.cols):
                for k in range(0, self.cols):
                    c.elements[i][j] += self.elements[i][k] * matrix.elements[k][j]

        return c

    def __eq__(self, matrix):
        if self.rows == matrix.rows and self.cols == matrix.cols:
            for i in range(0, self.cols):
                for j in range(0, self.rows):
                    if self.elements[i][j] != matrix.elements[i][j]:
                        return False

    def is_equal(self, b):
        if self.rows == len(b) and self.cols == len(b):
            for i in range(0, self.cols):
                for j in range(0, self.rows):
                    if self.elements[i][j] != b[i][j]:
                        return False

        return True

    def get(self, row, col):
        return self.elements[row][col]

    def __getitem__(self, coord):
        i = coord[0]
        j = coord[1]
        if isinstance(coord[0], slice):
            row = []
            for k in range(0, self.cols):
                row.append(self.elements[k][j])
            return row
        elif isinstance(coord[1], slice):
            col = []
            for k in range(0, self.rows):
                col.append(self.elements[i][k])
            return col
        else:
            return self.elements[i][j]

    def __setitem__(self, coord, value):
        i = coord[0]
        j = coord[1]
        if isinstance(coord[0], slice):
            for k in range(0, self.cols):
                self.elements[k][j] = value[k]
            return self
        elif isinstance(coord[1], slice):
            for k in range(0, self.rows):
                self.elements[i][k] = value[k]
            return self
        else:
            self.elements[i][j] = value
            return self

    def swap_rows(self, row1Num, row2Num):
        print('row1Num', row1Num)
        print('row2Num', row2Num)
        tempRow = self.elements[row1Num]
        self.elements[row1Num] = self.elements[row2Num]
        self.elements[row2Num] = tempRow
        self.determinant_number *= -1

        return self

    def scale_row(self, row_num):
        scalar_col = self.find_col_num_of_first_nonzero_element_in_row(row_num)

        if scalar_col == None:
            self.determinant_number *= 0
            return self
        else:
            scalar = self.get_scalar(row_num)
            for col_num in range(0, self.cols):
                self.elements[row_num][col_num] /= scalar

            self.determinant_number *= scalar
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
                    self.elements[i][j] -= scalar * self.elements[row_num][j]

        return self

    def get_pivot_row(self, col_num):
        for i in self.elements:
            j = self.find_col_num_of_first_nonzero_element_in_row(
                self.elements.index(i))
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
            a = self.copy(self)
            for _ in range(0, exp - 1):
                a @= self

            return a

    def show(self):
        print(self.elements)

    def create_matrix(self, x, y, fill):
        elements = []
        for i in range(0, x):
            elements.append([])
            for _ in range(0, y):
                elements[i].append(fill)
        return Matrix(elements=elements)

    def create_matrix_elements(self, x, y, fill):
        elements = []
        for i in range(0, x):
            elements.append([])
            for _ in range(0, y):
                elements[i].append(fill)

        return elements

    def create_identity(self, x, y):  # x is col and y is row
        elements = self.create_identity_elements(x, y)
        return Matrix(elements=elements)

    def create_identity_elements(self, x, y):
        elements = []
        for i in range(0, x):
            elements.append([])
            for j in range(0, y):
                if i == j:
                    elements[i].append(1)
                else:
                    elements[i].append(0)

        return elements

    def copy(self, matrix):
        c = self.create_matrix(matrix.rows, matrix.cols, 0)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                c.elements[i][j] = self.elements[i][j]

        return c

    def rref(self, return_determinant=False):
        A = self.copy(self)  # creates a new copy matrix
        print('A', A.elements)
        for i in range(0, A.cols):  # i in range of the columns
            pivot_row = A.get_pivot_row(i)
            if pivot_row != None:
                if pivot_row != i:
                    A.swap_rows(pivot_row, i)
                    A.determinant_number *= -1
                A.scale_row(i)
                A.determinant_number *= A.get_scalar(i)
                if i != A.cols - 1:  # if not last row
                    A.clear_below(i)
                if i != 0:  # if not first row
                    A.clear_above(i)
            else:
                if return_determinant: return 0
        self.determinant_number = A.determinant_number
        if return_determinant:
            print('A.elements', A.elements)
            return self.determinant_number
        return A

    def check_if_matrix_is_invertable(self):
        print('1.01')
        self.determinant = self.determinant_function()
        if self.rows != self.cols:
            print('1.02')
            return False
        
        elif self.determinant == 0:
            print('1.03')
            return False
        
        else:
            print('1.04')
            return True

    def inverse_with_cofactors(self):
        A = self.copy(self)
        print('1')
        if self.check_if_matrix_is_invertable():
            print('1.1')
            print('self.determinant', self.determinant)
            if len(self.elements) == 2:
                return Matrix(elements=[[self.elements[1][1] / self.determinant, -1 * self.elements[0][1] / self.determinant],
                                        [-1 * self.elements[1][0] / self.determinant, self.elements[0][0] / self.determinant]])
            print('2')
            cofactors = []
            for row in range(0, self.rows):
                print('row', row)
                cofactorRow = []
                for col in range(0, self.cols):
                    print('col', col)
                    minor = A.compute_minor(row, col)
                    cofactorRow.append(
                        ((-1) ** (row + col)) * minor.determinant_function())
                cofactors.append(cofactorRow)
            cofactors = self.transpose(cofactors)
            print('5')
            for row in range(0, cofactors.rows):
                print('5', row)
                for col in range(0, cofactors.cols):
                    print('6', col)
                    cofactors[row, col] /= self.determinant
            return cofactors
        else:
            print('ERROR: Matrix is not Invertible. Please give a Invertible matrix')

    def inverse_by_minors(self):
        A = self.copy(self)
        big_matrix = self.copy(self)
        #assert self.cols == self.rows, 'ERROR: Matrix is not Invertible. Please give a Invertible matrix'
        if self.check_if_matrix_is_invertable():
            for i in range(0, A.rows):
                for j in range(0, A.cols):
                    small_matrix = A.compute_minor(i, j)
                    small_matrix.cols = len(small_matrix.elements[0])
                    small_matrix.rows = len(small_matrix.elements)
                    # print(small_matrix.elements)
                    # print(self.recursive_determinant(small_matrix))
                    # print(self.recursive_determinant(big_matrix))
                    if isinstance(self.recursive_determinant(small_matrix), str) and isinstance(self.recursive_determinant(big_matrix), str):
                        A.elements[i][j] = self.recursive_determinant(
                            small_matrix) / self.recursive_determinant(big_matrix)
                A.transpose()

            return A
        else:
            print('ERROR: Matrix is not Invertible. Please give a Invertible matrix')

    def inverse(self):
        copy_matrix = self.copy(self)
        identity_elements = self.create_identity_elements(self.cols, self.rows)
        for i, row in enumerate(copy_matrix.elements):  # adding the matrix b
            for value in identity_elements[i]:
                row.append(value)  # to the end of A

        copy_matrix.rows = len(copy_matrix.elements)
        copy_matrix.cols = len(copy_matrix.elements[0])
        solved_aug_matrix = copy_matrix.rref()

        return Matrix(elements=[row[solved_aug_matrix.cols // 2:] for row in solved_aug_matrix.elements])

    def determinant_function(self):
        if self.rows == self.cols:
            if len(self.elements) == 2:
                return (self.elements[0][0] * self.elements[1][1] - self.elements[0][1] * self.elements[1][0])
            else:
                return self.rref(return_determinant=True)
        else:
            return 'Matrix not square, please give a square matrix'
        

    def recursive_determinant(self, matrix): #correct way of doing a determinant
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

    def compute_minor(self, i, j):
        #print('minor', [row[:j] + row[j + 1:] for row in (self.elements[:i] + self.elements[i + 1:])])
        return Matrix(elements=[row[:j] + row[j + 1:] for row in (self.elements[:i] + self.elements[i + 1:])])
        
    def round(self, num_of_decimals=0):  #for tests
        A = self.copy(self)
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                A.elements[row][col] = int(round(self.elements[row][col], num_of_decimals))

        return A
