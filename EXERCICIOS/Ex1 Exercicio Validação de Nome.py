def validar_nome(nome):
    # Um nome vazio não é válido
    if len(nome) == 0:
        return False, "Nome inválido: o nome não pode estar vazio."
 
    espaco_anterior = True  # Começa como True para validar a 1ª letra
 
    for i in range(len(nome)):
        c = nome[i]
        codigo = ord(c)
 
        # Verificar se é espaço
        if c == " ":
            espaco_anterior = True
            continue
 
        # Verificar se é letra (maiúscula: 65-90, minúscula: 97-122)
        e_maiuscula = 65 <= codigo <= 90
        e_minuscula = 97 <= codigo <= 122
 
        if not e_maiuscula and not e_minuscula:
            # Não é letra nem espaço → inválido
            return False, f"Nome inválido: contém caracteres não permitidos."
 
        # Se vem a seguir a um espaço (ou é o primeiro caractere),
        # tem de ser maiúscula
        if espaco_anterior:
            if not e_maiuscula:
                return False, f"Nome inválido: contém caracteres não permitidos."
            espaco_anterior = False
        else:
            # No meio de uma palavra tem de ser minúscula
            if not e_minuscula:
                return False, f"Nome inválido: contém caracteres não permitidos."
 
    return True, "Nome válido!"
 
 
 
nome = input("Introduz o teu nome completo: ")
valido, mensagem = validar_nome(nome)
print(mensagem)