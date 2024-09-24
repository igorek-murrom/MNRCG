commands = []
registers = [0] * 1000


def j(q1, q2, t):
    q1 = str(q1)
    q2 = str(q2)
    t = str(t)
    commands.append(['j', q1, q2, t])

def t(x, v):
    x = str(x)
    v = str(v)
    commands.append(['t', x, v])

def s(a):
    a = str(a)
    commands.append(['s', a])

def z(a):
    a = str(a)
    commands.append(['z', a])

def p():
    commands.append(['p'])


def summ(ans, r1, r2, dop):
    cnt = len(commands)
    t(r1, ans)
    j(r2, dop, cnt + 6)
    s(ans)
    s(dop)
    j(0, 0, cnt + 2)
    z(dop)

def difference(ans, r1, r2, dop):
    cnt = len(commands)
    t(r2, dop)
    j(r1, dop, cnt + 6)
    s(ans)
    s(dop)
    j(0, 0, cnt + 2)
    z(dop)

def multiplied(ans, r1, r2, dop1, dop2):
    cnt = len(commands)
    j(r2, dop2, cnt + 9)
    j(r1, dop1, cnt + 6)
    s(ans)
    s(dop1)
    j(0, 0, cnt + 2)
    z(dop1)
    s(dop2)
    j(0, 0, cnt + 1)
    z(dop1)
    z(dop2)

def divide(ans, r1, r2, dop1, dop2):
    cnt = len(commands)
    j(r1, dop2, cnt + 9)
    j(r2, dop1, cnt + 6)
    s(dop1)
    s(dop2)
    j(0, 0, cnt + 2)
    z(dop1)
    s(ans)
    j(0, 0, cnt + 1)
    z(dop1)
    z(dop2)

def exponentiation(ans, r1, r2, dop1, dop2, dop3, dop4):
    cnt = len(commands)
    s(ans)
    j(dop1, r2, cnt + 22)
    z(ans)
    t(r1, dop4)
    s(dop3)
    j(r2, dop3, cnt + 21)
    multiplied(ans, r1, dop4, dop1, dop2)
    s(dop3)
    t(ans, dop4)
    z(ans)
    j(0,0, cnt + 6)
    t(dop4, ans)
    z(dop3)
    z(dop4)

def fact(ans, r, dop1, dop2, dop3, dop4):
    cnt = len(commands)
    s(dop3)
    t(r, dop4)
    j(r, dop3, cnt + 18)
    multiplied(ans, dop3, dop4, dop1, dop2)
    s(dop3)
    t(ans, dop4)
    z(ans)
    j(0, 0, cnt + 3)
    t(dop4, ans)
    z(dop3)
    z(dop4)

def square(ans, r, dop1, dop2, dop3):
    cnt = len(commands)
    z(dop3)
    multiplied(dop3, ans, ans, dop1, dop2)
    j(dop3, r, cnt + 15)
    s(ans)
    j(0, 0, cnt + 1)
    z(dop3)


def write_code():
    text = ""
    for i in commands:
        text += ' '.join(i) + "\n"
    print(text)
    with open("gen_code.txt", "w") as f:
        f.write(text)

def code():
    p()

if __name__ == '__main__':
    code()
    write_code()