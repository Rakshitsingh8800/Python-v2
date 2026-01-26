import math 

angle_rad = float(input("Enter the angle in degree: "))\

angle_rad = math.radians(angle_rad)

sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

print("Sin(", angle_rad,") =" , sin_value)
print("Cos(", angle_rad,") =" , cos_value)
print("Tan(", angle_rad,") =" , tan_value)