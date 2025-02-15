def parse_csv_line(line):
    fields = []
    current_field = []
    is_inside_quotes = False
    
    for char in line:
        if char == '"':
            is_inside_quotes = not is_inside_quotes
        elif char == ';' and not is_inside_quotes:
            fields.append(''.join(current_field))
            current_field = []
        else:
            current_field.append(char)
    
    fields.append(''.join(current_field))  # Último campo
    return fields

def read_and_parse_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    
    parsed_data = []
    accumulated_lines = []

    for raw_line in lines[1:]:  # Ignorar cabeçalho
        accumulated_lines.append(raw_line)
        combined_lines = '\n'.join(accumulated_lines)
        parsed_fields = parse_csv_line(combined_lines)
        
        if len(parsed_fields) == 7:  # Número esperado de campos
            parsed_data.append(parsed_fields)
            accumulated_lines = []
        elif len(parsed_fields) > 7:  # Linha corrompida
            accumulated_lines = []  # Resetar acumulador
    
    return parsed_data

def process_entries(parsed_data):
    composers_list = []
    period_counts = {}
    period_to_titles = {}

    for entry in parsed_data:
        composer = entry[4].strip()
        period = entry[3].strip()
        title = entry[0].strip()

        composers_list.append(composer)
        period_counts[period] = period_counts.get(period, 0) + 1
        period_to_titles.setdefault(period, []).append(title)
    
    return composers_list, period_counts, period_to_titles

def display_results(composers, period_counts, period_titles):
    unique_composers = sorted(set(composers))
    
    print("Lista de compositores ordenada alfabeticamente:")
    print(unique_composers)
    
    print("\nDistribuição das obras por período:")
    print(period_counts)
    
    print("\nDicionário de períodos com títulos ordenados:")
    for period in period_titles:
        period_titles[period].sort()
    print(period_titles)

def main():
    # 1. Ler e processar ficheiro
    parsed_data = read_and_parse_csv('obras.csv')
    
    # 2. Extrair e organizar dados
    composers, period_counts, period_titles = process_entries(parsed_data)
    
    # 3. Mostrar resultados
    display_results(composers, period_counts, period_titles)

if __name__ == "__main__":
    main()