import sys
from lab_3_1a import read_log


def print_entries(lista_krotek, ilosc):
    for log in lista_krotek:
        if ilosc == 0:
            break
        print(log)
        ilosc -= 1



if __name__ == "__main__":
    dwie_listy = True
    if len(sys.argv) != 2:
        # jeżeli brak rozszerzenia lub za dużo argumentów
        raise RuntimeError("Brak rozszerzenia lub nieprawidlowy argument")
    try:
        ilosc = int(sys.argv[1])
        if ilosc < 0:
            raise RuntimeError("Ilość nie może być cyfrą ujemną")
    except:
        raise RuntimeError("Ilość nie jest cyfrą całkowitą")
    # Pobieramy listę krotek z zadania lab_3_1a
    lista_krotek = read_log()

    # testowy wydruk     python lab_3_1f.py < NASA 5
    print_entries(lista_krotek, ilosc)
