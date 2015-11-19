# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packModelo import ListaScript
import GestorScript, GestorUsuario, GestorTag

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CAdminScripts(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_todos_scripts(self):
        """
        Obtiene todos los scripts en el sistema

        :return:
        """
        lista_scripts = ListaScript.ListaScript()
        gestor_script = GestorScript.GestorScript()
        resultado = gestor_script.obtener_todos_scripts()
        # Transformo el resultado
        lista_scripts.construir(resultado)
        return lista_scripts

    def obtener_aplicaciones_por_script(self, p_id_script):
        """
        Obtiene las aplicaciones existentes dado el identificador de un script determiando

        :param p_id_script: El identificador de un script
        :return: La lista con las aplicaciones de un script.
        """
        # La lista que devuelve no es tipo de dato es dick
        gestor_script = GestorScript.GestorScript()
        resultado_bd = gestor_script.obtener_aplicaciones_por_script(p_id_script)
        return resultado_bd

    def borrar_script(self, p_id_script):
        """
        Borra un script del sistema y elimina toda relación existente con cualquier usuario, alumno o tag

        :param p_id_script: El identificador del script
        :return:
        """
        gestor_script = GestorScript.GestorScript()
        gesto_usuario = GestorUsuario.GestorUsuario()
        gestor_tag = GestorTag.GestorTag()
        # Obtenemos la lista de tags afectado por el Script
        lista_tags = gestor_tag.obtener_tags_script(p_id_script)
        # Obtener todos los aplicados afectados por el borrado
        lista_aplicado = gestor_script.obtener_alumnos_aplicacion_script(p_id_script)
        # Obtener los usuarios que van a peder el Script
        lista_usuario = gesto_usuario.obtener_afectados_script(p_id_script)
        resultado = False
        enviar_mails = False
        for aplicado in lista_aplicado:
            # Borramos la aplicación asociada y su Script
            exito = gestor_script.eliminar_aplicacion_unitaria(p_id_script, aplicado['Dni'])
            if exito is True:
                enviar_mails = True
            else:
                enviar_mails = False
                break

        # Una vez eliminado las aplicaciones y los scripts se envian los mails a los afectados
        if enviar_mails is True:
            for usuario in lista_usuario:
                # Obtenemos sus datos
                email = gesto_usuario.obtener_mail(usuario['IdUsuario'])
                # todo enviar mail


        # Borrar el Script
        resultado_borrado = gestor_script.borrar_script(p_id_script)
        if resultado_borrado == 1:
            # Obtenemos si por cada TAg, queda algun script, en caso contrario, eliminamos el TAG
            for tag in lista_tags:
                lista_scripts = gestor_tag.obtener_scripts_del_tag(tag['IdTag'])
                if len(lista_scripts) == 0:
                    # Hay que borrar el TAg porque se ha quedado sin scripts
                    gestor_tag.borrar_tag(tag['IdTag'])
            resultado = True

        return resultado