import time
from tqdm import tqdm


def loading(load: int, msg: str, slp=0.1) -> None:
    for _ in tqdm(range(load), desc=msg, ascii=False):
        time.sleep(slp)


if __name__ == '__main__':
    loading(100, "Downloading")
