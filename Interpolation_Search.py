def interpolation_search(data, target):
    """
    Melakukan pencarian harga jasa menggunakan Interpolation Search
    dengan data list of dictionary.
    """
    # Sorting berdasarkan harga dulu
    data = sorted(data, key=lambda x: x['harga'])
    low = 0
    high = len(data) - 1

    while low <= high and data[low]['harga'] <= target <= data[high]['harga']:
        if data[high]['harga'] == data[low]['harga']:
            break

        pos = low + ((target - data[low]['harga']) * (high - low)) // \
              (data[high]['harga'] - data[low]['harga'])

        if pos >= len(data):
            break

        if data[pos]['harga'] == target:
            return pos, data[pos]
        elif data[pos]['harga'] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, None

# Data Rahman Editing
jasa_desain = [
    {"nama": "Desain Feed Instagram", "harga": 75000},
    {"nama": "Desain Banner", "harga": 85000},
    {"nama": "Desain Katalog", "harga": 120000},
    {"nama": "Desain Poster A3", "harga": 50000},
    {"nama": "Desain CV", "harga": 65000}
]

# Input dari user
target = int(input("Masukkan harga jasa yang dicari: "))
index, jasa = interpolation_search(jasa_desain, target)

if index != -1:
    print(f"✅ Ditemukan di indeks {index}: {jasa['nama']} - Rp{jasa['harga']}")
else:
    print("❌ Harga tidak ditemukan dalam data jasa Rahman Editing.")
