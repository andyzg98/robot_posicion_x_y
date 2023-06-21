class Vista_Robot: #mostrara los datos  
    def solicitar_comando(self):
        return input("ingrese un comando de movimiento para el robot")
    def mostrar_error(self,mensaje):
        print("¡ error:", mensaje,"!")