a = 'bottles of beer on the wall,'
b = a[0:15] + '.'
c = 'Take one down and pass it around,'
d = a.replace(',', '.')
e = 'no more '
f = 'Go to the store and buy some more,'

for n in reversed(range(0, 100)):
    if n > 2:
        print(n, a, n, b, '\n', c, n-1, d, '\n')
    elif n == 2:
        print (n, a, n, b, '\n', c, n-1, d.replace('s', ''), '\n')
    elif n == 1:
        print (n, a.replace('s', ''), n, b.replace('s', ''), '\n', c, e + d, '\n')
    elif n == 0:
        print (e.replace('n', 'N') + a, e + b, '\n', f, '99 ' + d, '\n')
