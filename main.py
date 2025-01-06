from collections import deque

def bfs_find_max(matrix, start):
    """
    Выполняет поиск в ширину (BFS) по матрице из заданной точки и находит максимальное число.

    :param matrix: Список списков (матрица) чисел
    :param start: Кортеж (x, y) с начальными индексами
    :return: Максимальное число, найденное в процессе обхода
    """
    rows, cols = len(matrix), len(matrix[0])
    index_max_value = list(start)
    #print(index_max_value)
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
            index_max_value = [current_x,current_y]
            if max_value == 1:
                #matrix[index_max_value] = -1
                matrix[index_max_value[0]][index_max_value[1]]=-1
                return [index_max_value, max_value]

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    matrix[index_max_value[0]] [index_max_value[1]] = -1
    return [index_max_value,max_value]

def main ():
    matrix =[[0  , 1  , 0.9, 1  , 0.3, 0.1, 0.3, 1  , 0.8, 0.9, 0.9, 0.8, 1  , 0.3, 0.1, 0.3, 1  , 0.8, 0.9, 0.9, 0.8, 1  , 0.3, 0.1, 0.3, 1  , 0.9, 1  , 0  ],
             [0.5, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.5],
             [0  , 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0  ],
             [0  , 1  , 0.9, 1  , 0.5, 0.4, 0.5, 1  , 0.8, 0.9, 0.9, 0.8, 1  , 0.5, 0.4, 0.5, 1  , 0.8, 0.9, 0.9, 0.8, 1  , 0.4, 0.5, 0.4, 1  , 0.9, 1  , 0  ]]

    start = [(0,5),(0,14), (0,23)]
    flag = False
    while flag == False:
        countpeople = list(map(int,input("Введите через 'Пробел' 3 числа, сколько людей стоят у каждой двери").split()))
        start_index =int(input("Введите номер входа в вагон ")) - 1
        value=int(input("Введите ваше номер в очереди "))
        if value > countpeople[start_index] and countpeople[0]>=0 and countpeople[1]>=0 and countpeople[2]>=0 and 0<start_index<=3 :
            print("Введены некоректные данные! Попробуйте ещё раз")
        else:
            flag=True

    while value > 0:
        for i in range (3):
            countpeople[i] -= 1
            if countpeople[i] >= 0:
                index, maxvalue = (bfs_find_max(matrix, start[i]))
                if (start_index == i):
                    value-=1
                    if (value==0):
                        print(index,maxvalue)
    
if __name__ == '__main__':
    main()
