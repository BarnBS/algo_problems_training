input = open("J2/input2","r")
read_input = input.readlines()

#Part 1

#A ROCK X       +1 points
#B PAPER Y      +2 points
#C SCISSORS Z   +3 points

WIN = 6
DRAW = 3
LOSS = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

score = 0

for round in read_input :
    #Win Draw or Loss point count
    if (round[0] == "A" and round[2] == "Y") or (round[0] == "B" and round[2] == "Z") or (round[0] == "C" and round[2] == "X") :
        score += WIN
    elif (round[0] == "A" and round[2] == "X") or (round[0] == "B" and round[2] == "Y") or (round[0] == "C" and round[2] == "Z") :
        score += DRAW
    elif (round[0] == "A" and round[2] == "Z") or (round[0] == "B" and round[2] == "X") or (round[0] == "C" and round[2] == "Y") :
        score += LOSS
    #Shape point count
    if (round[2] == "X"):
        score += ROCK
    elif (round[2] == "Y"):
        score += PAPER
    elif (round[2] == "Z"):
        score += SCISSORS

print(score)


#Part 2

# A ROCK        +1 points
# B PAPER       +2 points
# C SCISSORS    +3 points

# X LOSS        +0 points
# Y DRAW        +3 points
# Z WIN         +6 points

score = 0

for round in read_input :
    #If LOSS
    if ((round.find("A X")!=-1) or (round.find("B X")!=-1) or (round.find("C X")!=-1)):
        if round[0] == "A" :
            score += SCISSORS
        elif round[0] == "B" :
            score += ROCK
        elif round[0] == "C":
            score += PAPER
    #Else If DRAW
    elif ((round.find("A Y")!=-1) or (round.find("B Y")!=-1) or (round.find("C Y")!=-1)):
        score += DRAW
        if round[0] == "A" :
            score += ROCK
        elif round[0] == "B" :
            score += PAPER
        elif round[0] == "C":
            score += SCISSORS
    #Else If WIN
    elif ((round.find("A Z")!=-1) or (round.find("B Z")!=-1) or (round.find("C Z")!=-1)):
        score += WIN
        if round[0] == "A" :
            score += PAPER
        elif round[0] == "B" :
            score += SCISSORS
        elif round[0] == "C":
            score += ROCK

print(score)