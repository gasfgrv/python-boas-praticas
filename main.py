from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida
from constantes import TIPO_FILA_PRIORITARIA

teste_fabrica = FabricaFila.pega_fila(TIPO_FILA_PRIORITARIA)
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(15))
print(teste_fabrica.estatistica(EstatisticaResumida('06/06/2006', 120)))
print(teste_fabrica.estatistica(EstatisticaDetalhada('06/06/2006', 120)))

