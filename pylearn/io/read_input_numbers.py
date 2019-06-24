import sys

"""
Read numbers from standard input
"""


list = []
size = int(input("Enter size of input : "))

print("Enter ", size, " numbers")
for i in range(size):
    list.append(int(input()))

