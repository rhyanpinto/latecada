import ply.yacc as yacc
from lexico import tokens
from semantico import ast_para_latex

# Regras de produção e análise sintática
class Nodo:
    def __init__(self, tipo, valor=None, filhos=None):
        self.tipo = tipo
        self.valor = valor
        self.filhos = filhos if filhos else []

def p_documento(t):
    '''documento : elementos'''
    t[0] = Nodo('documento', filhos=t[1])
    print("Documento válido")

def p_elementos(t):
    '''elementos : elemento
                 | elemento elementos'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = [t[1]] + t[2]

def p_elemento(t):
    '''elemento : titulo
                | subtitulo
                | paragrafo
                | lista
                | link'''
    t[0] = t[1]

def p_titulo(t):
    '''titulo : SECTION'''
    t[0] = Nodo('titulo', valor=t[1][9:-1])

def p_subtitulo(t):
    '''subtitulo : SUBSECTION'''
    t[0] = Nodo('subtitulo', valor=t[1][12:-1])

def p_paragrafo(t):
    '''paragrafo : conteudo NEWLINE'''
    t[0] = Nodo('paragrafo', filhos=t[1])

def p_conteudo(t):
    '''conteudo : texto
                | texto conteudo'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = [t[1]] + t[2]

def p_texto(t):
    '''texto : TEXT
             | NEGRITO_INI texto NEGRITO_FIM
             | ITALICO_INI texto ITALICO_FIM'''
    if len(t) == 2:
        t[0] = Nodo('texto', valor=t[1])
    else:
        tipo = 'negrito' if t.slice[1].type == 'NEGRITO_INI' else 'italico'
        t[0] = Nodo(tipo, filhos=[Nodo('texto', valor=t[2])])

def p_lista(t):
    '''lista : ITEMIZE itens ENDITEMIZE'''
    t[0] = Nodo('lista', filhos=t[2])

def p_itens(t):
    '''itens : item
             | item itens'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = [t[1]] + t[2]

def p_item(t):
    '''item : ITEM conteudo'''
    t[0] = Nodo('item', filhos=t[2])

def p_link(t):
    '''link : LINK'''
    parts = t[1][6:-7].split(']=')
    t[0] = Nodo('link', valor=parts[1], filhos=[Nodo('url', valor=parts[0])])

def p_error(t):
    print(f"Erro de sintaxe em '{t.value}'")

parser = yacc.yacc()
