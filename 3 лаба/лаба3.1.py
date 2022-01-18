import random

def CreateTwoMatrix():
    global M1
    global M2
    global N1
    global N2
    M1 = []
    M2 = []
    N1 = int(input("Введите размер 1 матрицы (а*а): "))
    N2 = int(input("Введите размер 2 матрицы (b*b): "))
    chance = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    # Шанс 1 - 70%
    # Шанс 0 - 30%

    # Создание 2 матриц смежности неориентированных помеченных графов
    # № 1
    for i in range(N1):
        M1.append([])
        for j in range(N1):
            M1[i].append(random.choice(chance))
            if (i == j):
                M1[i][j] = 0

    for i in range(N1):
        for j in range(N1):
            M1[i][j] = M1[j][i]
            print(M1[i][j], end='\t')
        print('\n')
    print('\n' * 3)
    # № 2

    for i in range(N2):
        M2.append([])
        for j in range(N2):
            M2[i].append(random.choice(chance))
            if (i == j):
                M2[i][j] = 0

    for i in range(N2):
        for j in range(N2):
            M2[i][j] = M2[j][i]
            print(M2[i][j], end='\t')
        print('\n')
    print('\n' * 3)


CreateTwoMatrix()
# Преобразование в список смежности
List_S1 = []
print("Первый список смежности:\n")
for i in range(N1):
    List_S1.append([])
    for j in range(N1):
        if (M1[i][j] == 1):
            List_S1[i].append(j + 1)

for i in range(N1):
    print(i + 1, ' -- ', end='')
    for j in range(len(List_S1[i])):
        print(List_S1[i][j], end=' ')
    print('\n')
print("\n" * 2)
List_S2 = []
print("Второй список смежности:\n")
for i in range(N2):
    List_S2.append([])
    for j in range(N2):
        if (M2[i][j] == 1):
            List_S2[i].append(j + 1)

for i in range(N2):
    print(i + 1, ' -- ', end='')
    for j in range(len(List_S2[i])):
        print(List_S2[i][j], end=' ')
    print('\n')
print('\n' * 3)

M11 = M1.copy()
M22 = M2.copy()
