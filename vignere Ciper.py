import string
main=string.ascii_lowercase
while True:
    print("Enter 1 For Encryption")
    print ("Enter 2 for Decryption")
    print ("Enter 3 For Exit")
    Choice =int(input("Enter Your Choice:"))
    if Choice ==1:
        def encryption(plain_text,key):
            index=0
            cipher_text=""
            plain_text=plain_text.lower()
            key=key.lower()
            for c in plain_text:
                if c in main:
                    off=ord(key[index])-ord('a')
                    encrypt_num=(ord(c)-ord('a')+off)%26
                    encrypt=chr(encrypt_num+ord('a'))
                    cipher_text+=encrypt
                    index=(index+1)%len(key)
                else:
                    cipher_text+=c

            print("plain text: ",plain_text)
            print("cipher text: ",cipher_text)
            plain_text=input("Enter the message to be decrypted: ")
            key=input("Enter the key for decryption: ")
    elif Choice ==2:
        plain_text=input("Enter the message: ")
        key=input("Enter the key: ")
        encryption(plain_text,key)

        def decryption(cipher_text,key):
            index=0
            plain_text=""
            cipher_text=cipher_text.lower()
            key=key.lower()
            
            for c in cipher_text:
                if c in main:
                    off=ord(key[index])-ord('a')
                    positive_off=26-off
                    decrypt=chr((ord(c)-ord('a')+positive_off)%26+ord('a'))
                    plain_text+=decrypt
                    index=(index+1)%len(key)
                else:
                    plain_text+=c

            print("cipher text: ",cipher_text)
            print("plain text (message): ",plain_text)
            cipher_text=input("Enter the message to be decrypted: ")
            key=input("Enter the key for decryption: ")
            decryption(cipher_text,key)
    elif Choice ==3:
        break
    else:
        print("Enter Valid Command")
