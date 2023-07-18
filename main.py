class RotateMatrics:
    def rotate(self, array, rows, column):
        new_array = [[0 for _ in range(rows)] for _ in range(column)]
        for i in range(rows):
            for j in range(column):
                new_array[j][i] = array[i][j]

        for i in range(rows):
            for j in range(column):
                new_array[j][i] = array[i][j]

        c = rows-1
        for i in range(rows):
            array[i] = new_array[c]
            c -= 1

        return array

rows = int(input())
column = int(input())
array = []

for i in range(rows):
    a = list(map(int, (input().split())))
    array.append(a)

object = RotateMatrics()
print(object.rotate(array, rows, column))
