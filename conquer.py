from math import floor


def conquer(a, low, middle, high):

    left_sum = -9999999
    right_sum = -9999999

    # Sum of left
    summation = 0
    for i in range(middle, low - 1, -1):
        summation = summation + a[i]

        if (summation > left_sum):
            left_sum = summation

    # Sum of right
    summation = 0
    for i in range(middle + 1, high + 1, 1):
        summation = summation + a[i]

        if (summation > right_sum):
            right_sum = summation

    return left_sum + right_sum


def div_and_conq(a, low, high):

    # Base Case.
    if low == high:
        return a[low]

    # Find middle point
    middle = floor((low + high) / 2)

    # Go to left most
    # Then right
    # Sum all the elements.
    return max(
        div_and_conq(a, low, middle),
        div_and_conq(a, middle + 1, high),
        conquer(a, low, middle, high)
    )
