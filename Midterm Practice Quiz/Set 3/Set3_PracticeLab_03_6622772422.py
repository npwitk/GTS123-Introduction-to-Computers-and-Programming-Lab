import math as m

## ข้อนี้ตัวอย่างไม่ตรง

sphereVolume = float(input("Input a sphere volume: "))
inputVolumeUnit = input("Input a unit of the volume: ")
desireRadiusUnit = input("Input a unit of the sphere radius length: ")

if (sphereVolume >= 1) and (inputVolumeUnit in ["ft", "in"]) and (desireRadiusUnit in ["ft", "in"]):

    if inputVolumeUnit == "ft":
        volumeInFT = sphereVolume
    else:
        volumeInFT = sphereVolume/12
    
    if desireRadiusUnit == "ft":
        radius = (((3/(4*m.pi)*volumeInFT))**(1/3))
    else:
        radius = ((((3/(4*m.pi)*(volumeInFT))**(1/3))))*12

    print("The radius of a sphere with a volume of %.2f cubic %s is %.2f %s." % (sphereVolume, inputVolumeUnit, radius, desireRadiusUnit))
else:
    print("Invalid input")