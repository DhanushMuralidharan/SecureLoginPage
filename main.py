from flask import Flask,render_template,request,redirect,url_for
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import base64
import hashlib
import os

def generate_salt():
    # Generate a random salt (you can customize the length)
    return os.urandom(16)

def hash_password(password, salt):
    # Combine password and salt, and then hash using SHA-256
    combined = password.encode('utf-8') + salt
    hashed_password = hashlib.sha256(combined).hexdigest()
    return hashed_password

def verify_password(entered_password, stored_salt, stored_hashed_password):
    # Combine entered password and stored salt
    combined = entered_password.encode('utf-8') + stored_salt
    # Hash the combined value using SHA-256
    hashed_password_attempt = hashlib.sha256(combined).hexdigest()
    # Compare the hashed password attempt with the stored hashed password
    return hashed_password_attempt == stored_hashed_password

app = Flask(__name__)
keys = None


# password : YouBetterEncryptThis
user_credentials = {'administrator':{'password':'b70b565d8dc72c700acf94f908215301bee2f25c42ea012178c934a4b30b37a1','salt':b'\x8e\xbf\xaa%\x80\x95\xa23\xadH\xc7\xfc\xbbl:\xec'}}

@app.route('/',methods=['GET','POST'])
def index():
    global keys

    if request.method == 'GET':
        keys = RSA.generate(1024)
        return render_template("index.html",key = keys.public_key().exportKey().decode().replace('\n','\\n'))
    
    elif request.method == 'POST':
        if keys is None:
            return redirect(url_for('index'))
        username = request.form.get('username')
        password = request.form.get('password')
        decryptor = PKCS1_v1_5.new(keys)
        sentinel = Random.new().read(128)
        if username not in user_credentials.keys():
            return "User Not Found!"
        else:
            if verify_password(decryptor.decrypt(base64.b64decode(password),sentinel).decode(),user_credentials[username]['salt'],user_credentials[username]['password']):
                return "Successfully Authenticated!"
            else:
                return "Incorrect Password!"

if __name__ == '__main__':
    app.run(debug=True)