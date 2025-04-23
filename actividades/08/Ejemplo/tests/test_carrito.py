## Ejemplo de prueba
# tests/test_carrito.py

import pytest
from src.factories import ProductoFactory


def test_agregar_producto_nuevo(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)

    # Act
    carrito.agregar_producto(producto)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad(carrito, producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito.agregar_producto(producto, cantidad=1)

    # Act
    carrito.agregar_producto(producto, cantidad=2)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto(carrito, producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito.agregar_producto(producto, cantidad=3)

    # Act
    carrito.remover_producto(producto, cantidad=1)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(carrito, producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto, cantidad=2)

    # Act
    carrito.remover_producto(producto, cantidad=2)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto(carrito, producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto, cantidad=1)

    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=5)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto(carrito, producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto, cantidad=3)

    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00, stock=2)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150

    # Act
    total = carrito.calcular_total()

    # Assert
    assert total == 550.00



def test_aplicar_descuento(carrito, producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    producto = ProductoFactory(nombre="Tablet", precio=500.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total 1000

    # Act
    total_con_descuento = carrito.aplicar_descuento(10)

    # Assert
    assert total_con_descuento == 900.00


def test_aplicar_descuento_limites(carrito, producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito.agregar_producto(producto, cantidad=1)

    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)


def test_obtener_items_vacio(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos.
    Act: Se vacia el carrito.
    Assert: Se verifica que el carrito este vacio.
    """
    # Arrange
    producto1 = ProductoFactory(nombre="Laptop", precio=1000.0)
    producto2 = ProductoFactory(nombre="Mouse", precio=50.0)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=1)

    # Act
    carrito.vaciar()

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0

    total = carrito.calcular_total()
    assert total == 0.0


def test_descuento_condicional_aplicado(carrito_con_productos):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se aplica un descuento condicional.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    # Esto fue realizando en conftest.py

    # Act
    total_con_descuento = carrito_con_productos.aplicar_descuento_condicional()

    # Assert
    assert total_con_descuento == carrito_con_productos.calcular_total() * (1 - 0.15)


def test_descuento_condicional_no_aplicado(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se aplica un descuento condicional.
    Assert: Se verifica que el total sin descuento sea el correcto.
    """
    # Arrange
    producto1 = ProductoFactory(nombre="Monitor", precio=300.0, stock=4)
    producto2 = ProductoFactory(nombre="Teclado", precio=100.0, stock=3)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=1)

    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional()

    # Assert
    assert total_con_descuento == carrito.calcular_total()


def test_agregar_producto_dentro_de_limite_stock(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto con stock limitado.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    producto = ProductoFactory(nombre="Laptop", precio=1000.0, stock=5)

    # Act
    carrito.agregar_producto(producto)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 1


def test_agregar_producto_fuera_de_limite_stock(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto con stock limitado.
    Act: Se intenta agregar el producto al carrito con una cantidad mayor al stock.
    Assert: Se verifica que se lanza una excepcion de ValueError y la lista de items vacia.
    """
    # Arrange
    producto = ProductoFactory(nombre="Laptop", precio=1000.0, stock=5)

    # Act
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=10)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_obtener_items_ordenados_precio(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos.
    Act: Se obtienen los items ordenados por precio.
    Assert: Se verifica que los items esten ordenados correctamente.
    """
    # Arrange
    producto1 = ProductoFactory(nombre="Laptop", precio=1000.0)
    producto2 = ProductoFactory(nombre="Teclado", precio=50.0)
    producto3 = ProductoFactory(nombre="Monitor", precio=300.0)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=1)
    carrito.agregar_producto(producto3, cantidad=1)

    # Act
    items_ordenados = carrito.obtener_items_ordenados(critero="precio")

    # Assert
    assert items_ordenados[0].producto.precio == 50.0
    assert items_ordenados[1].producto.precio == 300.0
    assert items_ordenados[2].producto.precio == 1000.0


def test_obtener_items_ordenados_nombre(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos.
    Act: Se obtienen los items ordenados por nombre.
    Assert: Se verifica que los items esten ordenados correctamente.
    """
    # Arrange
    producto1 = ProductoFactory(nombre="Laptop", precio=1000.0, stock=1)
    producto2 = ProductoFactory(nombre="Teclado", precio=50.0, stock=3)
    producto3 = ProductoFactory(nombre="Monitor", precio=300.0, stock=2)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=2)
    carrito.agregar_producto(producto3, cantidad=2)

    # Act
    items_ordenados = carrito.obtener_items_ordenados(critero="nombre")

    # Assert
    assert items_ordenados[0].producto.nombre == "Laptop"
    assert items_ordenados[1].producto.nombre == "Monitor"
    assert items_ordenados[2].producto.nombre == "Teclado"


@pytest.mark.parametrize(
    "precio, cantidad, porcentaje, total_esperado", [
        (100.0, 2, 10, 180.0),
        (100.0, 2, 25, 150.0),
        (100.0, 2, 50, 100.0),
        (100.0, 2, 0, 200.0),
        (100.0, 2, 100, 0.0),
    ]
)
def test_aplicar_descuento_parametrizado(carrito, precio, cantidad, porcentaje, total_esperado):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con precio y cantidad.
    Act: Se aplica un porcentaje de descuento.
    Assert: Se verifica que el total con descuento.
    """
    # Arrange
    nuevo_stock = cantidad + 5
    producto = ProductoFactory(nombre="Producto Test", precio=precio, stock=nuevo_stock)
    carrito.agregar_producto(producto, cantidad=cantidad)

    # Act
    total_con_descuento = carrito.aplicar_descuento(porcentaje)

    # Assert
    assert total_con_descuento == total_esperado


@pytest.mark.parametrize(
    "cantidad_inicial, nueva_cantidad, es_valido", [
        (2, 5, True),
        (2, 1, True),
        (2, 0, True),
        (2, -1, False),
    ]
)
def test_actualizar_cantidad_parametrizado(carrito, cantidad_inicial, nueva_cantidad, es_valido):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad inicial.
    Act: Se intenta actualizar la cantidad.
    Assert: Se verifica si la operacion es valida.
    """
    # Arrange
    producto = ProductoFactory(nombre="Producto Test", precio=100.0, stock=10)
    carrito.agregar_producto(producto, cantidad=cantidad_inicial)

    # Act & Assert
    if es_valido:
        carrito.actualizar_cantidad(producto, nueva_cantidad)
        items = carrito.obtener_items()
        if nueva_cantidad == 0:
            assert len(items) == 0
        else:
            assert len(items) == 1
            assert items[0].cantidad == nueva_cantidad
    else:
        with pytest.raises(ValueError):
            carrito.actualizar_cantidad(producto, nueva_cantidad)
