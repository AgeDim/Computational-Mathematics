def getResult(matrix, size):
    result = [0] * size
    for i in range(size):
        result[size - i - 1] = helpResult(matrix, size, result, size - i - 1)
    return result


def helpResult(matrix, size, result, i):
    res = matrix[i][size]
    for k in range(size):
        if k != i:
            res = res - matrix[i][k] * result[k]
    res = res / matrix[i][i]
    return res
