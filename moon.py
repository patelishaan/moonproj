import streamlit as st
import cv2
from PIL import Image

def main():
    st.title("Resolution Selection and Camera Display")

    options = ['144p', '240p', '480p', '720p', '1080p']
    choice = st.selectbox("Select Resolution", options)

    if choice == '144p':
        image = Image.open("144p.png")
        st.image(image)

    elif choice == '240p':
        image = Image.open("240p.png")
        st.image(image)

    elif choice == '480p':
        image = Image.open("480p.png")
        st.image(image)

    elif choice == '720p':
        image = Image.open("720p.png")
        st.image(image)
    elif choice == '1080p':
        #st.write(f"Selecting {choice} for live camera feed...")
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

        if not cap.isOpened():
            st.error("Error: Could not open camera.")
        else:
            frame_placeholder = st.empty()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    st.error("Error: Failed to capture frame from camera.")
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_placeholder.image(frame, channels="RGB")

            cap.release()

if __name__ == "__main__":
    main()
