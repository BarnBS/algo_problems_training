#copier/coller le code à :
# https://demo.isograd.com/runtest/QuestionDisplayer

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = lines[0]
del lines[0]

sys.stderr.write("\n"+str(lines))

counter_case = 0
plateforms_list = []

for case in lines:
    if case == "B" :
        counter_case += 1
        if case == lines[len(lines)-1]:
            plateforms_list.append(counter_case)
    elif case =="X" :
        if counter_case != 0:
            plateforms_list.append(counter_case)
        else :
            continue
        counter_case = 0

sys.stderr.write("\n LISTE DE COUNTERS :"+ str(plateforms_list))

print(max(plateforms_list)-1)