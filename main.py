# from fila_normal import FilaNormal
from fabrica_fila import FabricaFila

# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(5))

# from fila_prioritaria import FilaPrioritaria

# fila_teste_2 = FilaNormal()
# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.chama_cliente(4)


# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.chama_cliente(13))
# print(fila_teste_2.estatistica('10/01/1995', 198, 'detail'))

teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
