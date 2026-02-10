#Given an integer n, return how many even numbers exist from 1 to n (inclusive).

def countEvens(n):
    count = 0
    for i in range(1, 1+n):
        if i % 2 == 0:
            count += 1
    return count

print(countEvens(5))
print(countEvens(300))

