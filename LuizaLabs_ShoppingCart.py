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

def remove_item_id(shoppingcart):
    if len(shoppingcart)==0:
        return "O carrinho está vazio"
    
    removalquestion = input("Você gostaria de excluir algum item do carrinho? Escolha S/N \n")
    dicionario = {}
    y=0
    while removalquestion=="s" or removalquestion=="S":
        print("Segue abaixo a lista de produtos atualmente presentes no carrinho:\n")
        while y<len(shoppingcart):
            print(f"Produto: {shoppingcart[y][1]}\tID: {shoppingcart[y][2]}")
            dicionario[shoppingcart[y][2]]=y
            y+=1
            
        itemtoberemoved = input("Digite o ID do item que gostaria de remover \n")
        shoppingcart.pop(dicionario[itemtoberemoved])
            
        removalquestion = input("Você gostaria de excluir outro item? Escolha S/N \n")
    
    #listafinal=[]
    #for item2 in range(len(shoppingcart)):
    #    listafinal.append(shoppingcart[item2[1]])
    #return f"O carrinho final contem os seguintes itens: {listafinal}"
    #return f"O carrinho final contem os seguintes itens: {shoppingcart}"
    
    return shoppingcart

print(f"Segue a lista atualizada de produtos no carrinho:\n{remove_item_id(shoppingcart)}")