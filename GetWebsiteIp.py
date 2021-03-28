import socket, sys


def get_ip(url: str) -> str:
    return socket.gethostbyname(url)


print(get_ip(sys.argv[1]))
