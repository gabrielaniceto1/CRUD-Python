import os
os.system("cls")

def vizualizar_treinos():
    with open("csv\Treinos.csv","r",encoding="utf8") as file:
        for i in file:
            separados=i.split(",")
            print(f"nome: {separados[0]} | data: {separados[1]} | tempo: {separados[2]}min | distancia: {separados[3]}km | local: {separados[4]} | clima: {separados[5]} \n")
    import os
    sair=input("Digite ENTER para sair ")
    os.system("cls")        

if  __name__=="__main__":
    vizualizar_treinos()