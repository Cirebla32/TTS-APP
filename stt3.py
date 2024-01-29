from pvrecorder import PvRecorder
import sounddevice
from pynput.keyboard import KeyCode, Controller, Listener
import speech_recognition as sr
import threading
import wave
import struct
from time import sleep
from utils import tts_pico2wave
from deep_translator import GoogleTranslator

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

def read_record_thread(name):
    global start
    global record
    global audio
    while 1:
        if start:
            stt()
        sleep(5)
        if (not record and not audio[endPoint:]):
            break

def stopRecordSTT3():
    global record
    global text
    record=False

def stt():
    global endPoint
    global textBrowserSTTobj
    global textBrowser1STSobj
    global textBrowser2STSobj
    global lang1
    global lang2
    global lang3
    global is_STS

    # première methode

    audio_copy = audio.copy()
    audio.clear()

    # deuxième méthode

    # audio_copy = audio[endPoint:].copy()
    # endPoint = len(audio)

    with wave.open(path, 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio_copy), *audio_copy))
        with sr.AudioFile(path) as source:
            audio_text = r.listen(source)
        # recoginize_() La méthode générera une erreur de requête si l'API est inaccessible, utilisant donc la gestion des exceptions
            try:
                # utilisation de google speech recognition
                print('Convertion de l\'audio en texte ...')
                text = r.recognize_google(audio_text, language = lang1)
                print(text)
                if not is_STS:
                    textBrowserSTTobj.insertPlainText(text + "\n")
                else:
                    lang = {"fr-FR":0, "en-US":1, "en-GB":2, "de-DE":3, "es-ES":4, "it-IT":5}
                    textBrowser1STSobj.insertPlainText(text + "\n")
                    #----------------Translate
                    translation = GoogleTranslator(source=lang2[:2], target=lang3[:2]).translate(text)
                    with open("data/translation_result.txt", "w") as f:
                        f.write(translation)
                    print(text, "-->", translation)
                    
                    textBrowser2STSobj.insertPlainText(translation + "\n")
                    tts_pico2wave(lang[lang3], translation)

                
            except:
                print('Sorry.. run again...')
                return None




def recordSTT3(language1, textBrowserSTT, language2, textBrowser1STS, language3, textBrowser2STS, isSTS):
    global record
    global textBrowserSTTobj
    global textBrowser1STSobj
    global textBrowser2STSobj
    global lang1
    global lang2
    global lang3
    global is_STS
    is_STS = isSTS
    lang1 = language1
    lang2 = language2
    lang3 = language3
    textBrowserSTTobj = textBrowserSTT
    textBrowser1STSobj = textBrowser1STS
    textBrowser2STSobj = textBrowser2STS
    record = True
    sp_rc = threading.Thread(target=speech_record_thread, args=('stt-thread',))
    sp_rc.start()
    st_rc = threading.Thread(target=read_record_thread, args=('stop-thread',))
    st_rc.start()

    

    print('Je suis dehors')

