#1- Continue utilizando a programação em Python, utilizando os
#comandos “if”, “else” e “elif” nas diferentes condições que
#podem ocorrer no caminho ao seu objetivo. Agora nós iremos
#elaborar uma análise SWOT inserindo também o input.
def SelecionarSWOT():
    swot=input("Insira uma das letras da inicial SWOT").lower().strip()
    if swot=="s":
        s=input("Detalhe quais são suas forças")
        RecomecarSWOT()
    elif swot=="w":
        w=input("Detalhe quais são suas fraquezas")
        RecomecarSWOT()
    elif swot=="o":
        o=input("Detalhe quais são suas oportunidades")
        RecomecarSWOT()
    elif swot=="t":
        t=input("Detalhe quais são suas ameaças")
        RecomecarSWOT()
    else:
        print("Letra incorreta\n")
        SelecionarSWOT()
def RecomecarSWOT():
    opcao=input("Deseja recomeçar?").lower().strip()
    if opcao=="sim":
        SelecionarSWOT()
    else:
        print("Muito obrigado")
        from sys import exit
        exit()
SelecionarSWOT()