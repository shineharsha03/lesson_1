def isPalindrome(x):
    original = str(x)
    reversed_number = original[::-1]
    return original == reversed_number


print(isPalindrome(121))
print(isPalindrome(123))
print(isPalindrome(321))