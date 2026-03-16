import numpy as np
from scipy.io.wavfile import read, write
import sys

if len(sys.argv) != 3:
    print("Usage: python signer.py <input_wav> <output_wav>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Load the audio file
sr, data = read(input_file)
if len(data.shape) > 1:
    data = data.mean(axis=1)
y = data.astype(np.float32) / 32767.0  # Normalize to float

# Ensure sample rate is high enough
if sr < 44100:
    print("Warning: Sample rate is low, high frequencies may not be captured properly.")

# Generate the watermark tone: 18.75 kHz, low amplitude
duration = len(y) / sr
t = np.linspace(0, duration, len(y), endpoint=False)
freq = 18750  # Hz
amplitude = 0.01  # Inaudible amplitude
tone = amplitude * np.sin(2 * np.pi * freq * t)

# Add the tone to the audio
y_watermarked = y + tone

# Normalize to prevent clipping
y_watermarked = np.clip(y_watermarked, -1, 1)

# Save the watermarked audio
write(output_file, sr, (y_watermarked * 32767).astype(np.int16))

print(f"Watermarked audio saved to {output_file}")
