#del archibo     importar clase 
from modelo_robot import Modelo_Robot
from vista_robot import Vista_Robot
from excepciones import MovimientoInvalidoError
class Controlador_robot:
    def crear_robot(self,posi_x,posi_y):
        return Modelo_Robot(posi_x,posi_y)
    def mover_robot(self,robot,comando):
        if comando=="adelante":
            robot.posi_y +=1
        elif comando=="atras":
            robot.posi_y +=1
        elif comando=="izquierda":
            robot.posi_y +=1
        elif comando=="derecha":
             robot.posi_y +=1
        elif comando=="salir":
            raise SystemExit
        else:
            raise MovimientoInvalidoError(comando)
        if not self.es_movimiento_valido(robot):
            raise MovimientoInvalidoError(comando)
        def es_movimiento_valido(robot):
            return -10 <= robot.posi_x <= 10 and -10 <=robot.posi_y <=10
        
