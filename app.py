from flask import Flask, request, jsonify
import hashlib
import requests

app = Flask(__name__)

@app.route('/verify_payment', methods=['POST'])
def verify_payment():
    key = request.form.get('key')
    txnid = request.form.get('txnid')
    salt = request.form.get('salt')

    data = f"{key}|verify_payment|{txnid}|{salt}"
    hash = hashlib.sha512(data.encode()).hexdigest()

    url = "https://test.payu.in/merchant/postservice?form=2"
    payload = f"key={key}&command=verify_payment&var1={txnid}&hash={hash}"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    return jsonify(response.text)

if __name__ == '__main__':
    app.run(debug=True)
