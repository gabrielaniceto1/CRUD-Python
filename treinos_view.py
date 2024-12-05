import os
os.system("cls")

def vizualizar_treinos():
    with open("Treinos.csv","r",encoding="utf8") as file:
        for i in file:
            print(i)

if  __name__=="__main__":
    vizualizar_treinos()