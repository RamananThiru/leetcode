'''


Consider an array:

Input: [5, 6, 6, 5]
Output: 5 

Note that if more than 1 number occurs the same number of times return the element that was visited first
'''


def ArrayChallenge(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_freq = max(freq.values(), default=0)

    if max_freq == 1:
        return -1

    for num in arr:
        if freq[num] == max_freq:
            return num

# Example test cases
print(ArrayChallenge([5, 5, 2, 2, 1]))  # Output: 5
print(ArrayChallenge([3, 4, 1, 6, 10])) # Output: -1
print(ArrayChallenge([10, 4, 5, 2, 4])) # Output: 4
print(ArrayChallenge([5, 10, 10, 6, 5])) # Output: 5