s = "A man, a plan, a canal: Panama"

def isPalindrome(s: str) -> bool:
    s = ''.join(si for si in s if si.isalnum())
    s = s.lower()
    return s == s[::-1]

print(isPalindrome(s))