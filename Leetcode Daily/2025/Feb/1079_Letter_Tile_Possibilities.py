class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        A       B       C
        AB AC   BA BC   CA CB
        ABC ACB BAC BCA CAB CBA

        A       A       B
        AA AB   AA AB   BA BA
        AAB ABA AAB ABA BAA BAA
        set = A, B, AA, AB, BA, AAB, ABA, BAA
        """
        sequences = set()
        visited = [False] * len(tiles)
        self.generateSequences("", sequences, visited, tiles)
        return len(sequences) - 1
    def generateSequences(self, curr, sequences, visited, tiles):
        sequences.add(curr)
        for i, c in enumerate(tiles):
            if not visited[i]:
                visited[i] = True
                self.generateSequences(curr + c, sequences, visited, tiles)
                visited[i] = False
# TC: O(n n!) For each of n! permutations, we perform O(n) work for string concatenation
# SC: O(n n!) We store up to n! unique sequences, each of length up to n, in the hash set.