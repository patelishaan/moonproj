import streamlit as st
import cv2
from PIL import Image
st.write('make a selection')
options = ['144p','240p','480p','720p','1080p']
choice = st.selectbox("choose", options)
if choice=='144p':
    image = Image.open("144p.png")
    st.image(image)
    #st.write('144p')
if choice=='240p':
    image = Image.open("240p.png")
    st.image(image)
if choice=='480p':
    image = Image.open("480p.png")
    st.image(image)
if choice=='720p':
    image = Image.open("720p.png")
    st.image(image)
if choice=='1080p':
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.write('the video capture has ended')
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")

    cap.release()

