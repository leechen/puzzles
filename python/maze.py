import math

n = 3
if n < 0:
    print('negative')
elif n > 2:
    print('n>2')
else:
    print('0<n<2')

# while n < 5:
#     print(n)
#     n += 1

# for i in range(5,1,-1):
#     print(i)

print(float("inf"))

arr = [1, 2 ,3]
arr.append(4)
print(arr)
arr.pop()
print(arr)
arr.pop(0)
print(arr)
arr.insert(1, 8)
print(arr)