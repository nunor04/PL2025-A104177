# TPC1: Somador on/off

## Autor
Nuno Miguel Matos Ribeiro (A104177)

## Enunciado 
Somador on/off: criar o programa em Python

1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto.

2. Sempre que encontrar a string "Off" (em qualquer combinação de maiúsculas e minúsculas), o comportamento de soma é desligado.

3. Sempre que encontrar a string "On" (em qualquer combinação de maiúsculas e minúsculas), o comportamento é novamente ligado.

4. Sempre que encontrar o caractere "=", o resultado da soma é colocado na saída.

## Explicação
Comecei por definir as variáveis essenciais:
- **sum**: acumulador da soma das sequências de dígitos encontradas.
- **text**: onde guardo o conteúdo lido do ficheiro.
- **char_Index**: índice que uso para percorrer o texto caractere a caractere.
- **length**: tamanho total do texto.
- **on_off_Flag**: flag que indica se o comportamento de soma está ligado (`True`) ou desligado (`False`).

Em seguida, verifico se o nome do ficheiro foi passado como argumento na linha de comando. Caso contrário, exibo uma mensagem de erro e termino o programa.

Depois, abro o ficheiro em modo de leitura e guardo todo o seu conteúdo na variável **text**.

No loop principal, processo o texto da seguinte forma:
- **Detecção de "off":**  
  Se os próximos 3 caracteres formarem a string `"off"` (ignorando maiúsculas/minúsculas), desativo o comportamento de soma definindo `on_off_Flag = False` e avanço o índice em 3 posições para ignorar essa palavra.
  
- **Detecção de "on":**  
  Se os próximos 2 caracteres formarem a string `"on"`, voltar a ativar o comportamento definindo `on_off_Flag = True` e avanço o índice em 2 posições para ignorar essa palavra.
  
- **Detecção do caractere "=":**  
  Quando encontro o `"="`, imprimo o valor acumulado em **sum**, avanço o índice e reinicio a flag para `True` (ligado), pronto para processar um novo segmento.
  
- **Processamento de Sequências de Dígitos:**  
  Se o comportamento (on/off) estiver ligado e o caractere atual for um dígito, entro num loop que junta todos os dígitos consecutivos numa string (chamada **num**). Converto essa sequência para inteiro e adiciono ao acumulador **sum**. Se não for dígito ou se o comportamento estiver desligado, simplesmente avanço para o próximo caractere.

Repito esse processo até percorrer todo o texto. Assim, o programa soma os números conforme as regras definidas e imprime o resultado sempre que encontrar um sinal de "=".

## Como Executar
   ```bash
   python3 nome_do_script.py nome_do_ficheiro.txt

