from itertools import product

# Dicionário com as letras associadas a cada dígito
digit_to_letters = {
    '1': ['A', 'B', 'C'],
    '2': ['D', 'E', 'F'],
    '3': ['G', 'H', 'I'],
    '4': ['J', 'K', 'L'],
    '5': ['M', 'N', 'O'],
    '6': ['P', 'Q', 'R'],
    '7': ['T', 'U', 'V'],
    '8': ['W', 'X', 'Y'],
    # Adicione mais dígitos e letras conforme necessário
}

# Número de telefone de 7 dígitos
phone_number = '1234567'

# Função para gerar todas as combinações possíveis para uma lista de letras
def generate_combinations(letters_list, length):
    return [''.join(c) for c in product(letters_list, repeat=length)]

# Total de combinações possíveis
total_combinations = 1
output=[]
possibilidade=pow(len(phone_number),3)

for i in range (possibilidade):
    for j 
    

print(f"Total de combinações possíveis: {len(combinations)}")
print(combinations)