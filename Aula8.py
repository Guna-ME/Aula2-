# Sintaxe de uma função em python;
def inicio():
    print("Minha primeira função!")

inicio()

# Parâmetro definido;
def passandoparametro(nome):
    print("Meu nome é", nome)

passandoparametro("Maria Eduarda")

# Parâmetro indefinifo;
def parametroindefinido(*nome):
    print("Nomes para gatas: ", nome[0], nome[1], nome[2])

parametroindefinido("Branca,", "Eva,", "Kitara.")

# Parâmetro definido com chave;
def passandoparametrochave(nome,idade,cpf):
    print("Meu nome é", nome, idade, cpf)

passandoparametrochave(nome="Maria Eduarda",idade="16",cpf="103217339")

# Parâmetro indefinifo com chave;
def indefinidocomchave(**dados):
    print("Informações pessoais", dados["idade"], dados["nome"], dados["cpf"])

indefinidocomchave(nome="Maduh", idade="16", cpf="103217339")

# Valor padrão;
def passandoparametrocompadrao(nome="sem nome"):
    print("Bem-vindo, ", nome)

passandoparametrocompadrao("Maduh")
passandoparametrocompadrao()

# Lista por parâmetro;
def passandolista(lista):
    for i in lista:
        print(i)

minhalista = ["Branca", "Eva", "Kitara"]

passandolista(minhalista)

def funcaovazia():
    pass

# Função com retorno;
def retornavalor(nome):
    if nome == "Maduh":
        return True
    else:
        return False
recebeRetorno = retornavalor("Branca de Neve")
if recebeRetorno == True:
    print("É tois ")
else:
    print("Nois não!")