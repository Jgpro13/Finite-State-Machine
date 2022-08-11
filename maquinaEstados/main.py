# Nome : Juliano Gaona Proença
# Criar arquivo diretamente nos Files do repl.it

# Determinar se uma String de entrada faz parte da linguagem L definida por L = x E {a,b} e cada a em x é seguido por pelo menos dois b}

# Receber como entrada três arquivos de texto diferentes contendo várias strings.

# 1 Linha = qntd Strings no arquivo de texto

# Linhas subsequentes = uma string por linha

# Exemplo:
# 3
# abbaba
# abababb
# bbabbaaab

# Como saída deve-se haver uma linha de saída para cada string, nela haverá a string de entrada e o resultado da validação

# Exemplo:
# abbaba: não pertence

# ==================================

# alfabeto permitido
sigma = ['a', 'b', 'c']


# verificando se string possui caracteres do alfabeto
def verifica_string(texto):
    for x in range(0, len(texto)):
        carac = texto[x]

        # estado atual = a (gatilho) e não possui 2 estados possíveis seguintes
        if (carac == sigma[0] and x < len(texto) - 2):

            # verificando os dois próximos estados e verificando se pode haver a transição de estado corretamente
            for i in range(x + 1, x + 3):
                carac = texto[i]
                x = i
                # verificação dos estados seguintes a partir do gatilho
                if texto[i] != sigma[1]:
                    return False

        # Verificando se texto está dentro do alfabeto permitido
        elif carac not in sigma:
            return False

            # retornando verdadeiro, caso nenhuma das condições sejam ocorridas
    return True


def verifica_arquivo():
    # digite o nome do arquivo .txt que deve estar na mesma pasta
    print("Digite o nome do arquivo desejado + .txt")
    abrir = input()

    with open(abrir, 'r') as arquivo:
        linha = arquivo.read()
        textos = linha.split()

        for l in range(1, len(textos)):
            if verifica_string(textos[l]):
                print(textos[l], "Verdadeiro")
            else:
                print(textos[l], "Falso")


verifica_arquivo()

























































