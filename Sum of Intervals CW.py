# Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths.
# Overlapping intervals should only be counted once.
#

# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

def sum_of_intervals(intervals):
    ## slow version
    max_num = max(intervals[0])
    min_num = min(intervals[0])
    for i in intervals:
        max_num = max(max_num, max(i))
        min_num = min(min_num, min(i))
    line = {i: 0 for i in range(min_num, max_num + 1)}
    for i in intervals:
        start, stop = i
        for j in range(start, stop):
            line[j] = 1
    print(sum([line[i] for i in range(min_num, max_num + 1) if line[i] == 1]))


sum_of_intervals( [
    [0, 20],
    [-100000000, 10],
    [30, 40]
] )
