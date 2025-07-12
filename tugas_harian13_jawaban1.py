def search(arr, n, x):
    # Membuat list kosong untuk menampung indeks yang ditemukan
    index = []
    for i in range(0, n):
        if arr[i] == x:
            index.append(i)
    return index

# Array yang berisi kumpulan angka
arr = [2, 4, 3, 13, 4, 24, 10, 4, 41, 24, 3, 3]
n = len(arr)

# Input dari user
x = int(input("Masukkan nilai yang dicari : "))

# Memanggil fungsi search
result = search(arr, n, x)

# Menampilkan hasil
if result:
    print("Elemen ditemukan pada indeks:", result)
else:
    print("Elemen tidak ditemukan dalam array.")
