# 📌 PL2025-A104177  

# 📝 Recursivo Descendente para expressões aritméticas

## 👨‍💻 Autor  
Nuno Miguel Matos Ribeiro (A104177) 

## Como funciona
1. **Análise Léxica**: O ficheiro `tokens.py` define os tokens da linguagem, como números, operadores (`+`, `-`, `*`, `/`) e parênteses.
2. **Análise Sintática**: O ficheiro `parser.py` define a gramática para avaliar expressões matemáticas e calcular o seu resultado.
3. **Interação com o utilizador**: O programa lê expressões matemáticas da entrada do utilizador e devolve o resultado.
4. **Saída do programa**: Para sair, podes escrever `exit`, `quit`, `q`, `sair` ou `fechar`.

## Como Executar
Corre o seguinte comando no terminal:
```sh
python parser.py
```
Depois, insere expressões matemáticas como:
```
Escreve uma expressão: 2 + 3 * 4
Resultado: 14
```

Para sair:
```
Escreve uma expressão: exit
```

## Erros
Se introduzires uma expressão inválida, o programa mostrará uma mensagem de erro, como:
```
Erro sintático no input!
```