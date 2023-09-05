class Cell:
    def __init__(self, letra, multiplicador=1, tipo_multiplicador=None):
        self.letra = letra
        self.multiplicador = multiplicador
        self.tipo_multiplicador = tipo_multiplicador

def calcular_valor_palabra(celdas):
    valor_total = 0
    multiplicador_palabra = 1

    for celda in celdas:
        valor_letra = celda.letra.valor
        if celda.tipo_multiplicador == 'letra':
            valor_letra *= celda.multiplicador
        elif celda.tipo_multiplicador == 'palabra':
            multiplicador_palabra *= celda.multiplicador

        valor_total += valor_letra

    return valor_total * multiplicador_palabra