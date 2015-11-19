# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packModelo import Usuario
from PyQt5.QtWidgets import QTableWidgetItem

class ListaUsuario(object):

    def __init__(self):
        self.lista = []

    # Definimos los métodos

    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def tamano(self):
        return len(self.lista)

    def _obtener_iterador(self):
        return iter(self.lista)

    def existe(self, p_id_usuario, p_usuario):
        """
        Dado el usuario actual, vamos a ver si el usuario está o no disponible

        :param p_usuario: El usuario en cuestion
        :return: True -> Si encuenta al usuario
                False -> Si no lo encuentra
        """
        encontrado = False
        it = self._obtener_iterador()
        while not encontrado:
            try:
                usuario = it.next()
                if p_usuario == usuario.usuario and p_id_usuario != usuario.id_usuario:
                    encontrado = True
            except StopIteration:
                break
        return encontrado

    def obtener_usuario(self, p_id_usuario):
        """
        Dado un usuario devuelve un objeto de tipo usuario

        :param p_usuario:
        :return: Un usuario
        """
        encontrado = False
        usuario = None
        it = self._obtener_iterador()
        while not encontrado:
            try:
                usuario = it.next()
                if p_id_usuario == usuario.id_usuario:
                    encontrado = True
            except StopIteration:
                break
        return usuario


    def deconstruir(self):
        """
        Transformamos la lista en un array de diccionarios
        :return: Un array de diccionarios con los elementos de la lista
        """
        lista_dic = []
        for elemento in self.lista:
            lista_dic.append({'IdUsuario': elemento.id_usuario,
                              'Usuario': elemento.usuario,
                              'Contrasena': elemento.contrasena,
                              'Email': elemento.email,
                              'Nombre': elemento.nombre,
                              'Apellido': elemento.apellido,
                              'Dni': elemento.dni,
                              'F_Alta': elemento.f_alta
                              })
        return lista_dic

    def construir(self, p_lista_diccionario):
        """
        Construimos la lista a partir de los datos que nos trae un diccionario
        :param p_lista_diccionario: Un diccionario con los datos
        :return:
        """
        for diccionario in p_lista_diccionario:
            un_usuario = Usuario.Usuario(diccionario['IdUsuario'], diccionario['Usuario'],
                            diccionario['Contrasena'], diccionario['Email'],
                            diccionario['Nombre'], diccionario['Apellido'], diccionario['Dni'], diccionario['F_Alta'])
            self.lista.append(un_usuario)


    def generar_tabla(self, p_table_widged):
        """
        Genera una tabla con las entradas de la lista del historial

        :param p_table_widged: La tabla perteneciente a la interfaz
        :return:
        """
        p_table_widged.setRowCount(len(self.lista))
        for i in range(0, len(self.lista)):
            # Rellenamos la tabla
            usuario = self.lista[i]
            newitem = QTableWidgetItem(str(usuario.id_usuario))
            p_table_widged.setItem(i, 0, newitem)
            newitem = QTableWidgetItem(usuario.usuario)
            p_table_widged.setItem(i, 1, newitem)
            newitem = QTableWidgetItem(usuario.nombre)
            p_table_widged.setItem(i, 2, newitem)
            newitem = QTableWidgetItem(usuario.apellido)
            p_table_widged.setItem(i, 3, newitem)
            newitem = QTableWidgetItem(usuario.dni)
            p_table_widged.setItem(i, 4, newitem)
            newitem = QTableWidgetItem(usuario.email)
            p_table_widged.setItem(i, 5, newitem)
            newitem = QTableWidgetItem(usuario.f_alta.strftime("%d-%m-%Y"))
            p_table_widged.setItem(i, 6, newitem)
