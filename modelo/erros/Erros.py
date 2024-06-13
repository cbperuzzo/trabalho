class InsufficientStockError(Exception):
    def __init__(self, stock: int):
        super().__init__(f'Estoque insuficiente: {stock} produto(s) disponíveis')

class ProductNotFoundError(Exception):
    def __init__(self, product_id: int):
        super().__init__(f'Produto com id {product_id} não encontrado')