import streamlit as st import numpy as np import cv2 from PIL import Image import io

إعداد الصفحة

st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

تصميم CSS

st.markdown(""" <style> .stApp { background: linear-gradient(to bottom, #e3f2fd, #ffffff); padding: 2rem; } .title { text-align: center; font-size: 36px; color: #0d47a1; font-weight: bold; margin-bottom: 1rem; } .subtitle { text-align: center; font-size: 20px; color: #1565c0; margin-bottom: 2rem; } .upload-box { background-color: #ffffffcc; padding: 20px; border-radius: 12px; border: 2px dashed #2196f3; margin-bottom: 20px; } </style> """, unsafe_allow_html=True)

العنوان

st.markdown("<div class='title'>مدرسة الأردن الأساسية المختلطة</div>", unsafe_allow_html=True) st.markdown("<div class='subtitle'>كيف سيبدو وجهك بعد 20 سنة من التدخين؟</div>", unsafe_allow_html=True)

رفع الصورة

st.markdown('<div class="upload-box">', unsafe_allow_html=True) uploaded_file = st.file_uploader("ارفع صورتك (jpg أو png)", type=["jpg", "jpeg", "png"]) st.markdown('</div>', unsafe_allow_html=True)

التأثير

def smoking_effect(img_np): faded = cv2.addWeighted(img_np, 0.9, np.full_like(img_np, 70), 0.1, 0) h, w = faded.shape[:2] mask = np.zeros((h, w), dtype=np.uint8) cv2.ellipse(mask, (w//2, h//2 + 20), (60, 20), 0, 0, 360, 255, -1) faded[mask > 0] = (faded[mask > 0] * 0.6).astype(np.uint8) gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY) edges = cv2.Canny(gray, 30, 100) edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB) result = cv2.addWeighted(faded, 1.0, edges_colored, 0.2, 0) return result

المعالجة

if uploaded_file: image = Image.open(uploaded_file).convert("RGB") img_np = np.array(image) processed = smoking_effect(img_np) result_img = Image.fromarray(processed)

col1, col2 = st.columns(2)
with col1:
    st.image(image, caption="قبل التدخين", use_column_width=True)
with col2:
    st.image(processed, caption="بعد 20 سنة من التدخين", use_column_width=True)

buf = io.BytesIO()
result_img.save(buf, format="PNG")
st.download_button("تحميل الصورة المعدلة", buf.getvalue(), "after_smoking.png", "image/png")
