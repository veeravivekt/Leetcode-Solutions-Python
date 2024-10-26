class Solution:
    def intervalIntersection(self, firstList, secondList) -> List[List[int]]:
        intersect = []
        fL, sL = len(firstList), len(secondList)
        i, j = 0, 0
        while i < fL and j < sL:
            head1, tail1 = firstList[i][0], firstList[i][1]
            head2, tail2 = secondList[j][0], secondList[j][1]

            head = max(head1, head2)
            tail = min(tail1, tail2)

            if head <= tail:
                intersect.append([head, tail])
            
            if tail1 < tail2:
                i += 1
            else:
                j += 1
        return intersect
