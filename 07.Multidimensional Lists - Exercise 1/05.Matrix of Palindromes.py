rows, columns = [int(el) for el in input().split()]
matrix = [[[chr(97+row)+chr(97+row+col)+chr(97+row)] for col in range(columns)] for row in range(rows)]

[print(" ".join(str(*el) for el in matrix[r][0:columns])) for r in range(rows)]