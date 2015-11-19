# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import Script
from PyQt5.QtWidgets import QTableWidgetItem


class ListaScript(object):
    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios

    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def _obtener_iterador(self):
        return iter(self.lista)

    def obtener_script(self, p_id_script):
        """
        Dado el identificador de un script. Obtiene el objeto del mismo

        :param p_id_script: El identificador del script
        :return: Un script
        """
        encontrado = False
        script = None
        it = self._obtener_iterador()
        while not encontrado:
            try:
                script = it.next()
                if p_id_script == script.id_script:
                    encontrado = True
            except StopIteration:
                break
        return script

    def tamano(self):
        """
        Obtiene el tamaño de la lista

        :return: El número de elementos que tiene la lista
        """

        return len(self.lista)

    def ya_existe(self, p_id_script, p_nombre_script):
        """
        Muesta si está disponible o no el nombre del script a aplicar

        :param p_id_script:
        :param p_nombre_script:
        :return: True -> Si el nombre del Script ya existe
                False -> Si el mombre del script no existe
        """
        encontrado = False
        it = self._obtener_iterador()
        while not encontrado:
            try:
                script = it.next()
                if p_nombre_script == script.nombre_s and p_id_script != script.id_script:
                    encontrado = True
            except StopIteration:
                break
        return encontrado

    def existe(self, p_elemento):
        """
        Comprueba si existe un elemento en la lista

        :param p_elemento: El elementoa  comprobar
        :return: True o False dependiendo si la lista contiene o no el elemento
        """
        encontrado = False
        it = self._obtener_iterador()
        while not encontrado:
            try:
                script = it.next()
                if p_elemento.id_script == script.id_script:
                    encontrado = True
            except StopIteration:
                break
        return encontrado

    def deconstruir(self):
        """
        Transformamos la lista en un array de diccionarios
        :return: Un array de diccionarios con los elementos de la lista
        """
        lista_dic = []
        for elemento in self.lista:
            lista_dic.append({'IdScript': elemento.id_script,
                              'NombreS': elemento.nombre_s,
                              'Descripcion': elemento.descripcion,
                              'Activo': elemento.activo,
                              'Ruta': elemento.ruta,
                              })
        return lista_dic

    def construir(self, p_lista_diccionario):
        """
        Construimos la lista a partir de los datos que nos trae un diccionario
        :param p_lista_diccionario: Un diccionario con los datos
        :return:
        """
        for diccionario in p_lista_diccionario:
            un_script = Script.Script(diccionario['IdScript'], diccionario['NombreScript'],
                                      diccionario['Descripcion'], diccionario['Activo'], diccionario['Ruta'])
            self.lista.append(un_script)


    def generar_tabla(self, p_table_widged):
        """
        Genera una tabla con las entradas de la lista del historial

        :param p_table_widged: La tabla perteneciente a la interfaz
        :return:
        """
        p_table_widged.setRowCount(len(self.lista))
        for i in range(0, len(self.lista)):
            # Rellenamos la tabla
            script = self.lista[i]
            newitem = QTableWidgetItem(str(script.id_script))
            p_table_widged.setItem(i, 0, newitem)
            newitem = QTableWidgetItem(script.nombre_s)
            p_table_widged.setItem(i, 1, newitem)
            newitem = QTableWidgetItem(script.descripcion)
            p_table_widged.setItem(i, 2, newitem)
            newitem = QTableWidgetItem(script.ruta)
            p_table_widged.setItem(i, 3, newitem)
            if script.activo == 1:
                newitem = QTableWidgetItem("Activado")
            else:
                newitem = QTableWidgetItem("Desactivado")
            p_table_widged.setItem(i, 4, newitem)
