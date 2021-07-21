alphabets = "abcdefghijklmnopqrstuvwxyz"
sc = "_}{"

def encryption():
    text = input("Enter the text/message : ")
    print("\n")
    shift = int(input("Enter Shift/Encryption key : "))
    print("\n")

    if (shift <= 26 and shift >= 0):
        pass

    else:
        print("[ERROR : INVALID SHIFT KEY(must between 0 and 26]")
        encryption()
        print("\n")

    encrypt = alphabets[int(shift):27] + alphabets[0:int(shift)] + sc[0:3]

    dictionary = dict(zip((alphabets + sc), encrypt))

    code = ''.join([dictionary[alphabets] for alphabets in text])

    encrypted_code = print(f"Encrypted code : {code}")

    return encrypted_code
    
def decryption():
    text = input("Enter the Code : ")
    print("\n")
    shift = int(input("Enter Shift/Decryption key : "))
    print("\n")

    if (shift <= 26 and shift >= 0):
        pass

    else:
        print("[ERROR : INVALID SHIFT KEY(must between 0 and 26]")
        encryption()
        print("\n")

    decrypt = alphabets[int(shift):27] + alphabets[0:int(shift)] + sc[0:3]

    dictionary = dict(zip(decrypt ,alphabets + sc))

    msg = ''.join([dictionary[alphabets] for alphabets in text])

    decrypted_code = print(f"Decrypted code : {msg}")

    return decrypted_code

def mass_decryption():
    text = input("Enter the text/message : ")
    print("\n")
    shift = 0

    while (shift < 27):

        decrypt = alphabets[int(shift):27] + alphabets[0:int(shift)] + sc[0:3]

        dictionary = dict(zip(decrypt, alphabets + sc))

        code = ''.join([dictionary[alphabets] for alphabets in text])

        print(f"Shift {shift} : {code}")
        print("\n")

        shift = shift + 1


print("Please choose the task to perform -")
print("\n")
print("[1] Encrypting")
print("[2] Decrypting")
print("[3] Mass Decrypting")
print("\n")

mode = input(" >  ")
print("\n")

if (mode == "1"):
    encryption()

elif (mode == "2"):
    decryption()

elif (mode == "3"):
    mass_decryption()

else :
    print("Wrong choice")
    exit()