def limpa_valores_negativos(transacoes: list) -> list:
    # List comprehension: mantemos apenas valores positivos
    return [t for t in transacoes if t['valor'] > 0]

def pega_transacoes_suspeitas(transacoes: list, corte: float) -> list:
    # List comprehension: filtramos pelo valor de corte
    return [t for t in transacoes if t['valor'] > corte]