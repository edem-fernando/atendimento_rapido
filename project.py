# import matplotlib.pyplot as plt
import random
import time

rows = {
    "Primeira Fila": [0, 0],
    "Segunda Fila": [0, 0],
    "Terceira Fila": [0, 0],
    "Quarta Fila": [0, 0],
}


def add_customer_to_queue(final, amountClient):
    if final > 60 or final <= 0:
        return False

    init = 0
    print("Organizando as filas...")
    time.sleep(final)
    terms = ""

    if rows["Primeira Fila"][0] > 11 or rows["Segunda Fila"][0] > 11 or rows["Terceira Fila"][0] > 11 or \
            rows["Quarta Fila"][0] > 11:
        return False

    if rows["Primeira Fila"][0] < rows["Segunda Fila"][0]:
        rows["Primeira Fila"][0] = amountClient
        rows["Primeira Fila"][1] = random.randint(5, 15)
        terms = "Primeira Fila"

    elif rows["Segunda Fila"][0] < rows["Terceira Fila"][0]:
        rows["Segunda Fila"][0] = amountClient
        rows["Segunda Fila"][1] = random.randint(5, 15)
        terms = "Segunda Fila"

    elif rows["Terceira Fila"][0] < rows["Quarta Fila"][0]:
        rows["Terceira Fila"][0] = amountClient
        rows["Terceira Fila"][1] = random.randint(5, 15)
        terms = "Terceira Fila"

    else:
        rows["Quarta Fila"][0] = amountClient
        rows["Quarta Fila"][1] = random.randint(5, 15)
        terms = "Quarta Fila"


    return terms

amountClient = random.randint(3, 11)
print("Em 1 minuto, chegaram", amountClient, "pessoas na", add_customer_to_queue(2, amountClient))
print(rows)

"""plt.xlabel('Cadeiras') 
plt.ylabel('Média') 
plt.bar(subjects, avarege, color='blue')
plt.show()"""
