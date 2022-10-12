def nome():
    '''
    - Solicita a entrada do nome completo a ser analizado;
    - Transforma o nome em um vetor de letras maiusculas.
    '''
    # entrada do nome completo
    print("Digite o nome completo:")
    # tranformação do nome em um vetor de letras
    nome = input().replace(" ", "").upper()

    return list(nome)

def letra_valor():
    '''
    Gera um dicionário que contém as letras maiusculas do alfabeto, com os seus 
    devidos valores (de acordo com as regras da numerologia).
    '''
    # lista das letras
    letra_list = list(map(lambda letra: chr(letra), range(ord("A"), ord("Z")+1)))

    # criação do dicionário com o valor das letras
    letra_dict = {}

    for letra in letra_list:
        if letra >= 'A' and letra <= 'I':
            letra_dict[letra] = letra_list.index(letra)+1

        elif letra >= 'J' and letra <= 'R':
            letra_dict[letra] = (letra_list.index(letra)+1) - 9

        elif letra >= 'S' and letra <= 'Z':
            letra_dict[letra] = (letra_list.index(letra)+1) - 18

    return letra_dict

def vetor_numero():
    '''
    - Gera um vetor numérico com o valor das letras do nome;
    - Soma os valores do vetor;
    - Reduz o valor da soma até um digito. Com exceção dos numeros
    11, 22 e 33.
    '''
    # criação do vetor numérico relacionando ao vetor do nome
    num = list(map(lambda l: letra_valor()[l], nome()))
    num_soma = str(sum(num))

    # redução do valor
    num_redu = 0
    for n in num_soma:
        num_redu += int(n)

        if num_redu > 9:
            if num_redu == 11 or num_redu == 22 or num_redu == 33:
                break
            else:
                num_redu = num_redu % 10 + num_redu // 10

    return num_redu
