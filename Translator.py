#Make sure path exists
from googletrans import Translator
import os
import re

#Importing Translator
translator = Translator()

#Make sure path exists
path = input("Folder path w/ untranslated file titles: ").replace("\\","")
destLang = input("Language you want to translate to (use the https://en.wikipedia.org/wiki/ISO_639-1 codes):")

print(path)

#Gives out an each folder as an object
for dirpath, dirnames, files in os.walk(path, topdown=False):
    print ("Searching Folder")
    #Go through each file
    for file_name in files:

        #Only get the name part to be translated
        print("Processing Files")
        name = os.path.splitext(file_name)[0]
        originLang = translator.detect(name).lang
        print(translator.detect(name))
        print(name)

        #Only translate if it's japanese
        if originLang != destLang:
            print(f"Processing Translation from {originLang} to {destLang}")

            #The actual translation
            translatedName = translator.translate(name, src=originLang, dest=destLang).text

            #Removing forbidden file elements
            pattern = '\?|>|<|/|:|"|(\\\\)|\*'
            repl = ''
            fixedName = re.sub(pattern, repl, translatedName) + os.path.splitext(file_name)[1]

            #Changing the name
            os.rename(f"{dirpath}/{file_name}",f"{dirpath}/{fixedName}")

            #Confirmation Prints
            print(f'In {dirpath} translated to {fixedName}')
            
    for dir_names in dirnames:
        print ("Processing Folder")
        name = os.path.splitext(dir_names)[0]
        originLang = translator.detect(name).lang
        print(translator.detect(name))
        print(name)
        if originLang != destLang:
            print(f"Processing Translation from {originLang} to {destLang}")
            translatedName = translator.translate(name, src=originLang, dest=destLang).text
            pattern = '\?|>|<|/|:|"|(\\\\)|\*'
            repl = ''
            fixedName = re.sub(pattern, repl, translatedName) + os.path.splitext(dir_names)[1]
            os.rename(f"{dirpath}/{dir_names}",f"{dirpath}/{fixedName}")
            print(f'In {dirpath} translated to {fixedName}')
