from lab_3_1a import read_log


def entry_to_dict(krotka):
    result_dict = {"ip": krotka[0], "datetime": krotka[1], "request": krotka[2], "link": krotka[3], "protocol": krotka[4], "status": krotka[5], "volume": krotka[6]}
    return result_dict


if __name__ == "__main__":
    # Pobieramy listę krotek z zadania lab_3_1a
    lista_krotek = read_log()
    # tworzymy słownik z krotki z indeksem 0
    slownik = entry_to_dict(lista_krotek[0])
    # testowy wydruk     python lab_3_2a.py < NASA
    print(slownik)
