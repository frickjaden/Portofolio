import streamlit as st
from PIL import Image # Untuk mengelola gambar
import base64 # Untuk meng-encode gambar ke base64 jika diperlukan untuk CSS atau metode lain

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Portofolio Anda",
    page_icon="✨",
    layout="centered", # Bisa 'wide' atau 'centered'
    initial_sidebar_state="expanded" # Bisa 'expanded' atau 'collapsed'
)

# --- Load Custom CSS ---
try:
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("File 'style.css' tidak ditemukan. Tampilan mungkin kurang menarik. Pastikan file tersebut berada di direktori yang sama.")

# --- Helper Function to create a section header ---
def section_header(title):
    st.markdown(f"<h2 class='section-header'>{title}</h2>", unsafe_allow_html=True)
    st.markdown("---")

# --- Profil Info (untuk Sidebar) ---
PROFILE_PIC_PATH = "profile_pic.jpg" # Pastikan nama file dan path benar
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/nama_anda",
    "GitHub": "https://github.com/nama_anda",
    "Medium": "https://medium.com/@nama_anda",
    "Email": "mailto:email_anda@example.com"
}

# --- SIDEBAR ---
with st.sidebar:
    st.header("Navigasi")
    # Tautan navigasi sebagai radio button atau selectbox
    selected_section = st.radio(
        "",
        ["Tentang Saya", "Proyek", "Keterampilan", "Kontak"],
        key="portfolio_navigation"
    )

    st.markdown("---")
    st.header("Profil")
    try:
        profile_pic = Image.open(PROFILE_PIC_PATH)
        st.image(profile_pic, width=150, caption="Foto Profil Anda")
    except FileNotFoundError:
        st.warning("Foto profil tidak ditemukan. Harap letakkan 'profile_pic.jpg' di direktori yang sama.")

    st.write("---")
    st.write("### Ikuti Saya:")
    for platform, link in SOCIAL_MEDIA.items():
        st.markdown(f"[{platform}]({link})")

# --- MAIN CONTENT AREA ---

if selected_section == "Tentang Saya":
    section_header("Tentang Saya")
    st.markdown("""
        <p>Halo! Saya [Nama Anda], seorang [Jabatan Anda, misal: Data Scientist / Web Developer / Desainer Grafis] dengan pengalaman dalam [sebutkan beberapa bidang keahlian, misal: analisis data, pengembangan front-end, desain UI/UX].</p>
        <p>Saya bersemangat untuk [sebutkan minat atau tujuan Anda, misal: mengubah data kompleks menjadi wawasan yang mudah dipahami / membangun aplikasi web yang intuitif dan responsif / menciptakan pengalaman visual yang menawan].</p>
        <p>Saya memiliki latar belakang pendidikan di [bidang pendidikan Anda] dari [Nama Universitas Anda].</p>
        <p>Selamat datang di portofolio saya!</p>
    """, unsafe_allow_html=True)

elif selected_section == "Proyek":
    section_header("Proyek")
    # Proyek 1
    st.subheader("Proyek 1: [Nama Proyek Anda Pertama]")
    st.markdown("""
        <p><b>Deskripsi:</b> [Jelaskan singkat tentang proyek ini, apa tujuannya, dan apa yang Anda lakukan].</p>
        <p><b>Teknologi:</b> [Python, Streamlit, Pandas, Plotly, dll.]</p>
        <p><b>Demo/Link:</b> [Link ke GitHub, live demo, atau video penjelasan]</p>
    """, unsafe_allow_html=True)
    st.image("project1_image.jpg", caption="Gambar Proyek 1 (opsional)", use_column_width=True) # Ganti dengan gambar proyek Anda
    st.markdown("---")

    # Proyek 2
    st.subheader("Proyek 2: [Nama Proyek Anda Kedua]")
    st.markdown("""
        <p><b>Deskripsi:</b> [Jelaskan singkat tentang proyek ini].</p>
        <p><b>Teknologi:</b> [HTML, CSS, JavaScript, React, dll.]</p>
        <p><b>Demo/Link:</b> [Link ke GitHub, live demo, atau video penjelasan]</p>
    """, unsafe_allow_html=True)
    st.image("project2_image.jpg", caption="Gambar Proyek 2 (opsional)", use_column_width=True) # Ganti dengan gambar proyek Anda
    st.markdown("---")

    # Tambahkan proyek lain jika ada...

elif selected_section == "Keterampilan":
    section_header("Keterampilan")
    st.subheader("Bahasa Pemrograman")
    st.write("Python, SQL, JavaScript, R, Java, dll.") # Sesuaikan

    st.subheader("Framework & Pustaka")
    st.write("Streamlit, Pandas, NumPy, Scikit-learn, Plotly, Matplotlib, React, Django, Flask, dll.") # Sesuaikan

    st.subheader("Alat & Platform")
    st.write("Git, GitHub, Docker, AWS, Google Cloud Platform, Microsoft Azure, Power BI, Tableau, Figma, Adobe Photoshop, dll.") # Sesuaikan

    st.subheader("Bidang Keahlian")
    st.write("Analisis Data, Pembelajaran Mesin, Pengembangan Web (Front-end/Back-end), Desain Grafis, Manajemen Proyek, dll.") # Sesuaikan

elif selected_section == "Kontak":
    section_header("Kontak")
    st.markdown("""
        <p>Tertarik untuk berkolaborasi atau ingin mengetahui lebih lanjut? Jangan ragu untuk menghubungi saya!</p>
        <p><b>Email:</b> email_anda@example.com</p>
        <p><b>LinkedIn:</b> [Link LinkedIn Anda]</p>
        <p><b>GitHub:</b> [Link GitHub Anda]</p>
        <p>Atau gunakan formulir di bawah ini:</p>
    """, unsafe_allow_html=True)

    # Formulir Kontak (Streamlit native form)
    with st.form("contact_form"):
        name = st.text_input("Nama Anda")
        email = st.text_input("Email Anda")
        message = st.text_area("Pesan Anda")
        submitted = st.form_submit_button("Kirim Pesan")

        if submitted:
            if name and email and message:
                st.success(f"Terima kasih, {name}! Pesan Anda telah terkirim. Saya akan segera menghubungi Anda.")
                # Di sini Anda bisa menambahkan logika untuk mengirim email atau menyimpan pesan
                # Contoh: print(f"Pesan dari {name} ({email}): {message}")
            else:
                st.error("Harap isi semua kolom formulir.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>© 2025 Nama Anda. Hak Cipta Dilindungi.</p>", unsafe_allow_html=True)
