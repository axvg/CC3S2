import pytest
from src.carrito import Carrito, Producto


def test_agregar_producto_excede_stock(carrito):
    """
    Red: Se espera que al intentar agregar una cantidad mayor a la disponible en stock se lance un ValueError.
    """
    # Arrange
    # Suponemos que el producto tiene 5 unidades en stock.
    producto = Producto("ProductoStock", 100.00, stock=5)

    # Act & Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=6)
