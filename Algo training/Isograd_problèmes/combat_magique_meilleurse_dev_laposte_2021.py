# Copy/paste at :
# https://www.isograd-testingservices.com//FR/solutions-challenges-de-code?cts_id=80#

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
motMagique = lines[0]
#sys.stderr.write("\n"+"------------------------"+ "\n"+"Mot Magique : " + str(motMagique) + "\n")
del lines[0]

incantation_finale = []
for line in lines :
    incantation = line.split()
    #sys.stderr.write("Incantation : " + str(incantation) + "\n")
    for word in incantation :
        #sys.stderr.write("Word : " + str(word) + "\n")
        if motMagique in word :
            incantation_finale.append(word)
        else :
            word = ''.join(reversed(word))
            incantation_finale.append(word)
    incantation_finale = ' '.join(incantation_finale)
print(incantation_finale)
