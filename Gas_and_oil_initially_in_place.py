print("\n")


print("Volume of Gas Initially in place(GIIP)\n")

print("The formula to determine gas in place is listed below:\n")


print("G =(43560AhQ(1-Swc))/Bgi\n")

print("where:")

print("G=gas oil in place at standard condition,scf")
print("A=area,acre")
print("h=reservoir thickness,ft")
print("Q=rock porosity,%")
print("Swc=connate water saturation,% ")
print("Bgi=gas formation volume factor,rcf/scf\n")

A = float(input("A="))
h = float(input("h="))
Q = float(input("Q="))
Swc = float(input("Swc="))
Bgi = float(input("Bgi ="))


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

A = float(input("A="))
h = float(input("h="))
Q = float(input("Q="))
Swc = float(input("Swc="))
Boi = float(input("Boi ="))
print('\n')

print('STOIIP=',(7758*A*h*Q*(1-Swc))/Boi)
print("\n")

print("Note: the stock tank condition is a standard surface condition of oil and gas at 60F and 14.7 psia\n")











        