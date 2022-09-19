# Program Aplikasi CRUD 
# Capstone Project Purwadhika Modul 1
# Muhammad Nighwan Hetami 

dict_barang = {
    "RBT01" : {"Nama" : "Balon 12\"", "Jenis" : "Latex Doff 3,2gr", "Warna":"Merah", "Harga" : 12000, "Stok" : 12},
    "RBT02" : {"Nama" : "Balon Huruf", "Jenis" : "Balon Foil", "Warna" : "Gold", "Harga" : 4000, "Stok" : 100},
    "RBT03" : {"Nama" : "Balon Love", "Jenis" : "Balon Foil", "Warna" : "Merah", "Harga" : 7000, "Stok" : 20}}

dict_tambah = {}
# Menu Awal atau Utama Program
def menu__awal():
    print('''
    === Selamat Datang di Database Toko "Rumah Balon Tegal" ===
    1. Menampilkan Daftar Barang
    2. Menambah Database
    3. Mengupdate Database
    4. Menghapus Database 
    5. Keluar dari Database Toko
    ''')
    inputan = input("Masukan pilihan anda : ")
    if (inputan) == "1":
        tampil()
    elif (inputan) == "2":
        tambah()
    elif (inputan) == "3":
        update()
    elif (inputan) == "4":
        hapus()
    elif (inputan) == "5":
        print("Terima Kasih Telah Menggunakan Aplikasi Database Ini")
        exit()
    else:
        print("Pilihan yang anda masukan salah, Program akan kembali ke menu utama.")
        return menu__awal()

# Menu Tampilan Barang atau Read Program (READ)
def tampil():
    print("""
    Anda Masuk Pada Menu Tampilkan Database
    1. Tampilkan Seluruh Database
    2. Tampilkan Database Berdasarkan Kode Barang
    3. Kembali Ke Menu Utama """)
    inputan = input("\nMasukan Pilihan : ")
    # Pilihan nomor 1 untuk menampilkan seluruh isi database.
    if (inputan) == "1":
        if len(dict_barang) != 0:
            print("""
                        === Database Toko "Rumah Balon Tegal ===
                            """)
            print("| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok").upper())
            for i in dict_barang:
                print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(i, dict_barang[i]["Nama"], dict_barang[i]["Jenis"], dict_barang[i]["Warna"], dict_barang[i]["Harga"], dict_barang[i]["Stok"]))
            return tampil()
        else:
            print("Data tidak tersedia.")
            return tampil()
    # Pilihan nomor 2 untuk menampilkan database berdasarkan primary key atau kode.
    elif (inputan) == "2":
        if len(dict_barang) != 0:
            print("Data Tersedia")
            inputpk = input("Silahkan Masukan Kode Barang : ")
            if inputpk not in dict_barang:
                print(f"\nTidak Ada Data dengan Kode Barang : {inputpk}")
                return tampil()
            else:
                print("""
                        === Database Toko "Rumah Balon Tegal ===
                                """)
                print("| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok").upper())
                print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputpk, dict_barang[inputpk]["Nama"], dict_barang[inputpk]["Jenis"], dict_barang[inputpk]["Warna"], dict_barang[inputpk]["Harga"], dict_barang[inputpk]["Stok"]))
                return tampil()
        else:
            print("Tidak Ada Data")
            return tampil()
    # Pilihan nomor 3 untuk kembali ke menu utama.
    elif (inputan) == "3":
        return menu__awal()
    else:
        print("Pilihan yang anda masukan tidak tersedia")
        return tampil()

# Menu Menambahkan Data (CREATE)
def tambah():
    print("""
    Anda Masuk Pada Menu Tambah Database
    1. Menambah Database 
    2. Kembali Ke Menu Utama
    """)
    inputan = input("Masukan Pilihan: ")
    if (inputan) == "1":
        inputkode = input("Masukan Kode Barang : ")
        if inputkode.isalnum() != True or len(inputkode) < 5 or inputkode[0:3] != "RBT" or inputkode[3:].isdigit() != True:
            print("""
            Peringatan : 
            Kode barang harus berisi minimal lima karakter, 
            tiga karakater pertama harus 'RBT', dan 
            setelah tiga karakter pertama harus berisi angka""")
            return tambah()
        if inputkode in dict_barang:
            print(f"Data dengan kode barang {inputkode} sudah ada, satu kode barang hanya boleh di isi oleh satu data")
            return tambah()
        else:
            nama = (input("Masukan Nama Barang : "))
            jenis = (input("Masukan Jenis Barang : "))
            warna = (input("Masukan Warna Barang : "))
            while True:
                harga = (input("Masukan Harga Barang : "))
                if harga.isnumeric() != True:
                    print("Kolom harga hanya boleh berisi angka")
                    continue
                break
            while True:
                stok = (input("Masukan Stok Barang : "))
                if stok.isnumeric() != True:
                    print("Kolom stok hanya boleh berisi angka")
                    continue
                break
            print("| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok"))
            print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputkode, nama, jenis, warna, harga, stok))

            tanya = input("Apakah Anda yakin akan menyimpan data?\nKetik 'YES' untuk menyimpan dan tekan tombol apa saja untuk membatalkan = ").upper()
            
            dict_tambah["Nama"] = nama
            dict_tambah["Jenis"] = jenis
            dict_tambah["Warna"] = warna
            dict_tambah["Harga"] = int(harga)
            dict_tambah["Stok"] = int(stok)
            if tanya == "YES":
                print(f"Data dengan kode barang {inputkode} sudah berhasil di simpan")
                dict_barang[inputkode] = dict_tambah
                return tambah()
            else:
                return tambah()
    elif (inputan) == "2":
        return menu__awal()
    else:
        return tambah()
        
# Menu Mengupdate data (UPDATE)
def update():
    print("""
    Anda Masuk Pada Menu Update/Edit Database
    1. Update/Edit Database
    2. Kembali Ke Menu Utama
    """)
    pilihan = input("Masukan pilihan: ")
    if (pilihan) == "1":
        inputpk = input("Masukan kode barang :")
        if inputpk in dict_barang:
            print("\nData yang Anda masukan tersedia dalam database toko")
            print("| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok"))
            print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputpk, dict_barang[inputpk]["Nama"], dict_barang[inputpk]["Jenis"], dict_barang[inputpk]["Warna"], dict_barang[inputpk]["Harga"], dict_barang[inputpk]["Stok"]))
            print("""
            \nSilahkan pilih data yang ingin anda Update atau Edit
            1. Nama Barang
            2. Jenis Barang
            3. Warna Barang
            4. Harga Barang
            5. Stok Barang
            """)
            edit = input("Silahkan Masukan Pilihan Anda : ")
            if (edit) == "1":
                print("Anda akan mengubah kolom 'Nama'")
                inputnama = input("Masukan Data: ")
                tanya = input("Apakah Anda yakin akan menyimpan data?\nKetik 'YES' untuk menyimpan dan tekan tombol apa saja untuk membatalkan = ").upper()
                if tanya == "YES":
                    dict_barang[inputpk]["Nama"] = inputnama
                    print("\nData sudah berhasil di update\n| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok"))
                    print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputpk, dict_barang[inputpk]["Nama"], dict_barang[inputpk]["Jenis"], dict_barang[inputpk]["Warna"], dict_barang[inputpk]["Harga"], dict_barang[inputpk]["Stok"]))
                    return update()
                else:
                    return update()
            elif (edit) == "2":
                print("Anda akan mengubah kolom 'Jenis'")
                inputjenis = input("Masukan Data: ")
                tanya = input("Apakah Anda yakin akan menyimpan data?\nKetik 'YES' untuk menyimpan dan tekan tombol apa saja untuk membatalkan = ").upper()
                if tanya == "YES":
                    dict_barang[inputpk]["Jenis"] = inputjenis
                    print("\nData sudah berhasil di update\n| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok"))
                    print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputpk, dict_barang[inputpk]["Nama"], dict_barang[inputpk]["Jenis"], dict_barang[inputpk]["Warna"], dict_barang[inputpk]["Harga"], dict_barang[inputpk]["Stok"]))
                    return update()
                else:
                    return update()
            elif (edit) == "3":
                print("Anda akan mengubah kolom 'Warna'")
                inputwarna = input("Masukan Data: ")
                tanya = input("Apakah Anda yakin akan menyimpan data?\nKetik 'YES' untuk menyimpan dan tekan tombol apa saja untuk membatalkan = ").upper()
                if tanya == "YES":
                    dict_barang[inputpk]["Warna"] = inputwarna
                    print("\nData sudah berhasil di update\n| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok"))
                    print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputpk, dict_barang[inputpk]["Nama"], dict_barang[inputpk]["Jenis"], dict_barang[inputpk]["Warna"], dict_barang[inputpk]["Harga"], dict_barang[inputpk]["Stok"]))
                    return update()
                else:
                    return update()
            elif (edit) == "4":
                print("Anda akan mengubah kolom 'Harga'")
                while True:
                    inputharga = input("Masukan Data: ")
                    if inputharga.isnumeric() != True:
                        print("Data yang dimasukan harus berupa angka")
                        continue
                    break
                tanya = input("Apakah Anda yakin akan menyimpan data?\nKetik 'YES' untuk menyimpan dan tekan tombol apa saja untuk membatalkan = ").upper()
                if tanya == "YES":
                    dict_barang[inputpk]["Harga"] = int(inputharga)
                    print("\nData sudah berhasil di update\n| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok"))
                    print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputpk, dict_barang[inputpk]["Nama"], dict_barang[inputpk]["Jenis"], dict_barang[inputpk]["Warna"], dict_barang[inputpk]["Harga"], dict_barang[inputpk]["Stok"]))
                    return update()
                else:
                    return update()
            elif (edit) == "5":
                print("Anda akan mengubah kolom 'Stok'")
                while True:
                    inputstok = input("Masukan Data: ")
                    if inputstok.isnumeric() != True:
                        print("Data yang dimasukan hanya boleh berupa angka")
                        continue
                    break
                tanya = input("Apakah Anda yakin akan menyimpan data? 'YES' untuk menyimpan dan tekan tombol apa saja untuk membatalkan = ").upper()
                if tanya == "YES":
                    dict_barang[inputpk]["Stok"] = int(inputstok)
                    print("\nData sudah berhasil di update\n| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok"))
                    print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputpk, dict_barang[inputpk]["Nama"], dict_barang[inputpk]["Jenis"], dict_barang[inputpk]["Warna"], dict_barang[inputpk]["Harga"], dict_barang[inputpk]["Stok"]))
                    return update()
                else:
                    return update()
            else:
                print("Pilihan yang anda masukan tidak tersedia")
                return update()
        else:
            print("Data yang anda masukan tidak tersedia")
            return update()
    elif (pilihan) == "2":
        return menu__awal()
    else:
        return update()
# Menu Mengapus Data (DELETE)
def hapus():
    print("""
    Anda masuk pada menu hapus database
    1. Hapus Database
    2. Kembali ke Menu Utama
    """)
    inputan = input("Masukan pilihan Anda : ")
    if inputan == "1":
        inputpk = input("Masukan kode barang :")
        if inputpk in dict_barang:
            print("Berikut adalah data yang ingin Anda hapus")
            print("| {:6} | {:20} | {:20} | {:10} | {:10} | {:6} |".format("Kode", "Nama", "Jenis", "Warna", "Harga", "Stok"))
            print("| {:6} | {:20} | {:20} | {:10} | Rp.{:7} | {:6} |".format(inputpk, dict_barang[inputpk]["Nama"], dict_barang[inputpk]["Jenis"], dict_barang[inputpk]["Warna"], dict_barang[inputpk]["Harga"], dict_barang[inputpk]["Stok"]))
            tanya = input("Apakah anda akan mengapus data ini? 'YES' untuk menyimpan dan tekan tombol apa saja untuk membatalkan = ").upper()
            if tanya == "YES":
                dict_barang.pop(inputpk)
                print(f"Database dengan kode barang {inputpk} sudah terhapus")
            else:
                return hapus()
        else:
            print(f"Kode {inputpk} yang anda masukan tidak memiliki data")
            return hapus()
    elif inputan == "2":
        return menu__awal()
    else:
        return hapus()
while True:
    menu__awal()


