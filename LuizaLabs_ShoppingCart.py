shoppigcart = []

diffproducts = int(input("How many different products would you like to buy?"))
for i in range(diffproducts):
    id_user = input("Insira o id do usuário:")
    id_product = int(input("Insira o id do produto:"))
    price_product = float(input("Insira o preço do produto:"))
    quantity_product = int(input("Insira a quantidade de produto:"))


item = [id_user, id_product, price_product, quantity_product]
print(item)

def add_item_cart(item):
    #shoppingcart.append[item]
    pass

def get_all_items_cart():
    #return todos os itens do carrinho
    pass

def get_item_cart_by_id(id_product):
    pass

def remove_item_id(id_product):
    #remover o item do carrinho que tem esse produto
    pass