# Data Karyawan 
karyawan = [
    ("K221", "Andita Puspa", "Manager"),
    ("K222", "Jesy Alamanda", "Kasir"),
    ("K223", "Aldo Bahrian", "Staff"),
    ("K224", "Mutia Alawia", "Pramuniaga/Sales Associate"),
    ("K225", "Putri Aisyah", "Stocker/merchandiser"),
    ("K226", "Andika Purnama", "Scurity/Satpam"),
    ("K227", "Badrun", "Cleaning Service"),
    ("K228", "Diva Laudsky", "Admin/Back Office"),
    ("K229", "Maya Agista", "Customer Service")
]

# Data Produk: ID Produk -> (Nama Produk, Harga Satuan)
produk = {
    "AB21": ("Kertas HVS A4", 42500),
    "AB22": ("Kertas HVS F4 80 gr Sinar Dunia", 54000),
    "RK01": ("Bak Stempel", 14800),
    "RD01": ("Ballpoint Snowman ", 17100),
    "AB01": ("Buku Doble Folio", 54100),
    "AB03": ("Buku Kwitansi Besar", 10700),
    "C110": ("Catridge Canon Black", 35000),
    "AB02": ("Map Bisnis File", 7000),
    "LP01": ("Lem Gum", 3000),
    "LP02": ("Tinta Stempel Biru", 14900),
    "LP03": ("Penggaris Besi", 9000),
    "C12K": ("Catridge Canon Black 110", 275000),
    "AB23": ("Tisue", 9800),
    "RK02": ("Gunting", 4900),
    "RK03": ("Staples", 21500),
    "RD02": ("Spidol White Board", 18100),
    "RD03": ("Stabilo Boss", 13100),
    "AB24": ("Kertas Transparan", 2200),
    "AB20": ("Map Dokumen", 86500)
}

# Data Transaksi: (ID Transaksi, ID Produk, Jumlah)
transaksi = [
    ("TAB21", "AB21", 4),
    ("TC110", "C110", 3),
    ("TAB20", "AB20", 1)
]

# ======= FUNGSI KARYAWAN =======
def tambah_karyawan():
    id_karyawan = input("Masukkan ID Karyawan: ")
    nama = input("Masukkan Nama: ")
    jabatan = input("Masukkan Jabatan: ")
    karyawan.append((id_karyawan, nama, jabatan))
    print("Data karyawan berhasil ditambahkan.")

def tampilkan_karyawan():
    print("\nData Karyawan:")
    for data in karyawan:
        print(f"ID: {data[0]}, Nama: {data[1]}, Jabatan: {data[2]}")

# ======= FUNGSI PRODUK =======
def tambah_produk():
    id_produk = input("Masukkan ID Produk: ").upper()
    if id_produk in produk:
        print("ID Produk sudah ada!")
        return
    nama = input("Masukkan Nama Produk: ")
    try:
        harga = int(input("Masukkan Harga Produk: "))
    except ValueError:
        print("Harga harus berupa angka.")
        return

    produk[id_produk] = (nama, harga)
    print("Produk berhasil ditambahkan.")

def tampilkan_produk():
    print("\nDaftar Produk:")
    for kode, (nama, harga) in produk.items():
        print(f"ID: {kode}, Nama: {nama}, Harga: Rp{harga}")

# ======= FUNGSI TRANSAKSI =======
def tambah_transaksi():
    id_transaksi = input("Masukkan ID Transaksi: ")
    id_produk = input("Masukkan ID Produk: ").upper()

    if id_produk not in produk:
        print("ID Produk tidak ditemukan!")
        return

    try:
        jumlah = int(input("Masukkan Jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    transaksi.append((id_transaksi, id_produk, jumlah))
    print("Transaksi berhasil ditambahkan.")

def tampilkan_transaksi():
    print("\nData Transaksi:")
    for t in transaksi:
        id_trx, id_produk, jumlah = t
        nama_produk, harga = produk.get(id_produk, ("Tidak diketahui", 0))
        total = jumlah * harga
        print(f"ID Transaksi: {id_trx}, Produk: {nama_produk}, Jumlah: {jumlah}, Harga Satuan: Rp{harga}, Total: Rp{total}")

# ======= MENU UTAMA =======
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Manajemen Karyawan")
    print("2. Manajemen Produk")
    print("3. Manajemen Transaksi")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        while True:
            print("\n-- Menu Karyawan --")
            print("1. Tambah Karyawan")
            print("2. Lihat Data Karyawan")
            print("3. Kembali ke Menu Utama")
            sub = input("Pilih menu (1-3): ")
            if sub == "1":
                tambah_karyawan()
            elif sub == "2":
                tampilkan_karyawan()
            elif sub == "3":
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan == "2":
        while True:
            print("\n-- Menu Produk --")
            print("1. Tambah Produk")
            print("2. Lihat Daftar Produk")
            print("3. Kembali ke Menu Utama")
            sub = input("Pilih menu (1-3): ")
            if sub == "1":
                tambah_produk()
            elif sub == "2":
                tampilkan_produk()
            elif sub == "3":
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan == "3":
        while True:
            print("\n-- Menu Transaksi --")
            print("1. Tambah Transaksi")
            print("2. Lihat Data Transaksi")
            print("3. Kembali ke Menu Utama")
            sub = input("Pilih menu (1-3): ")
            if sub == "1":
                tambah_transaksi()
            elif sub == "2":
                tampilkan_transaksi()
            elif sub == "3":
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
