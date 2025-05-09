import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io

# إعداد الصفحة
st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# تصميم CSS
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom, #e3f2fd, #ffffff);
            padding: 2rem;
        }
        .title {
            text-align: center;
            font-size: 36px;
            color: #0d47a1;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #1565c0;
            margin-bottom: 2rem;
