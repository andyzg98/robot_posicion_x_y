from .controlador_robot import Controlador_robot
from .vista_robot import Vista_Robot
from .excepciones import MovimientoInvalidoError
from .modelo_robot import Modelo_Robot

class Aplicacion_Robot:
    def iniciar(self):
        controlador=Controlador_robot()
        vista=Vista_Robot()

        robot=controlador.crear_robot(0,0)

        while True:
            comando=vista.solicitar_comando()
            try:
                controlador.mover_robot(robot,comando)
            except MovimientoInvalidoError as error:
                    vista.mostrar_error(str(error))
            except SystemExit:
                 break
            else:
                print("el robot se mueve a la posicion ({},{}).".format(robot.posi_x,robot.posi_y))