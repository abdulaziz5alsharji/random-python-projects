import socket


def get_host() -> str:
    return socket.gethostname()


def getIp(host: str) -> str:
    return socket.gethostbyname(host)


if __name__ == '__main__':
    print()
    print(f"[+] Your IP : {getIp(get_host())}")
