class Buku :
    pass
b = Buku()
b.judul = "contoh judul"
b.penulis = "contoh penulis"

print (b.judul,"-",b.penulis)

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
 
    def info(self):
        print(f"Judul   : {self.judul}")
        print(f"Penulis : {self.penulis}")

buku1 = Buku("Dasar Pemrograman Python", "Andi Pratama")
buku2 = Buku("Struktur Data", "Siti Aminah")
buku3 = Buku("Basis Data", "Budi Santoso")
 
buku1.info()
buku2.info()
buku3.info()
