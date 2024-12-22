import concurrent.futures
import json
import socket

from utils import GenerateDomain


def domain_is_ok(domain, domain_server_dict, retry_n=3):
    whois_server = domain_server_dict[domain.split('.')[-1]]['whois_server']
    data_mark = domain_server_dict[domain.split('.')[-1]]['data_mark']
    for retry in range(retry_n):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((whois_server, 43))
                s.send(f'{domain} \r\n'.encode())
                res = s.recv(4096).decode('utf-8')
                # print(res)
                return data_mark in res, domain, str(data_mark in res)
        except:
            continue
    else:
        return False, domain, "socket error"


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = []

        gd = GenerateDomain("tg")
        domains = gd.generate_domains("ll")
        # domains = gd.generate_xa(3)
        for domain in domains:
            with open("domain_suffix.json", "r") as f:
                domain_server_dict = json.loads(f.read())
            futures.append(executor.submit(domain_is_ok, domain, domain_server_dict))

        for future in concurrent.futures.as_completed(futures):
            try:
                is_ok, domain, msg = future.result()
                if is_ok:
                    print(domain, msg)
            except Exception as e:
                print(f"线程执行出错：{e}")
