import time

def better(a):

    res = -99999999999999
    max_num = 0

    start = time.time()

    for i in range(len(a)):
        max_num += a[i]
        if (res < max_num):
            res = max_num

        if max_num < 0:
            max_num = 0

    end = time.time()

    return res, end - start