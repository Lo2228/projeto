
# CADASTRAR PRODUTO
def cadastrar_produtos(nome: str, id_categoria: int, produtos: list):
    novo_produtos= {
        "id": len(produtos) + 1,
        "nome": nome,
        "categoria": id_categoria
    }
    produtos.append(novo_produtos)


# CONSULTAR PRODUTO

def consultar_produtos(produtos):
    return produtos

# APAGAR PRODUTO

def apagar_produto(id_produtos, produtos):
    for p in produtos:
        if p["id"] == id_produtos:
            produtos.remove(p)
            break

# ATUALIZAR PRODUTO

def atualizar_produtos(id_produtos, novo_nome, nova_categoria, produtos):
    for p in produtos:
        if p["id"] == id_produtos:
            p["nome"] = novo_nome
            p["categoria"] = nova_categoria
            break

# trocar_categoria_produto
        
def trocar_categoria_produtos(id_produtos, nova_categorias, produtos):
    for p in produtos:
        if p["id"] == id_produtos:
            p["categoria"] = nova_categorias
            print(f"Produto {id_produtos} foi movido para a categoria '{nova_categorias}'.")
            break
    else:
        print("Produto não encontrado.")

# CRIAR CATEGORIA

def criar_categorias(nome, categorias: list):
    nova_categorias = {
        "id": len(categorias) + 1,
        "nome": nome
    }
    categorias.append(nova_categorias)

# ATUALIZAR CATEGORIA

def atualizar_categorias(id_categorias, novo_nome, categorias):
    for c in categorias:
        if c["id"] == id_categorias:
            c["nome"] = novo_nome
            break

# CONSULTAR CATEGORIA
def consultar_categorias(categorias):
    return categorias

# CONSULTAR PRODUTOS POR CATEGORIA

def consultar_produtos_por_categoria(id_categorias, lista_produtos):
    produtos_categorias = [produto for produto in lista_produtos if produto["categoria"] == id_categorias]
    return produtos_categorias



