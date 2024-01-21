
def speech_to_text_pyttsx3():
    import pyttsx3
    import platform
    if platform.system() == "Linux":
        engine = pyttsx3.init('espeak')
    else:
        engine = pyttsx3.init('sapi5')
    engine.say("Ceci est juste un texte de test pour voir si ça marche.")
    engine.runAndWait()
    
def speech_to_text_pyttsx3_fr():
    import pyttsx3
    import platform
    if platform.system() == "Linux":
        engine = pyttsx3.init('espeak')
    else:
        engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'fr_FR' in voice.languages or 'fr-CA' in voice.languages:
            engine.setProperty('voice', voice.id)
        else:
            print('No french voice found')
    engine.say("Ceci est juste un texte de test pour voir si ça marche.")
    engine.runAndWait()

def speech_to_text_gtts():
    from gtts import gTTS
    from audioplayer import AudioPlayer
    audio = gTTS(text='Ceci est juste un texte de test pour voir si ça marche.', lang='fr')
    audio.save("good.mp3")
    AudioPlayer("good.mp3").play(block=True)
    
def speech_to_text_pico2wave(language=0, text="Ceci est juste un texte de test pour voir si ça marche."):
    import os
    lang = ["fr-FR", "en-US", "en-GB", "de-DE", "es-ES", "it-IT"]
    a=os.system("pico2wave --lang=" + lang[language] + """ --wave=data/tts_result.wav " """ + str(text) + """ " && play data/tts_result.wav""")
    
def speech_to_text_espeak(language=0, text="Ceci est juste un texte de test pour voir si ça marche."):
    import os
    a=os.system("""espeak -a 200 -w data/tts_result.wav " """ + str(text) + """ " && play data/tts_result.wav""")
    
speech_to_text_gtts()
# speech_to_text_pyttsx3_fr()