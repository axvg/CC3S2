# src/carrito.py

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio})"


class ItemCarrito:
    def __init__(self, producto, cantidad=1):
        self.producto = producto
        self.cantidad = cantidad

    def total(self):
        return self.producto.precio * self.cantidad

    def __repr__(self):
        return f"ItemCarrito({self.producto}, cantidad={self.cantidad})"


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad=1):
        """
        Agrega un producto al carrito. Si el producto ya existe, incrementa la cantidad.
        """
        if producto.stock < cantidad:
            raise ValueError(f"No hay suficiente stock ({producto.stock}) para este producto.")

        for item in self.items:
            if item.producto.nombre == producto.nombre:
                item.cantidad += cantidad
                return
        self.items.append(ItemCarrito(producto, cantidad))

    def remover_producto(self, producto, cantidad=1):
        """
        Remueve una cantidad del producto del carrito.
        Si la cantidad llega a 0, elimina el item.
        """
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if item.cantidad > cantidad:
                    item.cantidad -= cantidad
                elif item.cantidad == cantidad:
                    self.items.remove(item)
                else:
                    raise ValueError("Cantidad a remover es mayor que la cantidad en el carrito")
                return
        raise ValueError("Producto no encontrado en el carrito")

    def actualizar_cantidad(self, producto, nueva_cantidad):
        """
        Actualiza la cantidad de un producto en el carrito.
        Si la nueva cantidad es 0, elimina el item.
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if nueva_cantidad == 0:
                    self.items.remove(item)
                else:
                    item.cantidad = nueva_cantidad
                return
        raise ValueError("Producto no encontrado en el carrito")

    def calcular_total(self):
        """
        Calcula el total del carrito sin descuento.
        """
        return sum(item.total() for item in self.items)

    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento al total del carrito y retorna el total descontado.
        El porcentaje debe estar entre 0 y 100.
        """
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        return total - descuento

    def contar_items(self):
        """
        Retorna el número total de items (sumando las cantidades) en el carrito.
        """
        return sum(item.cantidad for item in self.items)

    def obtener_items(self):
        """
        Devuelve la lista de items en el carrito.
        """
        return self.items

    def vaciar(self):
        """
        Vacia el carrito.
        """
        self.items = []

    def aplicar_descuento_condicional(self, porcentaje=15, minimo=500):
        """
        Aplica un descuento si el total es mayor que un minimo.
        Retorna el total descontado o el total original si no se aplica el descuento.
        """
        if self.calcular_total() > minimo:
            return self.aplicar_descuento(porcentaje)
        return self.calcular_total()

    def obtener_items_ordenados(self, critero: str):
        """
        Devuelve la lista de items ordenados por el criterio especificado.
        Los criterios pueden ser precio o nombre.
        """
        if critero == "precio":
            return sorted(self.items, key=lambda item: item.producto.precio)
        if critero == "nombre":
            return sorted(self.items, key=lambda item: item.producto.nombre)
        else:
            raise ValueError("Criterio invalido.")
