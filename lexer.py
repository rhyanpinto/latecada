import ply.lex as lex

# Lista de tokens
tokens = (
    'SECTION', 'TEXTBF', 'EMPH', 'BEGIN_ITEMIZE', 'END_ITEMIZE',
    'ITEM', 'PLAINTEXT', 'RBRACE'
)

# Definição de expressões regulares para os tokens
t_SECTION = r'\\section\{'
t_TEXTBF = r'\\textbf\{'
t_EMPH = r'\\emph\{'
t_BEGIN_ITEMIZE = r'\\begin\{itemize\}\n?'
t_END_ITEMIZE = r'\\end\{itemize\}'
t_ITEM = r'\\item'
t_ignore = ' \t'

# Definição para o token PLAINTEXT
def t_PLAINTEXT(t):
    r'[^\n\{\}\\]+'
    return t

# Definição para capturar "}"
def t_RBRACE(t):
    r'\}'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore_SPACE = r'[\s]+'

# Função para tratar erros léxicos
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

__all__ = ['tokens', 'lexer']