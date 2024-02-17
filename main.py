from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()

    text = data.get('text')
    source_lang = data.get('source', 'auto')  
    target_lang = data.get('target', 'en')  
    if not text:
        return jsonify({"error": "No text provided"}), 400

    words = text.split()
    translated_words = []

    for word in words:

        try:
            translated_word = GoogleTranslator(source=source_lang, target=target_lang).translate(word)
        except Exception as e:
            translated_word = f"[Error: {str(e)}]"

        translated_words.append(translated_word)

    translated_sentence = ' '.join(translated_words)
    return jsonify({"translated_sentence": translated_sentence})

if __name__ == '__main__':
    app.run(debug=True)
