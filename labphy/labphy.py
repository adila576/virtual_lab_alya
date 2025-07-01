import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

def display_pythagorean_lab():
    """Menampilkan antarmuka laboratorium Pythagoras."""
    st.title("🔬 Laboratorium Pythagoras")
    st.write("Gunakan slider di bawah untuk mengatur panjang sisi 'a' dan 'b' segitiga siku-siku.")

    # Slider untuk sisi a dan sisi b
    col1, col2 = st.columns(2)
    with col1:
        side_a = st.slider("Panjang Sisi a", 1.0, 10.0, 3.0, 0.1)
    with col2:
        side_b = st.slider("Panjang Sisi b", 1.0, 10.0, 4.0, 0.1)

    # Hitung sisi c
    side_c = math.sqrt(side_a**2 + side_b**2)

    st.write(f"---")
    st.subheader("Hasil Perhitungan")
    st.write(f"Panjang Sisi a: **{side_a:.2f}**")
    st.write(f"Panjang Sisi b: **{side_b:.2f}**")
    st.write(f"Panjang Sisi c (Sisi Miring): **{side_c:.2f}**")

    st.write(f"---")
    st.subheader("Visualisasi Segitiga Siku-siku")

    # Buat plot segitiga
    fig, ax = plt.subplots(figsize=(6, 6))

    # Koordinat segitiga
    # Titik sudut siku-siku
    p_origin = np.array([0, 0])
    # Titik sudut a (sisi horizontal)
    p_a = np.array([side_b, 0])
    # Titik sudut b (sisi vertikal)
    p_b = np.array([0, side_a])

    # Plot sisi-sisi segitiga
    ax.plot([p_origin[0], p_a[0]], [p_origin[1], p_a[1]], 'b-', lw=2, label='Sisi b') # Sisi alas
    ax.plot([p_origin[0], p_b[0]], [p_origin[1], p_b[1]], 'g-', lw=2, label='Sisi a') # Sisi tegak
    ax.plot([p_a[0], p_b[0]], [p_a[1], p_b[1]], 'r-', lw=2, label='Sisi c (Miring)') # Sisi miring

    # Tambahkan teks label sisi
    ax.text(side_b / 2, -0.5, f'b = {side_b:.2f}', ha='center', va='top', color='b', fontsize=12)
    ax.text(-0.5, side_a / 2, f'a = {side_a:.2f}', ha='right', va='center', color='g', fontsize=12)
    ax.text(side_b * 0.6, side_a * 0.6, f'c = {side_c:.2f}', ha='center', va='bottom', color='r', fontsize=12, rotation=math.degrees(math.atan2(side_a, side_b)))

    # Atur batas plot agar segitiga terlihat jelas
    max_side = max(side_a, side_b, side_c) * 1.2
    ax.set_xlim(-1, max_side)
    ax.set_ylim(-1, max_side)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel("Sumbu X")
    ax.set_ylabel("Sumbu Y")
    ax.set_title("Representasi Segitiga Siku-siku")
    ax.grid(True)

    st.pyplot(fig)

def display_how_to_use():
    """Menampilkan langkah-langkah penggunaan."""
    st.title("Panduan Penggunaan Laboratorium Pythagoras")
    st.markdown("""
    Selamat datang di Laboratorium Pythagoras! Ikuti langkah-langkah di bawah untuk menggunakan aplikasi ini:

    1.  **Pilih 'Laboratorium Pythagoras'**: Dari menu sidebar di sebelah kiri, pastikan Anda berada di halaman utama Laboratorium Pythagoras.
    2.  **Atur Panjang Sisi a dan b**: Anda akan melihat dua slider:
        * **"Panjang Sisi a"**: Gunakan slider ini untuk mengatur panjang sisi tegak segitiga siku-siku.
        * **"Panjang Sisi b"**: Gunakan slider ini untuk mengatur panjang sisi alas segitiga siku-siku.
    3.  **Lihat Hasil Perhitungan**: Setelah Anda menyesuaikan slider, aplikasi akan secara otomatis menghitung dan menampilkan:
        * Panjang Sisi a
        * Panjang Sisi b
        * **Panjang Sisi c (Sisi Miring)**, yang dihitung menggunakan teorema Pythagoras ($c = \sqrt{a^2 + b^2}$).
    4.  **Amati Visualisasi Segitiga**: Di bawah hasil perhitungan, Anda akan melihat representasi visual dari segitiga siku-siku Anda dengan panjang sisi yang telah diperbarui.
    5.  **Akses Panduan Penggunaan**: Jika Anda ingin melihat panduan ini lagi, klik tombol "Panduan Penggunaan" di sidebar.

    Selamat bereksperimen dengan Teorema Pythagoras!
    """)

# Main aplikasi Streamlit
def main():
    st.sidebar.title("Navigasi")
    menu_options = {
        "Laboratorium Pythagoras": display_pythagorean_lab,
        "Panduan Penggunaan": display_how_to_use
    }
    
    selected_page = st.sidebar.radio("Pilih Halaman", list(menu_options.keys()))

    # Panggil fungsi yang sesuai dengan halaman yang dipilih
    menu_options[selected_page]()

if __name__ == "__main__":
    main()
