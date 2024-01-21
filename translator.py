

def translate(text, source, target):
    from deep_translator import GoogleTranslator
    translated = GoogleTranslator(source=source, target=target).translate(text)
    with open('data/translation_result.txt', 'w') as f:
            f.write(translated)
    print(text, '-->', translated)
    return translated

def translate_file(text_path, source, target):
    from deep_translator import GoogleTranslator
    with open(text_path, 'r') as f:
        text = f.read()
    translated = GoogleTranslator(source=source, target=target).translate(text)
    with open('data/translation_result.txt', 'w') as f:
            f.write(translated)
    print(text, '-->', translated)
    return translated

# translate("Bonjour", "fr", "en")
translate_file("data/stt_result.txt", "fr", "en")