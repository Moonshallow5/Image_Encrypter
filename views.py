"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
import random
from flask import Flask, flash, request, redirect, url_for
from flask import send_from_directory
from flask import send_file

app=Flask(__name__)
def encrypt(file):
    fo = open(file, "rb")
    image=fo.read()
    fo.close()
    image=bytearray(image)
    key=random.randint(0,256)
    for index,value in enumerate(image):
        # changes the bytearray of the image, hence, it encrypts it
        image[index]=value^key  
    fo=open("enc.jpg","wb")
    imageRes="enc.jpg"
    # makes a new image called enc.jpg which is now encrypted
    fo.write(image)
    fo.close()
    return (key,imageRes)

    
    
def decrypt(key,file):
    fo = open(file, "rb")
    image=fo.read()
    fo.close()
    image=bytearray(image)
    for index,value in enumerate(image):
        image[index]=value^key
    fo=open("dec.jpg","wb")
    imageRes="dec.jpg"
    fo.write(image)
    fo.close()
    return imageRes



@app.route('/')
def home():
    # This tab is just the homepae of the app
    return render_template(
        'index.html',
        title='Home Page',
    )

@app.route('/decryption')
def decryption():
    #This tab is for decrypting the image (comes in second)
    return render_template(
        'de.html',
        title='Decrypt',
        message='Please upload your encrypted image along with the key'
    )

@app.route('/encryption')
def encryption():
    # This tab is for encrypting the image (comes in first)
    return render_template(
        'en.html',
        title='Encrypt',
        message='Upload the image here'
    )

@app.route('/decryption1', methods = ['POST'])  
def decryption1():  
    if request.method == 'POST':  
        global f
        f = request.files['file']  # Requests for the encrypted file and the key
        f.save(f.filename)  
        text = request.form['key']
        key=int(text)
        image=decrypt(key,f.filename)
        return render_template('de1.html',
        title='Decrypted',
        message='This is your Decrypted image', name = 'dec.jpg') 

@app.route('/encryption1', methods = ['POST'])  
def encryption1():  
    if request.method == 'POST':  
        global f
        f = request.files['file']  
        f.save(f.filename)  
        key,image=encrypt(f.filename) # Requests for a normal image file, encrypts it and provides the key
        return render_template('en1.html',
        title='Encrypted',
        message='This is your encrypted image', name = f.filename,keys=key,images=image)

@app.route('/return-file')
def return_file():
    return send_file("../enc.jpg",attachment_filename="enc.jpg") # Encrypted file

@app.route('/return-file1')
def return_file1():
    return send_file("../dec.jpg",attachment_filename="dec.jpg") # Decrypted file

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
