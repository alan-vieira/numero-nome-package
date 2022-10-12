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
