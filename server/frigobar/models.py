from django.db import models

# Create your models here.

# Modelo para produtos
# Propriedades:
#           descrição: Descrição do produto
#           ativo: Indica se o produto está ativado
#           preço: Preço do produto
#           data_preco: Data da inserção do preço indicado
class Produto(models.Model):
    descricao = models.CharField("Descrição do produto", max_length=100)
    ativo = models.BooleanField("Produto esta ativo", default=True)
    preço = models.DecimalField("Preço do produto", max_digits=15, decimal_places=4)
    data_preco = models.DateTimeField("Data do preço")


# Modelo para usuarios
# Propriedades:
#           nome: Nome do usuário
#           descricao: Descrição adicional sobre o usuário
#           ultimo_login: Data e hora do ultimo login do usuário
#           admin: Indica se usuário tem permissão de administrador do frigobar
class Usuario(models.Model):
    nome = models.CharField("Usuário", max_length=50)
    descricao = models.CharField("Descrição Extra", max_length=100)
    ultimo_login = models.DateTimeField("Data do ultimo login do usuário")
    admin = models.BooleanField("Identifica se é adminsitrador", default=False)

# Modelo para tipo de pedidos
# Propriedades:
#           descrição: Descrição do tipo de pedido
#           tipo: Indica o tipo do pedido (1 - Venda, 2 - Exluído, 3 - Bonificado)
class TipoPedido(models.Model):
    descricao = models.CharField("Descrição do tipo de pedido", max_length=50)
    tipo = models.CharField("Tipo do pedido", max_length=1)

# Modelo para pedidos
# Propriedades:
#           usuario: Indica o usuário ao qual foi realizado o pedido
#           tipo : Indica qual o tipo do pedido
#           justificativa: Justificativa para caso haja exclusão ou bonificação do pedido
#           data: Data em que o pedido foi realizado
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoPedido, on_delete=models.CASCADE)
    justificativa = models.CharField("Justificativa", max_length=150)
    data = models.DateTimeField("Data do Pedido")

# Modelo para items
# Propriedades:
#           pedido: Indica qual pedido está relacionado o item
#           produto: Indica qual produto foi negociado
#           quantidade: Quantidade negociada para este produto neste pedido
#           preco: Preço unitário deste produto para este pedido
class Item(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField("Quantidade vendida")
    preco = models.DecimalField("Preço de venda", max_digits=15, decimal_places=4)
