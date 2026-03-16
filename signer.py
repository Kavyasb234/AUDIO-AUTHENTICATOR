import numpy as np
from scipy.io import wavfile

input_file = "temp_audio.wav"
output_file = "signed.wav"

sr, data = wavfile.read(input_file)

# convert stereo to mono
if len(data.shape) > 1:
    data = data.mean(axis=1)

data = data.astype(np.float32)

# watermark frequency
freq = 18750

t = np.arange(len(data)) / sr

# create watermark signal
watermark = 0.02 * np.sin(2 * np.pi * freq * t)

watermarked = data + watermark

wavfile.write(output_file, sr, watermarked.astype(np.int16))

print("Watermarked audio saved to signed.wav")

