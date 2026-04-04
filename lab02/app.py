from flask import Flask, render_template, request, json
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    PlayFair = PlayFairCipher()
    encrypted_text = PlayFair.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    PlayFair = PlayFairCipher()
    decrypted_text = PlayFair.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)