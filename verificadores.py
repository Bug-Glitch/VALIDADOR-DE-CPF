
def verifica_cpf(entrada):
    """
        PROGRAMA PRINCIPAL QUE CHAMA TODOS OS PARAMETROS

    Este programa testa o CPF de um indivíduo e retorna se é válido ou não

    :param: entrada: um CPF
    :return: se ele é um cpf válido ou não

    Criado por: 🎃 Panic_Halloween 🎃
    """

    cpf = ' '
    primeiro = False #teste do primeiro digito verificador do cpf
    segundo = False #teste do segundo digito verificador do cpf

    try:
        cpf = tratamento_entrada(entrada)
        confere_tamanho_do_cpf(cpf)

        #Armazena os valores
        primeiro = testa(cpf,9,0) #Testa o primeiro digito
        segundo = testa(cpf,10,1) #testa o segundo digito

        #Testa se os valores são verdadeiros
        if primeiro == False or segundo == False: #teste de verdade
            return print("CPF INVÁLIDO")
        else:
            #FINAL DO PROGRAMA SE TUDO CORRER BEM
            cpf = tratamento_saida(cpf)
            return cpf

    except:
        print("ERROR!! TESTE DO CPF FALHOU!")



def tratamento_entrada(um_cpf=''):
    """
    TRATA OS DADOS PARA SE TORNAREM NÚMEROS E SEPARA STRINGS DO CPF

    """
    try:
        nao_pode = [",", ".", "/", "-", " "]
        cpf_inteiro = []
        for numero in um_cpf:
            if numero in nao_pode:
                pass
            else:
                cpf_inteiro.append(int(numero))
        return cpf_inteiro
    except:
        raise ValueError("FALHA NO SEPARADOR DE ENTRADA")

def tratamento_saida(um_cpf):
    """
        Trata o CPF NA SAÍDA
    :param um_cpf: o cpf a ser editado
    :return: o cpf editado para olhos humanos
    """
    cpf_inteiro = " "
    contador_de_tres = 0
    contador_de_vezes = 0

    for numero in um_cpf:
        if contador_de_tres == 3:
            contador_de_tres = 0
            contador_de_vezes += 1
            if contador_de_vezes == 3:
                cpf_inteiro += str("-")
            else:
                cpf_inteiro += str(".")


        cpf_inteiro += str(numero)
        contador_de_tres += 1
    return cpf_inteiro

def confere_tamanho_do_cpf(cpf):
    """
    Confere o tamanho do CPF
    :param cpf: pega o cpf em um formato
    :return: retorna o tamanho dele ou erro
    """
    contador = 0
    for numero in cpf:
        contador += 1

    if contador == 11:
        return True
    else:
        raise ValueError("ERROR!!! CPF DE TAMANHO INVALIDO")

def multiplicacao(cpf='',iniciador=0,parador=''):
    """
        Multiplica os numeros do cpf
    :param cpf: numeros a serem multiplicados
    :param iniciador: aonde se inicia
    :param parador: aonde deve parar
    :return:
    """
    decontador = 10
    lista_multiplicada = []
    if iniciador == 1:
        decontador = 11
    try:

        for numero in cpf:
            if decontador <= 1:
                pass
            elif decontador == 11 and iniciador == 1:
                pass
            else:
                #print(numero,"x",decontador)
                lista_multiplicada.append(numero*decontador)
            decontador -= 1

    except: print("ERROR! NO METODO DE MULTIPLICACAO")
    return lista_multiplicada

def adicao(cpf=''):
    """
        Faz a adição dos numeros do cpf
    :param cpf: numero a ser adicionado
    :return: o valor somado de todos os numeros
    """
    numero_adicionado = 0

    try:
        for numero in cpf:
            numero_adicionado += numero

    except: print("ERROR! NO METODO ADIÇÃO")

    return numero_adicionado

def divisao(numero_total):
    divisor = numero_total % 11

    if divisor == 1:
        divisor = 0
        return divisor
    else:
        return divisor

def verificacao_final(numero):
    """

    :param numero: verifica se no final o cpf ainda tem 11 números
    :return: o valor verificado
    """
    try:
        if numero == 0:
            return numero
        else:
            return 11 - numero
    except: print("ERROR! NO TESTE FINAL")

def testa(cpf='',parametro=0,iniciador=0):
    """
        Faz a gestão e testa o CPF em suas 2 vezes no numero de verificação, chamando os outros metodos
    :param cpf: o cpf a ser testado
    :param parametro: parametro sempre em 0
    :param iniciador: parametro que da o inicio em determinado numero
    :return:
    """
    try:
        numero_real = cpf[parametro]
        verificador = multiplicacao(cpf,iniciador)
        verificador = adicao(verificador)
        verificador = divisao(verificador)
        verificador = verificacao_final(verificador)
        return verificador == numero_real

    except: False

entrada = str('cpf')
variavel = verifica_cpf(entrada)
print(variavel)

