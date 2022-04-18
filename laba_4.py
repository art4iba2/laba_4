'''
16.	Формируется матрица F следующим образом:
---если в Е минимальный элемент в нечетных столбцах в области 1 больше, чем сумма чисел в нечетных строках в области 3,
-----то поменять в В симметрично области 3 и 2 местами, иначе В и Е поменять местами несимметрично.
--При этом матрица А не меняется.
-----После чего вычисляется выражение: (К*F)*А– K*AT .
--Выводятся по мере формирования А, F и все матричные операции
'''

import numpy as np
import time

def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()


try :
    N = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while N < 6 or N > 100:
        N = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()

    Obl1, Obl3, = [], []    #задаю необходимые величины
    A, F, AF, AT = [], [], [], []
    ###################################################
    for i in range(N):
        A.append([0]*N)
        F.append([0] * N)
        AF.append([0]*N)
        AT.append([0]*N)
    for i in range(N):      # заполняем матрицу А
        for j in range(N):
            ###A[i][j] = np.random.randint(0,10)
            if i<j and j < N-1-i:
                A[i][j] = 1
            elif i<j and j > N-1-i:
                A[i][j] = 2
            elif i>j and j > N-1-i:
                A[i][j] = 3
            elif i>j and j < N-1-i:
                A[i][j] = 4

    time_next = time.time()
    print_matrix(F,"F",time_next-start)

    ###################################################
    n1 = int(N / 2) #размерность подматрицы

    time_prev = time_next
    time_next = time.time()
    for i in range(N):
        for j in range(N):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F,"F",time_next-time_prev)

    E = []  #формируем подматрицу E
    for i in range(n1):
        E.append([0] * n1)
    time_prev = time_next
    time_next = time.time()
    for i in range(n1):
        for j in range(n1):
            E[i][j] = F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(E, "E", time_next - time_prev)
    #################
    for i in range(n1):   # обрабатываем матрицу E
        for j in range(n1):
            if i < j and j < n1 - 1 - i and j % 2 == 0:
                Obl1.append(E[i][j])
    minima = min(Obl1)
    print(Obl1)
    print("Минимальный элемент в 1ой области в нечетных столбцах = ", minima)
    ###################
    for i in range(n1):   # обрабатываем матрицу E
        for j in range(n1):
            if i > j and j > n1 - 1 - i and i % 2 == 0:
                Obl3.append(E[i][j])
    summ = np.sum(Obl3)
    print(Obl3)
    print("Сумма элементов в 3ей области в нечетных строках = ", summ)

    B = []   #формируем подматрицу B
    for i in range(n1):
        B.append([0] * n1)
    time_prev = time_next
    time_next = time.time()
    for i in range(n1):
        for j in range(n1):
            B[i][j] = F[i][j + n1 + N % 2]
    time_prev = time_next
    time_next = time.time()
    print_matrix(B, "B", time_next - time_prev)


    if minima > summ:  #если минимальный элемент > суммы элементов

        for i in range(n1):   #меняем области 2 и 3 местами
            for j in range (n1):
                if j > n1-i-1:
                 F[j][i+n1] , B[i][j] = B[i][j] , F[j][i+n1]

        print_matrix(B,"B",time_next-time_prev)
        for i in range(n1):      # формируем матрицу F
            for j in range(n1):
                F[i][j+n1] = B[i][j]
    else:
       for i in range(N//2):  #меняем подматрицы B и E
            for j in range(N//2):
                F[i][j], F[i][N//2 + j] = F[i][N//2+j], F[i][j]


    time_prev = time_next
    time_next = time.time()
    print_matrix(F,"F",time_next-time_prev)
    print_matrix(A, "A", 0)
    print("\n")

    for i in range(N):      # K*F
        for j in range(N):
            F[i][j] = K*F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F,"K*F",time_next-time_prev)

    ###################################################

    for i in range(N):           # K*F*A
        for j in range(N):
            for p in range(N):
                AF[i][j] += F[i][p] * A[p][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF,"K*F*A",time_next-time_prev)

    ###################################################
    for i in range(N):      # AT
        for j in range(i,N,1):
            AT[i][j],AT[j][i] = F[j][i],F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT,"A^T",time_next-time_prev)
    ###################################################
    for i in range(N):      # K*AT
        for j in range(N):
            AT[i][j] = K*AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT,"K*AT",time_next-time_prev)

    ###################################################
    for i in range(N):  # (K*F)*A-K*AT
        for j in range(N):
            AF[i][j] = AF[i][j] - AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "(K*F)*A-K*A^T", time_next - time_prev)

    ###################################################
    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")
    ###################################################
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")


