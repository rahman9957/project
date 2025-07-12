# Data jasa desain Rahman Editing
jasa_desain = [
    {"nama": "Desain Feed Instagram", "harga": 75000},
    {"nama": "Desain Poster A3", "harga": 50000},
    {"nama": "Desain Katalog UMKM", "harga": 120000},
    {"nama": "Desain Banner", "harga": 85000}
]

# Fungsi Insertion Sort dengan ascending/descending
def insertionSort(data, ascending=True):
    """
    Fungsi insertionSort adalah algoritma pengurutan yang bekerja dengan menyisipkan elemen pada
    posisi yang tepat di bagian list yang sudah terurut. Proses ini diulang sampai seluruh elemen
    berada dalam urutan yang benar.
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and (
            (ascending and data[j]["harga"] > key["harga"]) or
            (not ascending and data[j]["harga"] < key["harga"])
        ):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        print(f"Iterasi ke-{i}: {[d['harga'] for d in data]}")
    print("Proses pengurutan selesai.")
    return data

# Menjalankan fungsi
print("\n=== Pengurutan Harga Jasa Desain (Insertion Sort) ===")
urutan = input("Urutkan secara ascending atau descending? (a/d): ")
asc = True if urutan.lower() == "a" else False

# Salin data agar data asli tidak berubah
data_urut = jasa_desain.copy()
insertionSort(data_urut, ascending=asc)

# Tampilkan hasil akhir
print("\nHasil Pengurutan:")
for jasa in data_urut:
    print(f"- {jasa['nama']} : Rp{jasa['harga']}")
