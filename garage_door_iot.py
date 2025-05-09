from gpio import *
from time import *

def sensorGerakan():
    nilai = digitalRead(0)
    if nilai == 0:
        print("Tidak ada gerakan!")
        customWrite(1, 0)
        customWrite(2, 0)
    else:
        print("Ada gerakan!")
        customWrite(1, 1)
        customWrite(2, 1)

def main():
    add_event_detect(0, sensorGerakan)
    while True:
        delay(100)

if __name__ == "__main__":
    main()
