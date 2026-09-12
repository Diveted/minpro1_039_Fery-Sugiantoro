koleksi_game = []

while True:
    print("===== SISTEM KOLEKSI GAME FERY KUMAR =====")
    print("1. tambah data game")
    print("2. tampilkan data game")
    print("3. ubah data game")
    print("4. hapus data game")
    print("5. keluar")
    print("====================================")

    pilihan = input("pilih menu (1-5): ")

    if pilihan == "1":
        print("\n--- tambah data game ---")

        nama = input("masukkan nama game: ")
        genre = input("masukkan genre game: ")
        platform = input("masukan platform: ")

        while True:
            print("status game:")
            print("1. belum dimainkan")
            print("2. sedang dimainkan")
            print("3. sudah tamat")

            status_pilihan = input("pilih status (1-3): ")

            if status_pilihan == "1":
                status = "belum dimainkan"
                break
            elif status_pilihan == "2":
                status = "sedang dimainkan"
                break
            elif status_pilihan == "3":
                status = "sudah tamat"
                break
            else:
                print("pilihan status tidak valid!")

        data_game = [nama, genre, platform, status]
        koleksi_game.append(data_game)

        print("\ndata game berhasil ditambahkan!")

    elif pilihan == "2":
        print("\n--- Data Koleksi Game ---")

        if len(koleksi_game) == 0:
            print("belum ada data game.")
        else:
            for i in range(len(koleksi_game)):
                print("\ndata ke-", i + 1)
                print("nama Game :", koleksi_game[i][0])
                print("genre     :", koleksi_game[i][1])
                print("platform  :", koleksi_game[i][2])
                print("status    :", koleksi_game[i][3])

    elif pilihan == "3":
        print("\n--- ubah Data Game ---")

        if len(koleksi_game) == 0:
            print("belum ada data game yang dapat diubah.")
        else:
            for i in range(len(koleksi_game)):
                print(i + 1, ".", koleksi_game[i][0])

            while True:
                nomor = input("pilih nomor data yang ingin diubah: ")

                if nomor.isdigit():
                    nomor = int(nomor)

                    if nomor >= 1 and nomor <= len(koleksi_game):
                        break
                    else:
                        print("nomor data tidak tersedia!")
                else:
                    print("masukkan nomor berupa angka!")

            index = nomor - 1

            print("\ndata lama:")
            print("nama Game :", koleksi_game[index][0])
            print("genre     :", koleksi_game[index][1])
            print("platform  :", koleksi_game[index][2])
            print("status    :", koleksi_game[index][3])

            nama_baru = input("\nmasukkan nama game baru: ")
            genre_baru = input("masukkan genre baru: ")
            platform_baru = input("masukkan platform baru: ")

            while True:
                print("status Game:")
                print("1. belum dimainkan")
                print("2. sedang dimainkan")
                print("3. sudah tamat")

                status_pilihan = input("pilih status (1-3): ")

                if status_pilihan == "1":
                    status_baru = "belum dimainkan"
                    break
                elif status_pilihan == "2":
                    status_baru = "sedang dimainkan"
                    break
                elif status_pilihan == "3":
                    status_baru = "sudah tamat"
                    break
                else:
                    print("pilihan status tidak valid!")

            koleksi_game[index] = [nama_baru, genre_baru, platform_baru, status_baru]

            print("\ndata game berhasil diubah!")

    elif pilihan == "4":
        print("\n--- Hapus Data Game ---")

        if len(koleksi_game) == 0:
            print("belum ada data game yang dapat dihapus.")
        else:
            for i in range(len(koleksi_game)):
                print(i + 1, ".", koleksi_game[i][0])

            while True:
                nomor = input("pilih nomor data yang ingin dihapus: ")

                if nomor.isdigit():
                    nomor = int(nomor)

                    if nomor >= 1 and nomor <= len(koleksi_game):
                        break
                    else:
                        print("nomor data tidak tersedia!")
                else:
                    print("masukkan nomor berupa angka!")

            index = nomor - 1

            print("\ndata yang dipilih:", koleksi_game[index][0])

            konfirmasi = input("yakin ingin menghapus data? (y/n): ")

            if konfirmasi.lower() == "y":
                koleksi_game.pop(index)
                print("data game berhasil dihapus!")
            else:
                print("penghapusan data dibatalkan.")

    elif pilihan == "5":
        print("\nterima kasih telah menggunakan sistem koleksi game fery kumar.")
        break

    else:
        print("\npilihan menu tidak valid!")
        print("silakan masukkan angka 1-5.")