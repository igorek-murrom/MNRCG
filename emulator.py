registers = [0]


commands = []
registers += [0] * 1000


def j(q1: int, q2: int, to: int) -> int:
    if len(commands) < to: error_catch(0)
    if registers[q1] == registers[q2]:
        return to - 1
    return -1

def t(x: int, v: int):
    registers[v] = registers[x]

def z(a: int):
    registers[a] = 0

def s(a: int):
    registers[a] += 1

def p():
    print(registers)


def parse() -> list:
    global commands
    with open("code.txt", 'r') as f:
        commands = f.read().split('\n')

    for i in range(len(commands)):
        commands[i] = commands[i].split(' ')
        for j in range(1, len(commands[i])):
            commands[i][j] = int(commands[i][j])

    return commands


def check_health():
    global commands
    for i in range(len(commands)):
        comm = commands[i][0]
        length = len(commands[i])

        if comm == 'j' and length != 4: return False, i
        if comm == 't' and length != 3: return False, i
        if comm == 's' and length != 2: return False, i
        if comm == 'z' and length != 2: return False, i

    return True, 0


def emulation():
    global commands

    i = 0
    while i < len(commands):
        command = commands[i]
        comm = command[0]

        print(comm, registers)

        if comm == 'p':
            p()
        if comm == 's':
            s(command[1])
        if comm == 'z':
            z(command[1])
        if comm == 't':
            t(command[1], command[2])
        if comm == 'j':
            out = j(command[1], command[2], command[3])
            if out != -1:
                i = out
                continue
        i += 1


def error_catch(number: int):
    print(f"error on line {number + 1}")
    quit()

if __name__ == "__main__":
    commands = parse()
    status, num = check_health()

    if not status:
        error_catch(num)

    # print(registers)
    emulation()
