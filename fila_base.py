import abc
from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO
from typing import List


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    @abc.abstractclassmethod
    def gerar_senha_atual(self):
        ...

    # @abc.abstractclassmethod
    # def estatistica(self, dia, agencia, flag_detail):
    #     ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gerar_senha_atual()
        self.insere_cliente()

    @abc.abstractclassmethod
    def chama_cliente(self, caixa: int):
        ...
