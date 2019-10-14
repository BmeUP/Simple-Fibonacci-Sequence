import time


def fibo(n):
    a, b = 0, 1
    fb = [0, 1]
    if n == 0:
        print([0])
    elif n == 1:
        print([0, 1])
    elif n == 2:
        print([0, 1, 1])
    else:
        for i in range(2, n):
            a, b = b, b+a
            fb.append(b)
            print(fb)
            time.sleep(1)


n = int(input("Insert the number: "))

fibo(n)
