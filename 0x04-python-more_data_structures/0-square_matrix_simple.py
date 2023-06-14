#!/usb/bin/python3
def square_matrix_simple(matrix=[]):
    sq = lambda x : x ** 2 
    square = []
    for row in matrix:
        square.append(map(sq, matrix))
    return square

