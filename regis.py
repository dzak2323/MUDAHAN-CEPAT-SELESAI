import json
import os
import re

def bersihkanLayar():
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi untuk membaca data pengguna dari file JSON
def baca_datauser():
    if not os.path.exists('datausername.json'):
        with open('datausername.json', 'w') as file:
            json.dump({}, file)  # Membuat file JSON kosong
    with open('datausername.json', 'r') as file:
        return json.load(file)

# Fungsi untuk menulis data pengguna ke file JSON
def tulis_datauser(datauser):
    with open('datausername.json', 'w') as file:
        json.dump(datauser, file, indent=4)

# Fungsi validasi username
def validasi_username(username):
    if not username:
        return False, "Username tidak boleh kosong."
    if re.search(r'[^a-zA-Z0-9_]', username):
        return False, "Username tidak boleh mengandung karakter spesial."
    return True, ""

# Fungsi validasi password
def validasi_password(password):
    if len(password) < 5:
        return False, "Password harus memiliki minimal 5 karakter."
    if not re.search(r'[A-Z]', password):
        return False, "Password harus memiliki minimal satu huruf kapital."
    if re.search(r'[^a-zA-Z0-9]', password):
        return False, "Password tidak boleh mengandung karakter spesial."
    return True, ""

# Membaca data pengguna saat pertama kali program dijalankan
datauser = baca_datauser()

def register():
    print("""
================================ 
      Anda memilih Register 
=================================""")
    
    # Validasi username
    while True:
        userregis = input("Username: ")
        valid, message = validasi_username(userregis)
        if not valid:
            print(message)
            input("Enter...")
            bersihkanLayar()
            continue
        if userregis in datauser:
            print("Username sudah ada yang pakai, silahkan pilih yang lain")
            input("Enter...")
            bersihkanLayar()
            continue
        break
    
    # Validasi password
    while True:
        passregis = input("Password: ")
        valid, message = validasi_password(passregis)
        if not valid:
            print(message)
            input("Enter...")
            bersihkanLayar()
            continue
        break

    datauser[userregis] = {'password': passregis, 'role': 'NPC'}
    tulis_datauser(datauser)
    print(f"Akun Anda berhasil terdaftar dengan ID: {userregis} sebagai NPC.")
    input("Enter...")
    bersihkanLayar()

# Contoh penggunaan
register()
