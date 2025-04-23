import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory


@pytest.fixture
def carrito():
    return Carrito()


@pytest.fixture
def producto():
    return ProductoFactory(nombre="test_producto", precio=10.0, stock=15)


@pytest.fixture
def carrito_con_productos():
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Monitor", precio=300.0, stock=1)
    producto2 = ProductoFactory(nombre="Teclado", precio=100.0, stock=3)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=3)
    return carrito
