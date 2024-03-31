from lab_3_1a import read_log
from lab_3_2b import log_to_dict


def print_dict_entry_dates(slownik):
    for site, entries in slownik.items():
        slownik_zadan = {}
        for entry in entries:
            code = entry.get("status")
            if code not in slownik_zadan:
                slownik_zadan[code] = 0
            slownik_zadan[code] += 1

        # Ilość żądań po każdym site
        ilosc_requests = len(entries)

        # Wyciągamy daty pierwszego i ostatniego żądania
        data_pierwszego_zadania = entries[0]['datetime']
        data_ostatniego_zadania = entries[-1]['datetime']

        # Wypisujemy site oraz liczbę żądań
        print(f"Site: {site}, Liczba żądań: {ilosc_requests}")

        # Wypisujemy datę pierwszego i ostatniego żądania
        print(f"Data pierwszego żądania: {data_pierwszego_zadania}")
        print(f"Data ostatniego żądania: {data_ostatniego_zadania}")
        # Wypisujemy stosunek po kodu
        for code in slownik_zadan:
            print("Dla kodu: ", code, " stosunek do wszystkich: ", round(slownik_zadan[code]/ilosc_requests, 2))
        # Dodajemy odstęp pomiędzy wpisami
        print()


if __name__ == "__main__":
    # Pobieramy listę krotek z zadania lab_3_1a
    lista_krotek = read_log()
    slownik = log_to_dict(lista_krotek)

    # testowy wydruk     python lab_3_2d.py < NASA
    print_dict_entry_dates(slownik)
