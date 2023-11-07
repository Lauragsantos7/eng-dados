def get_number_right():
    right_number = 8
    user_number = int(input("Digite um número entre 1 e 10: "))
    while user_number != right_number:
        print("Você errou, tente novamente")
        user_number = int(input("Digite um número entre 1 e 10: "))
    print("Você acertou, PARABENS!!!")


# get_number_right()


def average():
    sum = 0
    for i in range(1, 4):
        note = int(input(f"Digite sua nota {i}: "))
        sum = note + sum
    result = sum / 3
    print(f"Sua média final é { result:.2f}")


# average()

# slices
lista = [10, 2, 5, 44, 6, 8, 68, 4]

# print(lista[:3]) # saída:[10, 2,5]
# print(lista[3:6]) # saída:[44, 6, 8]
# print(lista[2:6:2]) # começa no 2, vai até o 6 e pula de 2 em 2

for item in lista:
    print(item)

for i in range(len(lista)):
    print(lista[i])


def sum(number1, number2=8):
    # valor default de number2 é 8.
    return number1 + number2


print(sum(2))


# dicionários
def students():
    alunos = { "nome": "Laura", "idade": 31, "curso": "Python" }
    
    for chave in alunos:
        print(chave, alunos[chave])


students()
