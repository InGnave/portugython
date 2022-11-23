from erros.tipo import ErroDeTipo


__nome__ = __name__

# TODO: Improve error messages


def absoluto(numero):
    """ Retorna o valor absoluto de um número. O argumento pode ser um inteiro, um número de ponto flutuante ou um
    objeto implementando __abs__(). Se o argumento é um número complexo, sua magnitude é retornada. """
    try:
        return abs(numero)
    except TypeError as err:
        print()
        raise

# TODO: aiter not yet implemented


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


# TODO: anext not yet implemented

# TODO: ascii not yet implemented


def binario(inteiro):
    """Converte um número inteiro para uma string de binários prefixada com “0b”. O resultado é uma expressão Python
    válida. Se x não é um objeto Python int, ele tem que definir um método __index__() que devolve um inteiro. """

    try:
        return bin(inteiro)
    except TypeError as err:
        raise
