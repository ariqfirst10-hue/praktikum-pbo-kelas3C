class Buku :
    pass
b = Buku()
b.judul = "contoh judul"
b.penulis = "contoh penulis"

print (b.judul,"-",b.penulis)

class Buku:
    def __init__(self, judul, penulis="tidak ketahui", tahun_terbit=None):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
 
    def info(self):
        print(f"Judul   : {self.judul}")
        print(f"Penulis : {self.penulis}")
        print(f"tahun_terbit : {self.tahun_terbit}")

buku1 = Buku("Dasar Pemrograman Python", "Andi Pratama", 2008)
buku2 = Buku("Struktur Data", "Siti Aminah", 2007)
buku3 = Buku("Basis Data", tahun_terbit=2006)
 
buku1.info()
buku2.info()
buku3.info()
