Liste1 = list(("P","Y","T","H","O","N"))
Liste2 = [300,2,3,"4","Hallo",99,"Test"]
# print("Liste1: ",Liste1,"\nListe2: ",Liste2)
# print(len(Liste1),len(Liste2))
# L1 = len(Liste1)
# print(L1)
# print(Liste1[0],Liste1[-3])
# print("Vom ersten bis zum 3.Element: ",Liste2[0:3])
# print("Die ersten 4 Elemente: ",Liste2[:4],"\nJedes 3.Element ab dem 2.Element: ",Liste2[1::3])
# print(Liste2[::-1])
# print(Liste2[1::-1])
# print(Liste1[0:5])
# for variable in Liste1:
#     print(variable)
# print("\n")
# for i in range(0, 6): #Die Null muss nicht geschrieben werden, da sie als Standardwert in dieser Funktion gesetzt ist
#     print(i,".Element: ",Liste1[i])
# Liste1.append(2.0)
# print(Liste1)
# Liste1.append(Liste2)
# print(Liste1[7])
# Liste1.insert(6, 1.0)
# print(Liste1)
# Liste1.extend([8,9,10])
# print(Liste1)
# Liste1.remove(1.0)
# print(Liste1)
# Liste1.pop(6)
# print(Liste1)
# del Liste1[6:len(Liste1)]
# print(Liste1)
# print(Liste1.index("T"))
# pythonL = Liste1
# print(pythonL,"\n",Liste1)
# pythonL.append("L")
# print(pythonL,"\n",Liste1)
# pythonL.remove("L")
pythonL = Liste1.copy()
pythonL.append("L")
# print(pythonL,"\n",Liste1)
# print(max(pythonL))
# print(sum(pythonL)) #Geht nicht mit Strings
# print(all(pythonL))
# pythonL.append(Liste1)
# print(pythonL,"\n",pythonL[7][1])
# for i in pythonL:
#     print(i)
#     for k in i:
#         print("inner loop ",k)
# NewList = ["Pzkw 3","Hellcat","Jagdpanzer","Pzkw Tiger I","Pzkw Tiger II","Lorett B"]
# print(NewList)
# DeutschePanzer = [var for var in NewList if "Pzkw" in var] #List Comprehension
# print(DeutschePanzer)
# DeutschePanzer.pop()
# print(DeutschePanzer)
# strList = ["abc","abcd","bacd","abcde","Ab","zycd"]
# print(max(strList))
# aList = [10, 20, 30, 40, 50, 60, 70, 80]
# print(aList[3:])
# my_list = ["Hello", "Python","Test"]
# print("--".join(my_list))
# Null = [None] * 10
# print(len(Null))
# aList = [4, 8, 12, 16]
# aList[1:3] = [20, 24, 28]
# print(aList)
print(pythonL[2:5])