from constantes import CODIGO_NORMAL
from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_NORMAL}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        display = []
        cliente_atual: str = self.fila.pop(0)
        display.append(f'Cliente: - {cliente_atual} - Caixa {caixa}')

        if len(self.fila) >= 3:
            display.append(f'Próximo: {self.fila[0]}')
            display.append(f'Fique atento: {self.fila[1]}')

        self.clientes_atendidos.append(cliente_atual)

        return f'Cliente atual:  {cliente_atual}, dirija-se ao caixa: {caixa}'
