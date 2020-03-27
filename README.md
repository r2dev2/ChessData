# ChessData
This is a dataset which contains millions of positions with a Stockfish evaluation. Please help contribute evaluations of the positions to the repo

## Prerequisites
Prerequisites include python3, python-chess, and stockfish.
To setup:

On Windows,

``python setup.py``

On other systems,

``python3 setup.py``

## Contributing
To get started, chose a fen database to analyse that isn't currently being analysed.
Use evalfen.py to analyse the dataset

On Windows,

``python evalfen.py -h``

On other systems,

``python3 evalfen.py -h``


The evaluation should go in fen folder for now

Current fen databases being analysed:

| User	 |	Fen Database | Status |
| -------|-------------- | ------ |
| @r2dev2bb8	 |	Bogoljubow.txt	 | finished |
| @r2dev2bb8  |  Adams.txt        | generating |
| @r2dev2bb8  |  Anderssen.txt    | generating |
| @oliver-ni  |  Ni.txt           | generating |
| @Chubtato  |  Benko.txt     | generating |
| @r2dev2bb8  | BenkoGambit.txt | generating  |
