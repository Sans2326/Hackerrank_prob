def check_sq(val):
    s = 0
    for i in val:
        if i.isdigit():
            s += (int(i)) ** 2
        else:
            return -1
    return s


def check(s):
    if s % 2==0:
        return 'r'
    else:
        return 'l'


def rotate_right(sam, sq):
    for i in range(0, sq):
        sam = sam[-1:] + sam[:-1]

    print(sam)


def rotate_left(sam, sq):
    for j in range(0, sq):
        sam = sam[1:] + sam[:1]

    print(sam)


a = input()
s = a.split()
if not a:
    print(-1)
for i in s:
    d = i.split(':')
    res1 = check_sq(d[1])
    res = check(res1)

    if res=='r':
        rotate_right(d[0], res1)
    elif res=='l':
        rotate_left(d[0], res1)
    else:
        print(-1)
# i/p-hello:11 card:23
# o/p- lohel ardc