# 1 задача
import random

a = [i for i in range(1,random.randint(2, 10))]
b = [i**2 for i in a ]

print(b)

# 2 задача
a = ["apple", "pear", "banana", "plum"]
b = ["pear", "tangerine", "plum", "coconut"]
c = [i for i in a if i in b ]
print(c)

# 3 задача
a = [2,12,34,3,4,-3,0,-14,-12, 9]
c = [i for i in a if i % 3 == 0 and i % 4 != 0 and i > 0]
print(c)