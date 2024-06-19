import ply.yacc as yacc

# Tokens necessários
tokens = (
    'TITULO',
    'PARAGRAFO',
    'LISTA',
    'ITEM',
    'LINK',
    'NEGRITO',
    'ITALICO',
    'URL',
    'TEXTO',
)

# Regras de produção
def p_documento(t):
    '''documento : elementos'''
    print("Documento válido")

def p_elementos(t):
    '''elementos : elemento
                 | elemento elementos'''

def p_elemento(t):
    '''elemento : titulo
                | paragrafo
                | lista
                | link'''

def p_titulo(t):
    '''titulo : TITULO TEXTO TITULO'''

def p_paragrafo(t):
    '''paragrafo : PARAGRAFO conteudo PARAGRAFO'''

def p_conteudo(t):
    '''conteudo : TEXTO
                | TEXTO negrito TEXTO
                | TEXTO italico TEXTO
                | negrito
                | italico'''

def p_negrito(t):
    '''negrito : NEGRITO TEXTO NEGRITO'''

def p_italico(t):
    '''italico : ITALICO TEXTO ITALICO'''

def p_lista(t):
    '''lista : LISTA itens LISTA'''

def p_itens(t):
    '''itens : item
             | item itens'''

def p_item(t):
    '''item : ITEM TEXTO ITEM'''

def p_link(t):
    '''link : LINK TEXTO '</link>'''

def p_error(t):
    print(f"Erro de sintaxe em '{t.value}'")

parser = yacc.yacc()

# Teste
parser.parse(data)
