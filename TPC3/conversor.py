import re
import sys

def convertToHTML(lines):
    html = []
    currentList = False  # Flag para ver se estamos dentro de uma lista
    headerMatch = re.compile(r'^#+')
    boldMatch = re.compile(r'\*\*(.*?)\*\*(.*?)')
    italicMatch = re.compile(r'\*(.*?)\*(.*?)')
    listMatch = re.compile(r'^(\d+)\.\s\.*')
    linkMatch = re.compile(r'(.*?)\[(.*?)\]\((.*?)\)') # texto [nome da pagina](url)
    imageMatch = re.compile(r'(.*?)!\[(.*?)\]\((.*?)\)(.*?)') # texto [nome da imagem](url)


    for line in lines:
        line = line.strip()  # Remove espaços em branco no início e no fim da linha incluindo \n

        if currentList and not listMatch.match(line):
            html.append('</ol>')
            currentList = False

        if headerMatch.match(line):
            headerSize = line.count('#')
            line = f'<h{headerSize}>{line.strip("# ").strip()}</h{headerSize}>'

        elif listMatch.match(line):
            currentList = True
            if listMatch.match(line).group(1) == '1':
                html.append('<ol>')
            line = f'<li>{line.strip("123456789. ").strip()}</li>' #strip remove os numeros e o ponto

        line = boldMatch.sub(r'<b>\1</b>\2', line)
        line = italicMatch.sub(r'<i>\1</i>\2', line)
        line = linkMatch.sub(r'\1<a href="\3">\2</a>', line) #\3 é o url e \2 é o nome da pagina \1 é o texto
        line = imageMatch.sub(r'\1<img src="\3" alt="\2"/>\4', line) #\3 é o url e \2 é o nome da imagem \1 é o texto

        html.append(line)

    if currentList:
        html.append('</ol>')  # no caso em que o MD acaba com uma lista

    return "\n".join(html)

if __name__ == "__main__":
    MDFile = sys.argv[1]
    HTMLFile = sys.argv[2]
    with open(MDFile, 'r') as f:
        lines = f.readlines()
    with open(HTMLFile, 'w') as f:
        f.write(convertToHTML(lines))