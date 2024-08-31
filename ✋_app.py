import streamlit as st
import base64

# Sayfa ayarları
st.set_page_config(page_title="Yapay Zeka ile Mülakata Hoş Geldiniz", layout="centered")

# Sayfanın ortasında yazı
st.markdown(
    "<div style='display: flex; flex-direction: column; align-items: center; height: 50vh; justify-content: center;'>"
    "<h1 style='text-align: center; font-size: 3rem;'>📝 Yapay Zeka ile Mülakata Hoş Geldiniz</h1>"
    "</div>",
    unsafe_allow_html=True,
)

# GIF eklemek için fonksiyon
def add_gif(gif_url):
    gif_data = base64.b64encode(open(gif_url, "rb").read()).decode("utf-8")
    st.markdown(
        f'<img src="data:image/gif;base64,{gif_data}" alt="Welcome GIF" style="display:block; margin-left:auto; margin-right:auto; width: 20%; height: auto; border-radius: 8px; margin-top: -20px;">',
        unsafe_allow_html=True,
    )

# Hoşgeldiniz yazısı altına GIF ekleyin
gif_path = "Animation - 1725102837238.gif"  # Kullanmak istediğiniz GIF'in yolunu belirtin
add_gif(gif_path)

# GIF altına etkileyici bir yazı
st.markdown(
    "<div style='text-align: center; font-size: 1.25rem; margin-top: 10px; margin-bottom: 40px;'>"
    "<p>Bu platform, iş arayanlar ve profesyoneller için geleceğin mülakat deneyimini sunuyor. İster kendinizi geliştirmek için farklı yapay zeka tabanlı chat botlarla iletişim kurun, ister bir mülakat simülasyonu ile gerçekçi bir deneyim yaşayın. Her biri özenle tasarlanmış botlarımız, sizi profesyonel olarak bir adım öne taşıyacak kişisel ve pozisyonunuza özel sorular ile en iyi versiyonunuzu ortaya çıkarmanıza yardımcı olacak. Şimdi başlayın ve geleceğin iş dünyasına bir adım önde girin. </p>"
    "<p style='font-size: 18px;'>O zaman başlamaya hazır mısınız ?</p>"
    "</div>",
    unsafe_allow_html=True,
)

# Sayfanın en altına "Hakkımızda" bölümü
st.markdown(
    "<div style='text-align: center; font-size: 1.5rem; margin-top: 40px;'>"
    "<hr>"
    "<h2>Hakkımızda</h2>"
    "<p style='font-size: 1rem;'>Yapay Zeka ile Mülakat platformu, iş arayanların ve profesyonellerin kendilerini geliştirmeleri için "
    "tasarlanmış bir araçtır. Amacımız, en güncel teknolojileri kullanarak, her adayın en iyi versiyonunu ortaya çıkarmaktır.</p>"
    "</div>",
    unsafe_allow_html=True,
)

# Bize Ulaşın kısmı
st.markdown(
    """
    <div style='text-align: center; margin-top: 50px;'>
        <h2>📞 Bize Ulaşın</h2>
        <p>Sorularınız veya geri bildiriminiz için bizimle iletişime geçin.</p>
        <div style='display: flex; justify-content: center; gap: 20px;'>
            <a href="https://www.instagram.com/sizin_hesabiniz" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="40" height="40">
            </a>
            <a href="https://www.linkedin.com/sizin_hesabiniz" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="40" height="40">
            </a>
            <a href="https://www.facebook.com/sizin_hesabiniz" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="40" height="40">
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
