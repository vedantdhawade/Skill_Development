from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(left: int, right: int) -> None:
            if left >= right:
                return
            
            # Swap characters using tuple unpacking
            s[left], s[right] = s[right], s[left]
            
            # Recursive call for next pair
            reverse(left + 1, right - 1)
        
        reverse(0, len(s) - 1)
