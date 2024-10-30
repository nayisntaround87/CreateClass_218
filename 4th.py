class PersegiPanjang: # mendefinisikan kelas

    def __init__(self, panjang, lebar): # init = konstruktor
        self.panjang = panjang 
        self.lebar = lebar 
 
    def keliling(self): # menghitung keliling persegi panjang
        return 2 * (self.panjang + self.lebar) 
 
    def luas(self): # menghitung luas persegi panjang
        return self.panjang * self.lebar 
 
    def __str__(self): # representasi string dari objek 
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm" 
 
def main(): 
    try: 
        # membuat input dari pengguna untuk panjang dan lebar 
        panjang = float(input("Masukkan panjang persegi panjang (cm): ")) 
        lebar = float(input("Masukkan lebar persegi panjang (cm): ")) 
 
        # membuat objek persegi panjang dengan panjang dan lebar yang diberikan 
        persegi_panjang = PersegiPanjang(panjang, lebar) 
 
        # menampilkan hasil 
        print(persegi_panjang)  # Memanggil fungsi str 
        print("Keliling:", persegi_panjang.keliling(), "cm") 
        print("Luas:", persegi_panjang.luas(), "cm^2") 

    # menangani error saat memasukkan huruf atau simbol saat diminta angka 
    except ValueError: 
        print("Input tidak valid! Harap masukkan angka untuk panjang dan lebar.")
 
# memanggil fungsi main 
if __name__ == "__main__": 
    main()