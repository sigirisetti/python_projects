import os.path


f = open(os.path.expanduser('~/system.properties'))
print(f.read())