import smtplib
from email.message import EmailMessage
import dill

# send takes in msg and text file and sends it to me
with open("email.function", 'rb') as fin:
    send = dill.load(fin)

def sendNotification(username: str, filename: str) -> None:
    send(f"{username} is starting {filename}.")

def sendFile(username: str, filename: str) -> None:
    send(f"{username} has finished {filename}.", filename)

def main():
    send("Test mail")
    # sendFile("r2dev2", "dest/Berliner.txt")

if __name__ == "__main__":
    main()
