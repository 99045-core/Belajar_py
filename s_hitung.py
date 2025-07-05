# buat pengulangan!!! (3)
play = True
while play:
    # Judul
    print("\nKalkulator Sederhana".title())
    print("=" *30)
    
    
# user input (1)
    # buat kode error jika input selain angka!!
    try:
        angka_satu = int(input("Angka Pertama: "))
        angka_kedua = int(input("Angka Kedua: "))
        operator = input("Pilih operator (+, -, x, /): ")
    
        
# hasil operator (2)
        if operator == "+":
            print(f"Hasil Penjumlahan: {angka_satu + angka_kedua}")
        elif operator == "-":
            print(f"Hasil Pengurangan: {angka_satu - angka_kedua}")
        elif operator == "x":
            print(f"Hasil Perkalian: {angka_satu * angka_kedua}")
        elif operator == "/":
            try:
                print(f"Hasil Pembagian: {angka_satu / angka_kedua}")
            except ZeroDivisionError:
                print("Angka selain nol")
        else:
            print("Pilih (+, -, X, /)")  # harus pilih operator jika tidak kembali
    except Exception as error:
        print("Masukkan angka!!!")
            
# eksekusi inisialisasi loop    
    play = input("\nPlay again? \nY for YES or N to Quit\n")
    if play.lower() == "y":
        continue
    else:
        print("Terima kasih")
        play = False
