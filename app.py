
import streamlit as st
import subprocess
import os

st.title("Audio Authenticity Checker")

uploaded_file = st.file_uploader("Upload Audio File", type=["wav"])

if uploaded_file is not None:

    # save uploaded file
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.audio("temp_audio.wav")

    # add watermark
    if st.button("Add Watermark"):

        subprocess.run(["python", "signer.py"])

        if os.path.exists("signed.wav"):
            st.success("Watermark added successfully")
            st.audio("signed.wav")
        else:
            st.error("Watermark generation failed")

    # verify watermark
    if st.button("Verify Audio"):

        result = subprocess.run(
            ["python", "verifier.py"],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if "ORIGINAL AUDIO VERIFIED" in output:
            st.success("✔ ORIGINAL AUDIO VERIFIED")
        else:
            st.error("✖ EDITED / TAMPERED AUDIO")
