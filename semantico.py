from nodo import Nodo

# Função para transformar a árvore de sintaxe abstrata em LaTeX
def ast_para_latex(nodo):
    if nodo is None:
        return ''
    if nodo.tipo == 'documento':
        return ''.join(ast_para_latex(filho) for filho in nodo.filhos)
    elif nodo.tipo == 'titulo':
        return f'\\section{{{nodo.valor}}}\n'
    elif nodo.tipo == 'subtitulo':
        return f'\\subsection{{{nodo.valor}}}\n'
    elif nodo.tipo == 'paragrafo':
        return f'{"".join(ast_para_latex(filho) for filho in nodo.filhos)}\n\n'
    elif nodo.tipo in ['negrito', 'italico']:
        estilo = 'textbf' if nodo.tipo == 'negrito' else 'textit'
        return f'\\{estilo}{{{"".join(ast_para_latex(filho) for filho in nodo.filhos)}}}'
    elif nodo.tipo == 'lista':
        return f'\\begin{{itemize}}\n{" ".join(ast_para_latex(filho) for filho in nodo.filhos)}\\end{{itemize}}\n'
    elif nodo.tipo == 'item':
        return f'\\item {"".join(ast_para_latex(filho) for filho in nodo.filhos)}\n'
    elif nodo.tipo == 'link':
        url = nodo.filhos[0].valor
        return f'\\href{{{url}}}{{{nodo.valor}}}'
    elif nodo.tipo == 'texto':
        return nodo.valor
    elif nodo.tipo == 'newline':
        return '\n'
    elif nodo.tipo == 'end':
        return f'\\end{{{nodo.valor}}}'
    elif nodo.tipo == 'begin':
        return f'\\begin{{{nodo.valor}}}'
    elif nodo.tipo == 'ref':
        return f'\\ref{{{nodo.valor}}}'
    elif nodo.tipo == 'frac':
        numerador = ast_para_latex(nodo.filhos[0])
        denominador = ast_para_latex(nodo.filhos[1])
        return f'\\frac{{{numerador}}}{{{denominador}}}'
    else:
        return ''

# Teste com o arquivo exemplo.txt
def teste():
    from sintatico import parser
    with open('exemplo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
    resultado = parser.parse(conteudo)
    print(ast_para_latex(resultado))

# Teste da função
teste()
