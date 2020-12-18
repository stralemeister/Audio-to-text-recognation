import speech_recognition as sr
import inspect

r = sr.Recognizer()
file_audio = sr.AudioFile('test.wav')

with file_audio as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio_text = r.record(source)

#src = inspect.getsource(sr)
#print(src)

#print(type(audio_text))
print(r.recognize_google(audio_text))
