# MINIPROJECT-2-DDP--ALUR-PROGRAM-PENGELOLAAN-WISATA

1. Login
Pada tahap login, program meminta pengguna untuk memasukkan username dan password. Pengguna memasukkan username admin dan password yang sesuai. Program kemudian melakukan pengecekan terhadap data tersebut. Jika username dan password benar, program menampilkan pesan “Login berhasil!” dan “Role: admin”, yang berarti pengguna berhasil masuk sebagai admin. Apabila password yang dimasukkan salah, program akan menampilkan pesan login gagal dan meminta pengguna melakukan login kembali sampai data yang dimasukkan benar.

2. Menu Admin
Setelah proses login berhasil, program menampilkan Menu Admin yang terdiri dari lima pilihan, yaitu Lihat wisata, Tambah wisata, Ubah wisata, Hapus wisata, dan Logout. Menu tersebut digunakan sebagai pusat pengelolaan data wisata. Admin dapat memilih salah satu menu sesuai dengan kebutuhan, dan setelah proses pada menu 1 sampai 4 selesai, program akan kembali menampilkan Menu Admin.

3. Lihat Wisata
Ketika admin memilih menu Lihat wisata, program menampilkan seluruh data wisata yang telah tersimpan. Pada awal program terdapat tiga data wisata, yaitu Pantai Kuta yang berlokasi di Bali, Pantai Pandawa yang berlokasi di Bali, dan Raja Ampat yang berlokasi di Papua Barat Daya. Data tersebut ditampilkan dalam bentuk daftar agar admin dapat melihat informasi wisata yang tersedia. Setelah daftar ditampilkan, program kembali ke Menu Admin.

4. Tambah Wisata
Ketika admin memilih menu Tambah wisata, program meminta admin memasukkan nama dan lokasi wisata yang baru. Pada output, admin memasukkan Pantai Ora sebagai nama wisata dan Maluku sebagai lokasinya. Setelah data dimasukkan, program menyimpan data tersebut ke dalam daftar wisata dan menampilkan pesan “Wisata berhasil ditambahkan.” Setelah proses penambahan selesai, program kembali ke Menu Admin.

5. Ubah Wisata
Ketika admin memilih menu Ubah wisata, program terlebih dahulu menampilkan daftar wisata dan meminta admin menentukan nomor wisata yang ingin diubah. Admin memilih nomor 4, yaitu data Pantai Ora yang sebelumnya berlokasi di Maluku. Admin kemudian memasukkan nama baru Raja Ampat dan lokasi baru Papua Barat Daya. Program memperbarui data tersebut dan menampilkan pesan “Wisata berhasil diubah.” Setelah proses perubahan selesai, program kembali ke Menu Admin.

6. Logout
Setelah selesai mengelola data wisata, admin memilih menu Logout dengan memasukkan pilihan nomor 5. Program kemudian mengakhiri sesi admin dan menampilkan pesan “Logout berhasil.” Setelah itu program menampilkan “=== PROGRAM SELESAI ===”, yang menunjukkan bahwa pengguna telah keluar dari sistem dan seluruh proses program telah berakhir.

<img width="583" height="1013" alt="Screenshot 2026-10-06 184335" src="https://github.com/user-attachments/assets/9a97468c-58b2-4178-aa3a-534eb6f9addb" />
<img width="451" height="205" alt="Screenshot 2026-10-06 184345" src="https://github.com/user-attachments/assets/0fbdb5eb-a434-4a2e-a7d7-f2791cab7cce" />

Flowchart diawali dengan simbol Mulai yang menunjukkan bahwa program pertama kali dijalankan. Setelah program dimulai, pengguna diminta memasukkan username dan password untuk melakukan proses login ke dalam sistem.
Setelah username dan password dimasukkan, program melakukan pengecekan untuk menentukan apakah data login yang dimasukkan sudah benar. Jika username dan password benar, maka program menampilkan pesan “Login berhasil!” dan “Role: admin”, kemudian pengguna diarahkan ke Menu Admin. Jika username atau password salah, program menampilkan pesan “Login gagal” dan pengguna diarahkan kembali ke proses input username dan password untuk melakukan login ulang.

Setelah berhasil login sebagai admin, program menampilkan Menu Admin yang terdiri dari lima pilihan, yaitu Lihat wisata, Tambah wisata, Ubah wisata, Hapus wisata, dan Logout. Admin kemudian memilih salah satu menu sesuai dengan proses yang ingin dilakukan.
Jika admin memilih menu Lihat Wisata, program akan menampilkan daftar wisata yang telah tersimpan di dalam sistem. Setelah daftar wisata ditampilkan, proses tersebut selesai dan program kembali ke Menu Admin, sehingga admin masih dapat memilih menu lainnya.

Jika admin memilih menu Tambah Wisata, program meminta admin memasukkan nama wisata dan lokasi wisata baru. Setelah data dimasukkan, program menyimpan data tersebut dan menampilkan pesan “Wisata berhasil ditambahkan.” Setelah proses penambahan selesai, program kembali ke Menu Admin.
Jika admin memilih menu Ubah Wisata, program akan menampilkan daftar wisata dan meminta admin memilih nomor wisata yang ingin diubah. Setelah nomor wisata dipilih, admin memasukkan nama baru dan lokasi baru. Program kemudian memperbarui data wisata tersebut dan menampilkan pesan “Wisata berhasil diubah.” Setelah proses perubahan selesai, program kembali ke Menu Admin.

Jika admin memilih menu Hapus Wisata, program akan menampilkan daftar wisata dan meminta admin memilih nomor wisata yang ingin dihapus. Setelah nomor wisata dipilih dan proses penghapusan dikonfirmasi, program menghapus data tersebut dan menampilkan pesan “Wisata berhasil dihapus.” Setelah proses penghapusan selesai, program kembali ke Menu Admin.
Jika admin memilih menu Logout, program akan mengakhiri sesi admin dan menampilkan pesan “Logout berhasil.” Setelah logout berhasil, program tidak kembali ke Menu Admin karena sesi pengguna sudah berakhir. Program kemudian menuju ke bagian Program Selesai, yang menandakan bahwa seluruh proses program telah berakhir.

Dengan demikian, alur utama program adalah Mulai → Login → Verifikasi Login → Menu Admin → Pilih Menu → Proses Menu → Kembali ke Menu Admin, sedangkan jika admin memilih Logout, program akan menuju Program Selesai. Pada bagian login, apabila data yang dimasukkan salah, alur akan kembali ke Input Username & Password sampai pengguna berhasil melakukan login.

<img width="1102" height="947" alt="Screenshot 2026-10-06 192713" src="https://github.com/user-attachments/assets/ca444566-3233-4e32-aad8-84b847bd41f3" />
