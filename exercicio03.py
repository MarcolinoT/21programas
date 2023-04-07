Custo_fabrica = float(input('Informe o preço o custo de fabrica do veículo:'))
Distribuidor = Custo_fabrica *(28/100)
Imposto = Custo_fabrica *(45/100)
Consumidor = Custo_fabrica+Distribuidor+Imposto
print(f'O preço final do veículo é de: {Consumidor}')
