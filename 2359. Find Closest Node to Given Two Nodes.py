from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        queue1 = deque([node1])
        queue2 = deque([node2])
        visited1 = {node1}
        visited2 = {node2}
        possible_answer = set()
        go_exit = False
        while (queue1 or queue2) and not go_exit:
            if queue1:
                current1 = queue1.popleft()
            if queue2:
                current2 = queue2.popleft()
            if current1 in visited2:
                possible_answer.add(current1)
                go_exit = True
            if current2 in visited1:
                possible_answer.add(current2)
                go_exit = True
            if edges[current1] not in visited1 and edges[current1] != -1:
                queue1.append(edges[current1])
                visited1.add(edges[current1])
            if edges[current2] not in visited2 and edges[current2] != -1:
                queue2.append(edges[current2])
                visited2.add(edges[current2])

        if possible_answer:
            return min(possible_answer)
        else:
            return -1


Sol = Solution()
print(Sol.closestMeetingNode([23,21,28,30,25,10,13,18,1,22,16,10,27,8,6,26,19,0,-1,12,11,29,2,24,4,14,17,15,5,7,9], 28, 13))
