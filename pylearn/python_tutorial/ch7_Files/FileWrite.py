import os, errno

dir = "c:/tmp/test/test/"
file = "test.txt"

if not os.path.exists(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

fh = open(dir+file, "w")
fh.write("This is a test write")
fh.close()
