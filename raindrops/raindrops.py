def convert(number):
    number = int(number)
    retStr = ''
    if number%3 == 0:
        retStr += 'Pling'
    if number%5 == 0:
        retStr += 'Plang'
    if number%7 == 0:
        retStr += 'Plong'

    if retStr == '':
        retStr = str(number)

    return retStr