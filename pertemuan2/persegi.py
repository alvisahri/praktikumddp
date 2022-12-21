# Meminta masukan dari pengguna
size = int(input("Masukkan ukuran persegi: "))

# Mencetak persegi menggunakan loop
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()