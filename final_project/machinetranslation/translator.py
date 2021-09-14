"""
Create instance of IBM translator
Define english to french and french to english translation functions
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# create an instance of the IBM Watson Language translator
# Dan Jordan
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')


# Add function english_to_french
# Dan Jordan
def english_to_french(english_text):
    """ translate english to french """
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
    except ValueError:
        french_text='text must be provided'
    else:
        print(json.dumps(translation, indent=2, ensure_ascii=False))
        french_text=translation['translations'][0]['translation']
    return french_text

# Add function french_to_english
# Dan Jordan
def french_to_english(french_text):
    """ translate french to english """
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
    except ValueError:
        english_text='text must be provided'
    else:
        print(json.dumps(translation, indent=2, ensure_ascii=False))
        english_text=translation['translations'][0]['translation']
    return english_text
