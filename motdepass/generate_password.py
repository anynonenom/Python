
# store every possible characters into the list :
import random
def generaetePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []
    for i in pwlength :
        password = ""
        for j in range(i):
            nex_letter_index= random.randrange(len(alphabet))
            password = password + alphabet[nex_letter_index]
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        passwords.append(password)
    return passwords
def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword
def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword
def main():
    numPasswords = int(input("How many passwords do you want to generate : "))
    print("Generating"+str(numPasswords)+"passwords")
    passwordlenght = []
    print("Minimum lenght of passwords should be 3 ")
    for i in range(numPasswords):
        lenght = int(input("Enter the lenght of passwords : "))
        if lenght < 3:
            lenght = 3 
        passwordlenght.append(lenght)
    Password = generaetePassword(passwordlenght)
    for i in range(numPasswords):
        print("Passwordd # "+str((i+1))+"="+Password[i])
main()
