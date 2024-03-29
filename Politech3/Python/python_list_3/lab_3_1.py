import sys
from datetime import datetime


def read_log():
    result = []
    for line in sys.stdin:
        line = line.strip()
        # print("line: ", line)
        if line:  # Sprawdź, czy linia nie jest pusta
            elements = line.split()
            length = len(elements)
            # print("elements: ", elements)
            # print("length: ", length)
            ip = elements[0]
            # print("ip: ", ip)
            datetime_str = elements[3][1:] + " " + elements[4][:-1]
            # print("datetime_str: ", datetime_str)
            datetime_obj = datetime.strptime(datetime_str, "%d/%b/%Y:%H:%M:%S %z")
            # print("datetime_obj: ", datetime_obj)
            # print("date: ", datetime_obj.time())
            request = None
            link = None
            protocol = None
            if elements[length - 3][-2] != '"':
                request = elements[5][1:]
                if length < 10:
                    protocol = None
                    link = elements[6][:-1]
                else:
                    protocol = elements[-3][:-1]
                    link = elements[6]

            # print("request: ", request)
            # print("link: ", link)
            # print("protocol: ", protocol)
            status_code = int(elements[length - 2])
            # print("status_code: ", status_code)
            bytes_sent = 0 if elements[length - 1] == "-" else int(elements[length - 1])

            # print("bytes_sent: ", bytes_sent)
            log_entry = (ip, datetime_obj, request, link, protocol, status_code, bytes_sent)
            result.append(log_entry)
    return result


if __name__ == "__main__":
    logs = read_log()
    for log in logs:
        print(log)
