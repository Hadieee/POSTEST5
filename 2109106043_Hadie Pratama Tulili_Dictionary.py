import os


Menu = {
    'makanan1':'Nasi Goreng',
    'makanan2':'Mie Goreng',
    'makanan3':'Kwetiaw Goreng',
    'makanan4':'Ayam Goreng',
    'minuman1':'Es Kopi Hitam',
    'minuman2':'Es Kopi Susu',
    'minuman3':'Es Cokelat',
    'minuman4':'Es Stoberi'
}


def tambah_menu():
    ulang = 'Y'

    while ulang.casefold() == ("y"):
        os.system('cls')
        print("Input List Menu")
        pilihan = str(input("Menu apa yang ingin ditambahkan (Makanan/Minuman) ? : "))
        if pilihan == "Makanan":
            makanan = (str(input("Masukkan nama menu makanan yang ingin ditambahkan : ")))
            Menu['makanan5'] = makanan

        elif pilihan == "Minuman":
            minuman = (str(input("Masukkan nama menu minuman yang ingin ditambahkan : ")))
            Menu['minuman5'] = minuman

        ulang = input("Menu berhasil ditambahkan !!!\nApakah Anda Ingin Menambahkan menu lagi (Y / T) ? ")

def List_Menu():
    os.system('cls')
    print('====================================================================')
    for key in Menu:
        print(key,":", Menu[key])
    print('====================================================================')

def menu_delete():
    os.system('cls')
    ulang = 'Y'
    while ulang in ('y','Y'):
        hapus = input("Masukkan nama menu yang ingin dihapus : ")
        if hapus in Menu:
                del Menu[hapus]
                List_Menu()
                print("Menu telah dihapus")
        else:
            print("Menu tidak di temukan")
        input("Kembali ke Menu Utama")
        pilih()


def menu_update():
	List_Menu()
	edit = str(input("Input Menu yang akan di ubah namanya : ")) 
	if edit in Menu: 
		print("INPUT MENU YANG AKAN DI UPDATE ") 
		nama = (input("masukkan nama menu : "))
		Menu['makanan4'] = nama
		print("berhasil update menu")
	else : print("menu tidak ditemukan")
	input("kembali menu utama") 
    
def pilih():
    print(""" Author
    1.Tambah menu
    2.Hapus menu
    3.Ubah nama menu
    4.Keluar dari program
    """)
    pilihan = input("Masukkan pilihan : ")
    if pilihan == "1":
        tambah_menu()
        List_Menu()
        pilih()

    elif pilihan == "2":
        menu_delete()
        List_Menu()
        pilih()

    elif pilihan == "3":
        menu_update()
        List_Menu()
        pilih()

    elif pilihan == "4":
        os.system('cls')
        print("====================================================")
        print("Terimakasih telah menggunakan program ini :)\nSilahkan datang kembali")
        print("====================================================")
        exit()

List_Menu()
pilih()