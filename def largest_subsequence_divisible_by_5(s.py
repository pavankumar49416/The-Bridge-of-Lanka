def largest_subsequence_divisible_by_5(stones):
    n = len(stones)
    max_length = 0
    result = []

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += stones[j]
            if current_sum % 5 == 0:
                if (j - i + 1) > max_length:  
                    max_length = j - i + 1
                    result = stones[i:j + 1]

    return result



stones = [2, 3, 7, 1, 9, 6]
print("Largest subsequence:", largest_subsequence_divisible_by_5(stones))
