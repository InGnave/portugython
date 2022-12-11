# TODO: Improve error messages
# TODO: Improve importing structure: avoid deep nested import -> from example.a.b import


def absoluto(numero):
    """ Retorna o valor absoluto de um número. O argumento pode ser um inteiro, um número de ponto flutuante ou um
    objeto implementando __abs__(). Se o argumento é um número complexo, sua magnitude é retornada. """
    try:
        return abs(numero)
    except TypeError as err:
        print()
        raise


aiterador = aiter


def todos(iteravel):
    """ Retorna True se todos os elementos de iterable são verdadeiros (ou se iterable estiver vazio)."""
    try:
        return all(iteravel)
    except TypeError as e:
        raise TypeError(f'Erro de tipo. Objeto "{type(iteravel).__name__}" não é iterável')


def qualquer(iteravel):
    """
    Retorna True se algum elemento de iterable for verdadeiro. Se iterable estiver vazio, retorna False.
    :return:
    """
    try:
        return any(iteravel)
    except TypeError:
        raise



aproximo = anext

valor_ascii = ascii


def binario(inteiro):
    """Converte um número inteiro para uma string de binários prefixada com “0b”. O resultado é uma expressão Python
    válida. Se x não é um objeto Python int, ele tem que definir um método __index__() que devolve um inteiro. """

    try:
        return bin(inteiro)
    except TypeError as err:
        raise



ponto_de_parada = breakpoint


chamavel = callable
unicode = chr

compilar = compile
direito_autoral = copyright
creditos = credits
deletar_atributo = delattr
propriedades = dir
divisao_resto = divmod
avaliar = eval
executar = exec

sair = exit

formatar = format
obter_atributo = getattr
variaveis_globais = globals


tem_atributo = hasattr

valor_hash = hash
ajuda = help
hexadecimal = hex
identificador = id

entrada = input
isinstancia = isinstance
isumasubclasse = issubclass

iterador = iter

comprimento = len

licenca = license
variaveis_locais = locals
mapear = map


maior = max
menor = min
proximo = next


octal = oct

def abra(arquivo, modo=None, buffering=None, encoding=None, errors=None, newline=None, closefd=True):
    modos = {
        'leitura': 'r',
        'escrita': 'w',
        'exclusivo': 'x',
        'anexo': 'a',
        'binario': 'b',
        'text': 't',
    }
    return open(file=arquivo, mode=modos.get(modo, 'r'), encoding=encoding)


valor_unicode = ord

elevado = potencia = pow
imprima = print
parar = quit

representacao = repr 

invertido = reversed
arredonde = round
definaatributo = setattr
arrumado = sorted
some = sum

mostrar_dicionario = vars

junte = zip
