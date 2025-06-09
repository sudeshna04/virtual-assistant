import asyncio
from googletrans import Translator

async def translate_text(text, target_language):
    translator = Translator()
    translated = await translator.translate(text, dest=target_language)
    return translated.text

async def translation():
    try:
        text_to_translate = input("What would you like to translate? ").lower()
        target_language = input("To which language? ").lower()
        print("Target language:", target_language)
        translated_text = await translate_text(text_to_translate, target_language)
        print("Translated text:", translated_text)
    except Exception as e:
        print("Sorry, I couldn't understand what you said.")
        print("Error:", e)

# Run the async function
asyncio.run(translation())
