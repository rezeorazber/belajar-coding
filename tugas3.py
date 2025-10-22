nama = "Daru Trifrediyanto"
nim = "5250411151"
password = "admin123"
tanggal_lahir = "27 Juli 2006"
alamat = "Sunten"

def login(input_nim, input_password):
    if input_nim == nim and input_password == password:
        return True
    else:
        print("NIM atau password salah!")

def tampilkanProfil():
    print("===== PROFIL PENGGUNA =====")
    print("Nama: " + nama)
    print("NIM: " + nim)
    print("Tanggal Lahir: " + tanggal_lahir)
    print("Alamat: " + alamat)
    print("===========================")

def hitungRataRata(tugas_pertama, tugas_kedua, tugas_ketiga):
    rata_rata = (0.25 * tugas_pertama) + (0.25 * tugas_kedua) + (0.5 * tugas_ketiga)
    return rata_rata

print()
print("===== SELAMAT DATANG DI SISTEM MAHASISWA =====")
print()
print("Silakan login untuk melanjutkan.")
print()
input_nim_user = input("Masukkan NIM: ")
input_password_user = input("Masukkan Password: ")

if login(input_nim_user, input_password_user):
    print("Login berhasil! Selamat datang, " + nama)
    while True:
        print("===== DASHBOARD MAHASISWA =====")
        print("1. Lihat Profil Pengguna")
        print("2. Hitung Nilai Rata-rata tugas")
        print("3. Logout")
        
        pilihan_menu = input("Silakan pilih menu (1-3): ")
        
        if pilihan_menu == "1":
            tampilkanProfil()
            
        elif pilihan_menu == "2":
            print("--- Hitung Rata-rata Nilai Tugas ---")
            
            nilai_tugas_1 = float(input("Masukkan nilai tugas pertama (1-100): "))
            nilai_tugas_2 = float(input("Masukkan nilai tugas kedua (1-100): "))
            nilai_tugas_3 = float(input("Masukkan nilai tugas ketiga (1-100): "))
            hasil_rata_rata = hitungRataRata(nilai_tugas_1, nilai_tugas_2, nilai_tugas_3)
            print("Nilai rata-rata kamu adalah : ", hasil_rata_rata)
            
        elif pilihan_menu == "3":
            print("Terima kasih sudah berkunjung!")
            break

