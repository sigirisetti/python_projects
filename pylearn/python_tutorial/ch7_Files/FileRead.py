f = open('c:\\temp\\te.log', 'r')

# Print all contents
# print(f.read())

for line in f:
    print(line, end='')
f.close()

with open('c:\\temp\\te.log', 'r') as f:
    read_data = f.read()


