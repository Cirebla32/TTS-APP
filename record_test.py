import speech_recognition as sr
import sounddevice as sd

r = sr.Recognizer()
# print(sr.Microphone.list_microphone_names())
mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)