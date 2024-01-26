import speech_recognition as sr
import sounddevice
from time import sleep
from pynput.keyboard import KeyCode, Controller, Listener
import threading
import ctypes
import time
import subprocess

r = sr.Recognizer()

keyboard = Controller()

def print_key(*key): ## prints key that is pressed
    # key is a tuple, so access the key(char) from key[1]
    print(key)
    if key[0] == KeyCode.from_char('d'):
        print('yes!')
        subprocess.run(['kill', str(speech.pid)])
        with sr.AudioFile('audio.wav') as source:
            audio_text = r.listen(source)
        # recoginize_() La méthode générera une erreur de requête si l'API est inaccessible, utilisant donc la gestion des exceptions
            try:
                # utilisation de google speech recognition
                text = r.recognize_google(audio_text, language = 'fr-FR')
                print('Convertion de l\'audio en texte ...')
                print(text)
                
            except:
                print('Sorry.. run again...')

def check_key():
    print('check_key running')
    try:
        with Listener(on_press=print_key) as listener:
                listener.join()  
    except KeyboardInterrupt:
        listener.stop()

speech = subprocess.Popen(['arecord', '-f', 'S16_LE', '-t', 'wav', 'audio.wav'])
# print(speech.pid)
check_key()
print('Je suis dehors')

# stream = os.popen('arecord audio.wav &')
# x= stream.readlines()
# print(x)
# print(x.args)
# print(x.returncode)
# print(x.stdout)
# print(x.stderr)


