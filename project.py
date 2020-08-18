"""
    Criando intervalo de tempo com a classe datetime
    Falta criar o intervalo adicionar à matriz client
    e adicionar o final do tempo que o client ficou na fila row
"""

import random
from datetime import datetime
attendants = ['Maria', 'Augusto', 'Luisa', 'Mario']
client = [
    [1, 'Edem', 0, 0], [2, 'Ronaldo', 0, 0], [3, 'Victoria', 0, 0], [3, 'Michael', 0, 0], [4, 'Fernanda', 0, 0], [5, 'Amanda', 0, 0],
    [6, 'Alana', 0, 0]]
menu = ' 1 - Atender Cliente\n 2 - Visualizar tempo médio da fila\n 3 - Visualizar fila\n 4 - Encerrar'
serviceMenu = ' 1 - Passar Cartão\n 2 - Receber Dinheiro\n 3 - Troca de produto\n 4 - Devolução\n 5 - Finalizar Atendimento'
counter = 0
row = []
"""data = datetime.now()
print(data.strftime("%H:%M"))"""
for clientName in client:
    row.append(clientName[1])

while counter < 1:
    print("========== Atendimento rápido ==========")
    print(menu)
    actionMenu = int(input("Digite o número da sua opção: "))

    if actionMenu < 1 or actionMenu >= 4:
        print('Encerrando...')
        break

    if actionMenu == 3:
        for i in client:
            print(i)
        continue

    if actionMenu == 2:
        for clients in client:
            print(clients[0], ' - ', clients[1])

        clientSelected = int(input("Digite o número do seu cliente: "))
        if clientSelected < 1 or clientSelected > 6:
            print("Escolha uma opção válida")

        for i in client:
            if clientSelected == i[0]:
                print("O tempo médio de", i[1], 'foi de ', i[2], 'minutos')
        continue

    if actionMenu == 1:
        costumerServed = random.choice(row)

        print("Atendendo", costumerServed)
        print(serviceMenu)
        serviceSelected = int(input("Escolha a sua opção: "))

        if serviceSelected < 1 or serviceSelected > 5:
            print("Opção inválida")
            continue
    counter = counter + 1
