# Copier le code au problème "Prehistoire" du lien suivant :
# https://www.isograd-testingservices.com//FR/solutions-challenges-de-code?cts_id=80

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

del lines[0]

ligneCentrale = lines[int(len(lines)/2)]
caractereCentral = ligneCentrale[int(len(ligneCentrale)/2)]

print(caractereCentral)
