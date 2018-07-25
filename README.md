<p align="center">
  <img width="200" height="100" src="https://github.com/bosnivan/CPPU/blob/master/Logo.png">
</p>

-	Simulacija jednostavnog 32-bitnog procesora
-	Arhitektura je slična procesoru micro:bita
-	16 registara, 1kB memorije
-	17 naredbi, labele, komentari
- Izravno podržane osnovne funkcije micro:bita; rad s pinovima i ekranom micro:bita
- Jednostavno se proširi ili prilagodi željama korisnika
- Pogodno za upoznavanje s osnovama rada procesora i asemblerskog programiranja


## Naredbe
### mov (move)
Zapisuje broj u registar. Izravno, ili iz drugog registra.
```
mov r10 30  # zapisuje 30 u registar r10
```
```
mov r11 r9  # zapisuje broj iz registra r9 u registar r11
```

### movc (move character)
Zapisuje znak u registar, tj. njegovu brojčanu ASCII vrijednost.
```
movc r0 P  # zapisuje vrijednost 80 u registar r0
```

### ldr (load)
Dohvaća podatak iz memorije.
```
ldr r0 a0  # dohvaća podatak iz memorijske adrese a0 u registar r0
```

### str (store)
Sprema podatak u memoriju.
```
str a0 r0  # sprema podatak iz registra r0 u memorijsku adresu a0
```

### add (add)
Zbrajanje.
```
add r2 r0 r1  # r2 = r0 + r1
```

### sub (subtract)
Oduzimanje.
```
sub r2 r0 r1  # r2 = r0 - r1
```

### jmp (jump)
Skoči na naredbu označenu labelom.
```
jmp zbrajanje  # skoči na naredbu označenu labelom zbrajanje
```

### jmpz (jump if zero)
Skoči na naredbu označenom labelom, samo ako je zadnja operacija rezultirala nulom.
```
jmpz zbrajanje  # ako je zadnja operacija rezultirala nulom, skoči na naredbu zbrajanje
```

### pdr (pin digital read)
Čita digitalnu vrijednost pina i sprema ju u registar.
```
pdr r0 p0  # r0 = p0 (D)
```

### pdw (pin digital write)
Zapisuje digitalnu vrijednost kao izlaz pina.
```
pdw p0 1  # p0 = 1
```
```
pdw p0 r0  # p0 = r0
```

### par (pin analog read)
Čita analognu vrijednost pina i sprema ju u registar.
```
par r0 p0  # r0 = p0 (A)
```

### paw (pin analog write)
Zapisuje analognu vrijednost kao izlaz pina.
```
paw p0 r0  # p0 = r0
```

### btn (button)
Provjerava je li gumb pritisnut.
```
btn p0 bA  # p0 = 1 ako je gumb A pritisnut, 0 inače
```

### lmw (led matrix write)
Ispisuje vrijednost registra na zaslon micro:bita.
```
lmw r0  # ispisuje se vrijednost registra r0
```

### lmwc (led matrix write character)
Ispisuje vrijednost registra na zaslonu micro:bita, kao znak (ASCII).
```
lmwc r0  # ispisuje se vrijednost registra r0, kao znak
```

### nop (no operation)
Naredba koja ništa ne radi. Zapravo, uspava program u idućih 100 ms.
```
nop  # ništa se ne događa u idućih 100 ms
```

### halt
Završava izvođenje programa.
```
halt  # program uspješno prekida s izvođenjem
```

## Primjeri
### Množenje brojeva tri i četiri te spremanje rezultata u memoriju
```
mov r0 3
mov r1 4
mov r2 1
l2: add r3 r0 r3
sub r1 r1 r2
jmpz l1
jmp l2
l1: str a0 r3
halt
```

### Množenje unešenih brojeva i ispis rezultata na micro:bitu
```
mov r0 1
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
halt
```


## Što i kako?
Datoteka [CPPU.py](https://github.com/bosnivan/CPPU/blob/master/CPPU.py) sadrži izvršni program simulatora. Napisan je u MicroPythonu za micro:bit i najbolje ga je koristiti razvojnom okruženju [Mu](https://codewith.mu/). Kopirate ga u uređivač i na označeno mjesto unesete kod programa. Ako ćete pisati složenije programe, zbog memorijskog ograničenja MicroPythona, možda će micro:bit javiti grešku manjka memorije. Tada je najbolje izbaciti dijelove simulatora koji nisu korišteni. Za drugi primjer sam to napravio u datoteci [Primjer.py](https://github.com/bosnivan/CPPU/blob/master/Primjer.py). Budući da takva dorada simulatora nije za svakoga, radim na izradi uređivača koji će prihvaćati samo kod programa i sve ostalo raditi u pozadini. Ako se pokaže zanimanje, složit ću i lekcije za upoznavanje rada procesora i asemblersko programiranje.
