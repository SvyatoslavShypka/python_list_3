import sys
from lab_3_1 import read_log


def sort_log(lista, indeks):
    result = sorted(lista, key=lambda x: x[indeks])
    return result


if __name__ == "__main__":
    try:
        sort_indeks = int(sys.argv[1])
    except:
        raise RuntimeError("Nieprawidlowy argument")
    # Pobieramy listę krotek z poprzedniego zadania
    logs = read_log()
    if len(logs[0]) - 1 < sort_indeks or sort_indeks < 0:
        raise RuntimeError("Nieprawidlowy index do sortowania")
    sorted_logs = sort_log(logs, sort_indeks)
    # testowy wydruk     python lab_3_2.py < NASA 3
    for log in sorted_logs:
        print(log)
