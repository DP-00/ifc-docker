import pprint as pp
import ifcopenshell.util.element

model=ifcopenshell.open("Duplex_A.ifc")

# pp.pprint(Spaces)

print("Enter choice: ")
choice = int(input())

# for space in Spaces:
#     print(f'Space: {space.Name}, LongName: {space.LongName}, GlobalID {space.GlobalId}')

if choice == 1:
    Windows = model.by_type("IfcWindow")
    for window in Windows:
        PSetWin = ifcopenshell.util.element.get_psets(window)
        pp.pprint(PSetWin)
        print(f'Window: {window.Name}')
elif choice == 2:
    Walls = model.by_type("IfcWall")
    for wall in Walls:
        PSetWall = ifcopenshell.util.element.get_psets(wall)
        pp.pprint(PSetWall)
        print(f'Wall: {wall.Name}')
elif choice == 3:
    Spaces = (model.by_type("IfcSpace"))
    for space in Spaces:
        PSetSpace = ifcopenshell.util.element.get_psets(space)
        pp.pprint(PSetSpace)
        print(f'Space: {space.Name}')

# ilosc scian w modelu
Walls = model.by_type("IfcWall")
print(len(Walls))


# ilosc scian zewnetrznych w modelu (trzeba z properties to znalezc - isExternal)
count = 0
ext_walls=[]
for wall in Walls:
    PSetWall = ifcopenshell.util.element.get_psets(wall)
    if (PSetWall.get("Pset_WallCommon").get("IsExternal")) == True:
        count=count+1
        ext_walls.append(wall)
totalvolume = 0
for w in ext_walls:
    psets = ifcopenshell.util.element.get_psets(w)
    for psetname, pset_dict in psets.items():
            for name, value in pset_dict.items():
                # print(f"{name}:{value}")
                if name == "NetVolume":
                    totalvolume+=float(value)
print(f'TotalVolume: {totalvolume:.2f}')


print(f'Count: {count}')


