import os
list_produk = [
    {
     'ID'       : 'A001',
     'Nama'     : 'Nike Airmax',
     'Penjualan': 35,
     'Harga'    : 1800000,
     'Stok'     : 70
    },
    {
     'ID'       : 'A002',
     'Nama'     : 'Adidas',
     'Penjualan': 20,
     'Harga'    : 1500000,
     'Stok'     : 80
    },
    {
     'ID'       : 'A003',
     'Nama'     : 'Converse',
     'Penjualan': 43,
     'Harga'    : 750000,
     'Stok'     : 129
    },
    {
     'ID'       : 'A004',
     'Nama'     : 'Vans SK8',
     'Penjualan': 22,
     'Harga'    : 1650000,
     'Stok'     : 213
    },
    {
     'ID'        : 'A005',
     'Nama'     : 'Asiic gel-III',
     'Penjualan': 18,
     'Harga'    : 1250000,
     'Stok'     : 142
    }
]


#============================================================================================================
# FUNGSI READ : Menampilkan seluruh produk atau berdasarkan kode pencarian

def read_produk():   # function untuk melihat semua produk yang tersedia
    os.system('cls')
    print(f'\t============= Daftar Keseluruhan Produk =============\n')
    print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
    
    for nomor, produk in enumerate(list_produk, start=1):
        print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
        
def read_ID():    #function untuk melihat produk berdasarkan ID
    os.system('cls')
    while True:
        in_ID = input('\nMasukkan ID yang ingin dicari: ')
        if in_ID.isalnum():
            break
        else:
            print('Masukan angka (1-9) dan huruf(a-z)')
    os.system('cls')   
    found = False  # Gunakan variabel ini untuk mengecek apakah produk ditemukan
    print('\t============= Pencarian Berdasarkan ID Produk =============\n')
    print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
    
    for nomor, produk in enumerate(list_produk, start=1):
        if in_ID == produk['ID']:
            print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
            found = True
    
    if not found:
        os.system('cls')
        print(f'Produk dengan ID {in_ID} tidak ditemukan.')
    

def read_nama():      #function untuk melihat produk berdasarkan nama
    os.system('cls')
    in_nama = input('\nMasukan nama yang ingin dicari: ').lower()
    os.system('cls')
    found = False
    print(f'\t============= Pencarian Berdasarkan Nama Produk =============\n')
    print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')

    for nomor, produk in enumerate(list_produk, start=1):
        if in_nama == produk['Nama'].lower():
            print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
            found = True
    
    if not found:
        os.system('cls')
        print(f'Produk dengan Nama {in_nama} tidak ditemukan.')

def read_produk_terlaris():
    os.system('cls')
    print(f'\t============= Pencarian Berdasarkan Produk Terlaris =============\n')
    print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
    list_produk.sort(key=lambda x: x['Penjualan'], reverse=True)
    for nomor, produk in enumerate(list_produk, start = 1):
        print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
    
def read_harga_tertinggi():
    os.system('cls')
    print(f'\t============= Pencarian Berdasarkan Harga Tertinggi =============\n')
    print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
    list_produk.sort(key=lambda x: x['Harga'], reverse=True)
    for nomor, produk in enumerate(list_produk, start = 1):
        print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
    
def read_stok_terbanyak():
    os.system('cls')
    print(f'\t============= Pencarian Berdasarkan Stok Terbanyak =============\n')
    print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
    list_produk.sort(key=lambda x: x['Stok'], reverse=True)
    for nomor, produk in enumerate(list_produk, start = 1):
        print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
    

def menu_pencarian():
    os.system('cls')
    while True:
        print('''
            =================== Pencarian Kata Kunci ===================

                1. Tampilkan berdasarkan ID
                2. Tampilkan berdasarkan Nama
                3. Tampilkan berdasarkan Produk Terlaris
                4. Tampilkan berdasarkan Harga Tertinggi
                5. Tampilkan berdasarkan Stok Terbanyak
                6. Kembali 
            
            ============================================================
            ''')
        
        in_pencarian = input('Masukan nomor yang anda pilih: ')
        os.system('cls')
        if in_pencarian == '1' :
            read_ID()
        elif in_pencarian == '2' :
            read_nama()
        elif in_pencarian == '3' :
            read_produk_terlaris()
        elif in_pencarian == '4' :
            read_harga_tertinggi()
        elif in_pencarian == '5' :
            read_stok_terbanyak()        
        elif in_pencarian == '6' :
            break        
        else:
            print('=========== Masukan pilihan yang benar (1-6) ===========')

def read_data():
    os.system('cls')
    while True:
        print('''
            =========================== Menu Read ===========================
            
            1. Tampilkan seluruh produk
            2. Tampilkan berdasarkan kata pencarian
            3. Kembali ke menu utama
            
            ==================================================================
            ''')
        
        in_read = input('Masukan pilihan anda: ')
        if in_read == '1' :
            read_produk()            
        elif in_read == '2' :
            menu_pencarian()
        elif in_read == '3' :
            os.system('cls')
            break
        else :
            os.system('cls')
            print('========= Masukan Pilihan Yang Benar! ==========')
            

#============================================================================================================
# FUNGSI CREATE : menambahkan produk baru ke list produk
produk_list = []
def create_produk():
    os.system('cls')  # Untuk membersihkan layar (Windows), gunakan 'clear' untuk Linux/Mac
    while True:
        input_ID = input('Masukkan ID : ')
        if len(input_ID) == 4 and input_ID.startswith('A') and input_ID[1:].isdigit():
            if 'A001' <= input_ID <= 'A100':
                # Memeriksa apakah ID sudah ada dalam list_produk
                if any(produk['ID'] == input_ID for produk in list_produk):
                    print('ID sudah ada dalam produk_list. Masukkan ID yang berbeda.')
                else:
                    break
            else:
                print('ID harus berupa huruf dan angka sebanyak 4 digit')
        else:
            print('Masukan yang benar')
  
    # Validasi input Nama
    while True:
        input_nama = input('Masukkan Nama Produk: ')
        if input_nama.replace(" ", "").isalpha():
            break
        else:
            print('Masukan harus berupa huruf (a-z) dan boleh ada spasi.')
    
    # Validasi input Penjualan
    while True:
        input_penjualan = input('Masukkan Produk Terjual: ')
        if input_penjualan.isdigit():
            input_penjualan = int(input_penjualan)
            break
        else:
            print('Masukan angka (1-9)')

    # Validasi input Harga
    while True:
        input_harga = input('Masukkan Harga: ')
        if input_harga.isdigit():
            input_harga = int(input_harga)
            break
        else:
            print('Masukan angka (1-9)')

    # Validasi input Stok
    while True:
        input_stok = input('Masukkan Stok: ')
        if input_stok.isdigit():
            input_stok = int(input_stok)
            break
        else:
            print('Masukan angka (1-9)')

    # Menambahkan produk ke daftar produk
    tambahan = {
        'ID': input_ID,
        'Nama': input_nama,
        'Penjualan': input_penjualan,
        'Harga': input_harga,
        'Stok': input_stok
    }
    produk_list.append(tambahan)
    print('Produk berhasil ditambahkan.')

    print('Produk yang anda tambahkan adalah :', tambahan)
    os.system('cls')
    while True:
        cek_create = input('Apakah anda ingin menambahkan produk?(Y/N): ').upper()
        if cek_create == 'Y':
            list_produk.append(tambahan)
            read_produk()
            print('========== Produk telah ditambahkan ==========')
            break
        elif cek_create == 'N':
            read_produk()
            print('========== Produk tidak jadi ditambahkan ==========')
            break
        else:
            print('========== Masukan Pilihan Yang Benar ==========')
            

def create_data():
    os.system('cls')
    while True:
        print('''
            =========================== Menu Create ===========================
            
            1. Tambahkan Produk
            2. Kembali Ke Menu Utama
                        
            ===================================================================
        ''')
         
        menu_create = input('Ketik nomor yang ingin dijalankan:')
        if menu_create == '1':
            create_produk()
        elif menu_create == '2':
            os.system('cls')
            break
        else:
            os.system('cls')
            print('Pilihan yang Anda masukkan tidak valid. Silakan pilih 1 atau 2.')

#===================================================================================================
# FUNGSI UPDATE : 

def update_produk():
    os.system('cls')
    read_produk()
    in_update = input('\nMasukkan kode barang yang ingin diupdate: ')
    os.system('cls')
    nomor = 1  # Untuk memberikan nomor urutan pada produk yang sesuai

    found = False  # Variabel ini akan menunjukkan apakah setidaknya satu produk ditemukan
    print('\n=========================== Update Produk ===========================\n')
    

    for nomor, produk in enumerate(list_produk, start=1):
        if in_update == produk['ID']:
            found = True
            print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
            print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
            cek_update = input('\nMohon dikonfirmasi kembali apakah data yang ingin diupdate sudah benar? (Y/N): ').upper()
            os.system('cls')
            if cek_update == 'Y':
                while True:
                    print('''
            ============== Menu Update Berdasarkan Kata Kunci ================
            
            1. Update ID
            2. Update Nama
            3. Update Penjualan
            4. Update Harga
            5. Update Stok
            6. Selesai update data
            
            ==================================================================
                    ''')
          
                    sub_update = input('Pilih data yang ingin diubah [1-5]: ')
                    os.system('cls')
                
                    if sub_update == '1':
                        while True:
                            input_ID = input('Masukkan ID : ')
                            if len(input_ID) == 4 and input_ID.startswith('A') and input_ID[1:].isdigit():
                                if 'A001' <= input_ID <= 'A100':
                                # Memeriksa apakah ID sudah ada dalam list_produk
                                    if any(produk['ID'] == input_ID for produk in list_produk):
                                        print('ID sudah ada dalam produk_list. Masukkan ID yang berbeda.')
                                    else:
                                        produk['ID'] = input_ID
                                        print('\n========== ID berhasil Diupdate ==========\n')
                                        print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
                                        print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
                                        break  
                                else:
                                    print('ID harus berupa huruf dan angka')
                            else:
                                print('Masukan harus berupa huruf(a-z), dan angka(0-9)')

                    if sub_update == '2':
                        while True:
                            produk['Nama'] = input('Masukan Nama: ')
                            if produk['Nama'].replace(" ", "").isalpha():
                                print('\n========== ID berhasil Diupdate ==========\n')
                                print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
                                print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
                                break
                            else:
                                print('Masukan huruf (a-z)')

                    if sub_update == '3':
                        while True:
                            produk['Penjualan'] = input('Masukan produk terjual: ')
                            if produk['Penjualan'].isdigit():
                                print('\n========== ID berhasil Diupdate ==========\n')
                                print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
                                print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
                                break
                            else:
                                print('Masukan angka (0-9)')

                    if sub_update == '4':
                        while True :
                            produk['Harga'] = input('Masukan harga produk : ')
                            if produk['Harga'].isdigit():
                                print('\n========== ID berhasil Diupdate ==========\n')
                                print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
                                print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
                                break
                            else:
                                print('Masukan angka (0-9)')

                    if sub_update == '5':
                        while True:
                            produk['Stok'] = input('Masukan stok yang tersedia: ')
                            if produk['Stok'].isdigit():
                                print('\n========== ID berhasil Diupdate ==========\n')
                                print(' '+'Nomor\t|  ID\t|     Nama\t|   Penjualan\t|    Harga\t|   Stok')
                                print(f"   {nomor}\t| {produk['ID']}\t| {produk['Nama']}\t|      {produk['Penjualan']}\t|    {produk['Harga']}\t|    {produk['Stok']}")
                                break
                            else:
                                print('Masukan angka (0-9)')

                    if sub_update == '6':
                        cek_update = input(' Apakah anda sudah selesai mengubah produk?(Y/N): ').upper()
                        if cek_update == 'Y':
                            print('========== Data Selesai Diupdate ==========')
                            break
                        elif cek_update == 'N':
                            continue
                        else:
                            print('=============== Data yang anda masukan tidak tersedia ===============')
                            break

    if not found:
        os.system('cls')
        print('\n========== Kode Barang Tidak Ditemukan ==========')


def update_data():  # Fungsi untuk menampilkan menu update data
    os.system('cls')
    while True:
        print('''
            =========================== Menu Update ===========================
            
            1. Update Data
            2. Kembali ke menu utama
            
            ===================================================================
            ''')
                
        menu_update = input('Ketik nomor menu yang ingin dijalankan: ')

        if menu_update == '1':
            update_produk()
        elif menu_update == '2':
            os.system('cls')
            break
        else:
            os.system('cls')
            print('Pilihan yang Anda masukkan tidak valid. Silakan pilih 1 atau 2.')

#================================================================================================================
# FUNGSI DELETE : Menghapus Item pada List_Produk

def delete_ID():  # Fungsi untuk menghapus data
    os.system('cls')
    while True:  
        read_produk()  
        in_delete = input('\nMasukkan ID barang yang ingin dihapus: ')
        found = False  # Variabel ini akan menunjukkan apakah produk ditemukan
        for i, produk in enumerate(list_produk):
            if in_delete == produk['ID']:
                found = True
                print('\nData yang ingin dihapus adalah:', produk)
                cek_delete = input('\nApakah Anda yakin ingin menghapus data ini? (Y/N): ').upper()
                if cek_delete == 'Y':
                    del list_produk[i]
                    read_produk()
                    print('\n========== Data berhasil dihapus ==========')
                elif cek_delete == 'N':
                    read_produk()
                    print('\n========== Data tidak terhapus ==========')
                else:
                    print('\n========== Perintah yang Anda masukkan salah ==========')
                break  

        if not found:
            print('\n========== Data tidak ditemukan ==========')

        kembali = input('\nApakah Anda ingin menghapus data lain? (Y/N): ').upper()
        if kembali == 'Y':
            continue
        elif kembali == 'N':
            os.system('cls')
            break
        else:
            print('Masukan perintah yang benar (Y/N)')

def delete_nama():  # Fungsi untuk menghapus data berdasarkan nama
    os.system('cls') 
    while True:
        read_produk()  
        in_delete = input('\nMasukkan Nama Barang yang ingin dihapus: ').capitalize()
        found = False  # Variabel ini akan menunjukkan apakah produk ditemukan

        for i, produk in enumerate(list_produk):
            if in_delete == produk['Nama']:
                found = True
                print('\nData yang ingin dihapus adalah:', produk)
                cek_delete = input('\nApakah Anda yakin ingin menghapus data ini? (Y/N): ').upper()
                if cek_delete == 'Y':
                    del list_produk[i]
                    read_produk()
                    print('\n========== Data berhasil dihapus ==========')
                elif cek_delete == 'N':
                    print('\n========== Data tidak terhapus ==========')
                else:
                    print('\n========== Perintah yang Anda masukkan salah ==========')
                
                break  # Keluar dari loop setelah menemukan produk dengan nama yang sesuai

        if not found:
            print('\n========== Data tidak ditemukan ==========')

        kembali = input('\nApakah Anda ingin menghapus data lain? (Y/N): ').upper()
        if kembali == 'Y':
            continue
        elif kembali == 'N':
            os.system('cls')
            break
        else:
            print('Perintah tidak valid,Masukan perintah (Y/N)')

def delete_produk():
    os.system('cls')
    while True:
        read_produk()
        cek_del = input('\nApakah anda yakin ingin menghapus seluruh data produk?)Y/N : ').upper()
        if cek_del == 'Y':
            list_produk.clear()
            read_produk()
            print('\n\t================== Data Tidak Tersedia ==================')
            print('\n========== Seluruh Data Berhasil Dihapus ==========')
            break
        elif cek_del == 'N':
            print('========== Data Seluruh Produk Tidak Jadi Dihapus ==========')
            break
        else:
            print('Masukan Perintah Yang Benar!')
            break

def delete_data():
    os.system('cls')
    while True:
        print('''
                ======================== Menu Hapus ========================

                    1. Hapus Berdasarkan ID
                    2. Hapus Berdasarkan Nama
                    3. Hapus Seluruh Data
                    4. Kembali ke Menu Utama
                
                ============================================================
                ''')
            
        in_delete = input('Masukan nomor yang anda pilih: ')
        os.system('cls')
        if in_delete == '1' :
                delete_ID()
        elif in_delete == '2' :
                delete_nama()
        elif in_delete == '3' :
                delete_produk()
        elif in_delete == '4' :
                break       
        else:
            os.system('cls')
            print('Pilihan yang Anda masukkan tidak valid. Silakan pilih (1-4).')


#================================================================================================================
# FUNGSI KELUAR : keluar dari program

def keluar(): #fungsi untuk keluar dari aplikasi
    print('============================== Terimakasih ===========================')

def main_menu():
    
     while True:   
        print("""
            ======================== Manajemen Produk ========================

            1. Laporan Produk
            2. Menambahkan Produk
            3. Mengubah Data Produk
            4. Menghapus Data Produk
            5. Keluar

            ==================================================================
            """)

        menu = input('Ketik nomor menu yang ingin dijalankan(1-5): ')

        if menu == '1':
            read_data()
        elif menu == '2':
            create_data()
        elif menu == '3':
            update_data()
        elif menu == '4':
            delete_data()
        elif menu == '5':
            konfirmasi = input('Apakah Anda yakin ingin keluar? (Y/N): ').upper()
            # while True:
            if konfirmasi == 'Y':
                keluar()
                break
            elif konfirmasi == 'N':
                os.system('cls')
                continue
            else:
                os.system('cls')
                print('\n========== Perintah yang Anda masukkan Salah! ==========')
                continue
        else:
            os.system('cls')
            print('\n========== Perintah yang Anda masukkan Salah! ==========')


main_menu()