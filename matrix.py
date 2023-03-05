class SquareMatrix:
    def __init__(self, size_of_matrix, matrix_data):
        self.type_of_matrix = 'Square Matrix'
        self.size_of_matrix = size_of_matrix

        numbers = str.split(matrix_data, ' ')
        tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
        k = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                tmp_matrix[i][j] = int(numbers[k])
                k += 1
        self.matrix_data = tmp_matrix

    def __str__(self):
        return f'Type of Matrix = {self.type_of_matrix}; ' \
               f'Size of Matrix = {self.size_of_matrix}; ' \
               f'Matrix Data = {self.matrix_data}\n'


class SquareDiagonalMatrix:
    def __init__(self, size_of_matrix, matrix_data):
        self.type_of_matrix = 'Square Diagonal Matrix'
        self.size_of_matrix = size_of_matrix
        numbers = str.split(matrix_data, ' ')
        tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
        k = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                if i == j:
                    tmp_matrix[i][j] = int(numbers[k])
                    k += 1
        self.matrix_data = tmp_matrix

    def __str__(self):
        return f'Type of Matrix = {self.type_of_matrix}; ' \
               f'Size of Matrix = {self.size_of_matrix}; ' \
               f'Matrix Data = {self.matrix_data}\n'

# class Matrix:
#     def __init__(self, type_of_matrix, size_of_matrix, matrix_data):
#         self.type_of_matrix = type_of_matrix
#         self.size_of_matrix = size_of_matrix
#
#         if self.type_of_matrix == 1:
#             numbers = str.split(matrix_data, ' ')
#             tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
#             k = 0
#             for i in range(self.size_of_matrix):
#                 for j in range(self.size_of_matrix):
#                     tmp_matrix[i][j] = int(numbers[k])
#                     k += 1
#             self.matrix_data = tmp_matrix
#
#         elif self.type_of_matrix == 2:
#             numbers = str.split(matrix_data, ' ')
#             tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
#             k = 0
#             for i in range(self.size_of_matrix):
#                 for j in range(self.size_of_matrix):
#                     if i == j:
#                         tmp_matrix[i][j] = int(numbers[k])
#                         k += 1
#             self.matrix_data = tmp_matrix
#
#         else:
#             self.matrix_data = []


# def __str__(self):
#     return f'Type of Matrix = {self.type_of_matrix} ' \
#            f'Size of Matrix = {self.size_of_matrix} ' \
#            f'Matrix Data = {self.matrix_data}\n'