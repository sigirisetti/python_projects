import sys

print(sys.version)

print(sys.executable)

print(sys.platform)

# where the platform independent Python files are installed
print(sys.prefix)

import platform

print(platform.uname())
print(platform.system())
print(platform.architecture())
print(platform.machine())
print(platform.node())
print(platform.platform())
print(platform.processor())
print(platform.python_build())
print(platform.python_version())