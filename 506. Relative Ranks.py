class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {}
        for index, scores in enumerate(sorted_score):
            if index < 3:
                res = medals[index]
            else:
                res = str(index + 1)

            rank_mapping[scores] = res
        return [rank_mapping[a] for a in score]

s = Solution()
print(s.findRelativeRanks([10,3,8,9,4]))