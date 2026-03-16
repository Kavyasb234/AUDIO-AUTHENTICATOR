import streamlit as st
import subprocess
import os

st.title("Audio Authenticity Checker")

uploaded_file = st.file_uploader("Upload WAV Audio", type=["wav","mp3"])

if uploaded_file is not None:

    # Save uploaded file
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.audio("temp_audio.wav")

    # ADD WATERMARK
    if st.button("Add Watermark"):
        subprocess.run(["python", "signer.py", "temp_audio.wav", "signed.wav"])

        st.session_state["signed_file"] = "signed.wav"
        st.success("Watermark added")

    # VERIFY AUDIO
    if st.button("Verify Audio"):

        # check if watermark file exists
        file_to_verify = st.session_state.get("signed_file")

        if file_to_verify and os.path.exists(file_to_verify):

            result = subprocess.run(
                ["python", "verifier.py", file_to_verify],
                capture_output=True,
                text=True
            )

            if "OK" in result.stdout or "INTEGRITY OK" in result.stdout:
                st.success("ORIGINAL AUDIO VERIFIED")

            else:
                st.error("EDITED / TAMPERED AUDIO")

        else:
            st.warning("Please click 'Add Watermark' first")
