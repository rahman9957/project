# Penjelasan tentang fungsi bubbleSort:
# Fungsi bubbleSort adalah algoritma pengurutan yang bekerja dengan cara membandingkan elemen-elemen yang berdekatan
# dalam sebuah list dan menukarnya jika mereka berada dalam urutan yang salah. Proses ini diulang hingga list menjadi terurut.

def bubbleSortWithExplanation(arr):
    n = len(arr)
    for i in range(n-1):
        print(f"Iterasi ke-{i+1}:")
        for j in range(n-i-1):
            print(f"  Membandingkan {arr[j]} dan {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"  Menukar {arr[j]} dengan {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                print(f"  Tidak ada penukaran")
        print(f"List setelah iterasi ke-{i+1}: {arr}")
    print("Proses pengurutan selesai.")
    return arr

# Contoh penggunaan fungsi dengan penjelasan
# Studi kasus: Mengurutkan daftar harga jasa desain grafis Rahman Editing dari yang termurah ke termahal
arr = [75000, 50000, 100000, 65000, 85000, 45000, 120000]
print("\nDaftar harga jasa desain Rahman Editing (belum terurut):", arr)
bubbleSortWithExplanation(arr)
print("\nDaftar harga setelah diurutkan dari termurah ke termahal:", arr)