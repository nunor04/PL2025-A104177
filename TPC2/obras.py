def separar_campos(conteudo):
    campos = []
    campo_atual = []
    dentro_de_aspas = False # Flag para indicar se estamos dentro de aspas (vai alternando conforme encontramos aspas)
    i = 0

    while i < len(conteudo):
        char = conteudo[i]

        if char == '"':
            dentro_de_aspas = not dentro_de_aspas
        elif char == ';' and not dentro_de_aspas:
            # Se não estiver dentro de aspas, é uma separação de campo
            campos.append("".join(campo_atual).strip())
            campo_atual = []
        else:
            campo_atual.append(char)
        
        i += 1
    
    # Adiciona o último campo à lista
    if campo_atual:
        campos.append("".join(campo_atual).strip())

    return campos


def agrupar_obras(conteudo, campos_por_obra):
    elementos = separar_campos(conteudo)  # Usa a função que separa corretamente os campos
    obras = []

    for i in range(0, len(elementos), campos_por_obra):
        if i + campos_por_obra > len(elementos):  # Evita IndexError
            print("Erro: número de campos por obra inválido.")  

        obra = [elementos[i + j].strip() for j in range(campos_por_obra)]
        obra[-1] = obra[-1].split(' ')[0]  # Ajusta o último campo (ID)
        obras.append(obra)

    return obras

def lista_compositores(obras):
    compositores = {obra[4] for obra in obras}  # Usa um set para evitar duplicados
    return sorted(compositores)  # Retorna os compositores ordenados


def main():
    # nome;desc;anoCriacao;periodo;compositor;duracao;_id
    with open("obras.csv", "r") as f:
        f.readline()  # Ignora o cabeçalho
        conteudo = f.read()
    
    campos_por_obra = 7
    obras = agrupar_obras(conteudo, campos_por_obra)

    if not obras:
        print("Erro: Nenhuma obra válida foi encontrada.")
        return
    
    compositoresOrdenados = lista_compositores(obras)

    for obra in obras:
        print(obra)
    

if __name__ == "__main__":
    main()