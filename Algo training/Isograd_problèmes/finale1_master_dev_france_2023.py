# Copy/paste at finale1 :
# https://www.isograd-testingservices.com//FR/solutions-challenges-de-code?cts_id=104

#* Use sys.stderr.write() to display debugging information to STDERR
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
nombreSoumissions = lines[0]
del lines[0]

def getListOfSubmissions() :
    soumissionsList = []
    for line in lines :
        soumissionsList.append(line.split())
    return soumissionsList
    
# get a dictionnary of every submissions + the number of times the corresponding hash was used
def getDictOfSubmissionsHashCounter () :
    soumissionsList = getListOfSubmissions()
    counterDictionnary = {}
    for soumission in soumissionsList :
        if soumission[1] in counterDictionnary :
            counterDictionnary[soumission[1]] += 1
        else :
            counterDictionnary[soumission[1]] = 1
    return counterDictionnary
        
def getListOfWinningSubmissions () :
    soumissionsList = getListOfSubmissions()
    counterDictionnary = getDictOfSubmissionsHashCounter()
    winningSubmissions = []
    for soumission in soumissionsList :
        if counterDictionnary[soumission[1]] > 1 :
            continue
        else :
            winningSubmissions.append(int(soumission[0])) # str to int so that the sorting function works correctly
    return winningSubmissions

# This function convert the winningSubs from int to str to print correctly
def intToStrResult() : 
    winningSubmissions = getListOfWinningSubmissions()
    winningSubmissions.sort()
    result = []
    for sub in winningSubmissions :
        sub = str(sub)
        result.append(sub)
    return result

print(str(("\n").join(intToStrResult())))
