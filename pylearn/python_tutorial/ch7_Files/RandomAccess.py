f = open('c:\\temp\\results.txt', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # Go to the 6th byte in the file
print(f.read(1))
f.seek(-3, 2)  # Go to the 3rd byte before the end
print(f.read(1))
f.close()