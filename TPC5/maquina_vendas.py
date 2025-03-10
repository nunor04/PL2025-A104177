import json
import re
import os
from datetime import date

# Nome do ficheiro que armazena o stock
STOCK_FILE = "stock.json"

# Carregar o stock a partir do ficheiro JSON (ou iniciar com lista vazia se o ficheiro não existir)
if os.path.exists(STOCK_FILE):
    with open(STOCK_FILE, "r", encoding="utf-8") as f:
        stock = json.load(f)
else:
    stock = []  # Stock vazio

saldo = 0  # saldo em cêntimos

def listar_stock():
    print("maq:")
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for item in stock:
        print(f"{item['cod']} {item['nome']} {item['quant']} {item['preco']}")

def parse_coin(coin):
    """
    Converte uma moeda em string (ex.: "1e" ou "20c") para cêntimos.
    """
    coin = coin.strip()
    if coin.endswith('e'):
        try:
            value = int(coin[:-1])
        except ValueError:
            value = 0
        return value * 100
    elif coin.endswith('c'):
        try:
            value = int(coin[:-1])
        except ValueError:
            value = 0
        return value
    else:
        return 0

def inserir_moeda(cmd):
    """
    Processa o comando MOEDA, extraindo as moedas e retornando o total inserido (em cêntimos).
    Exemplo de comando: MOEDA 1e, 20c, 50c, 5c .
    """
    # Remover a palavra chave e o ponto final
    coins_str = cmd[6:].strip()
    if coins_str.endswith('.'):
        coins_str = coins_str[:-1]
    # Separar por vírgulas
    coins = [x.strip() for x in coins_str.split(',')]
    total = 0
    for coin in coins:
        total += parse_coin(coin)
    return total

def find_product(cod):
    for item in stock:
        if item['cod'] == cod:
            return item
    return None

def process_selecionar(cod, saldo):
    """
    Processa a seleção de um produto:
     - Verifica se o produto existe e se há stock.
     - Se houver saldo suficiente, decrementa a quantidade e atualiza o saldo.
    """
    product = find_product(cod)
    if not product:
        print(f"maq: Produto com código {cod} não encontrado.")
        return saldo
    if product['quant'] <= 0:
        print(f"maq: Produto {product['nome']} esgotado.")
        return saldo
    preco_cents = int(round(product['preco'] * 100))
    if saldo < preco_cents:
        print("maq: Saldo insuficiente para satisfazer o seu pedido")
        print(f"maq: Saldo = {saldo}c; Pedido = {preco_cents}c")
        return saldo
    # Efetuar a venda: diminuir o stock e subtrair o preço do saldo
    product['quant'] -= 1
    saldo -= preco_cents
    print(f"maq: Pode retirar o produto dispensado \"{product['nome']}\"")
    print(f"maq: Saldo = {saldo}c")
    return saldo

def calcular_troco(saldo):
    """
    Calcula o troco a devolver utilizando as moedas disponíveis.
    As moedas consideradas são: 200, 100, 50, 20, 10, 5, 2 e 1 cêntimos.
    """
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    troco = {}
    for moeda in moedas:
        count = saldo // moeda
        if count:
            troco[moeda] = count
            saldo %= moeda
    return troco

def process_adicionar(cmd):
    """
    Comando extra para adicionar ou atualizar produtos no stock.
    Exemplo de comando:
        ADICIONAR A23 "água 0.5L" 5 0.7
    """
    pattern = r'ADICIONAR\s+(\S+)\s+"([^"]+)"\s+(\d+)\s+([\d.]+)'
    match = re.search(pattern, cmd, re.IGNORECASE)
    if match:
        cod, nome, quant, preco = match.groups()
        quant = int(quant)
        preco = float(preco)
        product = find_product(cod)
        if product:
            product['quant'] += quant
            product['preco'] = preco  # atualiza também o preço
            print(f"maq: Produto {nome} atualizado, nova quantidade: {product['quant']}")
        else:
            stock.append({"cod": cod, "nome": nome, "quant": quant, "preco": preco})
            print(f"maq: Produto {nome} adicionado com sucesso.")
    else:
        print("maq: Comando ADICIONAR inválido. Exemplo: ADICIONAR A23 \"água 0.5L\" 5 0.7")

# Mensagem de início
print(f"maq: {date.today()}, Stock carregado, Estado atualizado.")
print("maq: Bom dia. Estou disponível para atender o seu pedido.")

# Loop principal para receber comandos
while True:
    try:
        command = input(">> ").strip()
    except EOFError:
        break  # encerra se houver fim de entrada

    if command.upper() == "LISTAR":
        listar_stock()

    elif command.upper().startswith("MOEDA"):
        added = inserir_moeda(command)
        saldo += added
        # Exibe o saldo no formato "1e30c" (exemplo: 130 cêntimos = 1e30c)
        euros = saldo // 100
        cents = saldo % 100
        print(f"maq: Saldo = {euros}e{cents}c")

    elif command.upper().startswith("SELECIONAR"):
        parts = command.split()
        if len(parts) >= 2:
            cod = parts[1]
            saldo = process_selecionar(cod, saldo)
        else:
            print("maq: Comando SELECIONAR inválido. Exemplo: SELECIONAR A23")

    elif command.upper().startswith("ADICIONAR"):
        process_adicionar(command)

    elif command.upper() == "SAIR":
        if saldo > 0:
            troco = calcular_troco(saldo)
            troco_str = ", ".join([f"{count}x {coin}c" for coin, count in troco.items()])
            print(f"maq: Pode retirar o troco: {troco_str}.")
        print("maq: Até à próxima")
        # Grava o stock atualizado no ficheiro JSON antes de terminar
        with open(STOCK_FILE, "w", encoding="utf-8") as f:
            json.dump(stock, f, ensure_ascii=False, indent=4)
        break

    else:
        print("maq: Comando não reconhecido. Tente novamente.")
