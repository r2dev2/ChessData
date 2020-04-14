import os
import sys
import zipfile
from pathlib import Path
from subprocess import call
from typing import *

import evalfen
from getFile import downloadName, getAvailableNames
from send import sendFile, sendNotification

STOCKFISH_DOWNLOAD = {
    "win32": "https://stockfishchess.org/files/stockfish-11-win.zip",
    "linux": "https://stockfishchess.org/files/stockfish-11-linux.zip",
    "linux32": "https://stockfishchess.org/files/stockfish-11-linux.zip",
    "darwin": "https://stockfishchess.org/files/stockfish-11-mac.zip"
}


def unzip(filepath, resultpath):
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(resultpath)


def promptNames(names: List[str]) -> str:
    for i, name in enumerate(names):
        print(i, name, sep='\t')
    uin = int(input("Which number? "))
    return names[uin]


def promptDownload() -> bool:
    uin = input("Do you need to download any other dataset?(y)es/(n)o ")
    return 'y' in uin


def downloadStockfish() -> None:
    link = STOCKFISH_DOWNLOAD[sys.platform]
    call(["curl", "-o", "stockfish.zip", link])
    unzip("stockfish.zip", "stockfish/")


def findStockfish() -> Path:
    pass


def promptStockfish() -> Path:
    uin = input("Do you have stockfish in your current directory?(y)es/(n)o ")
    needsfish = 'y' in uin
    if needsfish:
        downloadStockfish()


def main() -> None:
    if promptDownload():
        names = list(getAvailableNames())
        names.sort()
        name = promptNames(names)
        downloadName(name)
    print("Done for now")


if __name__ == "__main__":
    main()
