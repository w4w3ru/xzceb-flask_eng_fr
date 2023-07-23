from machinetranslation import translator
from flask import Flask, render_template, request
import json
import os

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text

@app.route("/")
def renderIndexPage():
    template_path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
    return render_template(template_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
