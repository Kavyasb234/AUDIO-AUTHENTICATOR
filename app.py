import numpy as np
from scipy.io.wavfile import write

# Create a simple test audio: 2 seconds of 440 Hz tone
sr = 44100
duration = 2
t = np.linspace(0, duration, int(sr * duration), endpoint=False)
y = 0.5 * np.sin(2 * np.pi * 440 * t)

# Save as test.wav
write('test.wav', sr, (y * 32767).astype(np.int16))
print("test.wav created")

# Now, sign it
import subprocess
subprocess.run(['python', 'signer.py', 'test.wav', 'signed.wav'])

# Verify signed
subprocess.run(['python', 'verifier.py', 'signed.wav'])

# Verify original
subprocess.run(['python', 'verifier.py', 'test.wav'])
