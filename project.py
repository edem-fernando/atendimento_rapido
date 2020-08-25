# foi passado como argumento 1 segundo na função sleep da biblioteca time
# para simular 1 minuto. Para o debug não ficar muito lento será usado dessa maneira
# interaja com o terminal para receber informações e simular ações em um sistema de atendimento

# import matplotlib.pyplot as plt
import random
import time

attendants = [
    "Edem",
    "Alexo",
    "Ana Maria",
    "Fernanda"
]

rows = {
    "Primeira Fila": [0, 1],
    "Segunda Fila": [3, 1],
    "Terceira Fila": [1, 1],
    "Quarta Fila": [2, 1],
}

menu = " 1 - Visualizar Atendentes\n 2 - Atender Cliente\n 3 - Gráfico de tempo nas filas\n 4 - Encerrar"
serviceMenu = " 1 - Receber dinheiro\n 2 - Troca de produto\n 3 - Devolução\n 4 - Encerrar Atendimento"
rowsMenu = " 1 - Primeira Fila\n 2 - Segunda Fila\n 3 - Terceira Fila\n 4 - Quarta Fila"
messageError = "\033[31m[ERROR] Escolha uma opção válida\033[m"

def add_customer_to_queue(final, amountClient):
    if final > 60 or final <= 0:
        return False

    print("Organizando as filas...")
    terms = ""
    time.sleep(final)

    if rows["Primeira Fila"][0] > 11 or rows["Segunda Fila"][0] > 11 or rows["Terceira Fila"][0] > 11 or \
            rows["Quarta Fila"][0] > 11:
        return False

    if rows["Primeira Fila"][0] < rows["Segunda Fila"][0]:
        rows["Primeira Fila"][0] = amountClient
        #rows["Primeira Fila"][1] = random.randint(5, 15)
        terms = "Primeira Fila"

    elif rows["Segunda Fila"][0] < rows["Terceira Fila"][0]:
        rows["Segunda Fila"][0] = amountClient
        #rows["Segunda Fila"][1] = random.randint(5, 15)
        terms = "Segunda Fila"

    elif rows["Terceira Fila"][0] < rows["Quarta Fila"][0]:
        rows["Terceira Fila"][0] = amountClient
        #rows["Terceira Fila"][1] = random.randint(5, 15)
        terms = "Terceira Fila"

    else:
        rows["Quarta Fila"][0] = amountClient
        #rows["Quarta Fila"][1] = random.randint(5, 15)
        terms = "Quarta Fila"

    return terms

while True:
    print("========== Atendimento Rápido ==========")
    print(menu)
    optionSelected = int(input("Digite a opção desejada: "))

    if optionSelected <= 0 or optionSelected > 4:
        print(messageError)
        continue

    if optionSelected == 4:
        print("Desligando...")
        break

    if optionSelected == 1:
        print("\033[34mAtendentes:\033[m")
        for attendant in attendants:
            print("\033[34m", attendant, "\033[m")

    if optionSelected == 2:
        counter = 0
        increment = 0

        while increment < 10:
            print(rowsMenu)
            rowsSelected = int(input("Escolha a fila para atender: "))
            rowSelected = ""

            if rowSelected == 1:
               rowSelected = "Primeira Fila"

            if rowsSelected == 2:
                rowSelected = "Segunda Fila"

            if rowsSelected == 3:
                rowSelected = "Terceira Fila"

            if rowsSelected == 4:
                rowSelected = "Quarta Fila"

            if rowsSelected <= 0 or rowsSelected > 4:
                print(messageError)
                continue

            while counter < 10:
                print(serviceMenu)
                serviceSelected = int(input("Digite a opção desejada: "))

                if serviceSelected == 1:
                    amount = float(input("Digite a quantia recebida R$: "))
                    continue

                if serviceSelected == 2:
                    print("\033[32mProduto trocado com sucesso\033[m")
                    continue

                if serviceSelected == 3:
                    luck = random.randint(0, 1)

                    if luck == 0:
                        print("\033[31mDevolução NÃO ACEITA. Por favor verifique os termos.\033[m")

                    print("\033[32mDevolução aceita com sucesso.\033[m")

                if serviceSelected == 4:
                    break
                    break
                    break
                counter = counter + 1

                increment = increment + 1

"""plt.xlabel('Cadeiras') 
plt.ylabel('Média') 
plt.bar(subjects, avarege, color='blue')
plt.show()"""
