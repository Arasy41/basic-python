# import pandas as pd

# # Membaca file Excel (XLSX)
# data = pd.read_excel("data.xlsx")

# # Menambahkan kolom "Pulau" yang menandai apakah provinsi berada di Pulau Jawa atau tidak
# data['Pulau'] = data['provinsi'].apply(lambda x: 'Jawa' if x in ['JAWA BARAT', 'JAWA TENGAH', 'JAWA TIMUR', 'DI YOGYAKARTA', 'DKI JAKARTA'] else 'Luar Jawa')

# # Menghitung jumlah mahasiswa untuk setiap kombinasi program studi, provinsi, dan pulau
# result = data.groupby(['programstudi', 'provinsi', 'Pulau']).size().reset_index(name='Jumlah Mahasiswa')

# # Menghitung total mahasiswa dari Jawa dan non-Jawa
# total_mahasiswa_jawa = result[result['Pulau'] == 'Jawa']['Jumlah Mahasiswa'].sum()
# total_mahasiswa_non_jawa = result[result['Pulau'] == 'Luar Jawa']['Jumlah Mahasiswa'].sum()

# # Menghitung persentase mahasiswa dari Jawa dan non-Jawa
# persentase_jawa = (total_mahasiswa_jawa / len(data)) * 100
# persentase_non_jawa = (total_mahasiswa_non_jawa / len(data)) * 100

# # Menambahkan persentase mahasiswa dari Jawa dan Luar Jawa ke dalam DataFrame hasil
# hasil_persentase = pd.DataFrame({
#     'Pulau': ['Jawa', 'Luar Jawa', 'Total'],
#     'Persentase (%)': [persentase_jawa, persentase_non_jawa, 100]
# })

# # Menghitung persentase mahasiswa dari Jawa dan non-Jawa untuk setiap kombinasi program studi, provinsi, dan pulau
# result['Persentase'] = result.apply(lambda row: (row['Jumlah Mahasiswa'] / total_mahasiswa_jawa) * 100 if row['Pulau'] == 'Jawa' else (row['Jumlah Mahasiswa'] / total_mahasiswa_non_jawa) * 100, axis=1)

# # Menggabungkan hasil persentase ke dalam DataFrame result
# result = pd.concat([result, hasil_persentase])

# # Menyimpan hasil ke dalam file Excel (XLSX)
# result.to_excel("hasil_penghitungan6.xlsx", index=False)

# print("Penghitungan dan persentase selesai. Hasil disimpan ke dalam file 'hasil_penghitungan.xlsx'")

import pandas as pd

# Membaca file Excel (XLSX)
excel_file = "data.xlsx"
excel_data = pd.ExcelFile(excel_file)

# Dictionary untuk menyimpan hasil penghitungan dari setiap sheet
results_dict = {}

for sheet_name in ['2020', '2021', '2022', '2023']:
    # Membaca data dari setiap lembar kerja (sheet)
    data = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Menambahkan kolom "Pulau" yang menandai apakah provinsi berada di Pulau Jawa atau tidak
    data['Pulau'] = data['namapropinsi'].apply(lambda x: 'Jawa' if x in ['JAWA BARAT', 'JAWA TENGAH', 'JAWA TIMUR', 'D.I. YOGYAKARTA', 'BANTEN', 'D.K.I. JAKARTA', 'JAMBI'] else 'Luar Jawa')

    # Menghitung jumlah mahasiswa untuk setiap kombinasi program studi, provinsi, dan pulau
    result = data.groupby(['namaprogstudi', 'namapropinsi', 'Pulau']).size().reset_index(name='Jumlah Mahasiswa')

    # Menghitung total mahasiswa dari Jawa dan non-Jawa
    total_mahasiswa_jawa = result[result['Pulau'] == 'Jawa']['Jumlah Mahasiswa'].sum()
    total_mahasiswa_non_jawa = result[result['Pulau'] == 'Luar Jawa']['Jumlah Mahasiswa'].sum()

    # Menghitung persentase mahasiswa dari Jawa dan non-Jawa
    persentase_jawa = (total_mahasiswa_jawa / len(data)) * 100
    persentase_non_jawa = (total_mahasiswa_non_jawa / len(data)) * 100

    # Menambahkan persentase mahasiswa dari Jawa dan Luar Jawa ke dalam DataFrame hasil
    hasil_persentase = pd.DataFrame({
        'Pulau': ['Jawa', 'Luar Jawa', 'Total'],
        'Persentase (%)': [persentase_jawa, persentase_non_jawa, 100]
    })

    # Menghitung persentase mahasiswa dari Jawa dan non-Jawa untuk setiap kombinasi program studi, provinsi, dan pulau
    result['Persentase'] = result.apply(lambda row: (row['Jumlah Mahasiswa'] / total_mahasiswa_jawa) * 100 if row['Pulau'] == 'Jawa' else (row['Jumlah Mahasiswa'] / total_mahasiswa_non_jawa) * 100, axis=1)

    # Menyimpan hasil penghitungan
    results_dict[sheet_name] = pd.concat([result, hasil_persentase])

# Menyimpan hasil ke dalam file Excel (XLSX) dengan setiap sheet hasilnya
with pd.ExcelWriter("hasil_penghitungan11.xlsx") as writer:
    for sheet_name, result_df in results_dict.items():
        result_df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Penghitungan dan persentase selesai. Hasil disimpan ke dalam file 'hasil_penghitungan11.xlsx'")

