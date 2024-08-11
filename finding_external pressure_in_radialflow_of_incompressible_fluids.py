import math
print("Reservoir Performance : Therotical Method")
print("radial flow of incompressible fluids")
print("\n")

print("Productivity index (J):")

print("J = Qo/(Pe-Pwf)")
print("J = (0.00708kh(Pe-pwf))/μoBo ln(re/rw)")
print("This equation can be rearranged as: ")
print("Pe = Pwf + [μoBoQo/0.00708kh] ln(re/rw)")
print("\n")

print("Where:")


print("Qo = oil,flow rate,STB/day")
print("Pe = external pressure,psi")
print("Pwf = bottom-hole flowing pressure ,psi")
print("k = permeability,md")
print("μo = oil viscosity,cp")
print("Bo = oil formation volume factor,bbl/STB")
print("h = thickness,ft")
print("re = external or drainage radius,ft")
print("rw = wellbore radius ,ft")
print("\n")
print("regime = steady state")
print("Fluid = incompressible")

#Example
#Qo=600 stb/day,k=120 md,h=25ft,Pwf=1800 psi,μo=2.5cp,Bo=1.25 bbl/STB,re=745 ft,rw=0.25 ft
#Pe = Pwf + [μoBoQo/0.00708kh] ln(re/rw)
#Pe=2506 psi


Qo = float(input("Qo="))
k = float(input("k="))
h = float(input("h="))
Pwf = float(input("pwf="))
μo = float(input("μo="))
Bo =float(input("Bo="))
re = float(input("re="))
rw = float(input("rw="))
print("pe=" ,Pwf + (((μo*Bo*Qo)/(0.00708*k*h)) * math.log(re/rw)))


