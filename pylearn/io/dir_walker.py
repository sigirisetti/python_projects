import os

for dirpath, dirnames, filenames in os.walk('c:\\q', topdown=True):
    for fp in filenames:
        print(os.path.abspath(os.path.join(dirpath, fp)))