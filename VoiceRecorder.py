import sounddevice as sd # for provides function of play and record the numpy arrays
import wavio as wv 
from scipy.io.wavfile import write # Wavio and scipy are used to save the audio in the file format

freq = 44100

dur=10

recording = sd.rec(int(dur * freq), samplerate=freq, channels =2) # No. of channels can be one or two only.

sd.wait()

write("recording0.wav", freq, recording)
wv.write("recording1.wav", freq, recording, sampwidth=3)