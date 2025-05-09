from gpio import *
from time import *

def main():
    pinMode(0, IN)     # Pin 0 sebagai input (misalnya tombol)
    pinMode(1, OUT)    # Pin 1 sebagai output (misalnya LED)
    print("light on")

    while True:
        if digitalRead(0) == HIGH:
            digitalWrite(1, HIGH)  # Nyalakan LED
        else:
            digitalWrite(1, LOW)   # Matikan LED
        delay(100)  # Tambahkan delay untuk meringankan loop

if __name__ == "__main__":
    main()
