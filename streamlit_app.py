import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="画像縮小アプリ", layout="centered")
st.title("📐 画像縮小アプリ（完全ローカル処理）")

uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="元画像", use_column_width=True)

    st.subheader("縮小サイズの指定")
    width = st.slider("幅（px）", min_value=50, max_value=img.width, value=int(img.width / 2))
    height = int(img.height * (width / img.width))

    resized_img = img.resize((width, height))
    st.image(resized_img, caption="縮小後の画像", use_column_width=True)

    buf = io.BytesIO()
    resized_img.save(buf, format="PNG")
    byte_data = buf.getvalue()

    st.download_button(
        label="📥 縮小画像をダウンロード",
        data=byte_data,
        file_name="resized.png",
        mime="image/png"
    )
else:
    st.info("画像ファイル（JPG/PNG）をアップロードしてください。")
