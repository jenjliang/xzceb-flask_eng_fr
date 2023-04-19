"""
Watson Language Translator service
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


# code to create an instance of IBM Language translator
authenticator = IAMAuthenticator(apikey)
app = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator,
    service_name=url
)

app.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')


def englishToFrench(english_text):
    """
    translates text from English to French
    """
    translation = app.translate(
        text = english_text,
        model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """
    translates text from French to English
    """
    translation = app.translate(
        text = french_text,
        model_id = 'fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
