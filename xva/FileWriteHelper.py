import os, errno

from constants import *


class FileWriteHelper:

    def write_blob(self, dir, file_name, contents):
        if not os.path.exists(dir):
            try:
                os.makedirs(dir)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        fh = open(dir + "/" + file_name + ".json", "w")
        fh.write(contents)
        fh.close()