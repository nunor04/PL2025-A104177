def main():
    counter = 0
    line = input()
    char_Index = 0
    while line != "":
        if(line[char_Index] == 'e' and line[char_Index + 1 : 2]):
            break
        currentChar = line[char_Index]
        if chr(currentChar) >= 31 and chr(currentChar) <= 39: 
            counter += currentChar
    


if __name__ == "__main__":
    main()