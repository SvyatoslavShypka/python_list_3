import sys
from lab_3_1a import read_log


def get_entires_by_extension(lista_krotek, rozszerzenie):
    lista = []
    for log in lista_krotek:
        if log[3].endswith(rozszerzenie):
            lista.append(log)
    return lista


if __name__ == "__main__":
    dwie_listy = True
    if len(sys.argv) != 2:
        # jeżeli brak rozszerzenia lub za dużo argumentów
        raise RuntimeError("Brak rozszerzenia lub nieprawidlowy argument")
    rozszerzenie = sys.argv[1]
    # Pobieramy listę krotek z zadania lab_3_1a
    lista_krotek = read_log()

    lista = get_entires_by_extension(lista_krotek, rozszerzenie)
    # testowy wydruk     python lab_3_1e.py < NASA txt
    for log in lista:
        print(log)

