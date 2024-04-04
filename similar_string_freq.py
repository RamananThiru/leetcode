# Arrays
# April 4 , 2024 


# Thoughtspot coding round #1

# **Problem Statement:**

# Write a function that accepts two strings a and b and returns whether they are similar or not. Two strings are considered similar if they can be transformed from one to another using the following operations any number of times:

# 1. Swap any two characters in a.
# 2. Replace all occurrences of a character in a with another character in a.

# **Examples:**

# areSimilar("abcdef", "fbcdea")  # True (swap a and f)
# areSimilar("aaaabbc", "ccccbba")  # True (replace all 'a' with 'c')
# areSimilar("ab", "ba")  # True (swap a and b)
# areSimilar("aa", "ab")  # False (cannot transform 'aa' to 'ab' with allowed operations)
# areSimilar('aaabbced', 'dbbaaceb') -> True ( because aaabbced-> bbbaaced-> dbbaaceb)






# Solution


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
str1 = "abcdef"
str2 = "fbcdeak"


str3 = "aaaabc"
str4 = "ccccba"


def calculateFrequency(input_string):
    hash = {}
    for i in range(0, len(input_string)):
        if input_string[i] not in hash:
            key = input_string[i]
            hash[key] = 1
        else:
            key = input_string[i]
            hash[key] += 1
    return hash       


def compareStrings(str1, str2):
    hash1 = calculateFrequency(str1)
    hash2 = calculateFrequency(str2)
        
    
    for key, value in hash1.items():
        print(value, value in hash2.values())
        if value == -1:
            next
        if value in hash2.values():
            sub_key = [k for k, v in hash2.items() if v == value][0]
            hash2[sub_key] = -1
            hash1[key] = -1
    
    
    return sum(hash1.values()) == sum(hash2.values())



print(compareStrings(str3, str4))    
