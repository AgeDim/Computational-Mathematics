swapping = 1

def getTriangularMatrix(matrix, size):
    triangularMatrix = matrix
    global swapping
    for indexCurrentString in range(size):
        triangularMatrix = columnSwapping(triangularMatrix, indexCurrentString, size)
        triangularMatrix = zeroingColumn(triangularMatrix, indexCurrentString, size)
    determinant = findDeterminant(triangularMatrix, size) * swapping
    return triangularMatrix


def columnSwapping(matrix, numberString, matrixSize):
    returnMatrix = matrix
    tmpNumberString = numberString
    firstElement = matrix[numberString][numberString]
    if firstElement == 0:
        while firstElement == 0 and tmpNumberString != matrixSize - 1:
            tmpString = matrix[numberString]
            matrix[numberString] = matrix[tmpNumberString + 1]
            matrix[tmpNumberString + 1] = tmpString
            firstElement = returnMatrix[numberString][numberString]
            tmpNumberString += 1
            global swapping
            swapping = swapping * (-1)
    return returnMatrix


def zeroingColumn(matrix, numberColumn, matrixSize):
    resultMatrix = matrix
    for i in range(numberColumn + 1, matrixSize):
        if matrix[numberColumn][numberColumn] == 0:
            break
        coefficient = (-1) * matrix[i][numberColumn] / matrix[numberColumn][numberColumn]
        for j in range(matrixSize+1):
            resultMatrix[i][j] = resultMatrix[i][j] + matrix[numberColumn][j] * coefficient
    return resultMatrix


def findDeterminant(matrix, size):
    det = 1
    for i in range(size):
        det = det * matrix[i][i]
    return det

