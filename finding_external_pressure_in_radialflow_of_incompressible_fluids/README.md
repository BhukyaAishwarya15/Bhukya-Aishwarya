# Reservoir Characteristics
## Types of Flow Regimes 
* Steady-state flow-.The flow regime is identified as a steady-state flow if the pressure at every location in the reservoir remains constant, i.e., does not change with time.
* Unsteady-state Flow-The unsteady-state flow (frequently called transient flow) is defined as the fluid flowing condition at which the rate of change of pressure with respect to time at any position in the reservoir is not zero or constant. This definition suggests that the pressure derivative with respect to time is essentially a function of both position i and time t,
* Pseudosteady state Flow-when the pressure at different locations in the reservoir is declining linearly as a function of time, i.e., at a constant declining rate, the flowing condition is characterized as the pseudo-steady-state flow. Mathematically, this definition states that the rate of change of pressure with respect to time at everyIt should be pointed out that the pseudo-steady state flow is commonly referred to as semi-steady-state flow and quasi-steady state flow. position is constant.

## Reservoir Fluid Types according to Compressibility 
* Incompressible Fluids-it is defined as the fluid whose volume (or density) does not change with pressure. 
* Slightly Compressible Fluids-These fluids exhibit small changes in volume, or density, with changes in pressure.
* Compressible Fluids-These are fluids that experience large changes in volume as a function of pressure. All gases are considered compressible fluids

## Types of Reservoir Geometries
* Radial Flow-The flow into or away from  a wellbore will follow radial flow lines. Because fluids move toward the well from all directions and coverage at the wellbore.
* Linear Flow-Linear flow occurs when flow paths are parallel and the fluid flows in a single direction. In addition, the cross sectional area to flow must be constant.
* Spherical and Hemispherical Flow-Depending upon the type of wellbore completion configuration, it is possible to have a spherical or hemispherical flow near the wellbore. A well with a limited perforated interval could result in spherical flow in the vicinity of the perforations. A well that only partially penetrates the pay zone,could result in hemispherical flow.

## Number of flowing fluids in the reservoir 
* Single-phase flow (oil, water, or gas)
* Two-phase flow (oil-water, oil-gas, or gas-water)
* Three phase flow (oil, water, and gas)

# Darcy’s Law
* The fundamental law of fluid motion in porous media is Darcy’s Law. 
* The mathematical expression developed by Henry Darcy in 1856 states that velocity of a homogeneous fluid in a porous medium is
 proportional to the pressure gradient and inversely proportional to the fluid viscosity. 
* For a horizontal linear system, this relationship is:
## v = q/A = - kdp/𝜇dx (eq:1)
* 𝑣 is the apparent velocity in centimeters per second and is equal to q/A,where q is the volumetric flow rate in cubic centimeters per second and A is total cross sectional area of the rock in square centimeters. In other words, A includes the area of the rock material as well as the area of the pore channels. 
* The fluid viscosity, 𝜇, is expressed in centipoise units, and the pressure gradient, dp/dx, is in atmospheres per centimeter, taken in the same direction as v and q. 
* The proportionality constant, k, is the permeability of the rock expressed in Darcy units.

# Darcy’s Law Assumptions 
* Darcy’s Law applies only when the following conditions exist: 
* Laminar (viscous) flow
* Steady-state flow
* Incompressible fluids
* Homogeneous formation

# let us derive the formula for linear flow of incompressible fluids-steady state (Darcy law assumptions)
* In the linear system, it is assumed the flow occurs through a constant cross-sectional area A, where both ends are entirely open to flow. It is also assumed that no flow crosses the sides, top.  
* If an incompressible fluid is flowing across the element dx, then the fluid velocity v and the flow rate q are constants at all points. The flow behavior in this system can be expressed by the differential form of Darcy’s equation
 ### v = q/A = - kdp/𝜇dx
Separating the variables of eq:1 and integrating over the length of the linear system gives: 

 #### q = kA(p1-p2)/𝜇L
* It is desirable to express the above relationship in customary field
units,that is

q=0.001127 𝑘𝐴 (𝑝1−𝑝2)/𝐿

 Where q= flow rate, bbl/day
 * k= absolute permeability, md
 * p= pressure, psia
 * 𝜇= viscosity, cp
 * L= distance, ft
 * A= cross-sectional area, 𝑓𝑡2

# let us derive the formula for Rdial flow of incompressible fluids-steadt satte condition(darcy law assumptions)
* In a radial flow system, all fluids move toward the producing well from all directions. 
Before flow can take place, however, a pressure differential must exist. 
* Thus, if a well is to produce oil, which implies a flow of fluids
through the formation to the wellbore, the pressure in the formation at the wellbore must be less than the pressure in the formation at some distance from the well. 
* The pressure in the formation at the wellbore of a producing well is known as the bottomhole flowing pressure (flowing BHP, 𝑝𝑤𝑓). 
* The formation is considered to a uniform thickness h and a constant permeability k. 
* Because the fluid is incompressible, the flow rate q must be constant at all radii. Due to the steady-state flowing condition, the 
pressure profile around the wellbore is maintained constant with time.  
* At any point in the reservoir the cross-sectional area across which flow occurs will be the surface area of a cylinder, which is 2𝜋𝑟ℎ, or:  
#### v = q/Ar = q/2πrh = o.001127kdp/𝜇dr
* The flow rate for a crude oil system is customarily expressed in surface units, i.e., stock-tank 
barrels (STB), rather than reservoir units. 
▪ Using the symbol 𝑄𝑜 to represent the oil flow as expressed in STB/day, then:
 𝑞 =𝐵𝑜𝑄𝑜
 Where 𝐵𝑜 is the oil formation volume factor bbl/STB. 
▪ The flow rate in Darcy’s equation can be expressed in STB/day to give:

#### 𝑄𝑜𝐵𝑜/2𝜋𝑟ℎ = 0.001127𝑘𝑑𝑝/𝜇𝑜𝑑r

  Integrating the above equation between two radii, 𝑟1 and 𝑟2, when the pressures are 𝑝1 and 𝑝2,gives
 
 #### 𝑄𝑜 = 0.00708𝑘ℎ(𝑝2 −𝑝1)/𝜇𝑜𝐵𝑜 ln( 𝑟2 - 𝑟1)
 Frequently the two radii of interest are the wellbore radius 𝑟𝑤 and the external or drainageradius 𝑟𝑒. Then: 
#### 𝑄𝑜 = 0.00708𝑘ℎ(𝑝e − 𝑝w)/𝜇𝑜𝐵𝑜 ln( 𝑟e/𝑟w) 
Where 𝑄𝑜= oil flow rate, STB/day
 𝑝𝑒= external pressure, psi
 𝑝𝑤𝑓= bottom-hole flowing pressure, psi
 k= permeability, md
 𝜇𝑜= oil viscosity, cp
 𝐵𝑜= oil formation volume factor, bbl/STB
 h= thickness, ft
 𝑟𝑒= external or drainage radius, ft
 𝑟𝑤= wellbore radius, ft

* The external (drainage) radius 𝑟𝑒 is usually determined from the well spacing by equating the area of the well spacing wit that of a circle, i.e., 
𝜋𝑟𝑒^2 = 43,560 𝐴
 Or
 𝑟𝑒 = (43,560A/𝜋)^0.5
 Where A is the well spacing in acres. 
 ### The above equation can be rearranged as
 *  𝑝e=𝑝𝑤𝑓+ (𝑄𝑜𝐵𝑜𝜇𝑜/0.00708𝑘ℎ) ln(𝑟e/𝑟𝑤) 
 * which is our required equation for finding external pressure
 
