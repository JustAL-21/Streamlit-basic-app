import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = ":fire:"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Jajar Genjang"])
    st.caption("Created By **Raffi Alfattah**")


match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `Luas` dan `Keliling` Persegi")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()


    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `Luas` dan `Keliling` Persegi panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()


    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `Luas` dan `Keliling` Lingkaran")
        jarijari = st.number_input("Masukkan Jari-jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jarijari * jarijari
            keliling = 2 * 3.14 * jarijari
            st.success(f"Luas lingkaran adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()


    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `Luas` dan `Keliling` Segitiga")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        s1 = st.number_input("Masukkan sisi 1")
        s2 = st.number_input("Masukkan sisi 2")
        s3 = st.number_input("Masukkan sisi 3")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = s1 + s2 + s3
            st.success(f"Luas segitiga adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()
    

    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung `Luas` dan `Keliling` Jajar Genjang")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi = st.number_input("Masukkan sisi")
        if st.button("Hitung", type="primary"):
            luas = alas * tinggi
            keliling = 2 * (alas + sisi)
            st.success(f"Luas jajar genjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()


    case _ :
        st.error("Terjadi Kesalahan")