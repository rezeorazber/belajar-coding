import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nI hold imagination cover all of the sadness", 0.16),
        ("I don't feel something special", 0.11),
        ("Turn off the phone to get some spatial", 0.08),
        ("Never thought I'd living in true", 0.14),
        ("The truth that has been so blue", 0.11),
        ("It was in a blink of an eye", 0.12),
        ("Find a way how to say goodbye", 0.13),
        ("....", 0.01),
        ("....", 0.01),
        ("....", 0.01),
        ("aduh keluar dikit njirrr:v\n", 0.01),
    ]

    delays = [0.03, 8.05, 12.00, 15.10, 20.00, 23.20, 27.10, 30.20, 30.21, 30.22, 30.23]

    threads = []
    for i in range(len(lyrics)):
         lyric, speed = lyrics[i]
         t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
         threads.append(t)
         t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()