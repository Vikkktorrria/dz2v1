def game(x: int, y: int, mylist: list, alive_or_dead: int):  # реализация самого алгоритма игры
    count_dead = 0
    count_alive = 0

    for _x in range(3):
        for _y in range(3):
            if mylist[x + (_x - 1)][y + (_y - 1)] == 1:
                count_alive += 1
            else:
                count_dead += 1

    if alive_or_dead == 1:  # если клетка изначально живая
        count_alive -= 1  # отняли значение, потому что в цикле посчитали ещё и саму клетку
        if count_alive < 2 or count_alive > 3:  # при этих условиях она умирает
            alive_or_dead = 0
    else:  # если клетка изначально мёртвая
        count_dead -= 1
        if count_alive == 3:  # при этих условиях она оживает
            alive_or_dead = 1

    return alive_or_dead

    pass


def neighbors(file_field1, temp_field1, field_cols1, field_rows1, temp_field_cols1, temp_field_rows1):  # поиск соседей

    for i in range(temp_field_cols1):
        for j in range(temp_field_rows1):
            temp_field1[i][j] = 0  # заполняю вспомогательное поле нулями

    temp_field1[0][0] = file_field[field_cols1 - 1][field_rows1 - 1]  # соседство у угловых элементов
    temp_field1[temp_field_cols1 - 1][0] = file_field1[0][field_rows1 - 1]
    temp_field1[0][temp_field_rows1 - 1] = file_field1[field_cols1 - 1][0]
    temp_field1[temp_field_cols1 - 1][temp_field_rows1 - 1] = file_field1[0][0]

    for i in range(field_cols1):
        for j in range(field_rows1):
            temp_field1[i + 1][j + 1] = file_field1[i][j]  # вписываю исходное поле в вспомогательное

    for i in range(field_cols1):  # добавляю соседей крайним клеткам
        for j in range(field_rows1):
            temp_field1[0][j + 1] = file_field1[field_cols1 - 1][j]
            temp_field1[temp_field_cols1 - 1][j + 1] = file_field1[0][j]
            temp_field1[i + 1][0] = file_field1[i][field_rows1 - 1]
            temp_field1[i + 1][temp_field_rows1 - 1] = file_field1[i][0]

    return temp_field1

    pass


with open('input.txt', 'r') as file:
    file_field = file.readlines()
gen_number = int(file_field[0])  # номер поколения, которое нужно вывести
del file_field[0]
file_field = [[int(elem) for elem in x.split()] for x in file_field]

print("\nИзначальное поле:")
for i in range(len(file_field)):
    print(" ", end="")
    for j in range(len(file_field[i])):
        print(file_field[i][j], end=' ')
    print(" ")

new_field = file_field  # создала новое временное поле, чтобы изменять его

# размерность заданного поля (можно вводить не только квадратные метрицы)
field_cols = len(file_field)
field_rows = len(file_field[0])

# размерность временного поля (оно нужно, чтобы удобно проверять соседей)
temp_field_cols = field_cols + 2
temp_field_rows = field_rows + 2

temp_field = [[0 for j in range(temp_field_rows)] for i in range(temp_field_cols)]
for i in range(temp_field_cols):
    for j in range(temp_field_rows):
        temp_field[i][j] = 0
""" пока заполнено нулями, в дальнейшем в него будет вписываться исходная матрица, а также соседи крайних значений """


while gen_number > 1:  # делаем m-1 ходов (т.к. исходная матрица - первое поколение)

    temp_field = neighbors(new_field, temp_field, field_cols, field_rows, temp_field_cols, temp_field_rows)
    gen_number -= 1
    for i in range(field_cols):
        for j in range(field_rows):
            if game(i + 1, j + 1, temp_field, temp_field[i + 1][j + 1]) == 1:
                new_field[i][j] = 1

            else:
                new_field[i][j] = 0


file_field = new_field

print("\nПолученная матрица:", )
for i in range(len(file_field)):
    print(" ", end="")
    for j in range(len(file_field[i])):
        print(file_field[i][j], end=' ')
    print(" ")

with open("output.txt", "w") as file:
    file.write('\n'.join(' '.join(str(j) for j in i) for i in file_field))
