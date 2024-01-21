import sys
import os
from ui_tts import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show

def tts(): 
    text = window.ui.userInput.toPlainText() if window.ui.userInput.toPlainText() != "" else "."
    if window.ui.ttsChoice.value() == 1:
        lang = ["fr-FR", "en-US", "en-GB", "de-DE", "es-ES", "it-IT"]
        print("tts@epac>>> " + "pico2wave --lang=" + lang[window.ui.languageChoiceTTS.value() - 1] + """ --wave=/tmp/rc.wav " """ + str(text) + """ " && play /tmp/rc.wav""")
        a=os.system("pico2wave --lang=" + lang[window.ui.languageChoiceTTS.value() - 1] + """ --wave=/tmp/rc.wav " """ + str(text) + """ " && play /tmp/rc.wav""")
    elif window.ui.ttsChoice.value() == 2:
        lang = ["fr", "en", "en", "de", "es", "it"]
        print("tts@epac>>> " + """pico2wave --lang=fr-FR --wave=/tmp/rc.wav " """ + str(text) + """ " && play /tmp/rc.wav && rm /tmp/rc.wav""")
        a=os.system("espeak -a 200 -w /tmp/rc.wav -v " + lang[window.ui.languageChoiceTTS.value() - 1] + ' " ' + str(text) + """ " && play /tmp/rc.wav""")
    elif window.ui.ttsChoice.value() == 3:
        import pyttsx3
        import platform
        if platform.system() == "Linux":
            engine = pyttsx3.init('espeak')
        else:
            engine = pyttsx3.init('sapi5')
        engine.say("Ceci est juste un texte de test pour voir si ça marche.")
        engine.runAndWait()
    elif window.ui.ttsChoice.value() == 4:
        from gtts import gTTS
        from audioplayer import AudioPlayer
        lang = ["fr", "en", "en", "de", "es", "it"]
        print("lang>>> ", lang[window.ui.languageChoiceTTS.value() - 1])
        audio = gTTS(text=text, lang=lang[window.ui.languageChoiceTTS.value() - 1])
        audio.save("/tmp/rc.wav")
        AudioPlayer("/tmp/rc.wav").play(block=True)
        #a=os.system("""rm /tmp/rc.wav""")

def stt(): 
    import speech_recognition as sr
    window.ui.sttTextBrowser.clear()
    #Initialiser la classe Recognizer (pour reconnaître la parole)
    r = sr.Recognizer()
    # Lecture du fichier audio comme source
    # écouter le fichier audio et le stocker dans la variable audio_text
    with sr.AudioFile('/tmp/rc.wav') as source:
        audio_text = r.listen(source)
    # recoginize_() La méthode générera une erreur de requête si l'API est inaccessible, utilisant donc la gestion des exceptions
        try:
            # utilisation de google speech recognition
            lang = ["fr-FR", "en-US", "en-GB", "de-DE", "es-ES", "it-IT"]
            text = r.recognize_google(audio_text, language = lang[window.ui.languageChoiceSTT.value() - 1])
            print('Convertion de l\'audio en texte ...')
            print(text)
            window.ui.sttTextBrowser.insertPlainText(text)
        except:
            print('Sorry.. run again...')
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    window.ui.playTTSbtn.clicked.connect(tts)
    window.ui.stopRecSTTbtn.clicked.connect(stt)

    sys.exit(app.exec())
