

def fibo():
    n1 = 0
    n2 = 1
    count = 0
    while count < 10:
        print(n1)
        nj = n1 + n2
        n1 = n2
        n2 = nj
        count += 1

fibo()