# MaxSubArray

This project contains 3 different algorithms to find maximum sub array.

## Installation

In order to run that project you must have following softwares and packages.

```bash
    * Python3
```

## Usage

In order to run that project follow below instructions.

```bash
* Open cmd or bash
* Use cd command to go to project\' s directory.
* py python main.py
```

## Input type

In order to feed algorithms please use input.txt.
__Note:__ White spaces and new lines are allowed.

## Algorithms

* The first algorithm(brute.py) uses 2 for loops. The second one is inner loop. So it takes O(n^2) time. It will calculate same values again and again.
* The second algorithm(better.py) uses 1 for loop. It was written in dynamic programming paradigm. It uses previous results if the previous result is not less than 0. It takes O(n) time.
* The third algorithm(div_and_conq.py) does not use for loop, but it divides arrays into sub arrays. This causes O(logn), then it sums all the values which also causes O(n). The result is O(nlogn)

## Comparison

In order to compare results of algorithms. you ca use elapsed times. Those values were wall clock time.
Also you can use other functionalites of "time" package like time_ns().
