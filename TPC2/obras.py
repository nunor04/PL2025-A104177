def agrupar_obras(conteudo, campos_por_obra):
    elementos = conteudo.split(";")
    obras = []
    # Cria uma lista de listas com os dados do ficheiro agrupados por obras
    for i in range(0, len(elementos), campos_por_obra):
        obra = []
        for j in range(campos_por_obra):
            if j == campos_por_obra - 1:
                elementos[j] = elementos[j].split(' ')[0]
            obra.append(elementos[i+j])
        obras.append(obra)
    return obras

def main():
    # nome;desc;anoCriacao;periodo;compositor;duracao;_id
    f = open("obras.csv", "r")
    f.readline() # Ignora a primeira linha
    conteudo = f.read().replace("\n", " ")
    campos_por_obra = 7 
    obras = agrupar_obras(conteudo, campos_por_obra)
    print(obras)
    f.close()
    

if __name__ == "__main__":
    main()