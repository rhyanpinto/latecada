import ply.yacc as yacc
from lexer import tokens

# Lista de tokens necessária para o yacc (parser)
tokens = tokens

# Variável para armazenar a tradução final
output = []

def p_document(p):
    '''document : section text itemize
                | section text
                | section itemize
                | section'''
    # Concatena as partes e gera a saída final
    p[0] = "\n".join(part for part in p[1:] if part)
    output.append(p[0])

def p_section(p):
    '''section : SECTION text RBRACE'''
    p[0] = f"Secao: {p[2]}"

def p_text(p):
    '''text : text text_part
            | text_part'''
    if len(p) == 3:
        p[0] = f"{p[1]} {p[2]}"
    else:
        p[0] = p[1]

def p_text_part(p):
    '''text_part : TEXTBF text RBRACE
                 | EMPH text RBRACE
                 | PLAINTEXT'''
    if len(p) == 4:
        if p[1] == '\\textbf{':
            p[0] = f"Texto em negrito: {p[2]}"
        elif p[1] == '\\emph{':
            p[0] = f"Texto italico: {p[2]}"
    else:
        p[0] = p[1]

def p_itemize(p):
    '''itemize : BEGIN_ITEMIZE item_list END_ITEMIZE'''
    p[0] = f"Inicio da lista:\n{p[2]}\nFim da lista:"

def p_item_list(p):
    '''item_list : item item_list
                | item'''
    if len(p) == 3:
        p[0] = f"{p[1]}\n{p[2]}"
    else:
        p[0] = p[1]

def p_item(p):
    '''item : ITEM text'''
    p[0] = f"Item da lista: {p[2]}"

# Regra de erro
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final da entrada")


# Construir o parser
parser = yacc.yacc()

__all__ = ['parser', 'output']