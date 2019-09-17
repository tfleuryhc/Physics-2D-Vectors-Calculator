import math

d1 = float(input("First vector?"))
dir1 = str(input("Direction?"))
d2 = float(input("Second Vector?"))
dir2 = str(input("Second Direction?"))

#find d_result only if the movements are perpendicular
d_result = math.sqrt(d1 * d1 + d2*d2)

dir_result = math.degrees(math.atan(float(d1/d2)))

d_result = round(d_result,2)
dir_result = round(dir_result,2)

d = str(d_result)
dir = str(dir_result) #str() does not return any data

print("The resulting vector is: " + d + "[" + dir1 + dir + dir2 + "]")
