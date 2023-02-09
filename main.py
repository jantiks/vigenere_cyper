from cipherEngine import CipherEngine
import textwrap

def initalMenu() :
    return int(input("""
    This is the Vigenere cipher, pick one of the menu items
    1. encryption of text
    2. decryption with a key
    3. decryption without key
    4. quit
    """))

def getTheKey():
    return str(input("please specify the key: "))


if __name__ == "__main__":

    while True:
        selectedMenu = initalMenu()
        
        if selectedMenu == 1:
            textForEncription = input("Type the text for encryption: ")
            key = getTheKey()

            print(f"here is the encrypted text: ")
            print("-" * 70)
            print(CipherEngine().encrypt(textForEncription, key))
        elif selectedMenu == 2:
            cipherText = input("Type the text for decryption: ")
            key = getTheKey()
            print(print(f"here is the decrypted text from a key {key}:"))
            print("-" * 70)
            print({CipherEngine().decrypt(cipherText, key)})

        elif selectedMenu == 3:
            foundKey = False
            cipherText = input("Cipher text: ")
            print ("Solving Vigenere cipher:")
            print ("*" * 70)
            for key in CipherEngine().decryptWithoutKey(cipherText):
                print ("")
                print ("Found possible key: {!r}".format(key))
                print ("Possible Solution:")
                print ("=" * 70)
                print (textwrap.fill(CipherEngine().decrypt(cipherText, key)))
                print ("=" * 70)
                while True:
                    userInput = input("Continue searching? Enter (y/n): ")
                    if userInput == "n":
                        foundKey = True
                        break
                    elif userInput == "y":
                        break
                if foundKey:
                    break
        elif selectedMenu == 4:
            break
                    
        else:
            print("please select a number between 1 to 3")
