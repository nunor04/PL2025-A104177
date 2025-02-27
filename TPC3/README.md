# PL2025-A104177

# Conversor Markdown para HTML

## Autor

***Nuno Miguel Matos Ribeiro (A104177)***

## Enunciado
O objetivo deste trabalho é desenvolver, em Python, um conversor simples de Markdown para HTML. O programa deve ler um ficheiro em Markdown (.md) e produzir um ficheiro HTML (.html) correspondente, convertendo os seguintes elementos, conforme especificado na "Basic Syntax" da Cheat Sheet:

- **Cabeçalhos**: Linhas iniciadas por `#`, `##` ou `###` devem ser convertidas em `<h1>`, `<h2>` ou `<h3>`, respetivamente.  
  **Exemplo:**  
  - **In:** `# Exemplo`  
  - **Out:** `<h1>Exemplo</h1>`

- **Texto em Negrito**: Pedaços de texto entre `**` devem ser convertidos para `<b>...</b>`.  
  **Exemplo:**  
  - **In:** `Este é um **exemplo** ...`  
  - **Out:** `Este é um <b>exemplo</b> ...`

- **Texto em Itálico**: Pedaços de texto entre `*` devem ser convertidos para `<i>...</i>`.  
  **Exemplo:**  
  - **In:** `Este é um *exemplo* ...`  
  - **Out:** `Este é um <i>exemplo</i> ...`

- **Lista Numerada**: Linhas que iniciam com números seguidos de ponto (por exemplo, `1.`, `2.`, etc.) devem ser agrupadas dentro de uma lista ordenada `<ol>`, com cada item envolvido por `<li>...</li>`.  
  **Exemplo:**  
  - **In:**
    ```
    1. Primeiro item
    2. Segundo item
    3. Terceiro item
    ```
  - **Out:**
    ```html
    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>
    ```

- **Link**: O padrão `[texto](URL)` deve ser convertido para `<a href="URL">texto</a>`.  
  **Exemplo:**  
  - **In:** `Como pode ser consultado em [página da UC](http://www.uc.pt)`  
  - **Out:** `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

- **Imagem**: O padrão `![texto alternativo](URL)` deve ser convertido para `<img src="URL" alt="texto alternativo"/>`.  
  **Exemplo:**  
  - **In:** `Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)`  
  - **Out:** `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>`

## Explicação
O conversor foi implementado utilizando expressões regulares (regex) para identificar e substituir os padrões do Markdown pelos correspondentes em HTML. A função principal `convertToHTML(lines)` realiza as seguintes operações:

- **Cabeçalhos:** Verifica se a linha inicia com um ou mais `#` e, a partir da contagem, determina o nível do cabeçalho (`<h1>`, `<h2>`, `<h3>`, etc.).
- **Listas Numeradas:** Detecta itens de lista que iniciam com números e agrupa-os entre as tags `<ol>` e `</ol>`, convertendo cada item em `<li>...</li>`.
- **Negrito e Itálico:** Utiliza regex (função sub) para substituir os delimitadores `**` e `*` pelos elementos `<b>` e `<i>`, respectivamente.
- **Links e Imagens:** Identifica os padrões de links e imagens e os converte nas tags HTML correspondentes, preservando o texto e a URL.

## Como Executar

Para utilizar o conversor, execute o seguinte comando no terminal:

```bash
python3 nome_do_script.py ficheiro_entrada.md ficheiro_saida.html
```
    ficheiro_entrada.md: Caminho para o ficheiro de entrada escrito em Markdown.
    ficheiro_saida.html: Caminho para o ficheiro de saída que conterá o HTML gerado.

Exemplo de Uso

Suponha que o ficheiro exemplo.md contenha o seguinte:

```md
# Cabeçalho Principal

Este é um **exemplo** de *Markdown*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Consulte [a página da UC](http://www.uc.pt) para mais informações.

Veja a imagem: ![imagem dum coelho](http://www.coellho.com)
```
Após executar:

```bash
python3 nome_do_script.py exemplo.md exemplo.html
```

O ficheiro exemplo.html gerado terá o seguinte conteúdo:

```html
<h1>Cabeçalho Principal</h1>

Este é um <b>exemplo</b> de <i>Markdown</i>.

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>

Consulte <a href="http://www.uc.pt">a página da UC</a> para mais informações.

Veja a imagem: <img src="http://www.coellho.com" alt="imagem dum coelho"/>
```