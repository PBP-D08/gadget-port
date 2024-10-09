# Proyek Tengah Semester PBP
## GadgetPort📱💻🛒
_"Empowering Your World, One Gadget at a Time"_  <br>
link APK : [GadgetPort](http://pbp.cs.ui.ac.id/muhammad.farid31/gadgetport)

### Nama Anggota 🧑‍🎓👩‍🎓👨‍🎓🧑‍🎓👨‍🎓
1. Akhyar Rasyid Asy syifa (2306241682)
2. Ahmad Nizar Sauki (2306152046)
3. Muhammad Farid Hasabi (2306152512)
4. Micheline Wijaya Limbergh (2306207013)
5. Muhammad Albyarto Ghazali (2306241695)

### Deskripsi Singkat 🛍️
Di tengah pesatnya perkembangan teknologi dan tingginya permintaan pasar terhadap barang elektronik, kami melihat adanya kebutuhan yang mendesak untuk menyediakan solusi yang inovatif. Batam, dengan lokasi strategisnya dan akses logistik yang mudah ke negara-negara tetangga, memiliki potensi besar untuk menjadi pusat perdagangan elektronik yang menjangkau pasar internasional. Banyak konsumen di Indonesia, khususnya yang mencari produk elektronik berkualitas, harus berkeliling dari satu toko ke toko lainnya hanya untuk menemukan produk yang mereka inginkan. Selain itu, sulitnya membandingkan harga dan kualitas di antara berbagai toko sering kali memakan waktu dan tenaga.

Sebagai solusi, kami memperkenalkan "GadgetPort", sebuah platform canggih yang dirancang khusus untuk memenuhi kebutuhan generasi modern dalam membeli produk elektronik. GadgetPort memudahkan para penjual dan pembeli elektronik untuk bertemu dalam satu tempat digital yang terorganisir. Penjual dapat dengan mudah merilis produk terbaru mereka beserta informasi rinci, sementara pembeli dapat melihat katalog produk, melihat ulasan pengguna, dan langsung membeli produk yang diinginkan secara aman dan nyaman.

#### Fitur-fitur unggulan GadgetPort 
- **Filter Produk Cerdas** – Memungkinkan pengguna untuk mencari produk sesuai kategori seperti smartphone, laptop, dan headset, serta memfilter berdasarkan harga dan brand.
- **Memberi dan Membaca Ulasan** – Sebelum melakukan pembelian, pembeli dapat membaca ulasan dari pengguna lain untuk memastikan kualitas dan keunggulan produk yang mereka pilih. Setelah melakukan pembelian, pembeli juga bisa memberikan ulasan produk tersebut. 
- **Pembelian Product** – Memberikan pengalaman belanja yang aman, cepat, dan real-time dengan berbagai opsi pembayaran.
- **Wishlist dan Notifikasi** – Fitur wishlist memudahkan pengguna menyimpan produk yang ingin dibeli nanti, serta mendapat notifikasi saat ada diskon atau promo menarik.
- **Frequently Asked Question** - Memudahkan pengguna mencari solusi apabila terjadi kesalahan pada aplikasi secara umum yang sering dijumpai.
- **Update profil** - Pembeli dapat memperbarui profil.

Kami percaya bahwa dengan menghadirkan GadgetPort, kami tidak hanya memberikan solusi modern untuk kebutuhan belanja produk elektronik, tetapi juga membantu menghubungkan konsumen dengan toko-toko terpercaya di Batam dan seluruh Indonesia. Melalui platform ini, harapan untuk menghadirkan pengalaman belanja elektronik yang lebih mudah, transparan, dan efisien bukan lagi sekedar wacana, melainkan sebuah langkah nyata yang dapat diwujudkan bersama-sama. Dengan GadgetPort, masa depan belanja elektronik ada di genggaman Anda.

### Daftar Modul 🧑🏻‍💻
Berikut adalah daftar modul yang diimplementasikan:
1. **Modul Authentication & User Management** --> bersama
    - Pendaftaran pengguna, login, logout.
    - Manajemen profil pengguna (pengubahan informasi seperti nama, email, foto).
    - Verifikasi email atau nomor telepon untuk keamanan tambahan.
2. **Modul Katalog Produk** --> bersama
    - Daftar produk yang dijual berdasarkan kategori (smartphone, laptop, headset).
    - Pencarian produk menggunakan filter (harga, brand, fitur).
    - Detail produk yang lengkap, termasuk spesifikasi, gambar, review pengguna, dan rating.
3. **Modul Cart & Checkout** --> Nizar
    - Fitur penambahan produk ke keranjang belanja.
    - Pemilihan metode pembayaran (transfer bank, kartu kredit, e-wallet).
    - Konfirmasi pembelian dan pengaturan pengiriman produk.
4. **Modul Review dan Rating Produk** --> Farid
   
   Modul ini berfungsi untuk memberikan review dan rating terhadap suatu produk.
   
   User | Admin
    -|-
   User dapat memberikan ulasan dan rating untuk tiap produk.|Admin dapat menghapus review yang telah dibuat oleh user.
6. **Modul Wishlist dan Frequently Asked Question (FAQ)** --> Akhyar
    - Pengguna dapat menambahkan produk ke wishlist untuk dibeli atau dilihat nanti.
    - Kumpulan pertanyaan yang sering ditanyakan terkait penggunaan aplikasi, produk, dan layanan.
7. **Modul Profile** --> Micheline 
    - Terdiri dari informasi pengguna seperti nama, email, foto profil.
    - Riwayat transaksi pemesanan.
    - Pengguna dapat mengunggah atau mengubah foto profil mereka.
    - Ubah password.
    - History barang yang sudah dibeli
8. **Modul Toko** --> Alby

   Modul ini berfungsi untuk mengatur pengelolaan produk yang dijual oleh toko, termasuk kategori produk dan harga.

   User|Admin
   -|-
   User dapat melihat tiap produk yang dijual oleh toko, termasuk kategori produk dan harga.|Admin dapat menambah, mengubah, serta menghapus produk pada toko mereka.

### Sumber Dataset 📊
Kategori Utama : Gadget

**Produk**:
- HP
- Laptop
- Headset/TWS

Headset    : https://www.kaggle.com/datasets/midhundasl/amazon-headset-specs <br>
HP         : https://www.kaggle.com/datasets/veer098/mobile-phone <br>
Laptop     : https://www.kaggle.com/datasets/owm4096/laptop-prices <br>

### Role pengguna 🙋🏻‍♀
- **User** (perlu login)
    - Melihat daftar dan detail produk gadget
    - Memasukkan produk ke wishlist
    - Memasukkan produk ke keranjang
    - Membeli produk (mengakses fitur checkout)
    - Menambahkan review produk yang sudah dibeli
    - Mengakses fitur sort dan filter kategori gadget
    - Mencari berdasarkan nama produk gadget
- **Admin** (perlu login)
    - Menambah produk yang ingin dijual
    - Mengedit dan menghapus detail produk dan produk yang dijual 



