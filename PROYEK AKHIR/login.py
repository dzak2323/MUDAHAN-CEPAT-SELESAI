import json
import re
import shutil
import os

# Fungsi untuk mencetak teks di tengah
def print_centered(text):
    terminal_width = shutil.get_terminal_size().columns
    centered_text = text.center(terminal_width)
    print(centered_text)

# Fungsi untuk membersihkan layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk membaca data pengguna dari file JSON
def baca_datauser():
    if not os.path.exists('datausername.json'):
        raise FileNotFoundError("Data user tidak ditemukan")
    with open('datausername.json', 'r') as file:
        return json.load(file)

# Fungsi untuk menulis data pengguna ke file JSON
def tulis_datauser(datauser):
    with open('datausername.json', 'w') as file:
        json.dump(datauser, file, indent=4)

# Validasi username
def validate_username(username):
    if not username:
        raise ValueError("Username tidak boleh kosong.")
    if len(username) <= 5:
        raise ValueError("Username harus lebih dari 5 karakter.")
    if not re.match("^[A-Za-z0-9]*$", username):
        raise ValueError("Username tidak boleh menggunakan karakter spesial.")
    if not any(char.isdigit() for char in username):
        raise ValueError("Username harus mengandung minimal 1 angka.")
    if not any(char.isupper() for char in username):
        raise ValueError("Username harus mengandung minimal 1 huruf kapital.")

# Validasi password
def validate_password(password):
    if not password:
        raise ValueError("Password tidak boleh kosong.")
    if len(password) <= 5:
        raise ValueError("Password harus lebih dari 5 karakter.")
    if not re.match("^[A-Za-z0-9]*$", password):
        raise ValueError("Password tidak boleh menggunakan karakter spesial.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password harus mengandung minimal 1 angka.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password harus mengandung minimal 1 huruf kapital.")

# Membaca data pengguna
datauser = baca_datauser()

# Fungsi login
def login():
    while True:
        clear()
        print_centered('='* 132)
        print_centered('Anda memilih menu login')
        print_centered('='* 132)
        username = input("\t\t\t\t\tMasukkan Username : ").strip()
        password = input("\t\t\t\t\tMasukkan Password : ").strip()
        
        try:
            # Validasi username dan password
            validate_username(username)
            validate_password(password)

            # Cek apakah username ada di datauser dan password sesuai
            akun = next((item for item in datauser["akun"] if item["username"] == username), None)
            if akun and akun['password'] == password:
                print(f"Akun Anda berhasil login dengan ID: {username} sebagai {akun['role']}.")
                input("Tekan enter untuk melanjutkan. . . . .")
                return akun
            else:
                print("Username atau password salah.")
                input("Tekan enter untuk melanjutkan. . . . .")
        
        except ValueError as e:
            print(e)
            input("Tekan enter untuk melanjutkan. . . . .")

        except FileNotFoundError as fnfe:
            print(fnfe)
            input("Tekan enter untuk keluar.")
            break

# print(datauser)