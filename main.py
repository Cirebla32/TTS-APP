import sys
import os
from ui_tts import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show

def play(): 
    text = window.ui.userInput.toPlainText() if window.ui.userInput.toPlainText() != "" else "."
    if window.ui.ttsChoice.value() == 1:
        lang = ["fr-FR", "en-US", "en-GB", "de-DE", "es-ES", "it-IT"]
        print("tts@epac>>> " + "pico2wave --lang=" + lang[window.ui.languageChoice.value() - 1] + """ --wave=/tmp/rc.wav " """ + str(text) + """ " && play /tmp/rc.wav""")
        a=os.system("pico2wave --lang=" + lang[window.ui.languageChoice.value() - 1] + """ --wave=/tmp/rc.wav " """ + str(text) + """ " && play /tmp/rc.wav""")
    elif window.ui.ttsChoice.value() == 2:
        print("tts@epac>>> " + """pico2wave --lang=fr-FR --wave=/tmp/rc.wav " """ + str(text) + """ " && play /tmp/rc.wav""")
        a=os.system("""espeak -a 200 -w /tmp/rc.wav " """ + str(text) + """ " && play /tmp/rc.wav""")
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
        audio = gTTS(text=text, lang='fr')
        audio.save("/tmp/rc.wav")
        AudioPlayer("/tmp/rc.wav").play(block=True)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    window.ui.playTTSbtn.clicked.connect(play)

    sys.exit(app.exec())
