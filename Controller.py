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

            #Removendo do arquivo
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Sem Categoria"), x.quantidade)
                           if(x.produto.categoria == categoriaRemover) else(x), estoque))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome +"|" + i.produto.preco +"|" + i.produto.categoria +"|" + str(i.quantidade))
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

                estoque = DaoEstoque.ler()

                estoque = list(
                    map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade)
                    if (x.produto.categoria == categoriaAlterar) else (x), estoque))

                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(
                            i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                        arq.writelines('\n')

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
                if len(est) == 0 or nomeAlterar == novoNome:
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

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        '''
        return 1 = O produto selecionado não existe !!
        return 2 = A Quantidade insuficiente em estoque :( !!
        return 3 = Venda realizada com sucesso
        :param nomeProduto:
        :param vendedor:
        :param comprador:
        :param quantidadeVendida:
        :return:
        '''
        # ler o estoque para saber se o produto a ser vendido existe em estoque
        x = DaoEstoque.ler()
        temp = []
        # verificar se a quantidade a ser vendida existe em estoque e se o produto tb existe
        existe = False # esta variável somente fala se existe ou não o produto em estoque
        quantidade = False # esta verifica a quantidade existente

        for i in x:
            # percorrendo e verificando se existe o produto e se a quantidade em estoque é maior que a quantidade a ser vendida
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria),vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)

            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open('estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome + "|" + i[0].preco + "|" + i[0].categoria + "|" + str(i[1]))
                arq.writelines('\n')

        if existe == False:
            print('O produto selecionado não existe !!')
            return None

        elif not quantidade:
            print('A Quantidade insuficiente em estoque :( !!')
            return None
        else:
            print('Venda realizada com sucesso')
            return valorCompra

    def relatorioVendas(self):
        # ler o arquivo Vendas
        vendas = DaoVenda.ler()
        # variável auxiliar para listar os produtos mais vendidos
        produtos =[]
        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.qtdoVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                                    if(x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
        print('Estes são os produtos mais vendidos !!')
        a = 1
        for i in ordenado:
            print(f'==========Produtos [{a}]==========')
            print(f"Produto: {i['produto']}\n"
                  f"Quantidade: {i['quantidade']}\n")
            a += 1


    def mostrarVenda(self, dataInicio, dataFim):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataFim1 = datetime.strptime(dataFim, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data,'%d/%m/%Y') >= dataInicio1 and datetime.strptime(x.data,'%d/%m/%Y') <= dataFim1, vendas))

        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f"===============Venda[{cont}]===============")
            print(f"Nome: {i.itensVendido.nome}\n"
                  f"Categoria: {i.itensVendido.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.qtdoVendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}")

            total += int(i.itensVendido.preco) * int(i.qtdoVendida)
            cont += 1

        print(f"Total vendido: {total}")

class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        categorias_Fornecedor = list()
        categoria_existe = False
        for i in x:
            if i.cnpj == cnpj and i.categoria == categoria:
                categoria_existe = True
        # fazendo filtro para evitar duplicação no arquivo
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.cnpj == cnpj, x))
        if len(listaCnpj) > 0 and categoria_existe:
            print('CNPJ já existe !!!')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('Digite um CNPJ ou telefone válido !!')

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0 :
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if(x.nome == nomeAlterar)else(x), x))
            else:
                print('CNPJ já existe !!')
        else:
            print('fornecedor que deseja alterar não existe !!')

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines((i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria)))
                arq.writelines('\n')
            print('Fornecedor alterado com sucesso !! :)')

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('\033[0;30;41mO fornecedor que deseja excluir não existe !! :(\033[m')
            return None

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines((i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria)))
                arq.writelines('\n')
            print('Fornecedor Removido com Sucesso !!!')

    def mostrarFornecedores(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print('Lista de fornecedores está Vazia')


        print('\033[4;34m===============Fornecedores===============\033[m')
        for i in fornecedores:
            print(f"Categoria = {i.categoria}\n"
                  f"Nome = {i.nome}\n"
                  f"Telefone = {i.telefone}\n"
                  f"Cnpj = {i.cnpj}")
            print('*'*40)

class ControllerClientes:
    def cadastrarClientes(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('CPF já existe !!!')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('\033[1;34mCliente Cadastrado com sucesso !! :) \033[m')
            else:
                print('\033[0;30;41mdigite um cpf ou telefone Válidos\033[m')

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail,novoEndereco)if(x.nome == nomeAlterar) else(x), x))
        else:
            print('\033[0;30;41mO cliente que seja alterar não existe :( \033[m')

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('\033[0;34;41mCliente alterado com sucesso !! :)\033[m ')

    def removerCliente(self, nome):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('\033[0;30;41mO cliente que seja Remover não existe :( \033[m')
            return None

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('\033[0;34;41mCliente Removido com sucesso !! :)\033[m ')

    def mostrarClientes(self):
        clientes = DaoPessoa.ler()

        if len(clientes) ==  0:
            print('\033[30;41mA Lista de Clientes esta vazia :( \033[m')
        print(f"\033[34m===============Clientes===============")
        for i in clientes:
            print(f"\033[34mNome = {i.nome}\n"
                  f"Telefone = {i.telefone}\n"
                  f"Endereço = {i.endereco}\n"
                  f"Cpf = {i.cpf}\n"
                  f"email = {i.email}\033[m")
            print('\033[32m*\033[m'*40)

class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) > 0:
            print('CPF já existe !!!')
        elif len(listaClt) > 0:
            print('Já existe um funcionário com essa CLT !!!')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionário cadastrado com sucesso !! :)')
            else:
                print('Informe um CPF ou telefone Válidos !!!')

    def alterarFuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar)
                         else(x), x))
        else:
            print('O Funcionário que deseja alterar não Existe !!!')
        with open ('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" +  i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Funcionário alterado com sucesso !!')

    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O Funcionário que deseja remover não existe !!!')
            return None

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Funcionario Removido com sucesso !!')

    def mostrarFuncionario(self):
        funcionario = DaoFuncionario.ler()
        if len(funcionario) == 0:
            print('Lista de Funcionários está Vazia !!!')

        print(f"\033[34m===============Funcionario===============\033[m")
        for i in funcionario:
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Endereço: {i.endereco}\n"
                  f"CPF: {i.cpf}\n"
                  f"CLT: {i.clt}")
            print('*'*35)





#a = ControllerFuncionario()
#a.alterarFuncionario('Pedro', '254','Pedro Luiz','34543333467','12885678920','Pedroma@gmail.com','Rua pepe numero 143')
#self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco
#a.removerFuncionario('Jurema')
#a.mostrarFuncionario()
#a.cadastrarFuncionario(254,'Pedro', '12885678920','34543333467','Pedroma@gmail.com','Rua pepe numero 143')
#a = ControllerClientes()
#a.mostrarClientes()
#a.removerCliente('Pedro')
#a.alterarCliente('Jose Carlos','Jose Carlos I','12345678923','98789876564','jl@hotmail.com', 'rua r numero 139')
#a.cadastrarClientes('Antonio', '17775444923', '54345678321','ytui@hotmail.com','rua r numero 139')
#a = ControllerFornecedor()
#a.cadastrarFornecedor()
#a.mostrarFornecedores()
#a.removerFornecedor('Carrefour')
#a.alterarFornecedor('Carrefour','WallMart','44444444444444','77777777777','Frutas')
#a.cadastrarFornecedor('Epa','34253627182934', '22222222222','Verduras')
#a = ControllerVenda()
#a.mostrarVenda('20/11/2021','21/11/2021')
#a.relatorioVendas()
#a.cadastrarVenda('kiwi', 'Ricardo', 'Luiz', 8)
#a = ControllerEstoque()
#a.mostrarEstoque()
#a.cadastrarProduto('Banana', '50', 'Frutas', 20)
#a.removeProduto('abacate')
#a.alterarProduto('cenoura','cenoura','R$2,0','Verduras',20)
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