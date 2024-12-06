arvore = [
    "É internacional?",
    [
        "É focado para  criança?",
        [
            "A protagonista é uma menina?", 
            "Título: O mágico de Oz \nAutor: Lyman Frank Baum \nAno: 1900 \nDescrição: \
Uma garota da fazenda do Kansas chamada Doroty e seu cachorro chamado Toto, foram levados, \
por um ciclone, para a Terra de Oz. Para voltar para casa, Doroty e seus companheiros da Terra de Oz \
precisam derrotar a Bruxa Má do Oeste.",
            [
            "Tem elementos filosóficos?",
            "Título: O Pequeno Principe \nAutor: Antonie de Saint-Exupéry \nAno: 1943 \nDescrição: \
A história se baseia nas recordações do narrador, que aos seis anos se lamenta a falta de criatividade dos \
adultos. Devido a esse ocorrido ele desiste da carreira de pintor, e se torna aviador. Durante seu voo, \
o avião falha e acaba chegando no deserto de Saara, lá ele encontra um menino com cabelos de ouro e cachecol \
amarelo. O desenrolar da historia é coberto por ensinamentos atuais, impactando cada pessoa de uma forma diferente",
            "Título: Pinóquio \nAutor: Carlo Collodi \nAno: 1883",
            ]
        ],
        [
            "Foi escrito no século XIX?",
            [
                "O livro se baseia nas questões sociais das mulheres da época?",
                "Título: Orgulho e Preconceito \nAutor: Jane Austen \nAno: 1813",
                "Título: Os Irmãos Karamazov \nAutor: Fiódor Dostoiévski \nAno: 1879 ",
            ],
            "Título: A Revolução dos Bichos \nAutor: George Owell \nAno: 1945",
        ],
    ],
    [
        "Foi escrito por Machado de Assis?",
        "Título: Dom Casmurro \nAutor: Machado de Assis \nAno: 1900",
        [
            "A história envolve questões sociais?",
            ["Se passa no sertão?",
             "Título: Vidas Seca \nAutor: Graciliano Ramos \nAno: 1938",
             "Tírulo: O Cortiço \nAutor: Aluíso Azevedo \nAno: 1890" ,
            ],
            "Título: Triste Fim de Policarpo e Quaresma \nAutor: Lima Barreto \nAno: 1911",
        ]
    ]
]

def navegar(no):
    if isinstance(no, str):
        print("\nLivro encontrado!")
        print(no)
        return
    
    pergunta = no[0]
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    if resposta == "sim":
        navegar(no[1])
    elif resposta == "não":
        navegar(no[2])
    else:
        print("Resposta inválida. Responda 'sim' ou 'não'.")
        navegar(no)

def iniciar():
    print("Olá jogador[a], vamos descobrir sobre livros clássicos, responda essas questões: ")
    navegar(arvore)
iniciar()
