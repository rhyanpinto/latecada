from sintatico import Nodo

# Função para transformar a árvore de sintaxe abstrata em LaTeX
def ast_para_latex(nodo):
    if nodo.tipo == 'documento':
        return ''.join(ast_para_latex(filho) for filho in nodo.filhos)
    elif nodo.tipo == 'titulo':
        return f'\\section{{{nodo.valor}}}\n'
    elif nodo.tipo == 'subtitulo':
        return f'\\subsection{{{nodo.valor}}}\n'
    elif nodo.tipo == 'paragrafo':
        return f'{"".join(ast_para_latex(filho) for filho in nodo.filhos)}\n\n'
    elif nodo.tipo in ['negrito', 'italico']:
        return f'{{{"".join(ast_para_latex(filho) for filho in nodo.filhos)}}}'
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
