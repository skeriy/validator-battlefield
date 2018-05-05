# Поле для проверки на правильную расстановку кораблей


# Подсчет кораблей на поле
def num_of_ships(count, number):
    if count == 1:
        number[0] += 1
    elif count == 2:
        number[1] += 1
    elif count == 3:
        number[2] += 1
    elif count == 4:
        number[3] += 1
    else:
        number[4] = 1


# функция-валидатор поля
def validate_grid(grid):
    # количество кораблей
    number_of_ships = [0, 0, 0, 0, 0]
    # для хранения проверенных ячеек
    checked_position = []
    # для хранения списков содержащих ячейки корабля
    ships_coordinates = []
    i = 0
    j = 0
    # проходим по всем ячейкам и заносим координаты кораблей
    while i < 10:
        while j < 10:
            # если найдена палуба корабля и в списке проверенных ячеек, нет этой ячейки
            if (grid[i][j] == 1) & (checked_position.count([i, j]) == 0):
                temp = []
                ti = i
                tj = j
                count = 0
                # если не выходим за границу сетки и следующая вниз ячейка является продолжением корабля
                if (i + 1 < 10) and (grid[i + 1][j] == 1):
                    while grid[ti][tj] != 0:
                        checked_position.append([ti, tj])
                        temp.append([ti, tj])
                        if ti >= 9:
                            count += 1
                            break
                        ti += 1
                        count += 1
                    j += 1
                    ships_coordinates.append(temp)
                    num_of_ships(count, number_of_ships)
                # если не выходим за границу сетки и следующая вправо ячейка является продолжением корабля
                elif (j + 1 < 10) and (grid[i][j + 1] == 1):
                    while grid[ti][tj] != 0:
                        checked_position.append([ti, tj])
                        temp.append([ti, tj])
                        if tj >= 9:
                            count += 1
                            break
                        tj += 1
                        count += 1
                    j = tj
                    ships_coordinates.append(temp)
                    num_of_ships(count, number_of_ships)
                # иначе корабль однопалубный
                else:
                    checked_position.append([ti, tj])
                    ships_coordinates.append([[ti, tj]])
                    j = tj + 1
                    num_of_ships(1, number_of_ships)
            else:
                j += 1
        i += 1
        j = 0

    if (number_of_ships[0] == 4) & (number_of_ships[1] == 3) & (number_of_ships[2] == 2) & (number_of_ships[3] == 1):
        pass
        #print("\nВсе корабли расставлены")
    elif number_of_ships[4] == 1:
        #print("\nНа поле находятся корабли больше 4-х палубного")
        return False
    else:
        #print("\nНе хватает или много расставленных кораблей! Кораблей на поле:\n"
        #      "1-палубных: {},\n2-палубных: {},\n3-палубных: {},\n4-палубных: {}".format(number_of_ships[0],
        #                                                                                 number_of_ships[1],
        #                                                                                 number_of_ships[2],
        #                                                                                 number_of_ships[3]))
        return False
    # цикл для прохода по найденым кораблям
    for num in range(len(ships_coordinates)):

        whole_ship = ships_coordinates[num]
        ship_len = len(whole_ship)

        # проходим по каждой палубе и смотрим нет ли вокруг нее других кораблей
        for first_arg in range(ship_len):
            # координаты палубы
            x = whole_ship[first_arg][0]
            y = whole_ship[first_arg][1]
            # циклы для обхода пространства вокруг палубы
            for zx in range(-1, 2):
                for zy in range(-1, 2):
                    # вспомогательные переменные проверяемой ячейки
                    nx = x + zx
                    ny = y + zy
                    # если проверяемая ячейка находится на поле
                    if (nx >= 0) and (nx < 10):
                        if (ny >= 0) and (ny < 10):
                            # если проверяемая ячейка является палкубой корабля
                            if whole_ship.count([nx, ny]) == 1:
                                pass
                            else:
                                # если проверяемая ячейка равна 0
                                if grid[nx][ny] != 1:
                                    pass
                                # иначе в ней находится палуба другого корабля
                                else:
                                    return False

    return True

