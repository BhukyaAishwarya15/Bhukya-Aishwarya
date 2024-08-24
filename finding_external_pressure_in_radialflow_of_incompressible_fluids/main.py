import math
print("Reservoir Performance : Theoretical Method")
print("radial flow of incompressible fluids")
print("\n")

print("Productivity index (J):")

print("J = Qo/(Pe-Pwf)")
print("J = (0.00708kh(Pe-pwf))/μoBo ln(re/rw)")
print("This equation can be rearranged as: ")
print("Pe = Pwf + [μoBoQo/0.00708kh] ln(re/rw)")
print("\n")

print("Where:")


print("Qo = oil flow rate,STB/day")
print("Pe = external pressure,psi")
print("Pwf = bottom-hole flowing pressure ,psi")
print("k = permeability,md")
print("μo = oil viscosity,cp")
print("Bo = oil formation volume factor,bbl/STB")
print("h = thickness,ft")
print("re = external or drainage radius,ft")
print("rw = wellbore radius ,ft")
print("\n")

#Example
#Qo=600 stb/day,k=120 md,h=25ft,Pwf=1800 psi,μo=2.5cp,Bo=1.25 bbl/STB,re=745 ft,rw=0.25 ft
#Pe = Pwf + [μoBoQo/0.00708kh] ln(re/rw)
#regime=steady state , fluid type= incompressible
#Pe=2506 psi


print("regime = steady state")
print("Fluid = incompressible")
Qo = float(input("Enter the value of Qo = "))
k = float(input("Enter the value of k= "))
h = float(input("Enter the value of h="))
Pwf = float(input("Enter the value of Pwf="))
μo = float(input("Enter the value of μo="))
Bo =float(input("Enter the value of Bo="))
re = float(input("Enter the value of re="))
rw = float(input("Enter the value of rw="))
print("pe=" ,Pwf + (((μo*Bo*Qo)/(0.00708*k*h)) * math.log(re/rw)))



