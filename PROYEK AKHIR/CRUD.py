import pandas as pd
from tabulate import tabulate
import os 
import time
import shutil
import csv
os.system("pip install openpyxl")
os.system("pip install tabulate")

def save_data(df):
    df.reset_index(drop=True, inplace=True)
    df['No'] = df.index + 1
    df = df[['No', 'Nama', 'Harga Beli', 'Stok', 'Harga Jual']]
    df.to_excel('produkk.xlsx', index=False)
    df.to_csv('products.csv', index=False)

def print_centered(text):
    # Mendapatkan lebar terminal
    terminal_width = shutil.get_terminal_size().columns
    # Menghitung padding kiri agar teks berada di tengah
    centered_text = text.center(terminal_width)
    print(centered_text)

def clear():
    os.system('cls||clear')

def loading_dots(detik):
    for _ in range(3):  # Ulangi animasi beberapa kali
        print("Loading", end="")
        for dots in range(3):  # Animasi titik-titik
            print(".", end="", flush=True)
            time.sleep(detik)
        print("\r", end="", flush=True)  # Hapus baris untuk mengulang animasi
        print(" " * 10, end="\r")  # Menghapus titik-titik sebelumnya
    
# Membaca data dari file Excel
def load_data():
    try:
        df = pd.read_excel('produkk.xlsx')
        return df
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file 'products.csv' berada di direktori yang benar.")
        return pd.DataFrame()

# Menyimpan data ke file Excel dengan mengisi ulang kolom "No"
def save_data(df):
    df.reset_index(drop=True, inplace=True)  # Reset indeks untuk menghindari duplikasi
    df['No'] = df.index + 1  # Isi kolom "No" sesuai indeks (mulai dari 1)
    # Menata ulang kolom agar "No" berada di paling kiri
    df = df[['No', 'Nama', 'Harga Beli', 'Stok', 'Harga Jual']]
    df.to_excel('produkk.xlsx', index=False)

# 1. Create (Membuat Data Baru)
def add_product():
    df = load_data()
    nama = input("Masukkan nama barang: ")
    hargaBeli = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    hargaJual = float(input("Masukkan harga pokok barang: "))
    
    # Data baru yang ingin ditambahkan
    data_baru = {'Nama': [nama], 'Harga Beli': [hargaBeli], 'Stok': [stok], 'Harga Jual': [hargaJual]}
    df_baru = pd.DataFrame(data_baru)
    
    # Menggabungkan data baru dengan data yang sudah ada
    df = pd.concat([df, df_baru], ignore_index=True)
    
    # Memperbarui dan menyimpan data
    save_data(df)
    print("Data berhasil ditambahkan.\n")

# 2. Read (Membaca Data)
def read_products():
    df = load_data()
    # Menggunakan tabulate untuk tampilan yang rapi
    table = tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False)
    # Dapatkan lebar terminal
    terminal_width = shutil.get_terminal_size().columns

    # Hitung padding kiri agar tabel berada di tengah
    padding_left = (terminal_width - len(table.splitlines()[0])) // 2

    # Cetak tabel dengan padding kiri
    for line in table.splitlines():
        print(" " * padding_left + line)

# 3. Update (Memperbarui Data)
def update_product():
    df = load_data()
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    try:
        index_value = int(input("Masukkan index barang yang ingin diupdate: "))
        
        if 0 <= index_value < len(df):
            hargaBeliBaru = float(input("Masukkan harga beli baru: "))
            stok_baru = int(input("Masukkan stok baru: "))
            hargaJualBaru = float(input("Masukkan harga jual baru: "))
            
            # Update DataFrame dengan nilai baru
            df.at[index_value, 'Harga Beli'] = hargaBeliBaru
            df.at[index_value, 'Stok'] = stok_baru
            df.at[index_value, 'Harga Jual'] = hargaJualBaru
            
            # Simpan DataFrame yang telah diupdate kembali ke file Excel
            df.to_excel('produkk.xlsx', index=False)
            
            input("Produk berhasil diubah! Tekan Enter untuk melanjutkan...")
            print("Data berhasil diupdate.\n")
        else:
            print("Index tidak valid.\n")
    except ValueError as e:
        print(f"Input tidak valid: {e}\n")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}\n")

# 4. Delete (Menghapus Data)
def delete_product():
    df = load_data()
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    df = df[df['Nama'] != nama]
    save_data(df)
    print("Data berhasil dihapus.\n")

# Menghitung Profit Bersih
def calculate_profit():
    # Membaca file Excel
    df = pd.read_excel('produkk.xlsx')
    
    # Membersihkan kolom Harga Beli dan Harga Jual
    # df['Harga Beli'] = df['Harga Beli'].replace('[Rp. ]', '', regex=True).str.replace('.', '').astype(int)
    # df['Harga Jual'] = df['Harga Jual'].replace('[Rp. ]', '', regex=True).str.replace('.', '').astype(int)
    
    # Menghitung profit
    df['Profit'] = (df['Harga Jual'] - df['Harga Beli']) * df['Stok']

    # Menghitung total profit
    total_profit = df['Profit'].sum()
    save_data(df)
     # Menampilkan data dengan profit
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    print("-"*101)
    print(f"\t\t\t\t   Total Profit: Rp {total_profit:,}")
    print("-"*101)



