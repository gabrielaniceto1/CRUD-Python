import os 
os.system("cls")

def deletar_treino():
    lista=[]
    deletar=input("Digite o nome do treino/competição que você quer apagar: ")
    with open("Treinos.csv","r") as file:
        for i in file:
            separar=i.split(",")
            if deletar==separar[0]:
                continue
            else:
                lista.append(i)
    with open("Treinos.csv","w",encoding="utf8") as file:
        file.writelines(lista)
    import os
    sair=input("Treino deletado com sucesso!\nAperte ENTER para sair")
    os.system("cls")

if __name__=="__main__":
    deletar_treino()