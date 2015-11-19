# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packControladoras import GestorUsuario

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CAdminAnadirUsuario(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def anadir_usuario(self, p_nombre, p_apellido, p_dni, p_email, p_usuario, p_contrasena, p_lista_usuarios):
        """
        Añade un nuevo usuario en el sistema. La contraseña se genera de forma automática

        :param p_nombre: El nombre del usuario
        :param p_apellido: El apellido
        :param p_dni: Su Dni
        :param p_email: El email
        :param p_usuario: Qué nombre de usuario tendrá en el sistema
        :param p_contrasena: La contraseña del usuario
        :param p_lista_usuarios: La lista de los usuarios actuales
        :return: True -> Si todo ha ido bien
                False -> Si algo no ha ido bien
                None -> Si el usuario ya existe en el sistema
        """
        # Comprobamos que no exista el mismo usuario registrado en el sistema
        ya_existe = p_lista_usuarios.existe(-1, p_usuario)
        if ya_existe is not True:
            # El usuario no existe en el sistema
            gestor_usu = GestorUsuario.GestorUsuario()
            resultado = gestor_usu.anadir_usuario(p_nombre, p_apellido, p_dni, p_email, p_usuario, p_contrasena)
            if resultado == 1:
                resultado = True
            else:
                resultado = False
        else:
            # El usuario ya existe en el sistema
            print "Ya existe el usuario en el sistema"
            resultado = None

        return resultado

    def modificar_usuario(self, p_nombre, p_apellido, p_dni, p_email, p_usuario, p_contrasena, p_id_usuario,
                          p_lista_usuarios):
        """
        Modifica el usuario actual

        :param p_nombre: El nombre del usuario
        :param p_apellido: El apellido del usuario
        :param p_dni: El dni del usuario
        :param p_email: El Email del usuario
        :param p_usuario:
        :param p_contrasena:
        :param p_id_usuario:
        :param p_lista_usuarios:
        :return:
        """
        # Comprobamos que no exista el mismo usuario registrado en el sistema
        ya_existe = p_lista_usuarios.existe(p_id_usuario, p_usuario)
        if ya_existe is not True:
            # El usuario no existe en el sistema
            gestor_usu = GestorUsuario.GestorUsuario()
            resultado = gestor_usu.modificar_usuario(p_nombre, p_apellido, p_dni, p_email, p_usuario, p_contrasena,
                                                     p_id_usuario)
            if resultado == 1:
                resultado = True
            else:
                resultado = False
        else:
            # El usuario ya existe en el sistema
            print "Ya existe el usuario en el sistema"
            resultado = None

        return resultado