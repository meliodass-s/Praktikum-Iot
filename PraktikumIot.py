from gpio import *
from time import *

# Fungsi callback saat sensor mendeteksi perubahan
def sensorGerakan():
    nilai = digitalRead(0)  # Membaca input dari PIR di pin 0
    if nilai == 0:
        print("Tidak ada gerakan!")
        customWrite(1, 0)    # Matikan lampu (OUTPUT 1)
        customWrite(2, 0)    # Tutup pintu garasi (OUTPUT 2)
    else:
        print("Ada gerakan!")
        customWrite(1, 1)    # Nyalakan lampu (OUTPUT 1)
        customWrite(2, 1)    # Buka pintu garasi (OUTPUT 2)

def main():
    pinMode(0, IN)             # Set pin 0 sebagai input (PIR)
    pinMode(1, OUT)            # Set pin 1 sebagai output (lampu)
    pinMode(2, OUT)            # Set pin 2 sebagai output (pintu garasi)
    add_event_detect(0, sensorGerakan)  # Deteksi event dari sensor
    while True:
        delay(100)             # Looping supaya program tetap jalan

if __name__ == "__main__":
    main()
