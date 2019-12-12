import time

def brute(a):
    sum_of_nums = 0
    max_num = -999999999999
    starting_index = 0
    ending_index = 0

    start = time.time()

    for i in range(len(a)):
        sum_of_nums = 0
        for j in range(i, len(a)):
            sum_of_nums += a[j]
            if sum_of_nums >= max_num:
                max_num = sum_of_nums
                starting_index = i
                ending_index = j
            if sum_of_nums < 0: 
                sum_of_nums = 0

    end = time.time()

    return max_num, (starting_index, ending_index), end - start
