953. Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', 
where '∅' is defined as the blank character which is less than any other character (More info).




"""
hashmap存 the position of ch in the list.
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = collections.defaultdict(int)
        for i, ch in enumerate(order):
            pos[ch] = i
        
        for i in range(1, len(words)):
            m, n = 0, 0
            prev, curr = words[i-1], words[i]
            while m < len(prev) and n < len(curr):
                if pos[prev[m]] > pos[curr[n]]:
                    return False
                elif pos[prev[m]] < pos[curr[n]]:
                    break       # this prev and curr is valid, so let's move on
                else:
                    m += 1
                    n += 1
                    
            if n == len(curr):
                return False
            
        return True
