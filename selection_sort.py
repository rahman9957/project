# Data jasa desain Rahman Editing
jasa_desain = [
    {"nama": "Desain Feed Instagram", "harga": 75000},
    {"nama": "Desain Poster A3", "harga": 50000},
    {"nama": "Desain Katalog UMKM", "harga": 120000},
    {"nama": "Desain Banner", "harga": 85000}
]

# Fungsi Selection Sort dengan pilihan ascending / descending
def selectionSort(data, ascending=True):
    """
    Fungsi selectionSort adalah algoritma pengurutan yang bekerja dengan cara menemukan elemen terkecil
    (atau terbesar, tergantung pada urutan) dari list yang belum diurutkan, lalu menukarnya dengan elemen
    di posisi awal list yang belum diurutkan. Proses ini diulang hingga seluruh list terurut.
    """
    n = len(data)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (ascending and data[j]["harga"] < data[idx]["harga"]) or \
               (not ascending and data[j]["harga"] > data[idx]["harga"]):
                idx = j
        data[i], data[idx] = data[idx], data[i]
        print(f"Iterasi ke-{i+1}: {[d['harga'] for d in data]}")
    print("Proses pengurutan selesai.")
    return data

# Menjalankan fungsi
print("\n=== Pengurutan Harga Jasa Desain (Selection Sort) ===")
urutan = input("Urutkan secara ascending atau descending? (a/d): ")
asc = True if urutan.lower() == "a" else False

# Salin data biar tidak mengubah aslinya
data_urut = jasa_desain.copy()
selectionSort(data_urut, ascending=asc)

# Menampilkan hasil akhir
print("\nHasil Pengurutan:")
for jasa in data_urut:
    print(f"- {jasa['nama']} : Rp{jasa['harga']}")
