import pwinput
from prettytable import PrettyTable


# DATA AKUN
users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}


# DATA WISATA
daftar_wisata = {
    "1": {
        "nama": "Pantai Kuta",
        "lokasi": "Bali"
    },
    "2": {
        "nama": "Pantai Pandawa",
        "lokasi": "Bali"
    },
    "3": {
        "nama": "Raja Ampat",
        "lokasi": "Papua Barat Daya"
    }
}


# LOGIN
def login():
    print("=== LOGIN ===")

    username = input("Username: ")
    password = pwinput.pwinput("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login berhasil!")
        print("Role:", users[username]["role"])
        return users[username]["role"]

    print("Username atau password salah.")
    return None


# LIHAT WISATA
def lihat_wisata():
    print("=== DAFTAR WISATA ===")

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Wisata", "Lokasi"]

    for nomor, wisata in daftar_wisata.items():
        tabel.add_row([
            nomor,
            wisata["nama"],
            wisata["lokasi"]
        ])

    print(tabel)


# TAMBAH WISATA
def tambah_wisata():
    print("=== TAMBAH WISATA ===")

    nama = input("Nama wisata: ")
    lokasi = input("Lokasi: ")

    if nama == "" or lokasi == "":
        print("Data tidak boleh kosong.")
        return

    nomor = str(len(daftar_wisata) + 1)

    daftar_wisata[nomor] = {
        "nama": nama,
        "lokasi": lokasi
    }

    print("Wisata berhasil ditambahkan.")


# UBAH WISATA
def ubah_wisata():
    print("=== UBAH WISATA ===")

    lihat_wisata()

    nomor = input("Nomor wisata: ")

    if nomor in daftar_wisata:
        nama = input("Nama baru: ")
        lokasi = input("Lokasi baru: ")

        if nama == "" or lokasi == "":
            print("Data tidak boleh kosong.")
        else:
            daftar_wisata[nomor] = {
                "nama": nama,
                "lokasi": lokasi
            }

            print("Wisata berhasil diubah.")

    else:
        print("Nomor tidak ditemukan.")


# HAPUS WISATA
def hapus_wisata():
    print("=== HAPUS WISATA ===")

    lihat_wisata()

    nomor = input("Nomor wisata: ")

    if nomor in daftar_wisata:
        del daftar_wisata[nomor]
        print("Wisata berhasil dihapus.")

    else:
        print("Nomor tidak ditemukan.")


# MENU ADMIN
def menu_admin():
    while True:
        print("=== MENU ADMIN ===")
        print("1. Lihat wisata")
        print("2. Tambah wisata")
        print("3. Ubah wisata")
        print("4. Hapus wisata")
        print("5. Logout")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            lihat_wisata()

        elif pilihan == "2":
            tambah_wisata()

        elif pilihan == "3":
            ubah_wisata()

        elif pilihan == "4":
            hapus_wisata()

        elif pilihan == "5":
            print("Logout berhasil.")
            return

        else:
            print("Pilihan tidak tersedia.")


# MENU USER
def menu_user():
    while True:
        print("=== MENU USER ===")
        print("1. Lihat wisata")
        print("2. Logout")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            lihat_wisata()

        elif pilihan == "2":
            print("Logout berhasil.")
            return

        else:
            print("Pilihan tidak tersedia.")


# PROGRAM UTAMA
role = login()

if role == "admin":
    menu_admin()

elif role == "user":
    menu_user()

else:
    print("Login gagal.")

print("=== PROGRAM SELESAI ===")