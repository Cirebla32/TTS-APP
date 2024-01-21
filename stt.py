import speech_recognition as sr
#Initialiser la classe Recognizer (pour reconnaître la parole)
r = sr.Recognizer()
# Lecture du fichier audio comme source
# écouter le fichier audio et le stocker dans la variable audio_text
with sr.AudioFile('audio.wav') as source:
    audio_text = r.listen(source)
# recoginize_() La méthode générera une erreur de requête si l'API est inaccessible, utilisant donc la gestion des exceptions
    try:
        # utilisation de google speech recognition
        text = r.recognize_google(audio_text, language = 'fr-FR')
        with open('data/stt_result.txt', 'w') as f:
            f.write(text)
        print('Convertion de l\'audio en texte ...')
        print(text)
        
    except:
         print('Sorry.. run again...')