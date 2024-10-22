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
- **Filter Produk Cerdas** – Memungkinkan pengguna untuk mencari produk sesuai kategori seperti smartphone, laptop, smartwatch, dan lainnya, serta memfilter berdasarkan harga dan brand.
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
    - Daftar produk yang dijual berdasarkan kategori (smartphone, laptop, smart watch, dll).
    - Pencarian produk menggunakan filter (harga, brand, fitur).
    - Detail produk yang lengkap, termasuk spesifikasi, gambar, review pengguna, dan rating.
3. **Modul Cart & Checkout** --> Nizar
    - Fitur penambahan produk ke keranjang belanja.
    - Pemilihan metode pembayaran (transfer bank, kartu kredit, e-wallet).
    - Konfirmasi pembelian dan pengaturan pengiriman produk.
4. **Modul Review dan Rating Produk** --> Farid
    - Pengguna dapat memberikan ulasan dan rating untuk produk yang sudah dibeli.
    - Sistem rating untuk membantu pengguna lain dalam memilih produk.
    - Pengguna dapat menambahkan produk ke wishlist untuk dibeli atau dilihat nanti.
5. **Modul Whistlist dan Frequently Asked Questionn (FAQ)** --> Akhyar
    - Pengguna dapat menambahkan produk ke wishlist untuk dibeli atau dilihat nanti.
    - Kumpulan pertanyaan yang sering ditanyakan terkait penggunaan aplikasi, produk, dan layanan.
6. **Modul Profile** --> Micheline 
    - Terdiri dari informasi pengguna seperti nama, email, foto profil.
    - Riwayat transaksi pemesanan.
    - Pengguna dapat mengunggah atau mengubah foto profil mereka.
    - Ubah password.
    - History barang yang sudah dibeli
7. **Modul Toko Official** --> Alby
    - Pengelolaan produk yang dijual oleh toko resmi, termasuk kategori produk dan harga.
    - Verifikasi dan label khusus untuk toko official.

### Sumber Dataset 📊
Kategori Utama : Gadget

**Produk**:
- HP
- Laptop
- Smartwatch
- Headset/TWS

Headset    : [Amazon Headset Specs (kaggle.com)](https://www.kaggle.com/datasets/midhundasl/amazon-headset-specs) <br>
HP         : https://www.kaggle.com/datasets/veer098/mobile-phone <br>
HP         : https://www.kaggle.com/datasets/animeshshukla44/flipkart-mobile-dataset <br>
Laptop     : https://www.kaggle.com/datasets/owm4096/laptop-prices <br>
Lainnya    : [Amazon Electronics Products 10k items - 2023 (kaggle.com)](https://www.kaggle.com/datasets/akeshkumarhp/electronics-products-amazon-10k-items) <br>

### Role pengguna 🙋🏻‍♀
- **Guest**
    - Melihat daftar dan detail produk gadget
    - Mengakses fitur sort dan filter kategori gadget
    - Mencari berdasarkan nama produk
- **User** (perlu login)
    - Melihat daftar dan detail produk gadget
    - Memasukkan produk ke wishlist
    - Memasukkan produk ke keranjang
    - Membeli produk (mengakses fitur checkout)
    - Menambahkan review produk yang sudah dibeli
    - Mengakses fitur sort dan filter kategori gadget
    - Mencari berdasarkan nama produk gadget
- **Seller** (perlu login)
    - Menambah produk yang ingin dijual
    - Mengedit detail produk dan produk yang dijual 



