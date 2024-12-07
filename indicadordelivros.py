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
            "Título: Pinóquio \nAutor: Carlo Collodi \nAno: 1883 \nDescrição: \
Um boneco de madeira chamado Pinóquio, construído pelo mestre Gepeto, é desobediente e durante suas aventuras\
 precisa aprender a reconhecer o certo e o errado, perceber que cada uma de suas encrencas \
 poderiam ter sido evitadas se não mentisse descaradamente. A história de Pinoquio está repleta de \
ensinamentos, reflexões e pura magia. No meio de tudo isso, será que ele conseguirá realizar seu maior \
sonho?",
            ]
        ],
        [
            "Foi escrito no século XIX?",
            [
                "O livro se baseia nas questões sociais das mulheres da época?",
                "Título: Orgulho e Preconceito \nAutor: Jane Austen \nAno: 1813 \nDescrição: \
A protagonista Elizabeth Bennet, aprende que não é sensato julgar uma pessoa pela primeria impressão \
mesmo que seja um homem que no primeiro momento aparenta ser arrogante e orgulhoso, mas isso não define \
quais são seus objeticvos ou como ela é verdadeiramente. Ao longo da história Elizabeth aprende que é \
possível mudar a opnião que uma impressão formada pode ser modificada.",

                "Título: Os Irmãos Karamazov \nAutor: Fiódor Dostoiévski \nAno: 1879 \nDescrição: \
Aventure-se em um dos maiores romances russos, conta a história de uma família conturbada  em \
uma cidade na Rússia. O patriarca da familia, considerado um palhaço devasso, Fiódor Pavlovitvh Karamazov, seu \
o primogênito e libertino, Dmitri, o do meio intelectual, Ivan, e o mais e puro, Aliocha. Cheia de \
desavenças e intrigas, entre o primogênito e o patriarca, a narrativa tras questões que são totalmente \
afastadas dos ideiais cristãos.",
            ],
            "Título: A Revolução dos Bichos \nAutor: George Owell \nAno: 1945 \nDescrição: \
Uma fábula sobre poder, narra a vivencia dos animais de uma fazenda, na qual fizeram uma relução \
contra os humanos, a fim de poderem prosperar sem serem oprimidos. No entanto, o que parecia ser uma \
grande ideia, torna-se uma tirania ainda mais opressiva que a dos humanos. ",
        ],
    ],
    [
        "Foi escrito por Machado de Assis?",
        "Título: Dom Casmurro \nAutor: Machado de Assis \nAno: 1900 \nDescrição: \
Bento Santiagonarra, durante sua velhice, a sua história e de seu casamento com Capitu, \
sua amiga de infância. A história passa por momentos em que o protagnonista precisava tomar uma \
decisão, mas no fim, quando conseguiu o que queria, sua vida passa a gerar desconfiança naquela \
em que mais amava.",
        [
            "A história envolve questões sociais?",
            ["Se passa no sertão?",
             "Título: Vidas Secas \nAutor: Graciliano Ramos \nAno: 1938 \nDescrição: \
Uma família, que viviam no nordeste, foram obrigado a se desllocar de tempos em tempos para \
areas castigadas pela seca. O pai, Fabiano, Sinha Vitória e os dois filhos que não têm nome \
filho mais velho e filho mais nova, são acompanhados pela cachorra Baleia.",
             "Tírulo: O Cortiço \nAutor: Aluíso Azevedo \nAno: 1890 \nDescrição: \
Em uma habitaçãõ coleteiva na capital do Segundo Império, ambição e exploração se misturam. \
 De um lado, a burguesia gananciosa e interesseira, disposta a tudo para enriquecer e subir na \
vida. De outro, personagens estereotipados, cheios de vícios e patologias, comparados a animais e \
movidos pelo instinto e pela fome.",
            ],
            "Título: Triste Fim de Policarpo e Quaresma \nAutor: Lima Barreto \nAno: 1911 \nDescrição: \
Um anti-herói quixotesco, imbuído de nobres ideais, alguns beirando ao tresloucado (tanto é que passa uma temporada no hospício). \
Bom coração, idealista, patriota, por causa de suas qualidades acaba sendo castigado e sempre se dá mal.",
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
