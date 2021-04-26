def is_armstrong_number(number):
    sum = 0
    str_of_num = str(number)
    power = len(str_of_num)

    for char in str_of_num:
        sum += int(char) ** power

    if number == sum:
        return True

    return False