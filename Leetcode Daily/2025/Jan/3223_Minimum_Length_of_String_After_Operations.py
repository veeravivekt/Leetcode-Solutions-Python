class Solution:
    def minimumLength(self, s: str) -> int:
        charStore = defaultdict(list)
        for c in s:
            charStore[c] = charStore.get(c, 0) + 1
        
        deleteCount = 0
        for value in charStore.values():
            if value % 2 == 0:
                deleteCount += value - 2
            else:
                deleteCount += value - 1
        
        return len(s) - deleteCount
# TC: O(n) - Count frequency O(n) + deletecount from charStore which is max 26 alphabets O(26)
# SC: O(1) - charStore can store max of 26 characters