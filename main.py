#Made by Arnolds Kumpiņš and Ralfs Bemberis

def saskaitisana(numurs1, numurs2):
    return numurs1 + numurs2

def atnemsana(numurs1, numurs2):
    return numurs1 - numurs2

def reizinasana(numurs1, numurs2):
    return numurs1 * numurs2

def dalisana(numurs1, numurs2):
    return numurs1 / numurs2

def kapinasana(numurs1, numurs2):
    return numurs1 ** numurs2

def modulis(numurs1, numurs2):
    return numurs1 % numurs2

def dalisana_bez_komatiem(numurs1, numurs2):
    return numurs1 // numurs2
  
print("Lūdzu izvēlaties opciju -\n" \
        "1. Saskaitīt\n" \
        "2. Atņemt\n" \
        "3. Sareizināt\n" \
        "4. Izdalīt\n" \
        "5. Kāpināt\n" \
        "6. Modulis\n" \
        "7. Dalisana bez komatiem\n" )
 
select = int(input("Izvēlies opciju - 1, 2, 3, 4, 5, 6, 7 :"))
  
pirmais_skaitlis = int(input("Ievadiet pirmo skaitli: "))
otrais_skaitlis = int(input("Ievadiet otro skaitli: "))
  
if select == 1:
    print(pirmais_skaitlis, "+", otrais_skaitlis, "=",
                    saskaitisana(pirmais_skaitlis, otrais_skaitlis))
  
elif select == 2:
    print(pirmais_skaitlis, "-", otrais_skaitlis, "=",
                    atnemsana(pirmais_skaitlis, otrais_skaitlis))
  
elif select == 3:
    print(pirmais_skaitlis, "*", otrais_skaitlis, "=",
                    reizinasana(pirmais_skaitlis, otrais_skaitlis))
  
elif select == 4:
    print(pirmais_skaitlis, "/", otrais_skaitlis, "=",
                    dalisana(pirmais_skaitlis, otrais_skaitlis))
elif select == 5:
    print(pirmais_skaitlis, "**", otrais_skaitlis, "=",
                   kapinasana(pirmais_skaitlis, otrais_skaitlis))
elif select == 6:
    print(pirmais_skaitlis, "%", otrais_skaitlis, "=",
                   modulis(pirmais_skaitlis, otrais_skaitlis))
elif select == 7:
    print(pirmais_skaitlis, "//", otrais_skaitlis, "=",
                   dalisana_bez_komatiem(pirmais_skaitlis, otrais_skaitlis))
else:
    print("Nepareiza ievade")