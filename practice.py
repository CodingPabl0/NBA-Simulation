import time
import os
from random import randint, random, sample
import random
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

Players={"Lebron James" : 95, "Kevin Durant" : 97,"Kahwi Leonard": 94,
"Paul George" : 85, "Russel Westbrook" : 90, "Kyrie Irving": 92,
"James Harden" : 96, "Wardell Stephen Curry" : 88, "Blake Griffin" : 78,
"Anthony Cruz" : 100, "Bradely Beal": 86,"CJ McCollum" : 88}




print("Hello, welcome to my NBA Simulation Game")
time.sleep(2)
print("Here are a list of players to choose from")
time.sleep(3)
# give me a list of players in dictonary
newlist=[]
for key in Players.keys():
    newlist.append(key)
newlist
for i in newlist:
    print(i)
time.sleep(5)

cls()

time.sleep(2)
print("The computer is going to choose first")
newlist
sampling = random.sample(newlist, k=5)
print("Here are the following players!\n", sampling)

time.sleep(3)
cls()
for i in newlist:
    print(i)
YourTeam = []
p=0
for i in range(0, 5):
    p+=1
    pyl = (input("Choose player {}: ".format(p)))
    YourTeam.append(pyl)
YourTeam
print("You chose well!", YourTeam)
print("Now that both teams are set, we will run the simulation to see who won \n Are you ready?? :)")
time.sleep(3)




User=YourTeam
PC=sampling
PcScore=0
YourScore=0

for epy in Players:
    for e in PC:
        if e==epy:
            PcScore+=Players[epy]
        else:
            continue
for epy in Players:
    for e in User:
        if e==epy:
            YourScore+=Players[epy]
        else:
            continue
print("The PC's score is ", PcScore)
print("This is your score ", YourScore)
time.sleep(3)

def FinalScore(q,t):
    if q>t:
        print("Sorry, you lose")
    elif q<t:
        print("You win! Congrats buddy")
    else:
        print("It's a tie -_-")

print(FinalScore(PcScore, YourScore))

time.sleep(6)
