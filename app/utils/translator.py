from googletrans import Translator


def translate_to_english(text: str) -> str:
    '''
        Function to translate obtained text into english to make request to API

    :param text: Text to be translated
    :return: Translated to eng text
    '''

    translator = Translator()
    try:
        return translator.translate(text, dest='en').text
    except Exception as e:
        print(f'Fail! {e}')
        return ''