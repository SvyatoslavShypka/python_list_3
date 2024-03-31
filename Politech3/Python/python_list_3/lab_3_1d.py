import sys
from lab_3_1a import read_log


def get_failed_reads(lista_krotek, dwie_listy):
    listy = []
    lista_all = []
    lista4xx = []
    lista5xx = []
    if dwie_listy:
        for log in lista_krotek:
            if 400 <= log[5] < 500:
                lista4xx.append(log)
            else:
                if 500 <= log[5] < 600:
                    lista5xx.append(log)
        listy.append(lista4xx)
        listy.append(lista5xx)
    else:
        for log in lista_krotek:
            if 400 <= log[5] < 600:
                lista_all.append(log)
        listy.append(lista_all)
    return listy


if __name__ == "__main__":
    dwie_listy = True
    try:
        if len(sys.argv) == 2:
            # bez opcjonalnego parametru - zwracamy dwie listy
            if sys.argv[1] == '1':
                dwie_listy = False
            elif sys.argv[1] == '2':
                dwie_listy = True
            else:
                raise RuntimeError("Nieprawidlowy argument")
        # z opcjonalnym parametrem (jakimkolwiek) - zwracamy jedną listę
        # dwie_listy = False
    except:
        raise RuntimeError("Nieprawidlowy argument")
    # print(dwie_listy)
    # Pobieramy listę krotek z zadania lab_3_1a
    lista_krotek = read_log()

    listy = get_failed_reads(lista_krotek, dwie_listy)
    # testowy wydruk     python lab_3_1d.py < NASA 1
    for lista in listy:
        # print("lista")
        for log in lista:
            print(log)

