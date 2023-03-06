class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(resutl, tempList, candidates, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                result.append(tempList.copy())
            else:
                for i in range (start, len(candidates)):
                    # Check for duplciates
                    if (i > start and candidates[i] == candidates[i-1]):
                        continue
                    tempList.append(candidates[i])
                    backtrack(result,tempList, candidates, remain-candidates[i], i+1)
                    tempList.pop()
        
        result = []
        candidates.sort()
        backtrack(result, [], candidates, target, 0)
        return result