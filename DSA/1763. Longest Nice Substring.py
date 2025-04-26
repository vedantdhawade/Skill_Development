s = "YazaAay"

def longestNice(s):
    if len(s) < 2:
        return ""
    
    seen = set(s)  # You should add characters, not indexes
    
    for i, ch in enumerate(s):
        if ch.islower() and ch.upper() not in seen:
            left = longestNice(s[:i])
            right = longestNice(s[i+1:])
            return left if len(left) >= len(right) else right
        if ch.isupper() and ch.lower() not in seen:
            left = longestNice(s[:i])
            right = longestNice(s[i+1:])
            return left if len(left) >= len(right) else right

    return s  # If the whole string is nice

print(longestNice(s))
