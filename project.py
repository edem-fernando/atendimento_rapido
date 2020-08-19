import random
import time

def transform_minute(hour, minute):
    hourMinute = hour * 60 + minute
    return hourMinute

def calculate_diff_time(bigValue, smallValue):
    return int(bigValue - smallValue)

client = [
    [1, 'Edem', 0, 0], [2, 'Ronaldo', 0, 0], [3, 'Michael', 0, 0], [4, 'Fernanda', 0, 0],
    [5, 'Amanda', 0, 0], [6, 'Antonio', 0, 0], [7, 'Elano', 0, 0], [8, 'Gabriel', 0, 0],
    [9, 'Alex', 0, 0], [10, 'Jardel', 0, 0], [11, 'Núbia', 0, 0], [12, 'Anastácia', 0, 0],
    [13, 'Luizilene', 0, 0], [14, 'Patrick', 0, 0], [15, 'Patricia', 0, 0], [16, 'Paloma', 0, 0],
    [17, 'Fernanda', 0, 0], [18, 'Adriana', 0, 0], [19, 'Darla', 0, 0], [20, 'Robério', 0, 0], [21, 'Francisco', 0, 0],
    [22, 'Ana Maria', 0, 0], [23, 'Ricardo', 0, 0], [24, 'Caio', 0, 0], [25, 'Kayane', 0, 0], [26, 'Ágata', 0, 0],
    [27, 'Beijamin', 0, 0], [28, 'Adan', 0, 0]
]
menu = ' 1 - Atender Cliente\n 2 - Visualizar tempo médio da fila\n 3 - Visualizar clientes\n 4 - Encerrar'
serviceMenu = ' 1 - Receber Dinheiro\n 2 - Troca de produto\n 3 - Devolução\n 4 - Finalizar Atendimento\n 5 - Voltar'
counter = 0
rows = []

# iniciando tempo
for clientName in client:
    rows.append(clientName[1])

    if len(rows) == 5:
        break

    if clientName[1] in rows:
        clientName.append(True)
        timeNow = time.localtime()
        clientName[2] = transform_minute(timeNow[3], timeNow[4])

while counter < 10:
    print("========== Atendimento rápido ==========")
    print(menu)
    actionMenu = int(input("Digite o número da sua opção: "))

    if actionMenu < 1 or actionMenu >= 4:
        print('Encerrando...')
        break

    if actionMenu == 3:
        for i in client:
            print(i[1])
        continue

    if actionMenu == 2:
        for clients in client:
            print(clients[0], ' - ', clients[1])

        clientSelected = int(input("Digite o número do seu cliente: "))
        if clientSelected < 1 or clientSelected > len(clients):
            print("Escolha uma opção válida")

        for i in client:
            if clientSelected == i[0]:
                #print("O tempo médio de", i[1], 'foi de', (i[2] - i[3]), 'minutos')
                print(i[1], ' - ', i[2], ' - ', i[3])
        continue

    if actionMenu == 1:
        print("Atendendo", rows[0])

        counterMenuService = 0

        while counterMenuService != 1:
            print(serviceMenu)
            serviceSelected = int(input("Escolha a sua opção: "))

            if serviceSelected == 5:
                break

            if serviceSelected < 1 or serviceSelected > 5:
                print("Opção inválida")
                continue

            if serviceSelected == 1:
                float(input("Digite a quantia recebida R$: "))
                continue

            if serviceSelected == 2:
                print("Produto trocado com sucesso!")
                continue

            if serviceSelected == 3:
                terms = [0,1]
                devolution = random.choice(terms)

                if devolution == 0:
                    print("Devolução negada")
                    continue
                print("Devolução aceita")
                continue

            if serviceSelected == 4:
                # tempo finalizado
                for clientName in client:
                    if rows[0] == clientName[1]:
                        finalTime = time.localtime()
                        clientName[3] = transform_minute(finalTime[3], finalTime[4])
                        clientName[4] = False
                        rows.pop(0)
                        print(clientName[4])

                        if clientName[4] != False:
                            rows.append(clientName[1])

                        if len(rows) > 5:
                            break
                break
            counterMenuService = counterMenuService + 1
    counter = counter + 1

