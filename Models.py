from datetime import datetime, date

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria
        
class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    #Estoque herda de produtos tendo somente a quantidade como específica
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        
class Venda:
    # herda de produtos e mais os itens específicos de vendas
    def __init__(self, itensVendido: Produtos, vendedor, comprador, qtdoVendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.qtdoVendida = qtdoVendida
        self.data = data
        
class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria
        
class Pessoa:
    #Cliente é uma pessoa e não tem mais atributos por tanto não precisa de uma classe específica
    def __init__(self, nome, telefone, cpf, email, endereco):     
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        
class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        # herda tudo que Pessoas + as informações de clt que são individuais
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)