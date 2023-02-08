input = open("J1/input1","r")
read_input = input.readlines()

#Part 1

count_cal = 0
max_cal = 0

for cal in read_input:
    if cal != "\n":
        count_cal += int(cal)
    else :  
        if count_cal > max_cal :
            max_cal = count_cal
        count_cal = 0
            
print(max_cal)

#Part 2

count_cal = 0
cal_list = []

for cal in read_input:
    if cal != "\n":
        count_cal += int(cal)
    else :
        cal_list.append(count_cal)
        count_cal = 0
cal_list.sort(reverse=True)
            
print(cal_list[0] + cal_list[1] + cal_list[2])