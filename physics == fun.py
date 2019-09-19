import math
import string

run = True
complex1 = False
complex2 = False

input_1 = input("First vector? (add space between elements)\n")
input_2 = input("Second Vector?\n")

#Split answers into a list and see if it's complex or not
vector_1 = input_1.split(" ")
num_1 = len(vector_1)
if num_1 == 4: # 95 S 56 E
    complex1 = True
if (num_1 % 2 != 0) or num_1 > 4:
    print("Question is invalid")
    exit()
vector_2 = input_2.split(" ")
num_2 = len(vector_2)
if num_2 == 4:
    complex1 = True
if (num_2 % 2 != 0) or num_2 > 4:
    print("Question is invalid")
    exit()

vector_1[0] = int(vector_1[0])
if complex1 == True:
    vector_1[2] = int(vector_1[2])
vector_2[0] = int(vector_2[0])
if complex2 == True:
    vector_2[2] = int(vector_2[2])

#Convert all North or South headed vectors into West or East headed vectors:
if complex1 == True:
    if vector_1[1] == "N" or "S":
        vector_1[2] = 90 - vector_1[2]
        main_dir = vector_1[1]
        vector_1[1] = vector_1[3]
        vector_1[3] = main_dir
        if vector_1[1] == "E" or "e":
            vecxval1 = 1
        else:
            vecxval1 = -1
        if vector_1[3] == "N" or "n":
            vecyval1 = 1
        else:
            vecyval1 = -1


if complex2 == True:
    if vector_2[1] == "N" or "S":
        vector_2[2] = 90 - vector_2[2]
        main_dir_2 = vector_2[1]
        vector_2[1] = vector_2[3]
        vector_2[3] = main_dir_2
        if vector_2[1] == "E" or "e":
            vecxval2 = 1
        else:
            vecxval2 = -1
        if vector_2[3] == "N" or "n":
            vecyval2 = 1
        else:
            vecyval2 = -1

#Convert inputted numbers into Intergers
vector_1[0] = int(vector_1[0])
if complex1 == True:
    vector_1[2] = int(vector_1[2])

vector_2[0] = int(vector_2[0])
if complex2 == True:
    vector_2[2] = int(vector_2[2])

#Solve direction for complex questions:
#List composition: [magnitude, heading direction, angle, direction of angle, x-value of vector, y-value]
if complex1 == True:
    vector_1.append(vector_1[0] * math.sin(vector_1[2])*vecxval1)
    vector_1.append(vector_1[0] * math.cos(vector_1[2])*vecyval1)
if complex2 == True:
    vector_2.append(vector_2[0] * math.sin(vector_2[2])*vecxval2)
    vector_2.append(vector_2[0] * math.cos(vector_2[2])*vecyval2)

#find d_result only if the movements are perpendicular

while run == True:
    d_result = math.sqrt(vector_1[0]*vector_1[0] + vector_2[0]*vector_2[0])
    dir_result = math.degrees(math.atan(float(vector_1[0]/vector_2[0])))
    answer = input("Any more vectors?\n")
    if answer == "yes":
        vector_1[0] = d_result
        input_2 = input("What is it?")
        vector_2 = input_2.split(" ")
        num_2 = len(vector_2)
        if num_2 == 4:
            complex2 = True
        if (num_2 % 2 != 0) or num_2 > 4:
            print("Question is invalid")
            exit()

    else:
        run = False

d_result = round(d_result,2)
dir_result = round(dir_result,2)

d = str(d_result)
dir = str(dir_result) #str() does not return any data

print("The resulting vector is: " + d + " [ " + vector_1[1] + " " + dir + " degree " + vector_2[1] + " ]")
