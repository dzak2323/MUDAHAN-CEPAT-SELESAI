import json
import os
import re
import shutil

# Fungsi untuk mencetak teks di tengah
def print_centered(text):
    terminal_width = shutil.get_terminal_size().columns
    centered_text = text.center(terminal_width)
    print(centered_text)

# Fungsi untuk membersihkan layar
def bersihkanLayar():
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi untuk membaca data pengguna dari file JSON
def baca_datauser():
    if not os.path.exists('datausername.json'):
        raise FileNotFoundError("Data user tidak ditemukan")
    with open('datausername.json', 'r') as file:
        return json.load(file)

# Fungsi untuk menambahkan data pengguna ke file JSON
def tambah_datauser(user_data):
    if not os.path.exists('datausername.json'):
        raise FileNotFoundError("Data user tidak ditemukan")
    with open('datausername.json', 'r') as file:
        datauser = json.load(file)
    
    datauser["akun"].append(user_data)
    
    with open('datausername.json', 'w') as file:
        json.dump(datauser, file, indent=4)

# Fungsi validasi username
def validasi_username(username):
    if not username:
        raise ValueError("Username tidak boleh kosong.")
    if re.search(r'[^a-zA-Z0-9_]', username):
        raise ValueError("Username tidak boleh mengandung karakter spesial.")

# Fungsi validasi password
def validasi_password(password):
    if len(password) < 5:
        raise ValueError("Password harus memiliki minimal 5 karakter.")
    if not re.search(r'[A-Z]', password):
        raise ValueError("Password harus memiliki minimal satu huruf kapital.")
    if re.search(r'[^a-zA-Z0-9]', password):
        raise ValueError("Password tidak boleh mengandung karakter spesial.")

def register():
    while True:
        bersihkanLayar()
        print_centered('='* 132)
        print_centered('Anda memilih menu Register')
        print_centered('='* 132)
        
        try:
            
            username = input("\t\t\t\t\tMasukkan Username: ")
            validasi_username(username)
            
            password = input("\t\t\t\t\tMasukkan Password: ")
            validasi_password(password)
            
            new_user = {
                "username": username,
                "password": password,
                "role": "Pembeli"
            }
            tambah_datauser(new_user)
            print(f"Akun Anda berhasil terdaftar dengan ID: {username} sebagai Pembeli.")
            input("Enter...")
            bersihkanLayar()
            break
        except ValueError as e:
            bersihkanLayar()
            print(e)
            print_centered("Tekan Enter untuk mengulang program. . .")
            input("")
        except EOFError:
            bersihkanLayar()
            print_centered("Input dihentikan oleh pengguna. Program akan keluar.")
            break