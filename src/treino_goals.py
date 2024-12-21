def adicionar_meta():
    while True:
        try:
            nome=input("Digite um nome que você reconheça a meta: ")
            tempo=float(input("Digite (em minutos) a duração desejada para seu treino/competição: "))
            distancia=float(input("Digite (em km) a distancia desejada: "))
            break
        except ValueError:
            print("Digite em numeros")

    meta=(f"{nome},{str(tempo)},{str(distancia)}")
    with open("csv\Metas.csv","a", encoding="utf8") as file:
        file.write(meta)
    print("meta adicionado como sucesso!")
    import os
    sair=input("Digite ENTER para sair ")
    os.system("cls")

def atualizar_meta():
    lista=[]
    meta_atualizar=input("Digite o nome da meta que você quer atualizar: ")
    with open("csv\Metas.csv","r") as file:
        for i in file:
            separar=i.split(",")
            if separar[0]==meta_atualizar:
                continue
            else:
                lista.append(i)
        while True:
            try:
                nome=input("Digite um nome que você reconheça a meta nova: ")
                tempo=float(input("Digite (em minutos) a nova duração: "))
                distancia=float(input("Digite (em km) a nova distancia desejada: "))
                break
            except ValueError:
                print("Digite em numeros")

        meta_nova=(f"{nome},{str(tempo)},{str(distancia)}")
        lista.append(meta_nova)
    with open("csv\Metas.csv","w",encoding="utf8") as file:
        file.writelines(lista)

    print("Meta atualizada com sucesso! ")

def deletar_meta():
    lista=[]
    meta_deletar=input("Digite o nome da meta que você quer deletar: ")
    with open("csv\Metas.csv","r") as file:
        for i in file:
            separar=i.split(",")
            if separar[0]==meta_deletar:
                continue
            else:
                lista.append(i)
    with open("csv\Metas.csv","w",encoding="utf8") as file:
        file.writelines(lista)
    print("Meta deletada com sucesso!")

if __name__=="__main__":
    deletar_meta()
