def tts_espeak(
    langNum=0, text="Ceci est juste un texte de test pour voir si ça marche."
):
    """
    Convertit un texte en parole en utilisant le moteur de synthèse vocale eSpeak.

    Args:
        langNum (int, optionnel): Le numéro de la langue à utiliser. Par défaut, 0 correspond au français.
        text (str, optionnel): Le texte à convertir en parole. Par défaut, "Ceci est juste un texte de test pour voir si ça marche."

    Renvoie:
        None
    """
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
    """
    Convertit un texte en parole en utilisant le moteur de synthèse vocale Pico2Wave.

    Args:
        langNum (int): Le numéro de la langue à utiliser. Par défaut, 1 correspond au français.
        text (str): Le texte à convertir en parole. Par défaut, il s'agit d'un texte de test en français.

    Renvoie:
        None
    """
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
    """
    Traduit le texte donné en français en utilisant la bibliothèque pyttsx3.

    Args:
        text (str): Le texte à traduire en français.

    Returns:
        None
    """

    import pyttsx3
    import platform

    if platform.system() == "Linux":
        engine = pyttsx3.init("espeak")
    else:
        engine = pyttsx3.init("sapi5")
    engine.say(text)
    engine.runAndWait()


def tts_gtts(text, langNum):
    """
    Convertit le texte donné en parole en utilisant la bibliothèque gTTS.

    Paramètres:
    texte (str): Le texte à convertir en parole.
    langNum (int): Le numéro de langue à utiliser pour la conversion en parole.

    Renvoie:
    None
    """
    from gtts import gTTS
    from audioplayer import AudioPlayer

    lang = ["fr", "en", "en", "de", "es", "it"]
    audio = gTTS(text=text, lang=lang[langNum - 1])
    audio.save("data/tts_result.wav")
    AudioPlayer("data/tts_result.wav").play(block=True)


def translate(text, langSource, langCible):
    """
    Traduit le texte donné de la langue source à la langue cible en utilisant Google Translator.

    Args:
        texte (str): Le texte à traduire.
        langSource (str): Le code de la langue source.
        langCible (str): Le code de la langue cible.

    Returns:
        str: Le texte traduit.
    """
    from deep_translator import GoogleTranslator

    traduit = GoogleTranslator(source=langSource, target=langCible).translate(text)
    with open("data/translation_result.txt", "w") as f:
        f.write(traduit)
    print(text, "-->", traduit)
    return traduit
