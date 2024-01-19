#Magic 8 Ball
#1-19-24
#Clementine Yi

#Initialize
import random
Responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook no so good", "Very doubtful"]


#Functions
def MagicEightBall():
    while True:
        question = input("Please ask a question here: ")
        if question.endswith("?"):
            print(random.choice(Responses))
            newInput = input("Would you like to ask another question?")
            if newInput == ("yes" or "y"):
                True
            if newInput == ("no" or "n"):
                print("Thank you for using Magic 8 Ball :)")
                break
        else:
            print("Invalid question, ask again with a question mark. ")



#Main
MagicEightBall()
