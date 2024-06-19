from lexico import lexer
from sintatico import parser
from semantico import ast_para_latex

# Função para ler conteúdo de um arquivo
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

# Teste com o arquivo exemplo.txt
if __name__ == '__main__':
    data = ler_arquivo('exemplo.txt')

    lexer.input(data)
    ast = parser.parse(data)
    latex = ast_para_latex(ast)

    print(latex)
