import json
from utils.text import get_current_formated_date_time
from modelo.produtos.Produtos import product_list

operationsList = list()

STOCK_DB_PATH = 'data_base/stockops.json'

class StockOps():
    def __init__(self,prod_id,amount,cost):
        self.prod_id = prod_id
        self.amount = amount
        self.cost = cost
        self.datetime = get_current_formated_date_time()
    def to_json(self):
        op = dict()
        op["prod_id"] = self.prod_id
        op["amount"] = self.amount
        op["cost"] = self.cost
        op["datetime"] = self.datetime
    @staticmethod
    def update_operation_json():
        with open(STOCK_DB_PATH, 'w') as write_file:
            json.dump(operationsList, write_file)
    @staticmethod
    def set_operation_list():
        with open(STOCK_DB_PATH,'r') as read_file:
            product_json = json.load(read_file)
        operationsList.clear()
        for item in product_json:
            prod_id = item['prod_id']
            if product_list[prod_id].modelo != 'produto inexistente':
                operationsList.append(item)

    def save(self):
        op = dict()
        op["prod_id"]=self.prod_id
        op["amount"]=self.amount
        op["cost"]=self.cost
        op["datetime"]=self.datetime
        operationsList.append(op)
        StockOps.update_operation_json()

    @staticmethod
    def get_total_cost():
        sum = 0
        for item in operationsList:
            sum += item["cost"]
        return sum
    @staticmethod
    def get_ops_list():
        StockOps.set_operation_list()
        return operationsList


StockOps.set_operation_list()
