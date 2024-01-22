import sys
import platform
from ui_tts import *
from ui_dialog import *
from utils import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show

class groupe1Dlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

def showGroup1():
        dlg = groupe1Dlg()
        dlg.setWindowTitle("Group 1 Members")
        dlg.exec()


def tts():
    text = (
        window.ui.userInput.toPlainText()
        if window.ui.userInput.toPlainText() != ""
        else "."
    )
    if window.ui.ttsChoice.currentIndex() == 0:
        tts_pico2wave(window.ui.languageChoiceTTS.currentIndex(), text)
    elif window.ui.ttsChoice.currentIndex() == 1:
        tts_espeak(window.ui.languageChoiceTTS.currentIndex(), text)
    elif window.ui.ttsChoice.currentIndex() == 2:
        tts_pyttsx3(text)
    elif window.ui.ttsChoice.currentIndex() == 3:
        tts_gtts(text, window.ui.languageChoiceTTS.currentIndex())





def stt_recorded():
    recorded = record(5, "data/recorded_speech.mp3")
    stt_result = stt_google(recorded)
    return stt_result

def stt():
    path_to_speech = "data/tts_result.wav"
    stt_result = stt_google(path_to_speech)
    return stt_result
    
def stt_google(speech):
    import speech_recognition as sr

    window.ui.sttTextBrowser.clear()
    # Initialiser la classe Recognizer (pour reconnaître la parole)
    r = sr.Recognizer()
    # Lecture du fichier audio comme source
    # écouter le fichier audio et le stocker dans la variable audio_text
    text = None
    with sr.AudioFile(speech) as source:
        audio_text = r.listen(source)
        # recoginize_() La méthode générera une erreur de requête si l'API est inaccessible, utilisant donc la gestion des exceptions
        try:
            # utilisation de google speech recognition
            lang = ["fr-FR", "en-US", "en-GB", "de-DE", "es-ES", "it-IT"]
            text = r.recognize_google(
                audio_text, language=lang[window.ui.languageChoiceSTT.currentIndex()]
            )
            print("Convertion de l'audio en texte ...")
            print(text)
            window.ui.sttTextBrowser.insertPlainText(text)
        except:
            print("Sorry.. run again...")
        return text



def sts():
    # ------------------STT---------------------
    sttLang = window.ui.languageChoiceSTT.currentIndex()
    sttText = window.ui.sttTextBrowser.toPlainText()
    window.ui.sttTextBrowser.clear()
    window.ui.languageChoiceSTT.setCurrentIndex(window.ui.language1ChoiceSTS.currentIndex())
    # Le chemin de l'audio utilisé pour stt étant pareil que celui de sts
    text = stt()
    window.ui.languageChoiceSTT.setCurrentIndex(sttLang)
    window.ui.sttTextBrowser.clear()
    window.ui.sttTextBrowser.insertPlainText(sttText)
    window.ui.stsText1Browser.clear()
    window.ui.stsText1Browser.insertPlainText(text)

    # ---------------TRANSLATE-------------------
    lang = ["fr", "en", "en", "de", "es", "it"]
    textTranslated = translate(
        text,
        lang[window.ui.language1ChoiceSTS.currentIndex()],
        lang[window.ui.language2ChoiceSTS.currentIndex()],
    )
    window.ui.stsText2Browser.clear()
    window.ui.stsText2Browser.insertPlainText(textTranslated)

    # ------------------TTS-----------------------
    ttsText = window.ui.userInput.toPlainText()
    ttsLang = window.ui.languageChoiceTTS.currentIndex()
    ttsTTS = window.ui.ttsChoice.currentIndex()
    if platform.system() == "Linux":
        window.ui.ttsChoice.setCurrentIndex(0)  # TTS de pico2wave
    else:
        window.ui.ttsChoice.setCurrentIndex(3)  # TTS de Google
    window.ui.languageChoiceTTS.setCurrentIndex(window.ui.language2ChoiceSTS.currentIndex())
    window.ui.userInput.clear()
    window.ui.userInput.setPlainText(textTranslated)
    tts()
    window.ui.userInput.clear()
    window.ui.userInput.setPlainText(ttsText)
    window.ui.languageChoiceTTS.setCurrentIndex(ttsLang)
    window.ui.ttsChoice.setCurrentIndex(ttsTTS)


def ttt():
    lang = ["fr", "en", "en", "de", "es", "it"]
    window.ui.stsText2Browser.clear()
    window.ui.stsText2Browser.setPlainText(
        translate(
            window.ui.stsText1Browser.toPlainText(),
            lang[window.ui.language1ChoiceSTS.currentIndex()],
            lang[window.ui.language2ChoiceSTS.currentIndex()],
        )
    )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("TTS - STT - TTT - STS")
    window.show()

    window.ui.playTTSbtn.clicked.connect(tts)
    # window.ui.recSTTbtn.clicked.connect(stt)
    window.ui.stopRecSTTbtn.clicked.connect(stt)
    window.ui.clearSTTbtn.clicked.connect(window.ui.sttTextBrowser.clear)
    # window.ui.recSTSbtn.clicked.connect(stt)
    window.ui.playSTSbtn.clicked.connect(sts)
    window.ui.clearSTSbtn.clicked.connect(window.ui.stsText1Browser.clear)
    window.ui.clearSTSbtn.clicked.connect(window.ui.stsText2Browser.clear)
    window.ui.tttBtn.clicked.connect(ttt)
    window.ui.group1Btn.clicked.connect(showGroup1)

    sys.exit(app.exec())
