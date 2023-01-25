class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())


# Space and Time Complexity = O(n)
"""
The space complexity of this solution is O(n), because the size of the dictionary scales linearly with the number of words. 
The time complexity is also O(n), because we iterate through the list of words once and do a constant amount of work for each word.
Sorting each word has a time complexity of O(nlogn), but since we only do this once for each word, the overall time complexity is still linear.
Note that if the words are very long, then the time complexity could potentially be dominated by the time it takes to sort each word, 
in which case the overall time complexity would be O(n * mlogm), where m is the length of the longest word. However, for most practical purposes, 
this solution should have adequate time performance.
"""