# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packControladoras import GestorScript
import subprocess as sub

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CAdminAnadirScript(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def anadir_script(self, p_ruta, p_nombre_s, p_descripcion, p_activado):
        """
        Añade un nuevo script en la base de datos

        :return: True -> Todo ha ido bien
                 False -> Algo no ha ido bien
        """
        devolver = False
        p = sub.Popen(("shasum", p_ruta), stdout=sub.PIPE, stderr=sub.PIPE)
        salidas_sha, errores_sha = p.communicate()
        if len(salidas_sha) != 0 and len(errores_sha) == 0:
            # La salida ha dado un resultado positivo
            # Split y asignar
            salidas = salidas_sha.split()
            sha = salidas[0] # Asignación del SHA. Separamos el path que devuelve el comando
            # Llamamos al gestor e insertamos el script
            gestor_script = GestorScript.GestorScript()
            resultado_db = gestor_script.anadir_script(p_ruta, p_nombre_s, p_descripcion, sha, p_activado)
            if resultado_db == 1:
                # Inserción correcta
                devolver = True

        return devolver

    def modificar_script(self, p_id_script, p_nombre_s, p_descripcion, p_activado):
        """
        Modifica los valores que establezca el usuario.

        :param p_nombre: El nuevo nombre para el Script
        :param p_descripción: La nueva descripción para el Script
        :param p_activado: Si el script está o no activado
        :return: True -> Actualización correcta
                False -> algo ha pasado
        """
        devolver = False
        gestor_script = GestorScript.GestorScript()
        resultado_db = gestor_script.modificar_script(p_id_script, p_nombre_s, p_descripcion, p_activado)
        if resultado_db == 1:
            devolver = True
        return devolver