from lab_3_1a import read_log
from lab_3_2b import log_to_dict


def get_addrs(slownik):
    return list(slownik.keys())


if __name__ == "__main__":
    # Pobieramy listę krotek z zadania lab_3_1a
    lista_krotek = read_log()

    slownik = log_to_dict(lista_krotek)

    lista_sites = get_addrs(slownik)
    # testowy wydruk     python lab_3_2c.py < NASA
    print(lista_sites)
