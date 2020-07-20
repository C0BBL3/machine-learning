class Matrix():

    def __init__(self, elements=None, shape=None, fill=0):
        self.elements = elements
        self.determinant_number = 1
        self.determinant_number_recursive = 0
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

    def __matmul__(self, b):
        c = self.create_matrix(self.rows, b.cols, 0)

        for i in range(0, self.rows):
            for j in range(0, b.cols):
                for k in range(0, self.cols):
                    c.elements[i][j] += self.elements[i][k] * b.elements[k][j]

        return c

    def __eq__(self, b):
        return self.isEqual(b)

    def isEqual(self, b):
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

    def scale_row(self, rowNum):
        scalarCol = self.find_col_num_of_first_nonzero_element_in_row(rowNum)

        if scalarCol == None:
            self.determinant_number *= 0
            return self
        else:
            scalar = self.get_scalar(rowNum)
            for colNum in range(0, self.cols):
                self.elements[rowNum][colNum] /= scalar

            self.determinant_number *= scalar
            return self

    def get_scalar(self, rowNum):
        scalarCol = self.find_col_num_of_first_nonzero_element_in_row(rowNum)
        return self.elements[rowNum][scalarCol]

    def find_col_num_of_first_nonzero_element_in_row(self, rowNum):
        for colNum in range(0, self.cols):
            element = self.elements[rowNum][colNum]
            if element != 0:
                return colNum

        return None

    def clear_above(self, rowNum):
        colNum = self.find_col_num_of_first_nonzero_element_in_row(rowNum)
        if colNum == None:
            return self
        else:
            divisor = self.elements[rowNum][colNum]
            for i in range(rowNum - 1, -1, -1):
                element = self.elements[i][colNum]
                if element != 0:
                    scalar = element / divisor
                    for j in range(colNum, self.cols):
                        self.elements[i][j] -= scalar * \
                            self.elements[rowNum][j]

            return self

    def clear_below(self, rowNum):
        colNum = self.find_col_num_of_first_nonzero_element_in_row(rowNum)
        for i in range(rowNum + 1, self.rows):
            if self.elements[i][colNum] != 0:
                scalar = self.elements[i][colNum] / self.elements[rowNum][
                    colNum]
                for j in range(colNum, self.cols):
                    self.elements[i][j] -= scalar * self.elements[rowNum][j]

        return self

    def get_pivot_row(self, colNum):
        for i in self.elements:
            j = self.find_col_num_of_first_nonzero_element_in_row(
                self.elements.index(i))
            if colNum == j:
                return self.elements.index(i)
        return None

    def min(self):
        minVal = self.elements[0][0]
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                if self.elements[i][j] < minVal:
                    minVal = self.elements[i][j]

        return minVal

    def max(self):
        maxVal = self.elements[0][0]
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                if self.elements[i][j] > maxVal:
                    maxVal = self.elements[i][j]

        return maxVal

    def transpose(self):
        C = [[] for _ in range(len(self.elements[0]))]
        for x, row in enumerate(self.elements):
            for y, val in enumerate(row):
                C[y].insert(x, val)
        return Matrix(C)

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
        return Matrix(elements, (x, y))

    def create_matrix_elements(self, x, y, fill):
        elements = []
        for i in range(0, x):
            elements.append([])
            for _ in range(0, y):
                elements[i].append(fill)

        return elements

    def create_identity(self, x, y):  # x is col and y is row
        elements = self.create_identity_elements(x, y)
        return Matrix(elements, (x, y))

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
                self.determinant_number = A.determinant_number
        if return_determinant == True:
            return self.determinant_number
        return A

    def inverse(self):
        A = self.copy(self)
        #assert self.cols == self.rows, 'ERROR: Matrix is not Invertible. Please give a Invertible matrix'
        if self.cols == self.rows:
            for i in range(0, self.rows):        #
                for j in range(0, self.cols):    #
                    if i == j:                   # adding the identity as the
                        A.elements[j].append(1)  # augmented part of the matrix
                    else:                        #
                        A.elements[j].append(0)  #
            A.rows = len(A.elements)
            A.cols = len(A.elements[0])
            b = self.create_matrix(self.cols, self.rows, 0)
            A2 = A.rref()
            for i in range(0, self.rows):                   #
                # get the augmented part of the matrix
                for j in range(self.cols, 2 * self.cols):
                    b[i, j - self.cols] = round(A2[i, j], 3)
            return b
        else:
            return 'ERROR: Matrix is not Invertible. Please give a Invertible matrix'

    def inverse_by_minors(self):
        A = self.copy(self)
        big_matrix = self.copy(self)
        #assert self.cols == self.rows, 'ERROR: Matrix is not Invertible. Please give a Invertible matrix'
        if A.cols == A.rows:
            for i in range(0, A.rows):
                for j in range(0, A.cols):
                    small_matrix = A.shrink_matrix(i, j)
                    small_matrix.cols = len(small_matrix.elements[0])
                    small_matrix.rows = len(small_matrix.elements)
                    #print(small_matrix.elements)
                    #print(self.recursive_determinant(small_matrix))
                    #print(self.recursive_determinant(big_matrix))
                    if isinstance(self.recursive_determinant(small_matrix), str) and isinstance(self.recursive_determinant(big_matrix), str):
                        A.elements[i][j] = self.recursive_determinant(small_matrix) / self.recursive_determinant(big_matrix)
                A.transpose()

            return A
        else:
            return 'ERROR: Matrix is not Invertible. Please give a Invertible matrix'

    def solve(self, b):
        A = self
        for i in range(0, self.rows):  # adding the matrix b
            A.elements[i].append(b[i])  # to the end of A

        A.rref()

        for i in range(0, self.rows):  #
            # get the augmented part of the matrix and replace b with it
            for j in range(self.cols - 1, self.cols + 1):
                b[i] = A.elements[i][j]  #

        return b

    def determinant_function(self):
        return self.rref(return_determinant=True)

    def recursive_determinant(self, matrix):
        if matrix.rows == matrix.cols:
            if matrix.rows == 2 and matrix.cols == 2:
                return (matrix[0, 0] * matrix[1, 1]) - (matrix[1, 0] * matrix[0, 1])
            elif matrix.rows == 1 and matrix.cols == 1:
                return matrix[0, 0]
            else:
                for i in range(0, matrix.rows):
                    small_matrix = matrix
                    small_matrix = small_matrix.shrink_matrix(i, 0)
                    small_matrix.cols = len(small_matrix.elements[0])
                    small_matrix.rows = len(small_matrix.elements)
                    print('smol matrix', small_matrix.elements)
                    print('smol determinant',
                          self.recursive_determinant(small_matrix))
                    print(
                        'determinant', matrix[i, 0] * self.recursive_determinant(small_matrix))
                    if i % 2 != 0:
                        self.determinant_number_recursive -= matrix[i, 0] * self.recursive_determinant(
                            small_matrix)
                    else:
                        self.determinant_number_recursive += matrix[i, 0] * self.recursive_determinant(
                            small_matrix)
                return self.determinant_number_recursive

        else:
            return 'Matrix not square, please give a square matrix'

    def shrink_matrix(self, row_num, col_num):
        small_matrix = self.copy(self)
        small_matrix.elements = small_matrix.elements[:row_num] + \
            small_matrix.elements[row_num+1:]
        small_matrix.rows = len(small_matrix.elements)
        if col_num >= 1:
            for i in range(0, small_matrix.rows):
                small_matrix.elements[i] = small_matrix.elements[i][:col_num] + \
                    small_matrix.elements[i][row_num+1:]
        elif col_num == 0:
            for i in range(0, small_matrix.rows):
                small_matrix.elements[i] = small_matrix.elements[i][row_num+1:]

        return small_matrix
