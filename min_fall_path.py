def minFallingPathSum(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for r in range(n):
        for c in range(m):
            if r>0 and 0<=c-1 and c+1<m:
                matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c+1],matrix[r][c]+matrix[r-1][c-1])
            elif r>0 and c-1==-1:
                matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c+1])
            elif r>0 and c+1==m:
                matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c-1])

    return min(matrix[n-1])   

print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))

# def minFallingPathSum(matrix):
#     def helper(r, c):
#         if r == 0:
#             return matrix[0][c]

#         left = helper(r - 1, c - 1) if c - 1 >= 0 else float('inf')
#         middle = helper(r - 1, c)
#         right = helper(r - 1, c + 1) if c + 1 < len(matrix[0]) else float('inf')

#         return matrix[r][c] + min(left, middle, right)

#     n = len(matrix)
#     m = len(matrix[0])
#     return min(helper(n - 1, j) for j in range(m))

# # Example usage:
# matrix = [
#     [2, 1, 3],
#     [6, 5, 4],
#     [7, 8, 9]
# ]

# result = minFallingPathSum(matrix)
# print(result)
