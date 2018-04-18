"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first

print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{}, {}, {}'.format('a', 'b', 'c'))  # 3.1+ only
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))      # unpacking argument sequence
print('{0}{1}{0}'.format('abra', 'cad'))   # arguments' indices can be repeated

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord)) #unpacking keyword args


c = 3-5j
print(('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.').format(c))


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)


print(str(Point(4, 2)))

coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))

print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))


print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))  # use '*' as a fill char

print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'


# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))


print('{:,}'.format(1234567890))
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))


import datetime
d = datetime.datetime(2013, 1, 31, 4, 0, 0)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))


for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))


octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

print(int(_, 16))

width = 5
for num in range(5,12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()
