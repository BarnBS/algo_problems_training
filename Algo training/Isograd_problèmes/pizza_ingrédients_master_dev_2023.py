# Copier le code à :
# https://demo.isograd.com/runtest/QuestionDisplayer#output

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