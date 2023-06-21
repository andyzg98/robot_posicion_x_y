class MovimientoInvalidoError(Exception):
    def __init__(self,comando):
        self.comando=comando

    def str (self):
       return f"el comando de movimiento '{self.comando}'es invalido"