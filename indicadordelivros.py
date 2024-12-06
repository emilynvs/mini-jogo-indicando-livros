livros_internacionais = [
    {'titulo': 'O mágico de Oz', 'autor': 'Lyman Frank Baum', 'ano': 1900},
    {'titulo': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry', 'ano': 1943},
    {'titulo': 'Pinóquio', 'autor': 'Carlo Collodi', 'ano': 1883},
    {'titulo': 'Orgulho e Preconceito', 'autor': 'Jane Austen', 'ano': 1813},
    {'titulo': 'Os Irmãos Karamazov', 'autor': 'Fiódor Dostoiévski', 'ano': 1879},
    {'titulo': 'A revolução dos bichos', 'autor': 'George Owell', 'ano': 1945},
    {'titulo': 'Alice no país das maravilhas', 'autor': 'Lewis Carroll', 'ano': 1865}
]

livros_nacionais = [
    {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis', 'ano': 1900},
    {'titulo': 'Memórias póstumas de Brás Cubas', 'autor': 'Machado de Assis', 'ano': 1881},
    {'titulo': 'O Cortiço', 'autor': ' Aluísio Azevedo', 'ano': 1890},
    {'titulo': 'Triste Fim de Policarpo Quaresma', 'autor': 'Lima Barretoo', 'ano': 1911},
    {'titulo': 'O Sítio do Pica-pau Amarelo ', 'autor': 'Monteiro Lobato', 'ano': 1920},
    {'titulo': 'Vidas Secas', 'autor': 'Graciliano Ramos', 'ano': 1938},
    {'titulo': 'Os Sertões ', 'autor': 'Euclides da Cunha', 'ano': 1902}
]
def exibir(livro):
    print(f"\nTítulo: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Ano: {livro['ano']}")
    

def perguntas(pergunta):
    return input(pergunta).lower().strip()

print("Jogo dos livros clássicos")

res = perguntas("nacional ou internacional? (nacional/internacional)")
if res == 'internacional':
    res = perguntas("Tem elementos de moralidade voltada para crianças?(sim/não)")
    if res == 'sim':
        res = perguntas("O protagonista é criança? (sim/não)")
        if res == 'sim':
            res = perguntas("A protagonista é uma menina? ")
            if res == 'sim':
                livro1 = livros_internacionais[0]
                exibir(livro1)
                livro2 = livros_internacionais[6]
                exibir(livro2)
            else:
                livro1 = livros_internacionais[1]
                exibir(livro1)
        elif res == 'não':
            livro1 = livros_internacionais[2]
            exibir(livro1)
        
elif res == "nacional":
    ...
else:
    print("Opção invalida")
