f = open('c:\\tmp\\netstat.txt', 'r')

# Print all contents
# print(f.read())

for line in f:
    print(line, end='')
f.close()

with open('c:\\tmp\\netstat.txt', 'r') as f:
    read_data = f.read()


