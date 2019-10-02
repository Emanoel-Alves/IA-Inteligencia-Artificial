# Variáveis, expressões e funções de entrada e saída

# Exercicio 1
def temperaturaCelsius():
    celsius = float(input("Digite a temperatura: "))
    fahrenheit = (celsius * 1.8) + 32
    print("A conversão de Celsius para Fahrenheit é igual a: ", fahrenheit, "ºF")

# Exercício 2
def temperaturaFahrenheit():
    fahrenheit= float(input("Digite a temperatura: "))
    celsius = (fahrenheit - 32) * 5/9
    print("A conversão de Fahrenheit para Celsius é igual a: ", celsius, "ºC")


# Expressões lógicas e operadores relacionais

# Exercicio 1
def anoBissexto():
    ano = int(input("Digite o ano: "))
    if (ano % 4) == 0:
        if (ano % 100) == 0:
            if (ano % 400) == 0:
                print("bissexto")
            else:
                print("Nao bissexto")
        else:
            print("Bissexto")
    else:
        print("Nao bissexto")

# Exercício 2
def almaGemea():
    nome = "Penny"
    sexo = "feminino"
    altura = 167
    peso   =  52
    idade  =  25
    cabelo = "loiro"
    escolaridade = "medio"

    compativel = sexo == 'feminino' and (altura >= 155 and altura <= 170) and (peso >= 45 and peso <= 65)
    compativel = compativel and (idade >= 25 and idade <= 35)  and (cabelo == "loiro") and (escolaridade != "phd")
    
    if compativel == True:
        compativel = "Compatível"
    else:
        compativel = "Não compatível"

    print("Candidata", nome, ":", compativel)

# Comando de repetição: while
# Exercicio 1
def seqNumeros():
    soma = 0
    valor = 1  

    while valor != 0:
        valor  = int(input("Digite o valor: "))
        soma  = soma + valor
    
    print("A soma dos numeros e: ", soma)

# Exercico 2
def potencia():
    n = int(input("Digite um numero n: "))
    k = int(input("Digite um numero k: "))
    mult = 1
    
    while k > 0:
        mult = mult * n
        k = k - 1

    print("A potencia de n elevado a k: ", mult)

# Exercicio 3
def fatorial():
    n = int(input("Digite um numero n: "))
    nfatorial = 1

    while n > 0:
        nfatorial = nfatorial * n
        n = n - 1
    
    print("O fatorial de n e: ", nfatorial)

# Exercicio 4
def sequencia():
    n = int(input("Digite um numero n maior que 0: "))
    i = int(input("Digite um numero i maior que 0: "))
    j = int(input("Digite um numero j maior que 0: "))
    x = 0

    while n >= x:
        if (x % i == 0) or (x % j == 0):
            print(x)
        x = x + 1 

# Exercicio 5
def mdc():
    n = int(input("Digite n: "))
    m = int(input("Digite m: "))

    ant = n
    b = m

    r = b % ant
    while r != 0:
        r = ant % b
        ant = b
        b = r

    print("MDC(%d,%d) = %d" %(n,m,ant))      


# Execução condicional e alternativas: if, if-else e if-elif-else
# Exercicio 1
def somaPares():
    n = int(input("Digite o total de numeros maior que 0: "))
    soma = 0
    i = n
    
    while i > 0:
        valor = int(input("Digite um numero: "))
        i = i - 1
        if valor % 2 == 0:
            soma = soma + valor
    
    print("A soma dos numeros é: ", soma)

# Exercicio 2
def qtd():
    n = int(input("Digite o total de numeros maior que 0: "))
    qtdPar = 0
    qtdImpar = 0
    i = n
    
    while i > 0:
        valor = int(input("Digite um numero: "))
        i = i - 1
        if valor % 2 == 0:
            qtdPar = qtdPar + 1
        else:
            qtdImpar = qtdImpar + 1
    
    print("Quanitade de numeros pares e ", qtdPar, " e impares e ", qtdImpar)

# Exercicio 3
def verifica():
    n = int(input("Digite o valor de n (n > 0): "))
    d = int(input("Digite o valor de d (0<=d<=9): "))

    qtd = 0
    numero = n

    while n > 0:
        digito = n % 10
        n = n // 10
        if digito == d:
            qtd = qtd + 1

    print("O numero ", d, "aparece ", qtd, " em ", numero)

# Exercicio 4
def numTriangular():
    n = int(input("Digite um numero para verificar: "))
    i = j = k = 1

    while i <= 9:
        while j <= 9:
            while k <= 9:
                if i * j * k == n:
                    print(i, " * ", j, " * ", k, " = ", n)
                    return
                k = k + 1
            j = j + 1
            k = 1
        i = i + 1
        j = k = 1
    
    print("O numero nao e triangular")

# Exercicio 5
def teoremaPiragoras():
    a = int(input("Digite um numero: "))
    b = int(input("Digite um numero: "))
    c = int(input("Digite um numero: "))    

    ladoA = a * a
    ladoB = b * b
    ladoC = c * c

    if ladoA > 0 and ladoB > 0 and ladoC > 0:
        if ladoA == ladoB + ladoC or ladoB == ladoA + ladoC or ladoC == ladoA + ladoB:
            print("Os numeros ", (a, b, c), " formam um triangulo reto")
        else:
            print("Nao e um trinagulo reto")

# Exercicio 6
def maior():
    a = int(input("Digite um numero: "))
    b = int(input("Digite um numero: "))
    c = int(input("Digite um numero: ")) 

    if a <= b and a <= c:
        if b <= c: 
            print(a, b, c)
        else:
            print(a, c, b)
    elif b <= a and b <= c: 
        if a <= c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        if a <= b: 
            print(c, a, b)
        else:
            print(c, b, a)

if __name__=='__main__':
    mdc()