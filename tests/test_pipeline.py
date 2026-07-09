from src.processamento import limpa_valores_negativos, pega_transacoes_suspeitas

def test_pipeline_basico():
    dados = [{'id': 1, 'valor': 100}, {'id': 2, 'valor': 9000}, {'id': 3, 'valor': -10}]
    
    limpos = limpa_valores_negativos(dados)
    assert len(limpos) == 2
    
    suspeitas = pega_transacoes_suspeitas(limpos, corte=5000)
    assert suspeitas[0]['valor'] == 9000
