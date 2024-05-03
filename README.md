<h1 align="center">
  <br>
  DATA HOTEL DI BANDUNG
  <br>
  <br>
</h1>


## DESCRIPTION OF THE DATA AND DBMS

### Data 
Tripadvisor, Inc. adalah perusahaan biro perjalanan daring asal Amerika Serikat yang mengoperasikan situs web dan aplikasi seluler yang berisi konten buatan pengguna dan situs web pencarian harga yang berhubungan dengan perjalanan dan wisata. Perusahaan juga menawarkan reservasi dan pemesanan daring untuk transportasi, penginapan, atraksi wisata, dan restoran.

Script ini ditujukan untuk melakukan scraping pada web tripadvisor yang menunjukkan hotel-hotel terbaik di Bandung. Data yang diambil antara lain:
- Nama hotel
- Alamat hotel
- Harga hotel pada saat data diambil
- Review hotel overall
- Review lokasi hotel
- Review kebersihan hotel
- Review Service hotel
- Review kesepadanan harga hotel

### DBMS
DBMS yang dipilih adalah PostgreSQL dengan fiturnya yang lengkap dan memadai sehingga cocok digunakan sebagai penampung data web scraping ini

## Spesifikasi program
Language version: Python 3
Library:
- Pandas
- numpy
- BeautifulSoup
- Selenium
- time

## How to Use

### Data scraper
Lakukan cloning atau download program scraper.py <br>
Install library yang diperlukan dengan `pip install (library)` pada command prompt <br>
Navigasi ke lokasi file pada .../Data Scraping/src dan lakukan run <br>
Akan digenerasi raw_data.csv pada direktori file scraper.py diletakkan <br>
<br >
### Data Cleaner
Lakukan cloning atau download program cleaner.py <br>
Install library yang diperlukan dengan `pip install (library)` pada command prompt <br>
Navigasi ke lokasi file pada .../Data Scraping/src dan lakukan run <br>
Akan digenerasi raw_data.csv pada direktori file cleaner.py diletakkan <br>

### Data Storing
Lakukan cloning atau download database hotels.sql <br>
Install postgresql jika belum terinstal pada perangkat yang digunakan <br>
Navigasi cmd ke .../Data Storing/export <br>
Restore database dengan perintah `psql -U {username} -d {database_name} < hotels.sql` sesuai dengan database yang ingin digunakan dan username postgres pada perangkat <br>

## JSON Structure
JSON digenerasi dengan menggunakan tools online untuk mengkonversi csv menjadi json <br>
JSON digunakan untuk menyimpan data yang nantinya dapat digunakan untuk export data ke sql <br>
![json](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Scraping/screenshot/json_file.png)

## Database Structure
### Entity Relationship Diagram (ERD)
![ERD](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Storing/design/ERD.png)
### Relational Diagram
![Rel Diagram](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Storing/design/Relation.png)

## Explanation of ERD to relational diagram and translational process
Pada ERD, dibuat dua buah entitas yaitu hotel dan price. Hotel terhubung dengan price dengan hotel_id sebagai foreign key. <br>
Hotel berisi alamat, point yaitu 50% berasal dari review dan 50% dari harga dan hotel_id sebagai primary key identifier, selain itu hotel juga memiliki review dan detail per kategori <br>
Prices adalah weak entity yang berisi harga per hari <br>

Hotel akan ditranslasikan as is pada psql karena tidak ada yang perlu digantikan, sementara itu prices akan memiliki hotel_id sebagai foreign key karena status prices sebagai weak entity <br>
Karena pengguna kemungkinan tidak memerlukan review setiap kali data hotel ingin diakses, maka akan dilakukan vertical partitioning dengan relasi baru reviews yang berisi detail review per kategori dari hotel <br>

## Screenshots of the program

### Website
![Webpage](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Scraping/screenshot/website.png)

### Export json ke sql
![sql](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Storing/screenshot/base_sql.png)

### Pembuatan tabel prices
<br>

![prices](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Storing/screenshot/prices_table.png)

### Pembuatan tabel reviews
![reviews](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Storing/screenshot/reviews_table.png)

### Update tabel hotels
![drop](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Storing/screenshot/hotel_drop_update.png)
![tabel akhir](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Storing/screenshot/hotel_table_final.png)
## Visualization
### Plot data berdasarkan postcode
<br>

![postcode](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Visualization/postcode.png)

### Hotel terbaik dari postcode terbanyak
<br>

![overall](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Visualization/overall.png)

### Plot korelasi harga dan review
<br>

![plot](https://github.com/Nicholas438/Seleksi-2023-Tugas-1/blob/main/Data%20Visualization/plot.png)

### Insight yang didapatkan
1. Kode pos 40115 memiliki frekuensi hotel terbaik oleh tripadvisor tertinggi yang mungkin terjadi karena adanya beberapa daerah wisata yang dapat dikunjungi dan lokasi strategis yang memiliki berbagai pilihan karena tingginya densitas penduduk pada daerah tersebut
2. Tebu Hotel Bandung adalah hotel yang relatif terbaik dari segi harga, review melalui poin dan lokasi yang diuraikan pada nomor satu. 
3. Ada korelasi positif antara harga dan review. Sehingga dengan naiknya harga, review memiliki kemungkinan tinggi untuk memiliki nilai yang lebih besar juga

## References
Libraries:
https://www.postgresql.org/<br>
https://pypi.org/project/beautifulsoup4/<br>
https://www.selenium.dev/<br>
https://pandas.pydata.org/<br>
<br>
Tutorials and tools:
https://realpython.com/beautiful-soup-web-scraper-python/<br>
https://realpython.com/modern-web-automation-with-python-and-selenium/<br>
https://www.codespeedy.com/beautifulsoup-lxml-parser-full-tutorial-python/<br>
https://antisyllogism.medium.com/how-to-webscrape-with-requests-selenium-and-beautifulsoup-in-python-d2b1b996399a<br>
https://csvjson.com/<br>
https://www.convertjson.com/json-to-sql.html<br>

## Author
Nicholas <br>
18221165 <br>
Seleksi Warga Basdat <br>
2023 
