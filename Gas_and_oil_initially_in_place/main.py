print("\n")


print("Volume of Gas Initially in place(GIIP)\n")

print("The formula to determine gas in place is listed below:\n")


print("G =(43560AhQ(1-Swc))/Bg\n")

print("where:")

print("G=gas oil in place at standard condition,scf")
print("A=area,acre")
print("h=reservoir thickness,ft")
print("Q=rock porosity,%")
print("Swc=connate water saturation,% ")
print("Bg=gas formation volume factor,rcf/scf\n")

A = float(input("Enter the value of  A="))
h = float(input("Enter the value of h="))
Q = float(input("Enter the value of Q="))
Swc = float(input("Enter the value of Swc="))
Bgi = float(input("Enter the value of Bg ="))


print("G=",(43560*A*h*Q*(1-Swc))/Bgi,"\n")

print("To estimate oil intially volume in place,the following formula is a volumetric calculation for oil \n")

print("STOIIP =7758AhQ(1-Swc)/Boi\n")
print("where:")
print("STOIIP= stock tank oil in place,stb")
print("A= area,acre")
print("h= reservoir thickness,ft")
print("Q= rock porosity,%")
print("Swc= connate water saturation,% ")
print("Boi=gas formation volume factor,rb/stb\n")

A = float(input("Enter the value of A="))
h = float(input("Enter the value of h="))
Q = float(input("Enter the value of Q="))
Swc = float(input("Enter the value of Swc="))
Boi = float(input("Enter the value of Boi ="))
print('\n')

print('STOIIP=',(7758*A*h*Q*(1-Swc))/Boi)
print("\n")

print("Note: the stock tank condition is a standard surface condition of oil and gas at 60F and 14.7 psia\n") 











        