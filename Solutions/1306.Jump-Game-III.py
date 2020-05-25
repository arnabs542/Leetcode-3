1306. Jump Game III

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque()
        q.append(start)
        visited = set()
        visited.add(start)
        
        while q:
            currIdx = q.popleft()
            if arr[currIdx] == 0:
                return True
            for nextIdx in [currIdx + arr[currIdx], currIdx - arr[currIdx]]:
                if nextIdx < 0 or nextIdx >= len(arr):
                    continue
                if nextIdx in visited:
                    continue
                    
                q.append(nextIdx)
                visited.add(nextIdx)
                
        return False
