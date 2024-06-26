# Product Errors

class InsufficientStockError(Exception):
    def __init__(self, stock: int):
        super().__init__(f'Estoque insuficiente: {stock} produto(s) disponíveis')

class ProductNotFoundError(Exception):
    def __init__(self):
        super().__init__(f'Produto não encontrado')

class CategoryNotFoundError(Exception):
    def __init__(self, category: str):
        super().__init__(f'Categoria "{category}" não encontrada')

class ModelNotFoundError(Exception):
    def __init__(self, model: str):
        super().__init__(f'Modelo "{model}" não encontrado')

class InvalidInput(Exception):
    def __init__(self,):
        super().__init__("algum(s) valores são inválidos")