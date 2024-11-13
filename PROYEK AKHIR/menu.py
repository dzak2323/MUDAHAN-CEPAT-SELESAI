from CRUD import *
import re
# Menu CRUD
def ownerMenu():
    while True:
        clear()
        print_centered("="*132)
        print_centered("MENU TOKO MEBEL")
        print_centered("="*132)
        print_centered("1. Tambah Produk")
        print_centered("2. Lihat Produk")
        print_centered("3. Update Produk")
        print_centered("4. Hapus Produk")
        print_centered("5. Lihat Profit")
        print_centered("6. Keluar")
        print_centered("="*132)
        try:
            choice = input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Pilih menu (1-6): ")
            if not choice:
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh kosong.")
            if not re.match("^[A-Za-z0-9]*$", choice):
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh menggunakan karakter spesial.")
            if not any(char.isdigit() for char in choice):
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t      Pilihan menu harus berupa angka (0,1,2).")
            if choice == '1':
                clear()
                loading_dots(0.3)
                print("Selesai!")
                add_product()
            elif choice == '2':
                clear()
                loading_dots(0.3)
                print("Selesai!")
                input("Tekan Enter. . . .")
                clear()
                read_products()
                print_centered("-"*87)
                print_centered("TEKAN ENTER UNTUK MELANJUTKAN. . . .")
                print_centered("-"*87)
                input("")
            elif choice == '3':
                clear()
                read_products()
                update_product()
            elif choice == '4':
                delete_product()
            elif choice == '5':
                clear()
                loading_dots(0.3)
                print("Selesai!")
                calculate_profit()
                input("\nTekan Enter. . . .")
            elif choice == '6':
                clear()
                print_centered("Keluar dari program.")
                time.sleep(3)
                break
            else:
                print("Pilihan tidak valid.\n")
        except Exception as e:
           clear()
           print(e)
           print_centered("Tekan Enter untuk mengulang program. . .")
           input("")

def pembeliMenu():
    while True:
        clear()
        print_centered("="*132)
        print_centered("MENU TOKO MEBEL")
        print_centered("="*132)
        print_centered("1. Lihat Produk")
        print_centered("2. Update Produk")
        print_centered("3. Keluar")
        print_centered("="*132)
        try:
            choice = input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Pilih menu: ")
            if not choice:
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh kosong.")
            if not re.match("^[A-Za-z0-9]*$", choice):
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh menggunakan karakter spesial.")
            if not any(char.isdigit() for char in choice):
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t      Pilihan menu harus berupa angka (0,1,2).")
            if choice == '1':
                clear()
                loading_dots(0.3)
                print("Selesai!")
                read_products()
            elif choice == '2':
                clear()
                loading_dots(0.3)
                print("Selesai!")
                input("Tekan Enter. . . .")
                clear()
                read_products()
                update_product()
                print_centered("-"*87)
                print_centered("TEKAN ENTER UNTUK MELANJUTKAN. . . .")
                print_centered("-"*87)
                input("")
            elif choice == '3':
                clear()
                print_centered("Terimakasih Telah Menggunakan Program Kami. . . .")
                time.sleep(5)
                clear()
                print_centered("Tekan Enter untuk mengakhiri program. . . .")
                input("")
                exit()
        except Exception as e:
           clear()
           print(e)
           print_centered("Tekan Enter untuk mengulang program. . .")
           input("")