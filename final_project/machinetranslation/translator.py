"""
Creates a Language Translator Service between French and English.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

#Instance of dotenv:
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Instance of IBM watson language-translator API:
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-07-18',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#Enable SSL verification:
#language_translator.set_disable_ssl_verification(False)

#Perform language translations:
def english_to_french(english_text):
    """
    Receives a text in English and returns its French translation.
    """
    if len(english_text) != 0:
        lang_dict = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        word_list = lang_dict['translations']
        word_dict = word_list[0]
        french_text = word_dict['translation']
    else:
        french_text = None
    return french_text


def french_to_english(french_text):
    """
    Receives a text in French and returns its English translation.
    """
    if len(french_text) != 0:
        lang_dict = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        word_list = lang_dict['translations']
        word_dict = word_list[0]
        english_text = word_dict['translation']
    else:
        english_text = None
    return english_text
