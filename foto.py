from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho) -> None:
        try:
            if nuevo_ancho <= 0 or nuevo_ancho > self.MAX:
                raise DimensionError("Ancho inválido", "ancho", self.MAX)
            self.__ancho = nuevo_ancho
        except DimensionError as e:
            print(f"Error al establecer el ancho: {e}")

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto) -> None:
        try:
            if nuevo_alto <= 0 or nuevo_alto > self.MAX:
                raise DimensionError("Alto inválido", "alto", self.MAX)
            self.__alto = nuevo_alto
        except DimensionError as e:
            print(f"Error al establecer el alto: {e}")