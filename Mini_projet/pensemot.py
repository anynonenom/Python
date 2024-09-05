import random
# library that we use in order to choose
# on random words from a list of words 
name = input("Guess a name : ")
print("Good Luck !" , name ) 

aleatoire_nome = ['rainbow' , 'computer'  , 'science','programming' , 'python' , 'mathematics']

# function will choose one random
# word from this list of words 
word = random.choice(aleatoire_nome)

print("Guess the charachters ")
guesse = '' 

turns = 12 

while turns > 0 :
    failed = 0 
    for char in word  :
     if char  in guesse :
        print(char , end=" ") 
     else :
        print("_")
        failed +=1 
    if failed == 0 :
       print("You Win :) ")
       print("The word is : " , word ) 
       break
    guess = input("guess a charachter : ")
    guesse+=guess

    # checks input with the charachter will be stored in guesse 
    if guess not in word :
       turns -=1 
       print("Wrong")

       print("You have " , +turns  , 'more guesses')
       if turns == 0 :
          print("You loose :( ")
