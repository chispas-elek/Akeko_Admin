# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


import subprocess as sub
from src.packGestorBD import MySQLConnector


class Singleton(type):
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance


class GestorTag(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_tags_script(self, p_id_script):
        """
        Dado el identificador de un Script. Obtenemos los Tags asociados al mismo

        :param p_id_script: El identificador del script
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdTag FROM Tag_Script WHERE IdScript=%s", (p_id_script, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_scripts_del_tag(self, p_id_tag):
        """
        Dado el identificador de un Tag. Obtenemos la lista de Scripts asociada al mismo

        :param p_id_tag:
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdScript FROM Tag_Script WHERE IdTag=%s", (p_id_tag, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def borrar_tag(self, p_id_tag):
        """
        Dado el identificador de un TAg. Borra del sistema el TAg

        :param p_id_tag: El identificador de un TAg
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Tag WHERE IdTag=%s", (p_id_tag, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd