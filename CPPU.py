from microbit import *

program = """OVDJE IDE PROGRAM
"""

broj_adresa_memorije = 256
broj_registara = 16

SR = 13
LR = 14
PC = 15

memorija = [0] * broj_adresa_memorije
registri = [0] * broj_registara

pinovi = [pin0, pin1, pin2]

labele = {}

def int32(n):
    b = 1 << 32
    i = n % b
    return i if i < b >> 1 else i - b

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
    elif naredba[0] == 'movc':
        registri[int(naredba[1][1:])] = ord(naredba[2])
    elif naredba[0] == 'ldr':
        registri[int(naredba[1][1:])] = memorija[int(naredba[2][1:])]
    elif naredba[0] == 'str':
        memorija[int(naredba[1][1:])] = registri[int(naredba[2][1:])]
    elif naredba[0] == 'add':
        registri[int(naredba[1][1:])] = int32(registri[int(naredba[2][1:])] + registri[int(naredba[3][1:])])
        if registri[int(naredba[1][1:])] == 0:
            registri[SR] = 1
        else:
            registri[SR] = 0
    elif naredba[0] == 'sub':
        registri[int(naredba[1][1:])] = int32(registri[int(naredba[2][1:])] - registri[int(naredba[3][1:])])
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
    elif naredba[0] == 'pdr':
        registri[int(naredba[1][1:])] = pinovi[int(naredba[2][1:])].read_digital()
    elif naredba[0] == 'pdw':
        if naredba[2].isdigit():
            pinovi[int(naredba[1][1:])].write_digital(int(naredba[2]))
        else:
            pinovi[int(naredba[1][1:])].write_digital(registri[int(naredba[2][1:])])
    elif naredba[0] == 'par':
        registri[int(naredba[1][1:])] = pinovi[int(naredba[2][1:])].read_analog()
    elif naredba[0] == 'paw':
        pinovi[int(naredba[1][1:])].write_analog(registri[int(naredba[2][1:])])
    elif naredba[0] == 'btn':
        if (naredba[2] == 'bA' and (button_a.was_pressed() or button_a.is_pressed())) or (naredba[2] == 'bB' and (button_b.was_pressed() or button_b.is_pressed())):
            registri[int(naredba[1][1:])] = 1
        else:
            registri[int(naredba[1][1:])] = 0
    elif naredba[0] == 'lmw':
        display.scroll(str(registri[int(naredba[1][1:])]))
    elif naredba[0] == 'lmwc':
        display.scroll(chr(registri[int(naredba[1][1:])]))
    elif naredba[0] == 'nop':
        sleep(100)
    elif naredba[0] == 'halt':
        break
    else:
        display.scroll("Naredba je nepoznata. Prekidam izvodjenje")
        break
    registri[PC] += 1