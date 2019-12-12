import time

from better import better
from brute import brute
from conquer import div_and_conq

# Read input file.
with open("input.txt", "r") as f:
    input_entered = f.read()

# Parse input file via white spaces and new lines.
parsed_input = input_entered.split()
a = [int(el) for el in parsed_input]

print()

print("Length of input is: {0}".format(len(a)))
print("Sum of input array: {0}".format(sum(a)))

# Check is it worth?
if (sum(a)) < 0:
    print("Result: {0}".format(0))
    print("Indexes: ({0}, {1})".format(-1, -1))
    exit()

# Run algorithms.
max_brute, indexes, time_brute = brute(a)
max_better, time_better = better(a)
# The divide and conquer algorithm is recursive.
# In order to measure elapsed wall clock time, I measured in here.
start = time.time()
max_conquer = div_and_conq(a, 0, len(a) - 1)
end = time.time()

# Print all results calcualted.
print()

print("--------------------- Brute Force Results --------------------------")
print("Result: {0}".format(max_brute))
print("Starting Index: {0}".format(indexes[0]))
print("Ending Index: {0}".format(indexes[1]))
print("Elapsed Time: {0} seconds".format(time_brute))

# For a blank line.
print()

print("------------------------ Better Results ----------------------------")
print("Result: {0}".format(max_better))
print("Elapsed Time: {0} seconds.".format(time_better))

print()

print("------------------- Divide and Conquer Results ---------------------")
print("Result: {0}".format(max_conquer))
print("Elapsed time: {0} seconds.".format(end - start))
