"""This module Leverages IBM traslator to ctralate langaure"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-01-27',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    """This convert text from french to english"""
    if len(english_text.strip()) == 0:
        french_text = ""
    else:
        french_text_dict = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text = french_text_dict["translations"][0]["translation"]
    return french_text

def frenchToEnglish(french_text):
    """This convert text from english to french"""
    if len(french_text.strip()) == 0:
        english_text = ""
    else:
        ebglish_text_dict = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text = ebglish_text_dict["translations"][0]["translation"]
    return english_text

