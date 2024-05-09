# You are given an array happiness of length n, and a positive integer k.
#
# There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.
#
# In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.
#
# Return the maximum sum of the happiness values of the selected children you can achieve by selecting k childre

#we'll basicly choose k largest values and decrease i'th value by i, if value - i <0 then set it to 0


class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        sorted_happines = sorted(happiness,reverse=True)
        return sum([sorted_happines[i]-i if sorted_happines[i]-i>0 else 0 for i in range(k)])
s = Solution()
print(s.maximumHappinessSum(happiness =[12,1,42],k =3))