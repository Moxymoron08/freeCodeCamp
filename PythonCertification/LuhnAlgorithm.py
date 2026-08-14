def verify_card_number(number):
    array = []
    for i in number:
        if i != ' ' and i != '-':
            array.append(int(i))
    array = array[::-1]
    for i in range(1,len(array),2):
        array[i] = array[i]*2
        if array[i] > 9:
            array[i] -= 9
    if sum(array) % 10 :
        return 'INVALID!'
    return 'VALID!'
