def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    def recursiveSearch(up,down,left,right):
        if up > down or left > right:
            return -1
        if left == right and up == down:
            return matrix[up][left] == target
        rowMid = (up + down) // 2
        colMid = (left + right) // 2
        addingHigh = 0 if up == down else 1
        addingCol = 0 if left ==right else 1
        if matrix[rowMid][colMid] == target:
            return True
        if matrix[rowMid][colMid] > target :
            return recursiveSearch(up,rowMid-addingHigh,left,colMid-addingCol)
        else:
            return recursiveSearch(rowMid + addingHigh,down,left,colMid)
    return recursiveSearch(0,rows-1,0,cols-1)

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 26
print(searchMatrix(matrix,target))