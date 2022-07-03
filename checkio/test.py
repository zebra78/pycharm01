def sum_num_in_str(text: str) -> int:
    sum_tot: int = 0
    for word_one in text.split():
        if word_one.isnumeric():
            sum_tot = sum_tot + int(word_one)
    return sum_tot


print(sum_num_in_str('hi'))
print(sum_num_in_str('who is 1st here'))
print(sum_num_in_str('my numbers is 2'))
print(sum_num_in_str('This picture is an oil on canvas '
                      'painting by Danish artist Anna '
                      'Petersen between 1845 and 1910 year'))
print(sum_num_in_str('5 plus 6 is'))
print(sum_num_in_str(''))
