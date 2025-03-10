# 📌 PL2025-A104177  

# 📝 Máquina de Vendas Automática

## 👨‍💻 Autor  
Nuno Miguel Matos Ribeiro (A104177) 

## 💡 Descrição
Este projeto implementa uma máquina de vendas automática em Python, permitindo listar produtos, inserir moedas, selecionar produtos e calcular troco.

## ⚙️ Funcionalidades  
- Listar os produtos disponíveis no stock.
- Inserir moedas para somar saldo.
- Selecionar um produto e verificar a sua disponibilidade.
- Atualizar automaticamente o stock após a compra.
- Calcular e devolver troco ao sair.
- Adicionar novos produtos ou atualizar existentes.
- Gravar e carregar o stock de um ficheiro JSON.

## 🪙 Moedas Aceites
O sistema aceita as seguintes moedas:
- `1e` (1 euro = 100 cêntimos)
- `2e` (2 euros = 200 cêntimos)
- `50c`, `20c`, `10c`, `5c`, `2c`, `1c` (cêntimos)

## 💻 Como Executar
1. Certifica-te de que tens Python instalado.
2. Guarda o ficheiro como `maquina_vendas.py`.
3. Corre o programa no terminal:

```sh
python3 maquina_vendas.py
```

## 📂 Formato do Stock
O stock é armazenado num ficheiro JSON (`stock.json`) e segue o seguinte formato:

```json
[
    {"cod": "A23", "nome": "água 0.5L", "quant": 5, "preco": 0.7},
    {"cod": "B12", "nome": "sumo 33cl", "quant": 3, "preco": 1.2}
]
```

## ✅ Comandos Disponíveis

- `LISTAR` → Lista todos os produtos no stock.
- `MOEDA 1e, 50c, 20c.` → Insere moedas no saldo.
- `SELECIONAR <Código>` → Escolhe um produto pelo seu código.
- `ADICIONAR <Código> "<Nome>" <Quantidade> <Preço>` → Adiciona ou atualiza um produto.
- `SAIR` → Encerra o programa e devolve o troco.

## 📈 Exemplo de Uso

**Entrada:**
```sh
MOEDA 1e, 50c.
SELECIONAR A23
SAIR
```

**Saída:**
```plaintext
maq: Saldo = 1e50c
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 80c
maq: Pode retirar o troco: 1x 50c, 1x 20c, 1x 10c.
maq: Até à próxima
```

## 💡 Notas
- O programa grava automaticamente o stock ao sair.
- Produtos esgotados ou saldo insuficiente impedem a compra.
- A formatação do saldo é feita no formato `xe yc` (exemplo: `1e30c` para 130 cêntimos).

