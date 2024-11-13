from menu import *
from login import *
from regis import *
clear()
# print_centered("SELAMAT DATANG DI PROGRAM KELOMPOK 6")
# time.sleep(5)
def main():      
        while True:
                clear()
                print_centered("="*132)
                print_centered("SELAMAT DATANG DI MENU UTAMA")
                print_centered("="*132)
                print_centered("1.Login")
                print_centered("2.Register")
                print_centered("0.Keluar")
                print_centered("="*132)
                try:
                        choice = input("\t\t\t\t\t\t\t\t\t\t\t\t  Pilih menu: ").strip()

                        if not choice:
                                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh kosong.")
                        if not re.match("^[A-Za-z0-9]*$", choice):
                                raise ValueError("\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh menggunakan karakter spesial.")
                        if not any(char.isdigit() for char in choice):
                                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t     Pilihan menu harus berupa angka (0,1,2).")
                        if choice == "1":
                                statusLogin = login()  # Asumsikan fungsi login mengembalikan username yang sedang login
                                if statusLogin:
                                        for user in datauser["akun"]:
                                           if user["username"] == statusLogin["username"]:
                                                if user["role"] == "Owner":
                                                        ownerMenu()
                                                elif user["role"] == "Pembeli":
                                                        pembeliMenu()
                                                 

                        elif choice == "2":
                                register()
                        elif choice == "0":
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
                        
main()                