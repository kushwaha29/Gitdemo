def solution(S):
    # Implement your solution here
        N = len(S)
        if N <= 2:
            return N

        max_len = 2
        current_len = 2

        for i in range(2, N):
            if S[i] != S[i - 1] or S[i] != S[i-2]:
                current_len += 1
            else:
                max_len = max(current_len, max_len)
                current_len = 2
        max_len = max(current_len, max_len)
        return max_len

    # Example usage:
s = "baaabbabbb"
result = solution(s)
print("Length of the longest semi-alternating substring:", result)


