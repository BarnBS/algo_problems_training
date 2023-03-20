# copier le code à :
# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=57&reg_typ_id=2&que_str_id=&cli_id=45alrk6jpdnaguf3oa3gto2875&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D55

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
n = int(lines[0])
N = int(lines[1])

del lines[0]
del lines[0]

classement_général = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

sys.stderr.write("PILOTE FAV ID :"+ str(n))
#print(N)
sys.stderr.write("\n NEW TEST")
sys.stderr.write(str(lines))
    
if (n>20 or n<1) or (N>100 or N<1):
    raise ValueError("Input n must be between 1 and 20 and N between 1 and 100")
    
else :
    
    for line in lines :
        id_pilote = int(line[0]+line[1])
        #sys.stderr.write("idPi : ", id_pilote)

        classement_pilote = classement_général.index(id_pilote)
        #sys.stderr.write("index Pi : ", classement_pilote)
        classement_pilote_depasse = classement_général.index(id_pilote)-1
        #sys.stderr.write("index Pi dépassé : ", classement_pilote_depasse)
        
        if line.find("I") != -1 and id_pilote == n :
            print("KO")
            
        else :
            if line.find("D") != -1 :
                classement_général[classement_pilote_depasse],classement_général[classement_pilote] = classement_général[classement_pilote], classement_général[classement_pilote_depasse]
                
            elif line.find("I") != -1 :
                del classement_général[classement_pilote]

        sys.stderr.write("\n Classement actuel")
        sys.stderr.write(str(classement_général))
        
    classement_fav = classement_général.index(n) + 1
    print (classement_fav)
