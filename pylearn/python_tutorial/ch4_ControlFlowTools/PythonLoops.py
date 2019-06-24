#
# basic while loop
#
a = 1
b = 20

while a < b:

    if a % 3 == 0:
        a += 2
        continue

    print(a)
    a+=2



#
# For loop a list
#

alist = [1,2,3,4,5,6,7,8,9,10]
strings = ["a", "b", "c", "d"]
tuple = ["There", "are", 5, "ways"]

for e in alist:
    if e == 5:
        break
    print(e)

for e in strings:
    print(e)

for e in tuple:
    print(e)



#
# Index loop this way
#
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#
# Range loop
#

