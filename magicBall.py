import random 

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "IT is Certain"
    elif answerNumber  == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask agin"
    elif answerNumber == 7:
        return "Outlook no so good"
    elif answerNumber == 8:
        return "Outlook so good"
    elif answerNumber ==9:
        return "very doubtfull"

#r = random.randint(1, 9)
#fortune = getAnswer(r)
#print(fortune)
print(getAnswer(random.randint(1, 9)))       
