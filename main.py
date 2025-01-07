from collections import deque
import random
import time
import os
import cv2
def bfs_find_max(matrix, start):
    """
    Выполняет поиск в ширину (BFS) по матрице из заданной точки и находит максимальное число.

    :param matrix: Список списков (матрица) чисел
    :param start: Кортеж (x, y) с начальными индексами
    :return: Максимальное число, найденное в процессе обхода
    """
    rows, cols = len(matrix), len(matrix[0])
    index_max_value = [list(start)]

    # Направления движения: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Очередь для BFS
    queue = deque([start])
    visited = set()
    visited.add(start)

    # Инициализация максимального значения
    max_value = matrix[start[0]][start[1]]
    while queue:
        current_x, current_y = queue.popleft()

        # Обновляем максимальное значение
        if max_value < matrix[current_x][current_y]:
            max_value = matrix[current_x][current_y]
            index_max_value = [[current_x,current_y]]

        elif max_value == matrix[current_x][current_y]:
            distanse = (abs (start[0] -current_x) + abs (start[1] - current_y) -
                        abs (start[0] - index_max_value[0][0]) + abs ( start[1]- index_max_value[0][1]))
            if distanse == 0:
                index_max_value.append([current_x,current_y])
            elif distanse < 0:
                index_max_value=[[current_x,current_y]]

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    #Выбираем рандомное ближайшее место
    index_result = random.choice(index_max_value)
    matrix[index_result[0]] [index_result[1]] = -1
    return [index_result,max_value]

def print_info(matrix):
    os.system('cls')
    for i in range(len(matrix)):
        print('|',end='')
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 0):
                print("   " , end='|')
            elif (matrix[i][j] == -1):
                print("###",end='|')
            else:
                print(matrix[i][j],end='|')
        print()
    #time.sleep(0.5)



def start_game(value, countpeople, matrix, start_index, start):

    while value > 0:
        enter = [0,1,2]
        for j in range (3):
            i = random.choice(enter)
            enter.remove(i)
            countpeople[i] -= 1
            if countpeople[i] >= 0:
                index, maxvalue = (bfs_find_max(matrix, start[i]))
                if maxvalue>0:
                    #print(index, maxvalue)
                    print_info(matrix)
                    if (start_index == i):
                        value-=1
                        if (value==0):
                            print(index,maxvalue)
                            return True, value
                else:
                    print("Мест нет")
                    return False, value

def init ():
    # Считываем массив из файла
    '''matrix =[[0  , 1  , 0.9, 1  , 0.3, 0.1, 0.3, 1  , 0.8, 0.9, 0.9, 0.8, 1  , 0.3, 0.1, 0.3, 1  , 0.8, 0.9, 0.9, 0.8, 1  , 0.3, 0.1, 0.3, 1  , 0.9, 1  , 0  ],
                [0.5, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.5],
                [0  , 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0  ],
                [0  , 1  , 0.9, 1  , 0.5, 0.4, 0.5, 1  , 0.8, 0.9, 0.9, 0.8, 1  , 0.5, 0.4, 0.5, 1  , 0.8, 0.9, 0.9, 0.8, 1  , 0.4, 0.5, 0.4, 1  , 0.9, 1  , 0  ]]'''
    with open("Train.txt") as file:
        matrix = []
        for i in range(4):
            matrix.append(list(map(float, file.readline().split(','))))
    return matrix

def main ():
    start = [(0,5),(0,14), (0,23)]

    flag = False
    #Ввод и проверка данных
    while flag == False:
        countpeople = list(map(int,input("Введите через 'Пробел' 3 числа, сколько людей стоят у каждой двери ").split()))
        start_index =int(input("Введите номер входа в вагон ")) - 1
        value=int(input("Введите ваше номер в очереди "))
        if ( (countpeople[0]>=0) and (countpeople[1]>=0) and (countpeople[2]>=0) and (0<start_index<=3) and (value > countpeople[start_index]) and len(countpeople) == 3) :
            print("Введены некоректные данные! Попробуйте ещё раз")
        else:
            flag=True

    win = False
    while not(win):
        matrix = init()
        win,value = start_game(value, countpeople, matrix, start_index, start)


if __name__ == '__main__':
    main()
