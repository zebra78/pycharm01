from typing import Iterable


def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    try:
        return text[0:text.index(" ")]
    except ValueError:
        return text[0:len(text)]


def is_acceptable_password(text: str) -> bool:
    if len(text) > 5:
        return True
    return False


def number_length(a: int) -> int:
    return len(str(a))


def most_frequent(data: list) -> str:
    my_dict = {}
    for str1 in data:
        keys1 = my_dict.keys()
        if str1 in keys1:
            val = my_dict.get(str1) + 1
            my_dict[str1] = val
        else:
            my_dict[str1] = 1
    keys = my_dict.keys()
    max_found_key = ''
    max_found_val_prev = 0
    for key in keys:
        max_found_val = my_dict[key]
        if max_found_val_prev == 0 or max_found_val > max_found_val_prev:
            max_found_val_prev = max_found_val
            max_found_key = key
    return max_found_key


def backward_string(val: str) -> str:
    val1 = ""
    for char in val:
        val1 = char + val1
    return val1


def no_of_zeroes(num: int) -> int:
    num_of_zeroes = 0
    if num == 0:
        return 0
    while num % 10 == 0:
        num_of_zeroes += 1
        num = num / 10
    return num_of_zeroes


def easy_unpack(elements: tuple) -> tuple:
    new_tuple = (elements[0], elements[2], elements[-2])
    return new_tuple


def remove_all_before(data: list, border_element: int) -> Iterable:
    sub_list = []
    element_matched = False
    for element in range(0, len(data)):
        if data[element] == border_element:
            element_matched = True
        if element_matched:
            sub_list.append(data[element])
    if not element_matched:
        return data
    return sub_list


def is_all_upper(text: str) -> bool:
    for chars in text:
        if 97 <= int(ord(chars)) <= 122:
            return False
    return True


def replace_first(items: list) -> Iterable:
    if len(items) > 0:
        items.append(items[0])
        items.pop(0)
    return items


def max_digit(number: int) -> int:
    prev_max_digit = 0
    while number > 0:
        curr_max_digit = number % 10
        if curr_max_digit > prev_max_digit:
            prev_max_digit = curr_max_digit
        number = int(number / 10)
    return prev_max_digit


def beginning_zeros(number: str) -> int:
    number2 = int(number)
    if number2 == 0:
        return len(number)
    return len(number) - len(str(number2))


def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin)+1: text.index(end)]


def split_pairs(a: str) -> list:
    mylist = []
    if len(a) % 2 != 0:
        a = a + '_'
    for n in range(0, len(a), 2):
        mylist.append(a[n:n+2])
    return mylist


def correct_sentence(text: str) -> str:
    if not text.endswith('.'):
        text = f"{text}."
    return f"{text[0].upper()}{text[1:]}"


def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


def nearest_value(values: set, one: int) -> int:
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


if __name__ == "__main__":
    print(nearest_value([0, -2], -1))
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
    # print(is_even(4))
    # print(is_even(7))
    # print(correct_sentence('Good morning. Venkat.'))
    # print(correct_sentence('Good morning. Venkat'))
    # print(correct_sentence('good morning. Venkat'))
    # print(correct_sentence('good morning. Venkat.'))

    # print(split_pairs('mystrings'))
    # print(between_markers('hello >madhu< sudhan', '>', '<'))
    #
    # assert between_markers('What is >apple<', '>', '<') == "apple"
    # assert between_markers('What is [apple]', '[', ']') == "apple"
    # assert between_markers('What is ><', '>', '<') == ""
    # assert between_markers('>apple<', '>', '<') == "apple"

    # print(beginning_zeros('100'))
    # print(beginning_zeros('001'))
    # print(beginning_zeros('100100'))
    # print(beginning_zeros('001001'))
    # print(beginning_zeros('012345679'))
    # print(beginning_zeros('0000'))
    # assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    # assert list(replace_first([1])) == [1]
    # assert list(replace_first([])) == []

    # print(is_all_upper('ALL UPPER'))
    # assert is_all_upper('ALL UPPER') == True
    # assert is_all_upper('all lower') == False
    # assert is_all_upper('mixed UPPER and lower') == False
    # assert is_all_upper('') == True
    # assert is_all_upper('     ') == True
    # assert is_all_upper('444') == True
    # assert is_all_upper('55 55 5') == True

    # assert first_word("Hello world") == "Hello"
    # assert first_word("a word") == "a"
    # assert first_word("hi") == "hi"
    #
    # assert number_length(2)
    # assert number_length(23)
    # assert number_length(34567)
    #
    # assert is_acceptable_password('short')
    # assert is_acceptable_password('muchlonger')
    #
    # assert most_frequent(['a', 'b', 'c', 'a', 'b', 'a']) == 'a'
    # assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'

    # assert backward_string('madhu') == 'uhdam'
    # assert backward_string('') == ''
    # assert backward_string('madhu sudhan') == 'nahdus uhdam'
    # assert backward_string('malayalam') == 'malayalam'

    # assert no_of_zeroes(0) == 0
    # assert no_of_zeroes(3450000) == 4
    # assert no_of_zeroes(34500004) == 0

    # assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    # assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    # assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    # assert easy_unpack((6, 3, 7)) == (6, 7, 3)

    # assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    # assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    # assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    # assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    # assert list(remove_all_before([], 0)) == []
    # assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]

