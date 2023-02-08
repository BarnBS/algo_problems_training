input = open("J3/input","r")
read_input = input.readlines()

# Part 1

item_types = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum_final = 0

for rucksack in read_input :

    rucksack_length = int(len(rucksack)-1)
    half_rucksack_length = int(rucksack_length/2)

    for i in range(0, half_rucksack_length) :
        for j in range(half_rucksack_length, rucksack_length) :
            if (rucksack[i] == rucksack[j]) :
                priority = item_types.index(rucksack[i])+1
    sum_final += priority

print(sum_final)

#Part 2
# POINTS DE VIGILANCE :
    # Boucle for : attention à ne pas être out of range d'où la length -2
    # Pas de l'itération à 3 DANS LE FOR et non pas i+=3 !!!

sum_final = 0

for i in range (0,len(read_input)-2,3) :

        rucksack1 = read_input[i]
        rucksack2 = read_input[i+1]
        rucksack3 = read_input[i+2]

        for j in range(0, int(len(rucksack1))-1) :
            for k in range(0, int(len(rucksack2))-1) :
                for l in range(0, int(len(rucksack3))-1) :
                    if (rucksack1[j] == rucksack2[k] == rucksack3[l]) :
                        priority = item_types.index(rucksack1[j])+1
        sum_final += priority

print(sum_final)