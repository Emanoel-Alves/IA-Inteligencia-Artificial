# Lista: Estrutura sequencial
# Exercicio 1
def exibirSeq():
    tam = int(input("Digite o tamanho da sequencia: "))
    sequencia = [0] * tam
    i = 0

    while i < tam :
        sequencia[i] = int(input("Digite um numero da sequencia: "))
        i +=1
    
    print("A sequencia inversa e: ")
    i = tam - 1
    while i >= 0:
        print(sequencia[i])
        i -=1

# Exercicio 2
def repeticoes():
    tam = int(input("Digite o tamanho da sequencia: "))
    sequencia = []
    i = 0

    while i < tam :
        elem = int(input("Digite um numero da sequencia: "))
        
        if elem not in sequencia:
            sequencia.append(elem)
        i +=1

    print("A sequencia sem repetições é: ", sequencia)

# Exerxcicio 3
def seqOrdenada():
    m = int(input("Digite um tamanho para m: "))
    n = int(input("Digite um tamanho para n: "))
    cont1 = cont2 = 0   
    sequen1 = []
    sequen2 = [] 
    seqOrden = []

    while cont1 < m:
        sequen1.append(int(input("Digite um numero da sequencia m em ordem: ")))
        cont1 +=1

    while cont2 < n:
        sequen2.append(int(input("Digite um numero da sequencia n em ordem: ")))
        cont2 +=1    

    cont1 = 0
    cont2 = 0
    while cont1 < m and cont2 < n:
        if sequen1[cont1] <= sequen2[cont2]:
            seqOrden.append(sequen1[cont1])
            cont1 +=1
        else:
            seqOrden.append(sequen2[cont2])
            cont2 +=1

    while cont1 < m:
        seqOrden.append(sequen1[cont1])
        cont1 +=1 
    
    while cont2 < n:
        seqOrden.append(sequen2[cont2])
        cont2 +=1 
    
    print(seqOrden)

# Exercicio 4 - Incompleta
def buscaSeq():
    n = int(input("Digite um numero n: "))
    lista = []
    i = 0

    while i < n:
        lista.append(int(input("Digite um numreo da sequencia: ")))
        i +=1

    i = 0
    max = 0
    soma_str = ""

    while i < n:
        if max < lista[i]:
            max = lista[i]
        i +=1
    aux_i = 0
    aux_j = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            aux_i = i
            aux_j = j
            aux = 0

            while aux_i <= aux_j:
                aux += lista[aux_i]
                aux_i += 1

            if max < aux:
                max = aux
                soma_str = somaString(i, j, lista)
            j += 1
        i += 1

    print("A soma maxima de um segmento e: ", soma_str, " = ", max)

# Funcoes com lista - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Exercicio 1
def pertence(item, lista):
    for elem in lista:
        if item == elem:
            return True
    return False

def verificarPertence():
    lista  = [1, "oi", 3.14, 7, True]

    if pertence("oi",lista):
        print("Passou no primeiro teste! :-)")
    else:
        print("Nao passou no primeiro teste! :-(")

    if pertence(True,lista):
        print("Passou no segundo teste! :-)")
    else:
        print("Nao passou no segundo teste! :-(")

    if not pertence(False,lista):
        print("Passou no terceiro teste! :-)")
    else:
        print("Nao passou no terceiro teste! :-(")

# Exercicio 2
def exibir():
    n = int(input("Digite um numero n: "))
    lista = []
    i = 0
    list_aux = []

    while i < n:
        lista.append(int(input("Digite um numreo da sequencia: ")))
        i +=1
    
    i = 0
    while i < len(lista):
        if not pertence(lista[i], list_aux):
            list_aux.append(lista[i])
        i += 1
    
    print(list_aux)
        
# Exercicio 3
def indice(item, lista):
    i = 0

    while i < len(lista):
        if item == lista[i]:
            return i
        i += 1
    return None

def buscarIndice():
    lista  = [1, "oi", 3.14, 7, True]
    
    if indice("oi",lista) == 1:
        print("Passou no primeiro teste! :-)")
    else:
        print("Nao passou no primeiro teste! :-(")

    if indice(True,lista) == 4:
        print("Passou no segundo teste! :-)")
    else:
        print("Nao passou no segundo teste! :-(")

    if indice(False,lista) == None:
        print("Passou no terceiro teste! :-)")
    else:
        print("Nao passou no terceiro teste! :-(")

# Exercicio 4
def contIndice():
    n = int(input("Digite um numero n: "))
    lista = []
    i = 0
    list_aux = []

    while i < n:
        lista.append(int(input("Digite um numreo da sequencia: ")))
        i +=1
    
    i = 0
    while i < n:
        if not pertence(lista[i], list_aux):
            print(lista[i], " aparece ", qtd(lista[i], lista) ," vezes")
        list_aux.append(lista[i])
        i +=1

def qtd(item, lista):
    cont = 0
    i = 0

    while i < len(lista):
        if item == lista[i]:
            cont +=1
        i += 1
    
    return cont

# Exercicio 5
def soma_elementos(ini, fim, lista):
    if ini >= 0 and fim <= len(lista):
        i = 0
        soma = 0
        while ini <= fim:
            soma += lista[ini]
            ini += 1
        return soma

def soma():
    lista  = [1, 2, 3, 4, 5]

    if soma_elementos(1,3,lista) == 9:
        print("Passou no primeiro teste! :-)")
    else:
        print("Nao passou no primeiro teste! :-(")

# Exercicio 6
def segmento():
    n = int(input("Digite um numero n: "))
    lista = []
    i = 0

    while i < n:
        lista.append(int(input("Digite um numreo da sequencia: ")))
        i +=1

    i = 0
    max = 0
    soma_str = ""

    while i < n:
        if max < lista[i]:
            max = lista[i]
        i +=1

    i = 0
    
    while i < n:
        j = i + 1
        while j < n:
            aux = soma_elementos(i, j, lista)
            if max < aux:
                max = aux
                soma_str = somaString(i, j, lista)
            j += 1
        i += 1

    print("A soma maxima de um segmento e: ", soma_str, " = ", max)

def somaString(ini, fim, lista):
    if ini >= 0 and fim <= len(lista):
        aux = lista[ini]
        soma_str = "" + str(aux)
        ini += 1

        while ini <= fim:
            aux = lista[ini]
            soma_str += " + " + str(aux)
            ini += 1

        return soma_str

if __name__== '__main__':
    buscaSeq()
