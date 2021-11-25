import Controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i,'w') as arq:
                arq.write("")


criarArquivos('categoria.txt','clientes.txt', 'fornecedores.txt', 'funcionarios.txt','venda.txt','estoque.txt')

if __name__ == "__main__":
    while True:
        local = int(input("Digite [1] para acessar (Categorias)\n"
                          "Digite [2] para acessar (Estoque)\n"
                          "Digite [3] para acessar (Fornecedor)\n"
                          "Digite [4] para acessar (Cliente)\n"
                          "Digite [5] para acessar (Funcionario)\n"
                          "Digite [6] para acessar (Vendas)\n"
                          "Digite [7] para ver produtos mais vendidos\n"
                          "Digite [8] para sair do sistema\n"))

        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite [1] para Cadastrar uma Categgoria\n"
                          "Digite [2] para Remover a Categoria\n"
                          "Digite [3] para Alterar a Categoria\n"
                          "Digite [4] para Mostrar a Categoria Cadastrada\n"
                          "Digite [5] para Sair\n"))

                if decidir == 1:
                    categoria = input("Informe a Categoria que deseja Cadastra-la\n")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Informe a Categoria que deseja remover\n')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Informe a Categoria que deseja Alterar\n")
                    novaCategoria = input('Informe a Categoria para a qual deseja alterar\n')
                    cat.alteraCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break

        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite [1] para Cadastrar um Produto\n"
                          "Digite [2] para Remover um Produto\n"
                          "Digite [3] para Alterar um Produto\n"
                          "Digite [4] para Mostrar o Estoque\n"
                          "Digite [5] para Sair\n"))
                if decidir == 1:
                       nome = input('Informe o Nome do Produto: \n')
                       preco = input('Iforme o preço do Produto: \n')
                       categoria = input('Iforme a Categoria do Produto: \n')
                       quantidade = input('Iforme a Quantidade do Produto: \n')

                       cat.cadastrarProduto(nome, preco, categoria, quantidade)

                elif decidir == 2:
                        produto = input('Informe o Produrto que deseja Remover: \n')

                        cat.removeProduto(produto)

                elif decidir == 3:
                        nomeAlterar = input('Informe o Nome do Produto que deseja Alterar: \n')
                        nome = input('Informe o Novo nome do Produto: \n')
                        preco = input('Iforme o Novo preço do Produto: \n')
                        categoria = input('Iforme a Nova Categoria do Produto: \n')
                        quantidade = input('Iforme a Nova Quantidade do Produto: \n')

                        cat.alterarProduto(nomeAlterar, nome, preco, categoria, quantidade)

                elif decidir == 4:
                    cat.mostrarEstoque()

                else:
                    break

        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite [1] para Cadastrar um Fornecedor\n"
                                    "Digite [2] para Remover um Fornecedor\n"
                                    "Digite [3] para Alterar um Fornecedor\n"
                                    "Digite [4] para Mostrar o Fornecedor\n"
                                    "Digite [5] para Sair\n"))

                if decidir == 1:
                    nome = input('Informe o Nome do Fornecedor: \n')
                    cnpj = input('Informe o CNPJ do Fornecedor: \n')
                    telefone = input('Informe o Telefone do Fornecedor: \n')
                    categoria = input('Informe a Categoria Fornecida: \n')

                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)

                elif decidir == 2:
                    fornecedor = input('Informe o Fornecedor que deseja Remover: \n')
                    cat.removerFornecedor(fornecedor)

                elif decidir == 3:
                    nomeAlterar = input('Informe o Nome do Fornecedor que deseja Alterar: \n')
                    novoNome = input('Informe o Novo nome do Fornecedor: \n')
                    novoCnpj = input('Informe o Novo CNPJ do Fornecedor: \n')
                    novoTelefone = input('Informe o Novo telefone do Fornecedor: \n')
                    novaCategoria = input('Informe a Nova Categoria Fornecida: \n')

                    cat.alterarFornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria)

                elif decidir == 4:
                    cat.mostrarFornecedores()

                else:
                    break

        elif local == 4:
            cat = Controller.ControllerClientes()
            while True:
                decidir = int(input("Digite [1] para Cadastrar um Cliente\n"
                                    "Digite [2] para Remover um Cliente\n"
                                    "Digite [3] para Alterar um Cliente\n"
                                    "Digite [4] para Mostrar  Clientes\n"
                                    "Digite [5] para Sair\n"))

                if decidir == 1:
                    nome = input('Informe o Nome do Cliente: \n')
                    telefone = input('Informe o Telefone do Cliente: \n')
                    cpf = input('Informe o CPF do Cliente: \n')
                    email = input('Informe o Email do Cliente: \n')
                    endereco = input('Informe o Endereço do Cliente: \n')

                    cat.cadastrarClientes(nome, telefone, cpf, email, endereco)

                elif decidir == 2:
                    cliente = input('Informe o Nome do Cliente que deseja Remover: \n')

                    cat.removerCliente(cliente)

                elif decidir == 3:
                    nomeAlterar = input('Informe o Nome do Cliente que deseja Alterar: \n')
                    novoNome = input('Informe o Novo nome do Cliente: \n')
                    novoTelefone = input('Informe o Novo Telefone do Cliente: \n')
                    novoCpf = input('Informe o Novo CPF do Cliente: \n')
                    novoEmail = input('Informe o Novo Email do Cliente: \n')
                    novoEndereco = input('Informe o Novo Endereço do Cliente: \n')

                    cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)

                elif decidir == 4:
                    cat.mostrarClientes()

                else:
                    break

        elif local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = int(input("Digite [1] para Cadastrar um Funcionario\n"
                                    "Digite [2] para Remover um Funcionario\n"
                                    "Digite [3] para Alterar um Funcionario\n"
                                    "Digite [4] para Mostrar  Funcionario\n"
                                    "Digite [5] para Sair\n"))

                if decidir == 1:
                    clt = input('Informe o nº CLT do Funcionario: \n')
                    nome = input('Informe o Nome do Funcionario: \n')
                    telefone = input('Informe o Telefone do Funcionario: \n')
                    cpf = input('Informe o CPF do Funcionario: \n')
                    email = input('Informe o Email do Funcionario: \n')
                    endereco = input('Informe o Endereço do Funcionario: \n')

                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)

                elif decidir == 2:
                    funcionario = input('Informe o Funcionario que deseja Remover: \n')

                    cat.removerFuncionario(funcionario)

                elif decidir == 3:
                    nomeAlterar = input('Informe o Nome do Funcionario que deseja Alterar: \n')
                    novoClt = input('Informe a Nova CLT do Funcionario: \n')
                    novoNome = input('Informe o Novo nome do Funcionario: \n')
                    novoTelefone = input('Informe o Novo telefone do Funcionario: \n')
                    novoCpf = input('Informe o Novo CPF do Funcionario: \n')
                    novoEmail = input('Informe o Novo Email do Funcionario: \n')
                    novoEndereco = input('Informe o Novo Endereço do Funcionario: \n')

                    cat.alterarFuncionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)

                elif decidir == 4:
                    cat.mostrarFuncionario()

                else:
                    break

        elif local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input('Digite [1] para Realizar uma Venda: \n'
                                    'Digite [2] para ver as Vendas: \n'
                                    'Digite [3] para sair\n'))

                if decidir == 1:
                    nome = input('Informe o Nome do Produto: \n')
                    vendedor = input('Informe o Nome do Vendedor: \n')
                    comprador = input('Informe o Nome do Cliente')
                    quantidade = input('Informe a Quantidade: \n')

                    cat.cadastrarVenda(nome,vendedor, comprador, quantidade)

                elif decidir == 2:
                    dataInicio = input('Informe a data de início no formato dia/mês/ano: \n')
                    dataTermino = input('Informe a data de término no formato dia/mês/ano: \n')

                    cat.mostrarVenda(dataInicio, dataTermino)
        elif local == 7:
            a = Controller.ControllerVenda()
            a.relatorioVendas()

        else:
            break

