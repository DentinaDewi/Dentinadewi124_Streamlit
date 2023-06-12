import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Menampilkan judul aplikasi
st.title('Aplikasi Uji Regresi Sederhana dan Korelasi')

# Mengambil input data dari pengguna
st.subheader('Masukkan Data')
x_values = st.text_input('Masukkan nilai-nilai X, dipisahkan oleh koma:')
y_values = st.text_input('Masukkan nilai-nilai Y, dipisahkan oleh koma:')

# Mengubah input string menjadi list
x_values = [float(x.strip()) for x in x_values.split(',') if x.strip()]
y_values = [float(y.strip()) for y in y_values.split(',') if y.strip()]

# Membuat DataFrame dari data yang dimasukkan
df = pd.DataFrame({ 'X': x_values, 'Y': y_values })

# Menampilkan data
st.subheader('Data')
st.write(df)

# Menghitung koefisien korelasi Pearson
correlation_coef = np.corrcoef(df['X'], df['Y'])[0, 1]

# Menampilkan hasil uji korelasi
st.subheader('Hasil Uji Korelasi')
st.write(f'Koefisien Korelasi Pearson: {correlation_coef:.2f}')

# Menghitung regresi sederhana
slope, intercept, r_value, p_value, std_err = stats.linregress(df['X'], df['Y'])
regression_line = intercept + slope * df['X']

# Menampilkan hasil uji regresi sederhana
st.subheader('Hasil Uji Regresi Sederhana')
st.write(f'Koefisien Regresi (slope): {slope:.2f}')
st.write(f'Intercept: {intercept:.2f}')
st.write(f'Koefisien Determinasi (R-squared): {r_value**2:.2f}')
st.write(f'p-value: {p_value:.4f}')
st.write(f'Standard Error: {std_err:.2f}')

# Plot regresi sederhana
fig, ax = plt.subplots()
ax.scatter(df['X'], df['Y'], label='Data')
ax.plot(df['X'], regression_line, color='red', label='Regresi Line')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Regresi Sederhana')
ax.legend()
st.subheader('Grafik Regresi Sederhana')
st.pyplot(fig)

# Interpretasi grafik regresi sederhana
st.subheader('Keterangan')
st.write('Grafik Regresi Sederhana menunjukkan hubungan linier antara variabel X dan Y. Garis regresi (garis merah) adalah hasil regresi sederhana yang memperkirakan hubungan linier antara X dan Y. Jika garis regresi memiliki kemiringan positif (slope positif), maka kita dapat menginterpretasikan bahwa terdapat kecenderungan positif antara X dan Y. Sebaliknya, jika garis regresi memiliki kemiringan negatif (slope negatif), maka terdapat kecenderungan negatif antara X dan Y.')

st.write('Koefisien Determinasi (R-squared) adalah ukuran seberapa baik model regresi memprediksi variabilitas Y berdasarkan variabel X. Nilai R-squared berkisar antara 0 hingga 1, dan semakin dekat ke 1, semakin baik model regresi memprediksi variabilitas Y.')

st.write('P-value menunjukkan signifikansi statistik dari hubungan linier antara X dan Y. Jika p-value lebih kecil dari tingkat signifikansi yang ditentukan (biasanya 0.05), kita dapat menyimpulkan bahwa ada hubungan yang signifikan antara X dan Y.')

st.write('Standard Error adalah estimasi kesalahan standar dari slope (koefisien regresi). Semakin kecil nilai standard error, semakin akurat estimasi slope.')

