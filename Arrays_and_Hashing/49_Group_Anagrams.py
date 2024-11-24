class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()
    

# EC: empty str? all same? all unqiue? maxSize of strs? len of str? case-senstive?
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize a hashmap to store values
        store = defaultdict(list)
        # check every str
        for s in strs:
            # sort the string and check if it matches with any key
            sortedS = ''.join(sorted(s))
            # if yes then add it to the list
            store[sortedS].append(s)
        # return all values as list
        return list(store.values())
# TC: O(m * nlogn) -> m is len of str, sorting n numbers(O(nlogn))
# SC: O(m * n) -> store(m len and n nums)