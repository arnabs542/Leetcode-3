398. Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);


"""
O(N) time O(N) space using random.choice(seq): Return a random element from the non-empty sequence seq.
"""
from random import choice

class Solution:

    def __init__(self, nums: List[int]):
        self.pos_dict = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.pos_dict[num].append(i)

    def pick(self, target: int) -> int:
        print(self.pos_dict)
        return choice(self.pos_dict[target])
    
或者这样写也是一样的：
from random import randrange

class Solution:

    def __init__(self, nums: List[int]):
        self.pos_dict = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.pos_dict[num].append(i)

    def pick(self, target: int) -> int:
        random_idx = randrange(len(self.pos_dict[target]))
        return self.pos_dict[target][random_idx]
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
