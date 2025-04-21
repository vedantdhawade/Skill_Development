def run_tests():
    test_cases  = [
    # Format: (nums, k, expected_output)
    ([1, 12, -5, -6, 50, 3], 4, 12.75),
    ([5], 1, 5.0),
    ([0, 0, 0, 0, 0], 1, 0.0),
    ([1, 2, 3, 4, 5, 6, 7], 3, 6.0),  # max avg from [5,6,7]
    ([7, 4, 5, 2, 6, 5], 2, 6.0),    # max avg from [6,5]
    ([4, 0, 4, 3, 3], 5, 2.8),
    ([9, 7, 3, 5, 6, 2, 1], 2, 8.0),  # max avg from [9,7]
    ([-1, -12, -5, -6, -50, -3], 2, -4.0),
    ([1, 2], 2, 1.5),
    ([10000, -10000, 10000, -10000, 10000], 1, 10000.0),
]


    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = Average(nums , k)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test Case {i}: {status} | Output: {result} | Expected: {expected}")

def Average(nums , k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k,len(nums)):
        window_sum = window_sum + nums[i] - nums[i-k]
        max_sum = max(max_sum,window_sum)
    return max_sum/k




run_tests()