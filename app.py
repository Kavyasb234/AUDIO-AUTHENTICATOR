import streamlit as st
import subprocess

st.title("Audio Authenticity Checker")

uploaded_file = st.file_uploader("Upload WAV Audio", type=["wav"])

if uploaded_file is not None:

    with open("uploaded.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.audio("uploaded.wav")

    if st.button("Add Watermark"):
        subprocess.run(["python", "signer.py", "uploaded.wav", "signed.wav"])
        st.success("Watermark added")

    if st.button("Verify Audio"):
        result = subprocess.run(
            ["python", "verifier.py", "uploaded.wav"],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if "ORIGINAL" in output:
            st.success("✔ ORIGINAL AUDIO VERIFIED")
        else:
            st.error("✖ EDITED / TAMPERED AUDIO")
