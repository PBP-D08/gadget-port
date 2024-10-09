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
   
      Modul ini untuk autentikasi akun User (Pelanggan dan Admin)
      | Pelanggan dan Admin |
      | :------------------- |
      |Pendaftaran pengguna, login, logout. |
      |Manajemen profil pengguna (pengubahan informasi seperti nama,email, foto).|
      |Verifikasi email atau nomor telepon untuk keamanan tambahan.|

2. **Modul Katalog Produk** --> bersama

      Modul ini berfungsi untuk melihat detail produk serta dapat menggunakan filter untuk pencarian produk.
      
      Pelanggan | Admin
      -|-
      Pelanggan dapat melihat daftar produk yang dijual berdasarkan kategori (smartphone. laptop, headset)| Admin dapat mengedit dan menghapus produk. |
      Pelanggan dapat menggunakan filter (harga, brand, dll)| - |
      Pelanggan dapat melihat detail produk yang lengkap, termasuk spesifikasi, gambar, review, pengguna, dan rating| Admin dapat mengedit detail produk. |

3. **Modul Cart & Checkout** --> Nizar
      
      Modul ini berfungsi sebagai proses pembayaran.
   
      | Pelanggan |
      | -------   |
      |Pelanggan dapat menambahkan produk ke keranjang belanja. |
      |Pelanggan dapat memilih metode pembayaran (transfer bank, kartu kredit, e-wallet).|
      | Pelanggan dapat konfirmasi pembelian dan pengaturan pengiriman produk |
4. **Modul Review dan Rating Produk** --> Farid
   
      Modul ini berfungsi untuk memberikan review dan rating terhadap suatu produk.
      
      Pelanggan | Admin
      -|-
      Pelanggan dapat memberikan ulasan dan rating untuk tiap produk.|Admin dapat menghapus review yang telah dibuat oleh Pelanggan.
5. **Modul Wishlist dan Frequently Asked Question (FAQ)** --> Akhyar
   
      Modul ini berfungsi untuk melihat daftar wishlist dan Frequently Asked Question (F.A.Q)
    
      | Pelanggan | Admin |
      | --------- | ----- |
      | Pengguna dapat melihat kumpulan pertanyaan yang sering ditanyakan terkait penggunaan aplikasi, produk, dan layanan. .| Admin dapat menambah, mengedit, dan menghapus daftar Frequently Asked Question |
      | Pengguna dapat menambahkan produk ke wishlist untuk dibeli atau dilihat nanti.| -  |
   
6. **Modul Profile** --> Micheline
    
     Modul ini berfungsi untuk mengubah data pada profil User
     
     | Pelanggan | Admin |
     | --------- | ----- |
     | Pelanggan dapat mengubah nama, email, foto profil.| Admin bisa mengubah nama, email, dan foto profil|
     | Pelanggan dapat mengubah password | Admin dapat mengubah password |
     | Pelanggan dapat melihat history transaksi pemesanan. | -|
   
7. **Modul Toko** --> Alby

      Modul ini berfungsi untuk mengatur pengelolaan produk yang dijual oleh toko, termasuk kategori produk dan harga.
   
      Pelanggan|Admin
      -|-
      Pelanggan dapat melihat tiap produk yang dijual oleh toko, termasuk kategori produk dan harga.|Admin dapat menambah, mengubah, serta menghapus produk pada toko mereka.

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
- **Pelanggan** (perlu login)
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



