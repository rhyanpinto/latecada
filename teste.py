import ply.lex as lex
import ply.yacc as yacc

lexer = lex.lex()
parser = yacc.yacc()

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
ast = parser.parse(data)
print(ast)