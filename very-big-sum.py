def aVeryBigSum(ar):
    total = 0

    for item in ar:
        total = total + item

    return total


ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

result = aVeryBigSum(ar)

print(result)
