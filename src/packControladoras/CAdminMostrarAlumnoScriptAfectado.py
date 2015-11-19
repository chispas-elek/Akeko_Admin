# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packControladoras import GestorAlumno, GestorUsuario, GestorGrupo

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CAdminMostrarAlumnoScriptAfectado(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_datos_alumno(self, p_dni):
        """
        Obtiene los datos de un alumno dado su dni

        :param p_dni: El dni del alumno
        :return:
        """
        gesto_alumno = GestorAlumno.GestorAlumno()
        el_alumno = gesto_alumno.obtener_alumno(p_dni)
        return el_alumno

    def obtener_datos_usuario(self, p_id_usuario):
        """
        Dado el identificador de un usuario, obtiene sus datos asociados

        :param p_id_usuario: El identificador de un usuario
        :return:
        """
        gestor_usuario = GestorUsuario.GestorUsuario()
        el_usuario = gestor_usuario.obtener_usuario(p_id_usuario)
        return el_usuario

    def obtener_datos_grupo(self, p_id_grupo):
        """
        Dado un identificador de un grupo, obtenemos sus datos asocaidos

        :param p_id_grupo: El identificador de un grupo
        :return:
        """
        gestor_grupo = GestorGrupo.GestorGrupo()
        el_grupo = gestor_grupo.obtener_grupo(p_id_grupo)
        return el_grupo