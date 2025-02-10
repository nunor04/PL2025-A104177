import sys

def main():
    sum = 0
    if len(sys.argv) < 2:
        print("Comando inválido.")
        sys.exit(1)
    
    nome_ficheiro = sys.argv[1]

    # Abre o ficheiro em modo de leitura
    with open(nome_ficheiro, 'r') as f:
        text = f.read()

    char_Index = 0
    length = len(text)  
    on_off_Flag = True # False = off, True = on

    while char_Index < length:
        currentChar = text[char_Index]
        # Em caso de 'off'
        if char_Index + 2 < length and currentChar.lower() == 'o' and text[char_Index + 1].lower() == 'f' and text[char_Index + 2].lower() == 'f':
            on_off_Flag = False
            char_Index += 3 # Skip 'off'
        # Em caso de 'on'
        elif char_Index + 1 < length and currentChar.lower() == 'o' and text[char_Index + 1].lower() == 'n':
            on_off_Flag = True
            char_Index += 2 # Skip 'on'
        elif currentChar == '=':
            print(sum)
            char_Index += 1
            on_off_Flag = True # Reinicio a flag
        else:
            if on_off_Flag:
                # Se o primeiro caratere for um dígito, junto a sequencia inteira
                if text[char_Index].isdigit():
                    num = ""
                    # Enquanto o próximo caractere for um dígito, junto à sequencia inteira
                    while char_Index < length and text[char_Index].isdigit():
                        num += text[char_Index]
                        char_Index += 1
                    sum += int(num)
                # Avança se não for um dígito
                else:
                    char_Index += 1
            # Avança se a flag estiver em 'off'
            else:
                char_Index += 1
        if char_Index >= length:
            break

if __name__ == "__main__":
    main()