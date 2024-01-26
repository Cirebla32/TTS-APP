from pvrecorder import PvRecorder
import sounddevice
from pynput.keyboard import KeyCode, Controller, Listener
import speech_recognition as sr
import threading
import wave
import struct
from time import sleep

path = './audio/audio.wav'
r = sr.Recognizer()

keyboard = Controller()
audio = []
audio_copy = []
record = True
start = False
endPoint = 0

def speech_record_thread(name):
    global audio
    global start
    for index, device in enumerate(PvRecorder.get_available_devices()):
        print(f"[{index}] {device}")
    recorder = PvRecorder(frame_length=512, device_index=-1)
    recorder.start()
    start= True
    try:
        while record:
            # print('read')
            frame = recorder.read()
            audio.extend(frame)
            # print(audio)
        print('stop')
        recorder.stop()
    finally:
        recorder.delete()

def print_key(*key): 
    global record
    if key[0] == KeyCode.from_char('d'):
        record=False

def check_key():
    print('check_key en cours ...')
    try:
        with Listener(on_press=print_key) as listener:
                listener.join()  
    except KeyboardInterrupt:
        print('list_stop')
        listener.stop()

def stop_record_thread(name):
    check_key()

def stt():
    global endPoint

    # première methode

    # audio_copy = audio.copy()
    # audio.clear()

    # deuxième méthode

    audio_copy = audio[endPoint:].copy()
    endPoint = len(audio)

    with wave.open(path, 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio_copy), *audio_copy))
        with sr.AudioFile(path) as source:
            audio_text = r.listen(source)
        # recoginize_() La méthode générera une erreur de requête si l'API est inaccessible, utilisant donc la gestion des exceptions
            try:
                # utilisation de google speech recognition
                print('Convertion de l\'audio en texte ...')
                text = r.recognize_google(audio_text, language = 'fr-FR')
                print(text)
                
            except:
                print('Sorry.. run again...')



if __name__ == "__main__":
    sp_rc = threading.Thread(target=speech_record_thread, args=('stt-thread',))
    sp_rc.start()
    st_rc = threading.Thread(target=stop_record_thread, args=('stop-thread',))
    st_rc.start()

    while 1:
        if start:
            stt()
        sleep(5)
        if (not record and not audio[endPoint:]):
            break

    print('Je suis dehors')

    sp_rc.join()
    st_rc.join()
