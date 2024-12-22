import socket

domain = ""
whois_server = ""
for retry in range(3):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((whois_server, 43))
            s.send(f'{domain} \r\n'.encode())
            res = s.recv(4096).decode('utf-8')
            print(res)
    except:
        continue
