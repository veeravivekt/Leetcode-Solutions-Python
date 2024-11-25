# EC: same frequency?, maxLen of nums?
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # intialize a hashmap and count frequency of each nums
        store = {}
        for n in nums:
            store[n] = store.get(n, 0) + 1
        # add all elements to maxHeap
        maxHeap = []
        for key, value in store.items():
            heappush(maxHeap, (-value, key))
        # return top k elements
        result = []
        while k > 0:
            value, key = heappop(maxHeap)
            result.append(key)
            k -= 1
        return result
# TC: O(nlogn) -> iternate every num for count(O(n)), heap(O(nlogn))
# SC: O(n) -> worst case store, maxHeap stores n unqiue elements