from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        #criando uma variavel par saber sa acategoria ja existe
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!!!')
        else:
            print('A categoria que deseja cadastrar já existe ')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A Categoria que deseja Excluir não existe')
        else:
            for i in range(len(x)):
                # Foi removido somente da memoria RAM
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('A Categoria removida com sucesso :) !')
            #todo: colocar sem categoria no estoque
            #Removendo do arquivo
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alteraCategoria(self,categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            #verificar se existe a categoria que será alterada
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                #usando  MAP
                x = list(map(lambda x: Categoria(categoriaAlterada)if(x.categoria == categoriaAlterar) else(x), x))
                print('Troca realizada!!')
                # todo: alterar categoria tambem do estoque

            else:
                print('A categoria que deseja alterar já existe !!')
        else:
            print('A categoria que deseja alterar não existe !!')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria esta vazia')

        else:
            for i in categorias:
                print(f'categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        # ler o arquivo estoque
        x = DaoEstoque.ler()
        #ler a o arquivo categoria
        z = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, z))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso !!!')
            else:
                print('Produto já existe em estoque')
        else:
            print('Não existe a Categoria selecionada :( ')

    def removeProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto Removido com sucesso :) !!')
        else:
            print('O produto a que deseja remover não existe :( !!')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                               i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        # verificar se a categoria existe
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            # verificar se o produto que quero alterar existe
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            #verificar se a variavel est é maior que zero o produto ja existe posso alterar se for menor o produto não existe
            if len(est) > 0:
                # verificar se o nome para o qual desejo alterar ja existe no arquivo para não ser duplicado
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                    print('Produto alterado com sucesso :) !!')
                else:
                    print('Produto já cadastrado !!!')
            else:
                print('O Produto que deseja alterar não existe :( !!')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                                   i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines('\n')
        else:
            print('A categoria informada não existe :( !!')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque esta vazio :( ')
        else:
            print('==========================Produtos==========================')
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                      f"Preco: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}")
                print('------------------------------------------------------------')


a = ControllerEstoque()
a.mostrarEstoque()
#a.alterarProduto('cenoura','R$2,0','Legumes','Verduras',20)
#a.removeProduto('abacate')
#a.cadastrarProduto('cenoura', 'R$,50', 'Legumes', 10)
#a = ControllerCategoria()
#a.removerCategoria('Frutas')
#a.alteraCategoria('Frios', 'Congelados')
#a.cadastraCategoria('Frutas')
#a.mostrarCategoria()
#Frutas
#Verduras
#Legumes
#Frios
#Congelados