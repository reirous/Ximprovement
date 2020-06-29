from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):  # TODO Se atentar às convenções para organização do código (nesse caso duas linhas em branco antes da classe)
    class Meta:
        model = Produto
        depth = 0
        fields = "__all__"