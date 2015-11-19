# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packGestorBD import MySQLConnector

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class GestorAlumno(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def borrar_alumno(self, p_dni):
        """
        La función verifica si el alumno pertenece a algún grupo. De no pertenecer
        lo borra del sistema.

        :param p_dni: El Dni del alumno
        :return: True o False indicando el exito de la operación
        """
        exito = False
        bd = MySQLConnector.MySQLConnector()
        # Verificar si el alumno está en un grupo
        consulta1 = "SELECT IdGrupo FROM Alumno_Grupo WHERE Dni=%s;", (p_dni, )
        respuesta_bd = bd.execute(consulta1)
        if len(respuesta_bd) == 0:
            # El alumno no pertenece a ningún grupo, podemos eliminarlo del sistema
            consulta2 = "DELETE FROM Alumno WHERE Dni=%s;", (p_dni, )
            respuesta_bd2 = bd.execute(consulta2)
            if respuesta_bd2 == 1:
                exito = True
        return exito

    def obtener_alumno(self, p_dni):
        """
        Dado el dni de un alumno obtiene sus datos

        :param p_dni: El dni del alumno
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT * FROM Alumno WHERE Dni=%s", (p_dni, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_alumnos_usuario(self, p_id_usuario):
        """
        Dado el identificador de un usuario. Obtener todos los alumnos que haya introducido en sus grupos

        :param p_id_usuario:
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT DISTINCT Dni FROM Alumno_Grupo WHERE IdGrupo IN (SELECT IdGrupo FROM Grupo WHERE IdUsuario=%s);",\
                   (p_id_usuario, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd