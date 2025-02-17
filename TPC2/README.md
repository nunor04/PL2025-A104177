# PL2025-A104177

## **Autor**

***Nuno Miguel Matos Ribeiro (A104177)***

## **Enunciado**

O objetivo deste trabalho é processar um dataset de obras musicais sem utilizar o módulo CSV do Python. O programa deve:

1. Ler o dataset e extrair as informações corretamente.
2. Gerar uma lista ordenada alfabeticamente dos compositores musicais.
3. Contar quantas obras pertencem a cada período musical.
4. Criar um dicionário onde cada período está associado a uma lista alfabética dos títulos das obras desse período.

## **Explicação**

Para cumprir os requisitos do trabalho, o programa foi dividido em várias funções:

### 📌 **Leitura e parsing do CSV**

Uma vez que o uso do módulo `csv` é proibido, foi criada a função `parse_csv_line(line)`, que processa uma linha do ficheiro CSV manualmente. Esta função leva em conta a presença de aspas (`"`) que podem envolver campos contendo o caractere `;`. Assim, os valores são extraídos corretamente sem divisão indevida.

A função `read_and_parse_csv(file_path)` lê o ficheiro linha a linha, acumulando-as quando necessário para lidar com possíveis quebras incorretas dentro de campos entre aspas. O resultado é uma lista de listas, onde cada sublista contém os campos corretamente extraídos de uma linha do CSV.

### 📌 **Processamento das entradas**

A função `process_entries(parsed_data)` percorre os dados extraídos, extraindo três elementos principais:

- **Lista de compositores**: todos os compositores mencionados no dataset.
- **Distribuição das obras por período**: um dicionário onde as chaves são períodos musicais e os valores são contagens das obras associadas a cada período.
- **Dicionário de períodos com títulos ordenados**: cada período musical é associado a uma lista alfabética dos títulos das suas obras.

### 📌 **Exibição dos resultados**

A função `display_results(composers, period_counts, period_titles)` apresenta os dados de forma organizada:

- **Lista de compositores** ordenada alfabeticamente.
- **Distribuição das obras** por período musical.
- **Dicionário de períodos com títulos ordenados alfabeticamente**.


## **Como Executar**

```bash
python3 nome_do_script.py
```

O programa lê automaticamente o ficheiro `obras.csv` e apresenta os resultados no terminal.

