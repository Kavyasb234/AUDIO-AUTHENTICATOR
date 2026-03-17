import streamlit as st
import time
import random
from detector import LatencyDetector

st.title("Latency-Based SQL Injection Detector")

st.write("Detects time-based SQL injection using response latency.")

# Only ONE control (optional)
delay = st.slider("Injected Delay (seconds)", 1.0, 5.0, 4.0)

if st.button("Start Monitoring"):

    detector = LatencyDetector()

    for i in range(20):  # fixed small steps
        start_time = time.time()

        # normal query
        time.sleep(random.uniform(0.01, 0.1))

        # simulate attack
        time.sleep(delay)

        latency = time.time() - start_time

        detected, msg = detector.detect(latency)

        if detected:
            st.error(msg)
        else:
            st.success(msg)

        time.sleep(0.3)
        
        
