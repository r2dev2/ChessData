import shlex
import sys
from subprocess import call
import zipfile

STOCKFISH_DOWNLOAD = {
    "win32": "https://stockfishchess.org/files/stockfish-11-win.zip",
    "linux": "https://stockfishchess.org/files/stockfish-11-linux.zip",
    "linux32": "https://stockfishchess.org/files/stockfish-11-linux.zip",
    "darwin": "https://stockfishchess.org/files/stockfish-11-mac.zip"
}

def unzip(filepath, resultpath):
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(resultpath)

def install(module):
    call(shlex.split(f"{sys.executable} -m pip install {module}"))

def main(needfish, needpychess):
    if needfish:
        link = STOCKFISH_DOWNLOAD[sys.platform]
        call(shlex.split(f"curl -o stockfish.zip {link}"))
        unzip("stockfish.zip", "stockfish/")
        print("Stockfish is in stockfish")
    if needpychess:
        install("python-chess")

if __name__ == "__main__":
    needfish = 'y' in input("Install stockfish(y/n)? ").lower()
    needpychess = 'y' in input("Install python-chess(y/n)? ").lower()
    main(needfish, needpychess)

