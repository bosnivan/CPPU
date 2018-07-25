from microbit import *

program = """mov r0 1
l1: btn r1 bA
sub r1 r1 r0
jmpz l2
btn r1 bB
nop
sub r1 r1 r0
jmpz l3
nop
jmp l1
l2: add r2 r2 r0
lmw r2
nop
jmp l1
l3: btn r1 bA
sub r1 r1 r0
jmpz l4
btn r1 bB
nop
sub r1 r1 r0
jmpz l5
nop
jmp l3
l4: add r3 r3 r0
lmw r3
nop
jmp l3
l5: add r4 r4 r2
sub r3 r3 r0
jmpz l6
jmp l5
l6: lmw r4
halt"""

broj_registara = 16

SR = 13
LR = 14
PC = 15

registri = [0] * broj_registara

labele = {}

program = program.split('\n')
for i in range(len(program)):
    program[i] = program[i].split(' ')
    if program[i][0].endswith(':'):
        labele[program[i][0][:-1]] = i
        program[i] = program[i][1:]

while True:
    naredba = program[registri[PC]]
    if naredba[0] == 'mov':
        if naredba[2].replace('-', '').isdigit():
            registri[int(naredba[1][1:])] = int(naredba[2])
        else:
            registri[int(naredba[1][1:])] = registri[int(naredba[2][1:])]
    elif naredba[0] == 'add':
        registri[int(naredba[1][1:])] = registri[int(naredba[2][1:])] + registri[int(naredba[3][1:])]
        if registri[int(naredba[1][1:])] == 0:
            registri[SR] = 1
        else:
            registri[SR] = 0
    elif naredba[0] == 'sub':
        registri[int(naredba[1][1:])] = registri[int(naredba[2][1:])] - registri[int(naredba[3][1:])]
        if registri[int(naredba[1][1:])] == 0:
            registri[SR] = 1
        else:
            registri[SR] = 0
    elif naredba[0] == 'jmp':
        registri[PC] = labele[naredba[1]]
        continue
    elif naredba[0] == 'jmpz':
        if registri[SR] == 1:
            registri[PC] = labele[naredba[1]]
            continue
    elif naredba[0] == 'btn':
        if (naredba[2] == 'bA' and (button_a.was_pressed() or button_a.is_pressed())) or (naredba[2] == 'bB' and (button_b.was_pressed() or button_b.is_pressed())):
            registri[int(naredba[1][1:])] = 1
        else:
            registri[int(naredba[1][1:])] = 0
    elif naredba[0] == 'lmw':
        display.scroll(str(registri[int(naredba[1][1:])]))
    elif naredba[0] == 'nop':
        sleep(100)
    elif naredba[0] == 'halt':
        break
    else:
        display.scroll("Naredba je nepoznata. Prekidam izvodjenje")
        break
    registri[PC] += 1