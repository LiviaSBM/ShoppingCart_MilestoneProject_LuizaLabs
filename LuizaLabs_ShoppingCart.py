shoppingcart = []
item = []

diffproducts = int(input("How many different products would you like to buy?"))
for i in range(diffproducts):
    id_user = input("Insira o id do usuário: ")
    productname = input("Insira o nome do produto: ")
    id_product = int(input("Insira o id do produto: "))
    price_product = float(input("Insira o preço do produto: "))
    quantity_product = int(input("Insira a quantidade de produto: "))
    
    def add_item_cart(item):
        item = [id_user, id_product, price_product, quantity_product]
        shoppingcart.append(item)
        return shoppingcart
    
def get_all_items_cart(shoppingcart):
    newlist = [item[1] for item in shoppingcart]
    return f"No carrinho, foram adicionados os seguintes itens: {newlist}"

def get_item_cart_by_id(shoppingcart):
    return [item[3] for item in shoppingcart]

def remove_item_id(id_product):
    #remover o item do carrinho que tem esse produto
    pass

get_all_items_cart(shoppingcart)