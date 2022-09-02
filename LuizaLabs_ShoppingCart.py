diffproducts = int(input("Quantos produtos gostaria de comprar?\nHow many different products would you like to buy?\n"))
shoppingcart = []
item = []


def add_item_cart(diffproducts): #Module for getting the item list and its info
    
    for i in range(diffproducts):
        id_user = input("Insira o id do usuário:\nEnter user ID:\n")
        productname = input("Insira o nome do produto:\nEnter product name:\n")
        id_product = input("Insira o id do produto:\nEnter product ID:\n")
        price_product = float(input("Insira o preço do produto:\nEnter product price:\n"))
        quantity_product = int(input("Insira a quantidade de produto:\nEnter the quantity:\n"))
    
        item = [id_user, productname, id_product, price_product, quantity_product]
        shoppingcart.append(item)
    
    return shoppingcart

shoppingcart=add_item_cart(diffproducts) #Saving the current cart content
print(shoppingcart)

def get_all_items_cart(shoppingcart): #Module for printing the cart item list by name
    newlist = [item[1] for item in shoppingcart]
    return f"No carrinho, foram adicionados os seguintes itens:\nThe following items were added to the cart:\n{newlist}\n"

print(get_all_items_cart(shoppingcart))

def get_item_cart_by_id(shoppingcart): #Module for printing the cart item list by item ID
    newlist = [item[2] for item in shoppingcart]
    return f"Os IDs desses itens são:\nThe items' IDs are:\n{newlist}\n"

print(get_item_cart_by_id(shoppingcart))

def remove_item_id(shoppingcart): #Module for removing item from the cart
    if len(shoppingcart)==0:
        return "O carrinho está vazio\nThe cart is currently empty"
    
    removalquestion = input("Você gostaria de excluir algum item do carrinho? Escolha S/N\nWould you like to remove an item? Answer Y/N\n")
    dicionario = {}
    y=0
    while removalquestion=="s" or removalquestion=="S": #While user wants to remove an item from the cart, loop
        print("Segue abaixo a lista de produtos atualmente presentes no carrinho:\nPlease find below the current cart item list\n")
        while y<len(shoppingcart):
            print(f"Produto/Product: {shoppingcart[y][1]}\tID: {shoppingcart[y][2]}")
            dicionario[shoppingcart[y][2]]=y
            y+=1
            
        itemtoberemoved = input("Digite o ID do item que gostaria de remover\nEnter the ID of the item you'd like to remove:\n")
        shoppingcart.pop(dicionario[itemtoberemoved]) #Requesting item ID for removal
            
        removalquestion = input("Você gostaria de excluir outro item? Escolha S/N\nWould you like to remove another item?\n")

    
    return shoppingcart

print(f"Segue a lista atualizada de produtos no carrinho:\nPlease find below the current cart content:\n{remove_item_id(shoppingcart)}")