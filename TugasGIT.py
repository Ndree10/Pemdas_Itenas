import pandas as pd

# Membuat kamus dengan informasi karyawan
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# Membuat DataFrame dari kamus
df = pd.DataFrame(data)

# Menampilkan DataFrame sebelum peningkatan gaji
print("DataFrame sebelum peningkatan gaji:")
print(df)

# Menetapkan persentase peningkatan gaji untuk semua karyawan

# fungsi lambda untuk menghitung gaji tambahan 5%
df['Gaji Setelah Peningkatan'] = df['Gaji'].apply(lambda x: x + (x * 0.05))

print("\nDataFrame setelah peningkatan gaji:")
print(df)

# Menggunakan loop for untuk menghitung gaji karyawan dengan usia > 30
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji Setelah Peningkatan Tambahan'] = row['Gaji Setelah Peningkatan'] + \
            (row['Gaji Setelah Peningkatan'] * 0.02)
    else:
        df.at[index, 'Gaji Setelah Peningkatan Tambahan'] = row['Gaji Setelah Peningkatan']


print("\nDataFrame setelah peningkatan tambahan gaji:")
print(df)
