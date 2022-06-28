def nearest_value(values: set, one: int) -> int:
    # your code here
    near_num_dif: int
    near_num_val: int
    i: int = 0
    for value in values:
        print('loop_value: ', value)
        if i == 0:
            near_num_dif = abs(value - one)
            near_num_val = value
            i += 1
        else:
            if abs(value - one) == near_num_dif:
                if value < near_num_val:
                    near_num_val = value
            elif abs(value - one) < near_num_dif:
                near_num_dif = abs(value - one)
                near_num_val = value
        if near_num_dif == 0:
            return one
    return near_num_val


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({0, 2}, 1))
    print(nearest_value({0, -2}, -1))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    # assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    # assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    # assert nearest_value({-6, -2, 4, 7, 12, 17}, -4) == -6
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    # assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    # assert nearest_value({5}, 5) == 5
    # assert nearest_value({5}, 7) == 5
    # assert nearest_value({0, -2}, -1) == -2
    print("Coding complete? Click 'Check' to earn cool rewards!")
