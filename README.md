# Image_Encrypter

## 💡Inspiration
14 bilion images are shared online on social media on any given day, and some of them might need some encryption. Thus, with my  image_encrypter rest assured, you can safely transfer images from one place to the next with an ecryption key

## 💭How does it work?

If you have an image you want to encrypt before sending it go the Encrypt tab on my Flask website. This would use a very simpel pixel manpulation algorithm to encrypt and decrypt the images.

First go to the **Encryption tab**, and upload an image to be encrypted and then go to the **Decryption tab** and upload the encrypted image along with the key to decrypt the image.




https://github.com/user-attachments/assets/10cc584a-4c81-4658-bcef-1cf73379e4f7

## 🚧Challenges I ran into

The algorithm itself to encrypt and decrypt the image isn't a very hard algo to implement as I'm using a very simple pixel-based manipulation. However, I focused more on the front-end part of this design, as I had to integret bootstrap.css with Flask to make a fully-functional website to encrypt and decrypt images for ease of use. Thus, the main challenges was utiling bootstrap.css and learning the documentation of Flask 

To run the project:

```docker pull moonshallow5/image_encrypter```



```docker run -d -p 5000:5000 -v /path/to/your/local/:/app/ moonshallow5/image_encrypter```

where  ```/path/to/your/local/``` is the path where you want the images to be saved in your computer 

For example my ```/path/to/your/local/``` 
is</br></br>
 ```C:/Users/Sandeep/OneDrive/Desktop/UNI-IMPORTANT-WORK/Image_Encrypter/```

Then go to ```http://localhost:5000/``` to see my project :)


Don't forget to ⭐ the repo if it helped you :)



