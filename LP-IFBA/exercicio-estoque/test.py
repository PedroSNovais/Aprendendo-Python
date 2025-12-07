from utils import salvar_estoque, carregar_estoque

estoque = carregar_estoque('estoque.json')
estoque.update({"salada":10})
salvar_estoque( estoque, 'estoque.json')