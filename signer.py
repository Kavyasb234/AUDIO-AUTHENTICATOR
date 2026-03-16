import numpy as np
from scipy.io import wavfile
from scipy.signal import resample

in_file = "temp_audio.wav"
out_file = "signed.wav"

sr, data = wavfile.read(in_file)

# convert to mono
if len(data.shape) > 1:
    data = data.mean(axis=1)

data = data.astype(np.float32)

# ensure 44.1 kHz
target_sr = 44100
if sr != target_sr:
    duration = len(data) / sr
    new_len = int(duration * target_sr)
    data = resample(data, new_len)
    sr = target_sr

# watermark
freq = 18750
t = np.arange(len(data)) / sr
watermark = 0.05 * np.sin(2*np.pi*freq*t)

watermarked = data + watermark

wavfile.write(out_file, sr, watermarked.astype(np.int16))

print("Watermarked audio saved to signed.wav")

