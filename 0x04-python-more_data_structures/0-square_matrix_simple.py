#!/usb/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for row in matrix:
        sub = []
        for e in row:
            sub.append(e ** 2)
        square.append(sub)
    return square
