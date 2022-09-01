diffproducts = int(input("How many different products would you like to buy?"))
shoppingcart = []
item = []


def add_item_cart(diffproducts):
    
    
    for i in range(diffproducts):
        id_user = input("Insira o id do usuário: ")
        productname = input("Insira o nome do produto: ")
        id_product = int(input("Insira o id do produto: "))
        price_product = float(input("Insira o preço do produto: "))
        quantity_product = int(input("Insira a quantidade de produto: "))
    
        item = [id_user, productname, id_product, price_product, quantity_product]
    
        shoppingcart.append(item)
    
    return shoppingcart

shoppingcart=add_item_cart(diffproducts)
#print(shoppingcart)

def get_all_items_cart(shoppingcart):
    newlist = [item[1] for item in shoppingcart]
    return f"No carrinho, foram adicionados os seguintes itens: {newlist}\n"

print(get_all_items_cart(shoppingcart))

def get_item_cart_by_id(shoppingcart):
    newlist = [item[2] for item in shoppingcart]
    return f"Os IDs desses itens são: {newlist}\n"

print(get_item_cart_by_id(shoppingcart))

def remove_item_id(diffproducts, shoppingcart):
    removalquestion = input("Você gostaria de excluir algum item do carrinho? Escolha S/N \n")
    dicrem = {}
    while removalquestion=="s" or removalquestion=="S":
        print("Segue abaixo a lista de produtos atualmente presentes no carrinho:\n")
        for item in range(diffproducts):
            print(f"Produto: {shoppingcart[item[1]]}\tID: {shoppingcart[item[2]]}")
            dicrem[item[2]]=item
            
        itemtoberemoved = input("Digite o ID do item que gostaria de remover \n")
        shoppingcart.pop(dicrem[itemtoberemoved])
            
        removalquestion = input("Você gostaria de excluir outro item? Escolha S/N \n")
            
    return f"The updated cart contains the following items: {shoppingcart}"

#print(get_item_cart_by_id(shoppingcart))