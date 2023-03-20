# Copier le code à :
# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=99&reg_typ_id=2&que_str_id=&cli_id=45alrk6jpdnaguf3oa3gto2875&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D33

#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
ingredients_list = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
del lines[0]

for line in lines :
    words = line.split()
    for word in words :
        if not word in ingredients_list :
            ingredients_list.append(word)
            
sys.stderr.write(str(ingredients_list))

print(len(ingredients_list))
