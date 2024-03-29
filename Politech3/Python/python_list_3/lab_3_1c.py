import sys
from lab_3_1a import read_log


def get_entries_by_addr(lists, page):
    result = []
    for lista in lists:
        if lista[0] == page:
            result.append(lista)
    return result


if __name__ == "__main__":
    try:
        page = sys.argv[1]
    except:
        raise RuntimeError("Nieprawidlowy argument")
    # Pobieramy listę krotek z poprzedniego zadania
    logs = read_log()

    logs_from_pages = get_entries_by_addr(logs, page)
    # testowy wydruk     python lab_3_1c.py < NASA burger.letters.com
    for log in logs_from_pages:
        print(log)
