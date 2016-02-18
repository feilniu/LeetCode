import random

def GenerateMatrix(m, n):
    '''
    Generate an m x n matrix which has the following properties:
    * Integers in each row are sorted in ascending from left to right.
    * Integers in each column are sorted in ascending from top to bottom.
    :type m: int
    :type n: int
    :rtype: List[List[int]]
    '''
    matrix = []
    for i in range(m):
        matrix.append([0] * n)
    val = random.randrange(10)
    positions = [[0, 0]]
    for i in range(m * n):
        pos = positions.pop(random.randrange(len(positions)))
        matrix[pos[0]][pos[1]] = val
        if pos[1] + 1 < n:
            posA = [pos[0], pos[1] + 1]
            for p in positions:
                if p[0] == posA[0] and p[1] < posA[1] \
                        or p[0] < posA[0] and p[1] == posA[1]:
                            break
            else:
                positions.append(posA)
        if pos[0] + 1 < m:
            posB = [pos[0] + 1, pos[1]]
            for p in positions:
                if p[0] == posB[0] and p[1] < posB[1] \
                        or p[0] < posB[0] and p[1] == posB[1]:
                            break
            else:
                positions.append(posB)
        val += random.randint(1, 5)
    return matrix

m = GenerateMatrix(12, 16)
print(m)

