import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrix_rain(rows=20, columns=40, speed=0.05):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    while True:
        clear()
        for _ in range(rows):
            line = "".join(random.choice(chars + " ") for _ in range(columns))
            print(line)
        time.sleep(speed)

if __name__ == "__main__":
    try:
        matrix_rain()
    except KeyboardInterrupt:
        print("\nMatrix effect stopped.")
