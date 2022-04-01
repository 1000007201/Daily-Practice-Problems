import string
import random


def check_string(str_):
    n = len(str_)
    count = 0
    while count >= 0:
        res = ''.join(random.choices(string.ascii_lowercase, k=n))
        count += 1
        if str_ == str(res):
            break
    return count


print(check_string('hello'))
# print("The generated random string : " + str(res))