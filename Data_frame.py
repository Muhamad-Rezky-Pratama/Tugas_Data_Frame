import pandas as pd

data_sampah = "data_sampah_jabar.xlsx"  
df = pd.read_excel(data_sampah)
df['jumlah_produksi_sampah'] = pd.to_numeric(df['jumlah_produksi_sampah']).fillna(0)
pd.set_option('display.max_columns', None)  
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)     

print("Data Sampah :")
print(df)


tahun_tertentu = int(input("Masukan Tahun yang dituju : "))  
total_tahun = 0


for index, row in df.iterrows():
    if row['tahun'] == tahun_tertentu:
        total_tahun += row['jumlah_produksi_sampah']

print(f"\nTotal produksi sampah di seluruh Kabupaten/Kota untuk tahun {tahun_tertentu}: {total_tahun} ton")


df_sampah_tahun_tertentu = pd.DataFrame({
    'Tahun': [tahun_tertentu], 
    'Total Produksi Sampah': [total_tahun]
})

data_sampah_tahunan = {}
for index, row in df.iterrows():
    tahun = row['tahun']
    jumlah = row['jumlah_produksi_sampah']

    if tahun not in data_sampah_tahunan:
        data_sampah_tahunan[tahun] = 0

    data_sampah_tahunan[tahun] += jumlah

df_tahunan = pd.DataFrame(
    list(data_sampah_tahunan.items()), 
    columns=['Tahun', 'Total Produksi Sampah']
)

print("\nJumlah Produksi Sampah Per Tahun:")
print(df_tahunan)

data_sampah_kota_tahunan = {}
for index, row in df.iterrows():
    tahun = row['tahun']
    kota = row['nama_kabupaten_kota']
    jumlah = row['jumlah_produksi_sampah']

    if (kota, tahun) not in data_sampah_kota_tahunan:
        data_sampah_kota_tahunan[(kota, tahun)] = 0
    data_sampah_kota_tahunan[(kota, tahun)] += jumlah

df_kota_tahunan = pd.DataFrame(
    [(kota, tahun, total) for (kota, tahun), total in data_sampah_kota_tahunan.items()],
    columns=['nama_kabupaten_kota', 'tahun', 'jumlah_produksi_sampah']
)

print("\nJumlah Produksi Sampah Per Kota/Kabupaten Per Tahun:")
print(df_kota_tahunan)

df_sampah_tahun_tertentu.to_csv("total_produksi_sampah_tahun_tertentu.csv", index=False)
df_sampah_tahun_tertentu.to_excel("total_produksi_sampah_tahun_tertentu.xlsx", index=False)
df_tahunan.to_csv("jumlah_per_tahun.csv", index=False)
df_tahunan.to_excel("jumlah_per_tahun.xlsx", index=False)
df_kota_tahunan.to_csv("jumlah_per_kota_tahun.csv", index=False)
df_kota_tahunan.to_excel("jumlah_per_kota_tahun.xlsx", index=False)
