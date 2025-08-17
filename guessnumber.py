import random

angka_sistem = random.randint(1, 100)
print("--GAME TEBAK ANGKA--")
nama_user = input("Masukkan namamu: ")

print(f"\nHalo {nama_user} Selamat Datang di Game Tebak Angka!")
print("\nAku memiliki sebuah angka dari 1-100, bisakah kamu menebak angka berapa itu?")

while True:
    try:
        angka_user = int(input("Masukkan angka: "))

        if angka_user < angka_sistem:
            print(
                "\nAngka yang kamu pilih terlalu rendah!")
        elif angka_user > angka_sistem:
            print(
                "\nAngka yang kamu pilih terlalu tinggi!")
        else:
            print("\nSELAMAT, KAMU MENANG!")
            break

    except ValueError:
        print("Tolong berikan angka yang valid!")
