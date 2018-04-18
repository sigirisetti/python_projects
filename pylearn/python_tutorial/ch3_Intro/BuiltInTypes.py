"""
Python has five standard data types −
    Numbers
    String
    List
    Tuple
    Dictionary
"""

int1 = 10

string1 = "Prakhya"

list1 = [1, "Sri", [1,2,3]]

"""
Tuple - The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed,
        while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists
"""
tuple1 = list1

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(int1)
print(string1)
print(list1)
print(tuple1)

try:
    tuple[3]="Can?"
except:
    print("Cannot modify tuple")


print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values
