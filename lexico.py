import ply.lex as lex

# Lista de tokens
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

# Definições de tokens
t_TITULO = r'</?titulo>'
t_PARAGRAFO = r'</?paragrafo>'
t_LISTA = r'</?lista>'
t_ITEM = r'</?item>'
t_NEGRITO = r'</?negrito>'
t_ITALICO = r'</?italico>'
t_LINK = r'<link url="[^"]*">'
t_ignore = ' \t'

def t_URL(t):
    r'url="[^"]*"'
    t.value = t.value[5:-1]  # Remove 'url="' e o último '"'
    return t

def t_TEXTO(t):
    r'[^<>]+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Teste
data = '''
<titulo>Exemplo</titulo>
<paragrafo>Este é um <negrito>parágrafo</negrito> de exemplo.</paragrafo>
<lista>
    <item>Item 1</item>
    <item>Item 2</item>
</lista>
<link url="http://example.com">Link</link>
'''

lexer.input(data)

for tok in lexer:
    print(tok)
