# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packGestorBD import MySQLConnector
import subprocess as sub
import random
import string

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class GestorUsuario(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_usuarios(self):
        """
        Obtiene los usuarios del sistema

        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdUsuario,Usuario,Contrasena,Email,Nombre,Apellido,Dni,F_Alta FROM Usuario;"
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def anadir_usuario(self, p_nombre, p_apellido, p_dni, p_email, p_usuario, p_contrasena):
        """
        Añade un nuevo usuario al sistema. La contrasña se genera de forma automática

        :param p_nombre: El nombre del usuario
        :param p_apellido: El apellido del usuario
        :param p_dni: El Dni del usuario
        :param p_email: El email del usuario
        :param p_usuario: El nombre de acceso del usuario
        :param p_contrasena: La contraseña del usuario
        :return: El resultado de la inserción
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """INSERT INTO Usuario(Usuario,Contrasena,Email,Nombre,Apellido,Dni)
                    VALUES(%s,%s,%s,%s,%s,%s);""", (p_usuario, p_contrasena, p_email, p_nombre, p_apellido, p_dni)
        respuesta_bd = bd.execute(consulta)
        if respuesta_bd == 1:
            # El usuario ha sido añadido de forma correcta enviamos mail de alta
            self._enviar_mail(p_email, p_contrasena, p_usuario, True)
        return respuesta_bd

    def modificar_usuario(self, p_nombre, p_apellido, p_dni, p_email, p_usuario, p_contrasena, p_id_usuario):
        """
        Modifica los datos de un usuario que existe actualmente en el sistema.


        :param p_nombre: El nuevo nombre del usuario
        :param p_apellido: El nuevo apellido para el usuario
        :param p_dni: El nuevo Dni para el usuario
        :param p_email: El nueo email para el usario
        :param p_usuario: EL nuevo usuario para iniciar sesión
        :param p_contrasena: La nueva contraseña para iniciar sesión
        :param p_id_usuario: Su identificador único
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        # Antes de modificar al usuario, obtenemos los datos anteriores del msimo
        datos_usu = self.obtener_usuario(p_id_usuario)
        consulta = """UPDATE Usuario SET Usuario=%s,Contrasena=%s,Email=%s,Nombre=%s,Apellido=%s,Dni=%s
                    WHERE IdUsuario=%s""", (p_usuario, p_contrasena, p_email, p_nombre, p_apellido, p_dni, p_id_usuario)
        respuesta_bd = bd.execute(consulta)
        if datos_usu[0]['Usuario'] != str(p_usuario) or datos_usu[0]['Contrasena'] != str(p_contrasena):
            # Se han modificado los datos, enviamosm mail
            self._enviar_mail(p_email, p_contrasena, p_usuario, False)
        return respuesta_bd

    def eliminar_usuario(self, p_id_usuario):
        """
        Dado el identificador del usuario. Elimina del sistema el usuario.


        :param p_id_usuario: El identificador del usuario
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Usuario WHERE IdUsuario=%s", (p_id_usuario, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_usuario(self, p_id_usuario):
        """
        Dado un identificador de usuario, obtiene todos los datos concernientes al usuario

        :param p_id_usuario: El identificador del usuario
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT * FROM Usuario WHERE IdUsuario=%s;", (p_id_usuario, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_mail(self, p_id_usuario):
        """
        Dado el identificador de un usuario, obtenemos su email

        :param p_id_usuario: El identificador del usuario
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT Email FROM Usuario WHERE IdUsuario=%s", (p_id_usuario, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_afectados_script(self, p_id_script):
        """
        Dado un identificador de un script. Obtenemos la lista de los usuarios que han usado dicho script

        :param p_id_script: El identificador del script
        :return: La lista de usuarios afectados
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT DISTINCT IdUsuario FROM Aplicacion WHERE IdScript=%s", (p_id_script, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd


    # todo reimplementar ésto haciendo uso de templates
    def _enviar_mail(self, p_email_usuario, p_contrasena, p_usuario, p_accion):
        """
        Contienen el texto que va a representar el cuerpo del Mail a enviar.

        :param p_email_usuario: El mail del usuario
        :param p_contrasena: La contraseña del usuario
        :param p_usuario: El identificador de inicio de sesión
        :param p_accion: La acción a realizar
        :return: True o False dependiendo de si se ha enviado correctamente el mail
        """
        enviado = False
        if p_accion:
            # Enviamos mail añadir usuario
            file_mail = open("./edi/email_reg_user.txt")
            el_texto = file_mail.read()
            el_texto = el_texto.replace('%usuario', str(p_usuario))
            el_texto = el_texto.replace('%scontrasena', str(p_contrasena))
            file_mail.close()
        else:
            # Enviamos mail de modificación de usuario
            file_mail = open("./edi/email_modif_user.txt")
            el_texto = file_mail.read()
            el_texto = el_texto.replace('%usuario', str(p_usuario))
            el_texto = el_texto.replace('%contrasena', str(p_contrasena))
            file_mail.close()
        # Enviamos el mail
        p = sub.Popen(("/bin/bash", "./scripts/sent_mail.sh", el_texto, p_email_usuario),
                      stdout=sub.PIPE, stderr=sub.PIPE)
        salidas_mail, errores_mail = p.communicate()
        if salidas_mail == "ok\n" and len(errores_mail) == 0:
            # Send OK
            enviado = True

        return enviado
