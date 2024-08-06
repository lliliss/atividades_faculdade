# 1- Escreva uma função que receba uma lista de números e retorne a soma deles.

'''def lista(num):
    soma = sum(num)
    return soma #def foi utilizado para definir uma lista, para quando puxássemos ela, viesse apenas ela para fazer a operação desejada.

num = [4, 8, 6, 0]
resultado = lista(num)
print(resultado)  #valor da saída: 18'''

# 2- Escreva uma função que receba um número e retorne se ele é par ou ímpar.

'''num = int(input("Coloque um valor: ")) #int para aceitar números apenas inteiros, input para você colocar o número que desejar.
if num % 2 == 0: #If e else utilizado pois a lógica seria "se não for um, é o outro". A % é utilizada para encontrar o resto da divisão (módulo), nesse caso, a divisão será por 2
    #pois todo valor par é divisível por 2 e o resto será 0.
    print("O valor inserido é par.")
else:
    print("O valor inserido é ímpar.") #Caso o resultado (resto) da divisão não seja 0, o valor é ímpar.'''

# 3- Escreva uma função que conte o número de vogais em uma string.

'''qnt = str(input("Escreva a palavra desejada: "))
def quantidade_vogais(qnt): #def para puxar apenas a função desejável para realizar operação
    vogais = "aeiouAEIOU" #vogais definidas dentro da função
    contador = 0 #variável que vai ser utilizada para fazer a contagem das vogais da palavra que será escrita, começando em 0.
    for char in qnt: #o for é melhor utilizado pois vai percorrer a string, cada elemento dela.
        #no loop que acontece (por conta do "for"), será buscado caracteres (char) na qnt (variável que definimos) // Vai acontecer uma "busca" entre os caracteres.
        if char in vogais: #o if vai funcionar para calcular a quantidade de caracteres (char) dentro da variável definida como "vogais" para as palavras a ele atribuida, fazendo a contagem
            # das vogais, que se caso tenha, faz a soma de 1 e retorna o contador com a quantidade de vogais encontradas e quebrando loop.
            contador += 1
    return contador
quantidade = quantidade_vogais(qnt)
print(quantidade) '''

# 4- Escreva uma função recursiva para calcular o fatorial de um número.

'''n = int(input("Digite um número para que seja calculado seu fatorial: ")) #n é a variável, que pode ser colocado qualquer valor inteiro para realizar a operação.
def fatorial(n): #atribuição de nome para a funão e colocação da variável a ser chamada.
    if n == 0: #se o valor colocado for igual a 0, retornará 1. Já que, 0! = 1.
        return 1
    else:
        return n * fatorial(n-1) #caso o valor seja diferente de 0, vai retornar o valor que colocamos na variável "n" vezes o valor dela -1, que faz com que a função chame ela mesma
    #para resolução do "problema".
print(fatorial(n)) #apenas para dar o valor que será feito na multiplicação.'''

# 5- Escreva uma função que verifique se uma string é um palíndromo.

'''frase = str(input("Escreva a frase desejada: "))

def palindromo(f):
    return f == f[::-1] #o termo ´f[::-1]´ faz com que a palavra escrita fique ao contrário. EXEMPLO: amor / roma. O f == f[::-1] vai comparar essas duas palavras, para ver se
#quando são alteradas, continuam a mesma coisa (como ANA, por exemplo). Caso seja igual, irá retornar ´true´ e se não for, retornará ´false´.

if palindromo(frase) == True:
    print(f"{frase} é um palíndromo") #aqui, puxamos a função definida como "palíndromo" para puxar a variável "frase" que iremos escrever qualquer palavra, e se caso o valor der "true",
    # (no caso, se ambos forem iguais mesmo invertidos), vai aparecer na tela que a palavra/frase escrita, é um palíndromo.
else:
    print(f"{frase} não é um palíndromo") #caso não seja "True"...'''

# 6- Escreva uma função que ordene uma lista de números em ordem crescente sem usar a função “sort”.

