def reverseString(s):
    return s[::-1]


print(reverseString("hello"))
print(reverseString("harsha"))
print(reverseString("Tashvi"))


def countOvels(s):
    count = 0
    ovels = "aeiou"
    for char in s.lower():
        if char in ovels:
            count += 1
    return count


print(countOvels("apple"))
print(countOvels("aharshae"))
print(countOvels("Tashvi"))


def findMax(nums):
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum


print(findMax([3, 4, 5, 6, 7, 12]))
