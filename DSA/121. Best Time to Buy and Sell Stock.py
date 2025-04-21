def run_tests():
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 1, 2, 1, 2], 1),
        ([5], 0),
        ([1, 10], 9),
        ([10, 1], 0),
        ([5, 1, 6, 2, 8], 7),
        ([2, 4, 1], 2),
        ([3, 3, 5, 0, 0, 3, 1, 4], 4),
        ([1, 2], 1),
    ]

    for i, (prices, expected) in enumerate(test_cases, 1):
        result = maxProfit(prices)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test Case {i}: {status} | Output: {result} | Expected: {expected}")

def maxProfit(prices):
    print(prices)


    
run_tests()
