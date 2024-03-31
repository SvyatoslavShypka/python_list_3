from lab_3_1a import read_log
from lab_3_2a import entry_to_dict


def log_to_dict(lista_krotek):
    result_dict = {}
    for krotka in lista_krotek:
        site = krotka[0]
        # jeżeli jeszcze nie mamy listy w słowniku - tworzymy nową
        if site not in result_dict:
            result_dict[site] = []
        result_dict[site].append(entry_to_dict(krotka))
    return result_dict


if __name__ == "__main__":
    # Pobieramy listę krotek z zadania lab_3_1a
    lista_krotek = read_log()

    slownik = log_to_dict(lista_krotek)
    # testowy wydruk     python lab_3_2b.py < NASA
    print(slownik)
