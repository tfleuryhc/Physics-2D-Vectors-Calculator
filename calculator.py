import math

vecx = ["E", "W"]
vecy = ["N", "S"]

d1 = float(input("First vector?"))
sorc1 = str(input("Simple Vector or Complex Vector\n S or C?\n"))
if (sorc == "S" or "s"):
  dir1 = str(input("Direction?"))
elseif (sorc == "C" or "c"):
  dirca1 = str(input("Direction?"))
  dircb1 = float(input("Angle?"))
  dircc1 = str(input("Angle Direction?"))
  if (dircb1 == vecy):
    dircb1 = 90 - dircb1
    ddira1 = dirca1
    ddirc1 = dircc1
    dirca1 = ddirc1
    dircc1 = ddira1    
else:
  print ("Not a valid answer.")

d2 = float(input("Second vector?"))
sorc2 = str(input("Simple Vector or Complex Vector\n S or C?\n"))
if (sorc == "S" or "s"):
  dir2 = str(input("Direction?"))
elseif (sorc == "C" or "c"):
  dirca2 = str(input("Direction?"))
  dircb2 = float(input("Angle?"))
  dircc2 = str(input("Angle Direction?"))
   if (dircb2 == vecy):
    dircb2 = 90 - dircb2
    ddira2 = dirca2
    ddirc2 = dircc2
    dirca2 = ddirc2
    dircc2 = ddira2
else:
  print ("Not a valid answer.")


#find d_result only if the movements are perpendicular
d_result = math.sqrt(d1 * d1 + d2*d2)

dir_result = math.degrees(math.atan(float(d1/d2)))

d_result = round(d_result,2)
dir_result = round(dir_result,2)

d = str(d_result)
dirc = str(dir_result) #str() does not return any data

print("The resulting vector is: " + d + "[" + dir1 + dirc + dir2 + "]")
