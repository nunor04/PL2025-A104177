# 📌 PL2025-A104177  

# 📝 Analisador Léxico para Linguagem de Consulta (SPARQL-like)  

## 👨‍💻 Autor  

Nuno Miguel Matos Ribeiro (A104177)  

# 📌 Enunciado  

O objetivo deste trabalho é desenvolver, em Python, um analisador léxico para uma linguagem de consulta inspirada no SPARQL. O programa deve ler um ficheiro contendo uma consulta e produzir uma sequência de tokens que representam os diferentes elementos da linguagem.  

# 🔍 Elementos Reconhecidos  

## ✅ Palavras-chave  

Reconhece palavras reservadas como `select`, `where` e `LIMIT`.  

**Exemplo:**  
**In:** `select ?nome ?desc where { ... } LIMIT 1000`  
**Out:** `('KW_SELECT', 'select'), ('KW_WHERE', 'where'), ('KW_LIMIT', 'LIMIT')`  

## ✅ Variáveis  

Identificadores que começam com `?`, como `?nome` e `?desc`.  

**Exemplo:**  
**In:** `?nome`  
**Out:** `('VAR', '?nome')`  

## ✅ Prefixos  

Reconhece prefixos conhecidos como `dbo:` e `foaf:`.  

**Exemplo:**  
**In:** `dbo:MusicalArtist`  
**Out:** `('PREFIX', 'dbo:'), ('ID', 'MusicalArtist')`  

## ✅ Identificadores  

Palavras genéricas como `a`, `MusicalArtist`, `name`, `artist` e `abstract`.  

**Exemplo:**  
**In:** `a`  
**Out:** `('ID', 'a')`  

## ✅ Strings  

Trechos de texto entre aspas, com possível marcação de idioma (por exemplo, `"Chuck Berry"@en`).  

**Exemplo:**  
**In:** `"Chuck Berry"@en`  
**Out:** `('STRING', 'Chuck Berry"@en')`  

## ✅ Números  

Sequências de dígitos que são convertidas para inteiros.  

**Exemplo:**  
**In:** `1000`  
**Out:** `('NUM', 1000)`  

## ✅ Operadores e Delimitadores  

Símbolos como `{`, `}`, `.` e `:`.  

**Exemplo:**  
**In:** `{`  
**Out:** `('OP', '{')`  

## ✅ Comentários  

Linhas iniciadas por `#` devem ser aceites mas ignoradas na saída final.  

**Exemplo:**  
**In:** `# Isto é um comentário`  
**Out:** `(Comentário é reconhecido mas filtrado e não aparece na sequência de tokens)`  

# ⚙️ Explicação  

O analisador léxico foi implementado utilizando expressões regulares (`regex`) para identificar e classificar os diferentes elementos do código de entrada.  

# 🔧 Como Funciona?  

## 1️⃣ Definição dos Tokens  

Uma lista de especificações (`token_specification`) define os padrões de `regex` para cada tipo de token (palavras-chave, variáveis, prefixos, identificadores, strings, números, operadores, comentários e espaços em branco).  

## 2️⃣ Processamento do Código  

O programa usa `re.finditer()` para percorrer o código e combinar cada parte com os padrões definidos. Cada correspondência gera um token representado por uma tupla contendo o tipo do token e o seu valor.  

## 3️⃣ Filtragem  

Espaços em branco e comentários são filtrados para não aparecerem na saída, permitindo uma análise mais limpa do conteúdo relevante.  

# 🚀 Como Executar?  

Para utilizar o analisador léxico, execute o seguinte comando no terminal:  

```sh
python3 tpc.py < query.txt
```

## 📂 Parâmetros  

- `query.txt` → Ficheiro que contém a consulta a ser analisada.  
- `tpc.py` → Script Python que contém o código do analisador léxico.  

# 🎯 Exemplo de Uso  

Suponha que o ficheiro `query.txt` contenha o seguinte:  

```sparql
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

Após executar:  

```sh
python3 tpc.py < query.txt
```

O programa deverá produzir a seguinte sequência de tokens:  

```plaintext
('KW_SELECT', 'select')
('VAR', '?nome')
('VAR', '?desc')
('KW_WHERE', 'where')
('OP', '{')
('VAR', '?s')
('ID', 'a')
('PREFIX', 'dbo:')
('ID', 'MusicalArtist')
('OP', '.')
('VAR', '?s')
('PREFIX', 'foaf:')
('ID', 'name')
('STRING', 'Chuck Berry"@en')
('OP', '.')
('VAR', '?w')
('PREFIX', 'dbo:')
('ID', 'artist')
('VAR', '?s')
('OP', '.')
('VAR', '?w')
('PREFIX', 'foaf:')
('ID', 'name')
('VAR', '?nome')
('OP', '.')
('VAR', '?w')
('PREFIX', 'dbo:')
('ID', 'abstract')
('VAR', '?desc')
('OP', '}')
('KW_LIMIT', 'LIMIT')
('NUM', 1000)
```

# 📌 Nota  

O comentário presente na entrada (`# DBPedia: obras de Chuck Berry`) é reconhecido, mas não aparece na lista final de tokens, pois foi filtrado durante a análise.  