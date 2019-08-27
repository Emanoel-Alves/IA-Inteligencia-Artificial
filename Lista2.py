import math
# Indicadores de passagem
#Exercicio 1
def seqPar():
    n = int(input("Digite o valor de n (n > 1): "))
    i = 1   

    par = True

    while i < n and par:
        x = int(input("Digite um número da sequência: "))
        if x % 2 != 0:
            par = False
        i = i + 1

    if par:
        print("A sequencia é par")
    else:
        print("A sequencia nao é par")

# Exercicio 2
def primo():
    n = int(input("Digite o valor de n (n > 1): "))
    primo = True
    d = 2

    if n <= 1:
	    primo = False

    while primo == True and d <= n / 2:
        if n % d  == 0:
            primo = False
        d = d + 1
    
    if (primo == True):
        print(n,"é primo")
    else:
        print(n,"não é primo")

# Exercicio 3
def adjacentes():
    aux = n = int(input("Digite um numero: "))

    anterior = n % 10
    n = n // 10
    adjIguais = False
    i = 0

    while n > 0 and not adjIguais:
        atual = n % 10
        if atual == anterior:
            adjIguais = True
            break
        else:
            i += 1
        anterior = atual
        n = n // 10

    if adjIguais:
        print(aux, "tem dois digitos", atual, "adjacentes")
    else:
        print(aux, "nao tem digitos iguais adjacentes")

# Exercicio 4 
def pa():
    n = int(input("Digite o valor de n (n > 0): "))
    proAritmetica = False

    if n > 2:
        atual = int(input("Digite um número da sequência: "))
        prox = int(input("Digite um número da sequência: "))

        razaoAtual = prox - atual
        atual = prox
        proAritmetica = True
        
        i = 1

        while i < n - 1 and proAritmetica:
            prox = int(input("Digite um número da sequência: "))
            razaoProx = prox - atual

            if razaoAtual == razaoProx:
                proAritmetica = True
                atual = prox
                i+=1
            else:
                proAritmetica = False
                break

    if proAritmetica or n == 2:
        print("A sequencia é uma progressão Aritmetica")
    else:
        print("A sequencia nao é uma progressão Aritmetica")

# Repetições encaixadas
# Exercicio 1
def mutiplicidade():
    
    primo = False
    n = int(input("Digite um numero n (n > 1): "))
    p = 2

    while (n > 1):
            q = 0
            while (n % p == 0):
                q = q + 1
                n = n / p
            
            if (q > 0):
                print("fator", p, "com multiplicidade", q)
                primo = False
                while (not primo):
                    p = p + 1
                    div = 2
                    primo = True
                    while (div <= p / 2 and primo):
                        if (p % div == 0):
                            primo = False
                        else:
                            div = div + 1
                
# Exercicio 2
def seqMdc():
    n = int(input("Digite n: "))
    numSeq = int(input("Digite um numero da sequencia: "))
    

    while n - 1 > 0:
       
        num = int(input("Digite um número da sequencia: "))
        maxDiv = 1

        while maxDiv <= numSeq and maxDiv <= num:
            if (numSeq % maxDiv == 0) and (num % maxDiv == 0):
                mdc = maxDiv

            maxDiv += 1

        numSeq = mdc
       
        n -=1

    print(numSeq)      

# Exercicio 3
def fatSeq():
    n = int(input("Digite um numero n: "))

    while n > 0:
        num = int(input("Digite um numero da sequencia: "))
        fatorial = 1

        while num > 0:
            fatorial = fatorial * num
            num -= 1

        print("O fatorial de ", num,"e: ", fatorial)
        n -= 1

# Exercicio 4
def contPrimos():
    aux = num = int(input("Digite um numero da sequencia ou 0 para terminar: "))
    sequencia = str(aux)
    totalPrimos = 0 
    
    while num != 0:
        
        ehPrimo = True
        i = 2

        while i < num and ehPrimo:
            if num % i == 0:    
                ehPrimo = False   
            i += 1

        if ehPrimo:
            totalPrimos += 1

        num = int(input("Digite um numero da sequencia ou 0 para terminar: "))
        numStr = num
        sequencia += " " + str(numStr) 

    print ("A sequencia", sequencia," tem ", totalPrimos," numeros primos")

# Exercicio 5
def imparesCon():
    m = int(input("Digite um numero m ( > 1) : "))
    inicio = 1
    n = 1

    while n <= m:
        soma = ""
        inicioStr = inicio
        soma += str(inicioStr)

        i = 1
        while i < n:
            aux = inicio + 2* i
            soma += " + " + str(aux)
            i += 1
        print(n, "**", "3", " = ", soma)  
        inicio = inicio + 2 * n
       
        n += 1

# Exercicio 6
def tabuada():
    n = int(input("Digite um numero n ( > 0) : "))

    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print(i," * ", j, " = ", i * j)
            j += 1
        print()
        i += 1

#Numeros reais
# Exercicio 1
def serieHar():
    n = int(input("Digite um numero n: "))

    h = 0
    i = 1

    while i <= n:
        h += 1/i
        i += 1 
    
    print("Soma da direita para a esquerda: ", h)
    
    h = 0
    i = n
    while i >= 1:
        h += 1/i
        i -= 1 

    print("Soma da esquerda para direita: ", h)

# Exercicio 2
def cos():
    x = float(input("Digite um numero x para cos(x): "))
    n = int(input("Digite um numero n para a serie: "))
    funCos = 1.0
    i = 1

    while i <= n:

        fatorial = j = 2 * i
        
        while j > 0:
            fatorial = fatorial * j
            j -= 1

        funCos += -((math.pow(x,2*i))/fatorial)
        i += 1 
    
    print("cos(x) = ", funCos)
# Exercicio 3
# Não deu tempo

# Eexercicio 4
def desenho():
    x = float(input("Digite um numero x: "))
    y = float(input("Digite um numero y: "))

    dentro = True

    if -3 <= x <=  3 and 1 <= y <= 2:
        dentro = False

    elif x <= -5 or 5 <= x or y <= 0 or 8 <= y:
        dentro = False

    elif  1 <= x <=  4 and 4 <= y <= 7:
        dentro = False
        if  2 < x <  3 and 5 < y < 6:
            dentro = True

    elif -4 <= x <= -1 and 4 <= y <= 7:
        dentro = False
        if -3 < x < -2 and 5 < y < 6:
            dentro = True

    if dentro:
        print("As coordenadas estaão dentro da região")
    else:
        print("As coordenadas estão fora da região ")

# Exercicio 5
def aproximacao():
    x = float(input("Digite um numero x: "))
    e = float(input("Digite um numero epsilon: "))

    f = 1.0 + x
    i = 2

    while f > e:

        fatorial = j = i
        
        while j > 0:
            fatorial = fatorial * j
            j -= 1

        f += ((math.pow(x,i))/fatorial)
        i += 1 
    
    print("e^x = ", f)

# Exercicio 6
# Nao deu tempo

# Funções
# Exercicio 1
# m!/((m-n)!n!)
def combinacao():
    m = int(input("Digite um numero m: "))
    n = int(input("Digite um numero n:"))
    
    comb = fatorial(m)/(fatorial(m - n) * fatorial(n))

    print("A combinação de m e n e: ", comb)

# Exercicio 2
def fatorial(num):
    
    fatorial = 1

    while num > 0:
        fatorial = fatorial * num
        num -= 1
    
    return fatorial

# Exercicio 3
def combinacao2(m, n):
    
    return fatorial(m)/(fatorial(m - n) * fatorial(n))


if __name__=='__main__':
    combinacao()