# Data harga jasa desain
jasa_desain = [
    {"nama": "Desain Feed Instagram", "harga": 75000},
    {"nama": "Desain Poster A3", "harga": 50000},
    {"nama": "Desain Katalog UMKM", "harga": 120000},
    {"nama": "Desain Banner", "harga": 85000}
]

# Fungsi Merge Sort dengan ascending/descending
def merge_sort(data, ascending=True):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid], ascending)
    right = merge_sort(data[mid:], ascending)

    return merge(left, right, ascending)

# Fungsi merge dua bagian terurut
def merge(left, right, ascending):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (ascending and left[i]['harga'] <= right[j]['harga']) or \
           (not ascending and left[i]['harga'] >= right[j]['harga']):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Menjalankan fungsi
print("=== Pengurutan Harga Jasa Desain Rahman Editing (Merge Sort) ===")
pilih = input("Urutkan secara ascending atau descending? (a/d): ")
asc = True if pilih.lower() == 'a' else False

# Salin data agar tidak mengubah data asli
data_urut = jasa_desain.copy()
hasil = merge_sort(data_urut, ascending=asc)

# Menampilkan hasil
print("\nHasil Pengurutan:")
for jasa in hasil:
    print(f"- {jasa['nama']} : Rp{jasa['harga']}")
