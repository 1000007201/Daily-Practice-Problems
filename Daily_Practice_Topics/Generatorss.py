# Fibonnacci series by generators

def fibo(length):
    first, second = 0, 1

    while first < length:
        yield first
        first, second = second, first+second

fiboc = fibo(4)
for i in fiboc:
    print(i)
