import numpy as np
from scipy.io import wavfile

file = "signed.wav"

sr, data = wavfile.read(file)

# convert to mono
if len(data.shape) > 1:
    data = data.mean(axis=1)

data = data.astype(np.float32)

fft = np.abs(np.fft.rfft(data))
freqs = np.fft.rfftfreq(len(data), 1/sr)

mask = (freqs > 18500) & (freqs < 19000)

peak = np.max(fft[mask])

if peak > 1000:
    print("ORIGINAL AUDIO VERIFIED")
else:
    print("EDITED / TAMPERED AUDIO")
