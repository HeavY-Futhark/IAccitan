from flask import Flask, render_template, request

app = Flask(__name__)


####################################################################################################### TRANSLATE FUNCTIONS


# Placeholder Translate functions
def translate_fr_occ(text):
    translated_text = "Hello World !"
    return translated_text


def translate_occ_fr(text):
    translated_text = "Goodbye World !"
    return translated_text


####################################################################################################### ROUTES
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate-fr-occ', methods=['POST'])
def translate_text():
    text = request.form['text']
    translated_text = translate_fr_occ(text)
    return translated_text


@app.route('/translate-occ-fr', methods=['POST'])
def translate_text_2():
    text = request.form['text']
    translated_text = translate_occ_fr(text)
    return translated_text


if __name__ == '__main__':
    app.run(debug=False)
