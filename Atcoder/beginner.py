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

    for i in range(numRow -1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(1, len(temp) -1):
            row.append(temp[j-1] + temp[j])
        res.append(row)
    return res
def mmp(map: list[list[int]]) -> None:
    nums = 