import ply.lex as lex
from tokens import tokens

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
t_END = r'\\end'
t_BEGIN = r'\\begin'
t_REF = r'\\ref'
t_FRAC = r'\\frac'
t_CITE = r'\\cite'
t_LABEL = r'\\label'
t_BIBITEM = r'\\bibitem'
t_BF = r'\\bf'
t_RIGHT = r'\\right'
t_LEFT = r'\\left'
t_RM = r'\\rm'
t_ALPHA = r'\\alpha'
t_MU = r'\\mu'
t_NEWCOMMAND = r'\\newcommand'
t_DEF = r'\\def'
t_ignore = ' \t'

def t_ENVIRONMENT(t):
    r'\{[^}]+\}'
    t.value = t.value[1:-1]  # Remove the curly braces
    return t

def t_TEXTO(t):
    r'[^\\{}]+'
    return t

def t_DELIMITER(t):
    r'[\(\)\[\]\{\}]|\.'
    return t

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