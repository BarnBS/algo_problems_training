#CODE A COLER DANS : https://demo.isograd.com/runtest/QuestionDisplayer#output

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

sys.stderr.write("\n NEW TEST" + str(lines))

voters_number = lines[0]
del lines[0]

voted_colors = lines


colors_classement = {}
def classement_des_couleurs():
    
    for color in voted_colors :
        if (color in colors_classement) :
            colors_classement[color] += 1
        else:
            colors_classement[color] = 1
            
    sys.stderr.write("\n CLASSEMENT" + str(colors_classement))
    return colors_classement



def max_search() :
    
    maxi_colors = ["",""]
    maxi = [None,None]
    
    for color in colors_classement:
        if maxi[0] is None :
            maxi[0] = colors_classement[color]
            maxi_colors[0] = color
            continue
        if maxi[1] is None :
            maxi[1] = colors_classement[color]
            maxi_colors[1] = color
            continue
        if colors_classement[color] > maxi[0]:
            if maxi[0] > maxi[1]:
                maxi[1] = maxi[0]
                maxi_colors[1] = maxi_colors[0]
            maxi[0] = colors_classement[color]
            maxi_colors[0] = color
        elif colors_classement[color] > maxi[1]:
            maxi[1] = colors_classement[color]
            maxi_colors[1] = color
    sys.stderr.write("\n MAXI_ARRAY : " + str(maxi_colors))
    print(maxi_colors[0] + " " + maxi_colors[1])
    sys.stderr.write("\n MAXI : " + maxi_colors[0] + " " + maxi_colors[1])



classement_des_couleurs()
max_search()