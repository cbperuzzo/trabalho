import json
from utils.text import get_current_formated_date_time

operationsList = list()

STOCK_DB_PATH = 'data_base/stockops.json'
def update_operation_json():
    with open(STOCK_DB_PATH, 'w') as write_file:
        json.dump(operationsList, write_file)
def set_operation_list():
    with open(STOCK_DB_PATH,'r') as read_file:
        product_json = json.load(read_file)
    operationsList.clear()
    for item in product_json:
        operationsList.append(item)
def new_operaion(prod_num,amount,cost):
    op = dict()
    op["prod_id"]=prod_num
    op["amount"]=amount
    op["cost"]=cost
    op["datetime"]=get_current_formated_date_time()
    operationsList.append(op)
    update_operation_json()


set_operation_list()
