# Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths.
# Overlapping intervals should only be counted once.
#

# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.


# будем работать с чем-то типа указателей
def sum_of_intervals(intervals):
    lenght = 0
    intervals.sort()  # для начала отсортируем массив, так получим что каждый новый интервал имеет старт больше чем у предыдущего
    start, stop = intervals[0]  # поставим начальные указатели
    lenght += stop - start  # инициализируем длину всех интервалов длиной первого интервала
    if len(intervals) == 1:  # если в массиве всего один интервал
        return lenght
    else:
        for j in intervals[1:]:  # пройдемся по оставшимся интервалам
            new_start, new_stop = j
            if new_start > stop:  # если интервалы не пересекаются, то просто добавляем длину и указатели сдвигаем на границы нового интервала
                lenght += new_stop - new_start
                start = new_start
                stop = new_stop
            elif new_stop > stop:  # если интервалы пересеклись то к длине добавим конец нового отрезка минус конец старого (т.к. они отсортированы уже)
                lenght += new_stop - stop
                start = stop  #перемещаем указатели
                stop = new_stop
            elif new_stop < stop:
                continue
    return lenght


print(sum_of_intervals( [
    [0, 20],
    [-100000000, 10],
    [30, 40]
] ))