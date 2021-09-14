import machinetranslation # DJ add
# DJ comment out
#from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_french = machinetranslation.translator.english_to_french(textToTranslate) # DJ add
    #return "Translated text to French" # DJ comment out
    return "Translated text to French: "+translated_french # DJ add

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_english = machinetranslation.translator.french_to_english(textToTranslate) # DJ add
    #return "Translated text to English"  # DJ comment out
    return "Translated text to English: "+translated_english  # DJ add

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html') # DJ add

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
