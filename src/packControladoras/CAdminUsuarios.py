# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packModelo import ListaUsuario
import GestorUsuario, GestorScript, GestorAlumno

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CAdminUsuarios(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_usuarios(self):
        """
        Obtiene todos los usuarios del sistema

        :return:
        """
        gestor_usuario = GestorUsuario.GestorUsuario()
        lista_usuarios = ListaUsuario.ListaUsuario()
        # Obtnemeos los usuarios de la BD
        resultado = gestor_usuario.obtener_usuarios()
        # Formateo la fecha de la BD
        # Transformamos las tuplas en tipos de datos
        lista_usuarios.construir(resultado)
        return lista_usuarios

    def borrar_usuario(self, p_id_usuario):
        """
        Dado el identificador de un usuario. Borramos del sistema a dicho usuario

        :param p_id_usuario: El identificador del usuario
        :return:
        """
        resultado = False
        gestor_script = GestorScript.GestorScript()
        gesto_usuaio = GestorUsuario.GestorUsuario()
        gestor_alumno = GestorAlumno.GestorAlumno()
        # Obtener todos los alumnos de los Grupos creados por el usuario
        lista_alumnos_usuario = gestor_alumno.obtener_alumnos_usuario(p_id_usuario)
        # Obtener las aplicaciones del usuario
        # todo verififcar si es necesario hacer un distinc
        lista_aplicaciones = gestor_script.obtener_aplicaciones(p_id_usuario)
        if len(lista_aplicaciones) != 0:
            podemos_borrar = False
            # El usuario tiene aplicaciones, vamos a eliminarlas
            exito = gestor_script.eliminar_aplicaciones(p_id_usuario)
            if exito > 0:
                # Recorremos la lista de aplicaciones actual, para eliminar aquellos scripts, de los alumnos que
                # ya no tengan más intenciones
                for aplicacion in lista_aplicaciones:
                    comprobar = gestor_script.comprobar_intencion(aplicacion['IdScript'], aplicacion['Dni'])
                    if comprobar is True:
                        print "Intención eliminada"
                        podemos_borrar = True
                    else:
                        print "Error garrafal"
                if podemos_borrar is True:
                    exito_borrar = gesto_usuaio.eliminar_usuario(p_id_usuario)
                    if exito_borrar == 1:
                        resultado = True

            else:
                print "Error serio"

        else:
            # Eliminamos el usuario de manera direxta
            exito_borrar = gesto_usuaio.eliminar_usuario(p_id_usuario)
            if exito_borrar == 1:
                resultado = True

        # Ahora voy a verificar si existen alumnos huérfanos
        for alumno in lista_alumnos_usuario:
            gestor_alumno.borrar_alumno(alumno['Dni'])
        return resultado