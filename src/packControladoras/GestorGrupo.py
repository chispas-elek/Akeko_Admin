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

class GestorGrupo(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_grupo(self, p_id_grupo):
        """
        Dado el identificador de un grupo, obtenemos todos los datos asociados al mismo

        :param p_id_grupo: El identificador de un Grupo
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT * FROM Grupo WHERE IdGrupo=%s;", (p_id_grupo, )
        respuesta_bd = bd.execute(consulta)
        return  respuesta_bd