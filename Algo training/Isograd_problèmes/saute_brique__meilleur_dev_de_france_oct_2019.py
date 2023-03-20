#copier/coller le code à :
# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=54&reg_typ_id=2&que_str_id=&cli_id=45alrk6jpdnaguf3oa3gto2875&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D99

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
