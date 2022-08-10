def worldCup (self, Y: int) -> int:
    correct = False
    while not correct:
        result = Y % 4 
        if result == 2:
            correct = True
            return Y
        Y += 1
    return Y
print(worldCup(0, 3000))
def traingle(self, numRow: int) -> list[list[int]]:
    res = [[1]]

    for i in range(1, numRow):
        res.append([1] * (i + 1))
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res
    