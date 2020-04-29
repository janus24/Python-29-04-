import os
os.system("cls")

x=input("Podaj wysokość wieży: ")
x=int(x)
i=1
for a in range(x):
    print("A"*i,"\n")
    i=i+1
    if(i==11):
        break