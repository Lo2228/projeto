
from database import produtos as lista_produtos, categorias as lista_categorias
import lib.funcoes as funcoes

def menu():
    print("\n1. Cadastrar novo produto")
    print("2. Consultar produtos")
    print("3. Apagar produtos")
    print("4. Atualizar produto")
    print("5. Trocar produto de categoria")
    print("6. Criar categoria")
    print("7. Atualizar categoria")
    print("8. Consultar categorias")
    print("9. Consultar produtos por categoria")
    print("10. Sair do programa")

def main():
    while True:
        menu()
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            nome = input("Digite o nome do produto: ")
            id_categorias = int(input("Digite o ID da sua categoria: "))
            funcoes.cadastrar_produtos(nome, id_categorias, lista_produtos)

        elif opcao == 2:
            print("\nProdutos:")
            produtos = funcoes.consultar_produtos(lista_produtos)
            for produtos in produtos:
                print(lista_produtos)

        elif opcao == 3:
            id_produtos = int(input("Digite o ID do produto a ser apagado: "))
            funcoes.apagar_produto(id_produtos, lista_produtos)

        elif opcao == 4:
            id_produtos = int(input("Digite o ID do produto a ser atualizado: "))
            nome = input("Digite o novo nome do produto: ")
            categorias = input("Digite a nova categoria do produto: ")
            funcoes.atualizar_produtos(id_produtos, nome, categorias, lista_produtos)

        elif opcao == 5:
            id_produtos = int(input("Digite o ID do produto a ser movido: "))
            nova_categorias = int(input("Digite o ID da nova categoria do produto: "))
            funcoes.trocar_categoria_produtos(id_produtos, nova_categorias, lista_produtos)

        elif opcao == 6:
            nome_categorias = input("Digite o nome da categoria: ")
            funcoes.criar_categorias(nome_categorias, lista_categorias)

        elif opcao == 7:
            id_categorias = int(input("Digite o ID da categoria a ser atualizada: "))
            novo_nome_categorias = input("Digite o novo nome da categoria: ")
            funcoes.atualizar_categorias(id_categorias, novo_nome_categorias, lista_categorias)

        elif opcao == 8:
            print("\nCategorias:")
            categorias = funcoes.consultar_categorias(lista_categorias)
            for categorias in categorias:
                print(lista_categorias)

        elif opcao == 9:
            id_categorias = int(input("Digite o ID da categoria para consultar: "))
            produtos_categorias = funcoes.consultar_produtos_por_categoria(id_categorias, lista_produtos)
            print(f"Produtos da categoria '{id_categorias}':")
            for produtos in produtos_categorias:
                print(f"ID: {produtos['id']}, Nome: {produtos['nome']}, Categoria: {produtos['categoria']}")

        elif opcao == 10:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
    

