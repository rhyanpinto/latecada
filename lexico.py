import ply.lex as lex

# Lista de tokens
tokens = (
    'SECTION',
    'SUBSECTION',
    'ITEMIZE',
    'ENDITEMIZE',
    'ITEM',
    'NEGRITO_INI',
    'NEGRITO_FIM',
    'ITALICO_INI',
    'ITALICO_FIM',
    'LINK',
    'TEXT',
    'NEWLINE'
)

# Definições de tokens
t_SECTION = r'\\section\{[^}]*\}'
t_SUBSECTION = r'\\subsection\{[^}]*\}'
t_ITEMIZE = r'\\begin\{itemize\}'
t_ENDITEMIZE = r'\\end\{itemize\}'
t_ITEM = r'\\item'
t_NEGRITO_INI = r'\[negrito\]'
t_NEGRITO_FIM = r'\[/negrito\]'
t_ITALICO_INI = r'\[italico\]'
t_ITALICO_FIM = r'\[/italico\]'
t_LINK = r'\[link=[^\]]*\][^\[]*\[/link\]'
t_ignore = ' \t'

def t_TEXT(t):
    r'[^\\\n]+'
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
