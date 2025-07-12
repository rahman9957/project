def search(arr, x):
    # Fungsi untuk mencari indeks x dalam array
    index = []
    for i in range(len(arr)):
        if arr[i] == x:
            index.append(i)
    return index

# Array awal
arr = [2, 4, 3, 13, 4, 24, 10, 4, 41, 24, 3, 3]
x = 3

# Menampilkan isi array
print("Isi array data:", arr)

# Menghitung jumlah angka 3 dalam array
print("Banyaknya angka 3:", arr.count(x))

# Mengurutkan array secara ascending
arr_sorted_asc = sorted(arr)
print("Array setelah sorting ascending:", arr_sorted_asc)

# Mencari posisi angka 3 dalam array ascending
result = search(arr_sorted_asc, x)
if result:
    print(f"Elemen {x} ada pada indeks {result} dalam array ascending")
else:
    print(f"Elemen {x} tidak ada pada array")

# Mengurutkan array secara descending
arr_sorted_desc = sorted(arr, reverse=True)
print("Array setelah sorting descending:", arr_sorted_desc)

# Mencari posisi angka 3 dalam array descending
result = search(arr_sorted_desc, x)
if result:
    print(f"Elemen {x} ada pada indeks {result} dalam array descending")
else:
    print(f"Elemen {x} tidak ada pada array")

# Menghapus data ganda dari array
arr_unique = list(dict.fromkeys(arr))
print("Array setelah menghapus data ganda:", arr_unique)

# Mencari posisi angka 3 dalam array unik
result = search(arr_unique, x)
if result:
    print(f"Elemen {x} ada pada indeks {result} dalam array yang data gandanya sudah dihapus")
else:
    print(f"Elemen {x} tidak ada pada array yang data gandanya sudah dihapus")
