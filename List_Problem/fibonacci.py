def fibo_series(length_):
    n1 = 0
    n2 = 1
    if length_ == 1:
        print(n1)
    else:
        for i in range(length_):
            print(n1, end=' ')
            n3 = n1 + n2
            n1 = n2
            n2 = n3


fibo_series(5)
