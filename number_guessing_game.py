import random
randnumber=random.randint(1,100)
userguess=None
guesses=0
d=None
s=None

print("HELLO and WELCOME TO THE GAME ")
#print("\n")
print("     Special Multiplications.")
print("\n")
print("Hope U'll Enjoy the game.")
#print("\n")
print("Lets Go ")

while(userguess!=randnumber):
    userguess=int(input("Enter your Guess. \n"))
    guesses+=1
    d=int(userguess-randnumber)
    s=int(randnumber-userguess)
    if(userguess==randnumber):
        print("You Guessed it Right!!")
        print("The Multiplication Table of the Number you have guessed is as follows ")
        for i in range(1,11):
            print(str(randnumber)+"X"+str(i)+"="+str(i*randnumber))
    elif(userguess-randnumber>0 and userguess-randnumber==d):
        print("The Difference between the numbers is ")
        print(d)
        print("You have Entered a a Larger Number.")
        print("Enter a Smaller Number.")
        print("The Multiplication Table Of the difference is as follows : \n")
        for i in range(1,11):
            print(str(d)+"X"+str(i)+"="+str(i*d))
    elif(randnumber-userguess>0 and randnumber-userguess==s):
        print("The Difference between the numbers is ")
        print(s)
        print("You have Entered a a Smaller Number.")
        print("Enter a Larger Number.")
        print("The Multiplication Table Of the difference is as follows : \n")
        for i in range(1,11):
            print(str(s)+"X"+str(i)+"="+str(i*s))
    else:
        print("The Number is out of Range.")

print(f"You have Guessed it in {guesses} guesses. ")
print("Hope U Might have enjoyed!!")
print("Thank You for Playing.")
