number = 540
hexa_list = []

dict_ = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

while number > 0:
    rem = number % 16
    if rem in dict_:
        rem = dict_[rem]
    hexa_list.insert(0, rem)
    number = number//16

print(hexa_list)