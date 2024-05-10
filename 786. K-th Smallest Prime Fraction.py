# You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
#
# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
#
# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        left, right = 0, 1

        while left < right:  # бинарный поиск
            mid = (left + right) / 2
            max_fraction = 0.0
            total_smaller_fractions = 0
            chislit, znamenat = 0, 0
            j = 1

            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:  # будем увиличивать знаменатель пока не получим дробь большую чем искомая (mid)
                    j += 1

                total_smaller_fractions += (n - j)  # посчитали сколько получилось дробей перед найденной

                if j == n:
                    break

                fraction = arr[i] / arr[j]

                if fraction > max_fraction:
                    chislit = i
                    znamenat = j
                    max_fraction = fraction

            if total_smaller_fractions == k:  # если оказалось что найденная дробь сразу к-тая то это победа
                return [arr[chislit], arr[znamenat]]
            elif total_smaller_fractions > k:  # иначе смещаем границу поиска влево или вправо
                right = mid
            else:
                left = mid
