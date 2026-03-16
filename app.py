import streamlit as st
import subprocess
import os

st.title("Audio Authenticity Checker")

uploaded_file = st.file_uploader("Upload Audio File", type=["wav"])

# Track if watermark was added in this session
if "watermark_added" not in st.session_state:
    st.session_state.watermark_added = False

if uploaded_file is not None:

    # Save uploaded file
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.audio("temp_audio.wav")

    # ADD WATERMARK
    if st.button("Add Watermark"):
        subprocess.run(["python", "signer.py"])
        st.session_state.watermark_added = True

        if os.path.exists("signed.wav"):
            st.success("Watermark added successfully")
            st.audio("signed.wav")
        else:
            st.error("Watermark generation failed")

    # VERIFY AUDIO
    if st.button("Verify Audio"):

        # Decide which file to verify
        file_to_verify = "signed.wav" if st.session_state.watermark_added else "temp_audio.wav"

        result = subprocess.run(
            ["python", "verifier.py", file_to_verify],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if "ORIGINAL AUDIO VERIFIED" in output:
            st.success("✔ ORIGINAL AUDIO VERIFIED")
        else:
            st.error("✖ EDITED / TAMPERED AUDIO")

            
