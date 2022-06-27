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
    str_chr = text.split(text)
    for c in chr(str_chr):
        if int(ord(c)) >= 97 and int(ord(c)) <= 122:
            return False
    return True


if __name__ == "__main__":
    print('Overcome Indentation warning in PyCharm')
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

    # assert is_all_upper('ALL UPPER') == True
    # assert is_all_upper('all lower') == False
    # assert is_all_upper('mixed UPPER and lower') == False
    # assert is_all_upper('') == True
    # assert is_all_upper('     ') == True
    # assert is_all_upper('444') == True
    # assert is_all_upper('55 55 5') == True