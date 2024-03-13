class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is not None and self.maximo is not None:
            return f"Error: {self.mensaje}. La {self.dimension} debe ser mayor a 0 y menor o igual a {self.maximo}."
        elif self.dimension is not None:
            return f"Error: {self.mensaje}. La {self.dimension} debe ser mayor a 0."
        else:
            return super().__str__()