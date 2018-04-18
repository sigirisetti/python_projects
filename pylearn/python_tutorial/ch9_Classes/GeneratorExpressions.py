print('Sum of squares from 0 to 10 ', sum(i*i for i in range(10)))                 # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
print('Dot product of two vectors ', sum(x*y for x,y in zip(xvec, yvec)))         # dot product


from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_table)

# unique_words = set(word for line in page for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
print(range(len(data)-1, -1, -1))
print(list(data[i] for i in range(len(data)-1, -1, -1)))
