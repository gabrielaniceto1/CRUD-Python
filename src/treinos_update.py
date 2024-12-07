import os
os.system("cls")

def treino_atualizar():
    lista=[]
    nome_atualizar=input("Digite o nome do treino/competição que voê deseja atualizar: ")
    with open("csv\Treinos.csv", "r", encoding="utf8") as file:
        for i in file:
            separar=i.split(",")
            nome_antigo=separar[0]
            if nome_atualizar==nome_antigo:
                nome=str(input("Digite o novo nome do treino/competição: ")).upper()
                data=str(input("Digite a nova data do treino/competição: "))
                while True:
                    try:
                        tempo=float(input("Digite (em minutos) a nova duração do seu treino/competição: "))
                        distancia=float(input("Digite (em km) a nova distancia percorrida: "))
                        break
                    except ValueError:
                        print("Digite em numeros")
                local=str(input("Digite o novo local do seu treino/competição: ")).upper()
                clima=str(input("Digite o novo clima do local: ")).upper()
                treino=(f"{nome},{data},{str(tempo)},{str(distancia)},{local},{clima}")
                lista.append(treino)
            else:
                lista.append(i)
    with open("csv\Treinos.csv","w",encoding="utf8") as file:
        file.writelines(lista)
    import os
    sair=input("Treino atualizado com sucesso!\nAperte ENTER para sair  ")
    os.system("cls")
if __name__=="__main__":
    treino_atualizar()