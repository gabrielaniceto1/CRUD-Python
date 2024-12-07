"""
1. definir as funções para retornar o tempo e adistancia
2. define a função de filtragem
2.1. abre o csv
2.2. transmorma tudo(csv) em uma lista separadas por \n
2.3. quebra cada elemento da lista em listas menores separadas po ,
2.4. recebe o modo e o reverso e, utilizando o key, chama a função de tempo ou distancia para definir a variavel de filtragem
(tempo ou distancia) e o modo de filtragem(crescente ou decrescente)
2.5. exibe os elementos separados por ,
3. pergunta ao usuario como ele quer a filtragem
3.1. chama a função
3.2. limpa a tela e encerra o loop ou continua
"""
#1. definir as funções para retornar o tempo e adistancia

def filtrar_tempo(lista):
    return float(lista[2])

def filtrar_distancia(lista):
    return float(lista[3])

#2. define a função de filtragem

def filtragem(modo, reverso):
    #2.1. abre o csv

    with open(r"csv\Treinos.csv", "r", encoding="utf8") as file:
        #2.2. transmorma tudo(csv) em uma lista separadas por "\n"

        linhas = file.read().split("\n")
        #2.3. quebra cada elemento da lista em listas menores separadas por ",""

        for i in range(len(linhas)):
            linhas[i] = linhas[i].split(",")
        #2.4. recebe o modo e o reverso e, utilizando o key, chama a função de tempo ou distancia para definir a variavel de filtragem
        #(tempo ou distancia) e o modo de filtragem(crescente ou decrescente)

        if modo == 1:
            linhas.sort(key=filtrar_tempo, reverse=reverso)
        else:
            linhas.sort(key=filtrar_distancia, reverse=reverso)
        #2.5. exibe os elementos separados por ","

        for linha in linhas:           
            print(f"nome: {linha[0]} | data: {linha[1]} | tempo: {linha[2]}min | distancia: {linha[3]}km | local: {linha[4]} | clima: {linha[5]} \n")

def menu_filtragem():
    import csv
    import os
    while True:
        #3. pergunta ao usuario como ele quer a filtragem

        modo =int(input("Gostaria de filtrar por:\n1 - Tempo\n2 - Quilometragem\n"))

        reverso =int(input(f"""
1 - Crescente
2 - Decrescente
"""))
        #3.1. chama a função

        filtragem(modo, True if reverso == 2 else False)

        sair=input("Aperte Enter para Sair ou escreva 'continue' para filtrar novamente: ")
        #3.2. limpa a tela e encerra o loop ou continua

        if sair=="continue":
            os.system("cls")
        else:
            os.system("cls")
            break

        
if __name__ == "__main__":
    menu_filtragem()