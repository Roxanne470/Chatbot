import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))

def english_to_french(engligh_text):

    output_dict = language_translator.translate(
        text = engligh_text,
        model_id='en-fr'
    ).get_result()

    return output_dict['translations'][0]['translation']

def french_to_english(french_text):

    output_dict = language_translator.translate(
        text = french_text,
        model_id='fr-en'
    ).get_result()

    return output_dict['translations'][0]['translation']

# print(english_to_french("Hello, how are you today?"))
# print(french_to_english("Bonjour, comment vous êtes aujourd'hui?"))

