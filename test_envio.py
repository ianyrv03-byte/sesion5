import pytest
from src.envio import Envio
from src.suministro import Suministro


def test_peso_total_es_la_suma_de_los_suministros():
    # Arrange
    envio = Envio()
    envio.agregar_suministro(Suministro("Agua", 10.0))
    envio.agregar_suministro(Suministro("Medicinas", 5.5))
    # Act
    peso = envio.calcular_peso_total()
    # Assert
    assert peso == 15.5


def test_envio_vacio_pesa_cero():
    assert Envio().calcular_peso_total() == 0


def test_suministro_con_peso_invalido_se_rechaza():
    with pytest.raises(ValueError):
        Suministro("Agua", 0)
