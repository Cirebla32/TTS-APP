def tts_espeak(
    langNum=0, text="Ceci est juste un texte de test pour voir si ça marche."
):
    import os
    lang = ["fr", "en", "en", "de", "es", "it"]
    print(
        "tts@epac>>> "
        + """espeak --lang=fr-FR --wave=data/tts_result.wav " """
        + str(text)
        + """ " && play data/tts_result.wav"""
    )
    a = os.system(
        "espeak -a 200 -w data/tts_result.wav -v "
        + lang[langNum - 1]
        + ' " '
        + str(text)
        + """ " && play data/tts_result.wav"""
    )


def tts_pico2wave(
    langNum=1, text="Ceci est juste un texte de test pour voir si ça marche."
):
    import os

    lang = ["fr-FR", "en-US", "en-GB", "de-DE", "es-ES", "it-IT"]
    print(
        "tts@epac>>> "
        + "pico2wave --lang="
        + lang[langNum - 1]
        + """ --wave=data/tts_result.wav " """
        + str(text)
        + """ " && play data/tts_result.wav"""
    )
    a = os.system(
        "pico2wave --lang="
        + lang[langNum - 1]
        + """ --wave=data/tts_result.wav " """
        + str(text)
        + """ " && play data/tts_result.wav"""
    )


def tts_pyttsx3(text):
    import pyttsx3
    import platform

    if platform.system() == "Linux":
        engine = pyttsx3.init("espeak")
    else:
        engine = pyttsx3.init("sapi5")
    engine.say(text)
    engine.runAndWait()


def tts_gtts(text, langNum):
    from gtts import gTTS
    from audioplayer import AudioPlayer

    lang = ["fr", "en", "en", "de", "es", "it"]
    audio = gTTS(text=text, lang=lang[langNum - 1])
    audio.save("data/tts_result.wav")
    AudioPlayer("data/tts_result.wav").play(block=True)
    
    
def translate(text, langSource, langTarget):
    from deep_translator import GoogleTranslator

    translated = GoogleTranslator(source=langSource, target=langTarget).translate(text)
    with open("data/translation_result.txt", "w") as f:
        f.write(translated)
    print(text, "-->", translated)
    return translated