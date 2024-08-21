# encoding: utf-8

from lexer import lexer
from parser import parser, output

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    lexer.input(data)
    result = parser.parse(data)

    if result:
        print("Arquivo em gerado:\n")
        print("\n".join(output))

        output_file = 'output.txt'
        with open(output_file, 'w') as out:
            out.write("\n".join(output))
        print(f"\nArquivo salvo como {output_file}.")
    else:
        print("Erro na análise sintática.")

# Processa o arquivo de exemplo
process_file('data.tex')
