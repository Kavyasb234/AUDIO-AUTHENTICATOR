import numpy as np
from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq
import sys

if len(sys.argv) != 2:
    print("Usage: python verifier.py <wav_file>")
    sys.exit(1)

file_path = sys.argv[1]

# Load the audio file
sr, data = read(file_path)
y = data.astype(np.float32) / 32767.0

# Compute FFT
N = len(y)
yf = fft(y)
xf = fftfreq(N, 1 / sr)

# Find frequencies in the range 18.5 kHz to 19 kHz
mask = (xf >= 18500) & (xf <= 19000)
indices = np.where(mask)[0]

if len(indices) == 0:
    print("ALERT: INTEGRITY COMPROMISED")
    sys.exit(0)

# Check the maximum magnitude in the frequency band
max_magnitude = np.max(np.abs(yf[indices]))

# Threshold: empirical, based on added amplitude
# For amplitude 0.01, N samples, peak ~ 0.01 * N / 2
# But to be safe, set threshold to 10 (for short audio, adjust)
threshold = 10  # Adjust based on audio length

if max_magnitude > threshold:
    print("ORIGINAL AUDIO VERIFIED")
else:
    print("EDITED/TAMPERED AUDIO ")

