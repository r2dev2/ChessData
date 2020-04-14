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
| @r2dev2bb8	 |	Boleslavsky.txt	 | Finished |
| @r2dev2bb8  |  Adams.txt        | Finished |
| @r2dev2bb8  |  Anderssen.txt    | Finished |
| @oliver-ni  |  Ni.txt           | Finished |
| @Chubtato  |  Benko.txt     | Finished |
| @r2dev2bb8  | BenkoGambit.txt | generating  |
| @oliver-ni  |  BenkoGambit2.txt  | Finished |
| @oliver-ni  |  Caro-KannAdv.txt  | generating |
| @oliver-ni  |  PircOtherBlack3.txt  | generating |
| Luke Zhao   |  Alburt.txt  | Finished |
| @oliver-ni  |  FourKnights.txt  | generating |
| @oliver-ni  |  English1g6.txt  | generating |
| @r2dev2bb8  |  Alekhine4Pawns.txt | Finished |
| Raymond Shao|  Akopian.txt    | generating |
| @azhang1001 |  Alekhine.txt   | generating |
| @Chubtato   |  AlekhineExchange.txt | generating |
| @r2dev2bb8  |  Alekseev.txt | Finished |
| @Kunal-Shirvastav| Anand.txt| generating |
| @r2dev2bb8  | Beliavsky.txt | Finished |
| Francis Chua| Bacrot.txt    | generating |
| Aryan Dwivedi| BecerraRivero.txt | generating |
| @AarushiM   | Andreiken.txt | generating |
| Bennie Chang| Benjamin.txt  | Finished |
| Saadhan Pittala | Azmaiparashvilieval.txt | generating |
| @r2dev2bb8  | Bogo4Nbd2.txt | generating |
| @r2dev2bb8  | Sic2Nc6-4Qc7-4Qb6.txt | generating |
| @r2dev2bb8  | SicDragon6Be2-6Bc4.txt| generating |
| @r2dev2bb8  | Sicilian2Nc3-d6.txt   | generating |
| @r2dev2bb8  | Sicilian2Nc3-e6.txt   | generating |
| @r2dev2bb8  | Sicilian2Nc6Other5.txt| generating |
| @r2dev2bb8  | Sicilian2d6-4Qxd4.txt | generating |
| @r2dev2bb8  | Sicilian2f4.txt       | generating |
| @r2dev2bb8  | SicilianAccelDragon.txt| generating|
| @r2dev2bb8  | SicilianAlapin2Nf6.txt| generating | 
| @Chubtato   | RuyLopezBreyer.txt | generating|
| @Chubtato   | RuyLopezChigorin.txt    | generating |
| @Chubtato   | RuyLopezClassical.txt   | generating |
| @Chubtato   | RuyLopezExchange.txt    | generating |
| @Chubtato   | RuyLopezFlohr-Zaitsev.txt| generating |
| @Chubtato   | RuyLopezModSteinitz.txt | generating |
| Luke Zhao   | Blackburne.txt | generating |
| Bennie Chang| Bu.txt | generating |

