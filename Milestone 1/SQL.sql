'''
Nama: Kamelia Ramandha
Batch: CODA - RMT - 010

Program ini dibuat untuk membuat dan menormalisasikan database pada PostgreSQL
'''

DROP TABLE brand_id
DROP TABLE brand_list
DROP TABLE var_id
DROP TABLE var_list;
DROP TABLE highend_bags


--- Membuat Struktur Database Utama
CREATE TABLE highend_bags (
id SERIAL PRIMARY KEY,
brand VARCHAR(100),
product_name VARCHAR(200),
var TEXT[],
starting_price NUMERIC(10,2)
);

--- Menyalin data dari file lokal csv yang sudah dibuat menggunakan python
COPY highend_bags (
  brand,
  product_name,
  var,
  starting_price
)
FROM '/private/tmp/h8/nordstorm_bag_clean.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM highend_bags


-- Memulai proses normalisasi

--- Menormaliasikan table baru dari 0NF menjadi 1NF dengan memisahkan kolumn var

---- Membuat kerangka table dictionary untuk var
CREATE TABLE var_list( 
var VARCHAR(100),
id_var SERIAL PRIMARY KEY) ;

---- Memasukan data unik var ke dalam tabel dictionary
INSERT INTO var_list (var) --memasukan data var
SELECT DISTINCT UNNEST(var) AS var --mengambil data unik var dari array var di tabel utama
FROM highend_bags;


---- Membuat kerangka tabel bridging untuk dictionary dan tabel utama
CREATE TABLE var_id ( 
id INTEGER REFERENCES highend_bags(id), -- id pada table ini akan merefer dari table utama
var VARCHAR(500),
id_var INTEGER REFERENCES var_list(id_var)); -- id_var table ini akan merefer dari dictionary

---- Memasukan data ke tabel bridging dari tabel utama
INSERT INTO var_id (id, var)
SELECT hb.id, v
FROM highend_bags AS hb
CROSS JOIN LATERAL UNNEST(hb.var) AS v;


---- Memperbaharui tabel bridging dengan memasukan id dari dictionary
UPDATE var_id 
SET id_var = var_list.id_var -- mendefinisikan bahwa id_var pada table bridging akan berasal dari id_var di table dictionary
FROM var_list
WHERE var_id.var = var_list.var; 

---- Menghapus column var di dalam tabel bridging untuk mengurangi duplikasi 
ALTER TABLE var_id
DROP COLUMN var; 

---- Menghapus column var di dalam tabel utama karena sudah dipisahkan
ALTER TABLE highend_bags
DROP COLUMN var; 


---- Melihat hasil dari tabel utama
SELECT * FROM highend_bags;


--- Melakukan proses normalisasi dari 1NF ke 2NF

---- Membuat kerangka table dictionary untuk brand
CREATE TABLE brand_list( 
brand VARCHAR(100),
id_brand SERIAL PRIMARY KEY) ;

---- Memasukan data unik brand ke dalam tabel dictionary
INSERT INTO brand_list (brand) --memasukan data brand
SELECT DISTINCT(brand) AS brand --mengambil data unik brand dari daftar brand unik
FROM highend_bags;

---- Mengecek hasil input
SELECT * FROM brand_list;

---- Membuat kerangka tabel bridging untuk dictionary dan tabel utama
CREATE TABLE brand_id ( 
id INTEGER REFERENCES highend_bags(id), -- id pada table ini akan merefer dari table utama
brand VARCHAR(500),
id_brand INTEGER REFERENCES brand_list(id_brand)); -- id_brand table ini akan merefer dari dictionary

---- Memasukan data ke tabel bridging dari tabel utama
INSERT INTO brand_id (id, brand)
SELECT hb.id, hb.brand
FROM highend_bags AS hb
JOIN brand_list bl ON bl.brand = hb.brand;


---- Memperbaharui tabel bridging dengan memasukan id dari dictionary
UPDATE brand_id 
SET id_brand = brand_list.id_brand -- mendefinisikan bahwa id_brand pada table bridging akan berasal dari id_brand di table dictionary
FROM brand_list
WHERE brand_id.brand = brand_list.brand; 

---- Menghapus column brand di dalam tabel bridging untuk mengurangi duplikasi 
ALTER TABLE brand_id
DROP COLUMN brand; 

---- Menghapus column brand di dalam tabel utama karena sudah dipisahkan
ALTER TABLE highend_bags
DROP COLUMN brand; 


---- Melihat hasil dari tabel utama
SELECT * FROM highend_bags;

------ Proses normalisasi selesai, semua tabel telah bergantung hanya kepada primary key
