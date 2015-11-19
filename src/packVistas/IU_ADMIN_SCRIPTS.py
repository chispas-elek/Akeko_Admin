# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QMessageBox
from src.packControladoras import CAdminScripts
import IU_ADMIN_ANADIRSCRIPT, IU_ADMIN_MOSTRAR_ALUMNO_SCRIPT_AFECTADO
from sys import argv

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(950, 645)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tScripts = QtWidgets.QTableWidget(Form)
        self.tScripts.setObjectName("tScripts")
        self.tScripts.setColumnCount(5)
        self.tScripts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/im-msn.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tScripts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/irc-operator.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tScripts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/documentinfo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tScripts.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/network-connect.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tScripts.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/irc-channel-active.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tScripts.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tScripts)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bAnadir = QtWidgets.QPushButton(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/irc-join-channel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAnadir.setIcon(icon5)
        self.bAnadir.setObjectName("bAnadir")
        self.horizontalLayout.addWidget(self.bAnadir)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bModificar = QtWidgets.QPushButton(Form)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/document-edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bModificar.setIcon(icon6)
        self.bModificar.setObjectName("bModificar")
        self.horizontalLayout.addWidget(self.bModificar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bEeliminar = QtWidgets.QPushButton(Form)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/irc-remove-operator.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEeliminar.setIcon(icon7)
        self.bEeliminar.setObjectName("bEeliminar")
        self.horizontalLayout.addWidget(self.bEeliminar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Panel de administración"))
        self.tScripts.setWhatsThis(_translate("Form", "Contiene la lista de los Scripts existentes en el sistema. Se podrá ver información detallada sobre cada script y se podrá elegir si se quiere activar o desactivar el script a necesidad del usuario para que éste sea mostrado o no a los usuarios."))
        item = self.tScripts.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Identificador"))
        item = self.tScripts.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tScripts.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Descripción"))
        item = self.tScripts.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Ruta"))
        item = self.tScripts.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Activado"))
        self.bAnadir.setToolTip(_translate("Form", "Añadir un nuevo Script"))
        self.bAnadir.setText(_translate("Form", "Añadir Script"))
        self.bModificar.setToolTip(_translate("Form", "Modificar el Script actualmente seleccionado"))
        self.bModificar.setText(_translate("Form", "Modificar Script"))
        self.bEeliminar.setToolTip(_translate("Form", "Borrar el Script actualmente seleccionado"))
        self.bEeliminar.setText(_translate("Form", "Eliminar Script"))


class AdminScripts(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_iu_admin_main, parent=None):
        # Llamamos al constructor de la clase padre
        super(AdminScripts, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        # Modificamos las propiedades de la tabla para que no pueda ser editable y solo se pueda seleccionar 1 fila
        self.ventana.tScripts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ventana.tScripts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ventana.tScripts.setSelectionMode(QAbstractItemView.SingleSelection)
        # Ajustamos la tabla para que haga un fit correcto con el espacio que tiene el layout.
        self.ventana.tScripts.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # inicializar valores
        self.controlador_scripts = CAdminScripts.CAdminScripts()
        self.lista_scripts = None
        self.iu_admin_main = p_iu_admin_main

        # Cargamos los datos
        self.cargar_datos()

        # Conectamos botones
        self.ventana.bAnadir.clicked.connect(self.anadir_script)
        self.ventana.bModificar.clicked.connect(self.modificar_script)
        self.ventana.bEeliminar.clicked.connect(self.eliminar_script)

        self.window_nuevo_script = None
        self.window_modificar_script = None
        self.window_borrar_script = None

        # Condición de cerrado
        self.quiero_cerrar = True

    def anadir_script(self):
        """
        Abre la interfaz de anadir un nuevo script

        :return:
        """
        self.window_nuevo_script = IU_ADMIN_ANADIRSCRIPT.AdminAnadirScript(None, self.lista_scripts, self)
        self.window_nuevo_script.show()

    def modificar_script(self):
        """
        Abre la interfaz de modificación de un nuevo script

        :return:
        """
        # Obtener el identificador del script actual
        script_seleccionado = self.ventana.tScripts.selectionModel().selectedRows()
        id_script = None
        # Este for está preparado para procesar varias selecciones, en nuestro caso sólo hace 1
        for index in sorted(script_seleccionado):
            row = index.row()  # Se obtiene el número de la línea
            id_script = int(index.sibling(row, 0).data())  # Se obtiene el dato de la columna 0.

        if id_script is not None:
            # Obtenemos los datos del script
            script = self.lista_scripts.obtener_script(id_script)
            self.window_modificar_script = IU_ADMIN_ANADIRSCRIPT.AdminAnadirScript(script, self.lista_scripts, self)
            self.window_modificar_script.show()
        else:
            # Error de seleccion
            error_box_1 = QMessageBox()
            error_box_1.setIcon(3)
            error_box_1.setWindowTitle("Panel de administración")
            error_box_1.setText("ERROR")
            error_box_1.setInformativeText("No has seleccionado nada")
            error_box_1.exec_()


    def eliminar_script(self):
        """
        Dado un script, elimina dicho script del sistema con todos los alumnos que lo tengan aplicado

        :return:
        """
        # Comprobar primero si al menos se tiene un usuario seleccionado.
        script_seleccionado = self.ventana.tScripts.selectionModel().selectedRows()
        id_script = None
        # Este for está preparado para procesar varias selecciones, en nuestro caso sólo hace 1
        for index in sorted(script_seleccionado):
            row = index.row()  # Se obtiene el número de la línea
            id_script = int(index.sibling(row, 0).data())  # Se obtiene el dato de la columna 0.

        if id_script is not None:
            # Preguntamos si desea hacer o no el borrado
            warm_box = QMessageBox()
            warm_box.setIcon(2)
            warm_box.setWindowTitle("Panel de administración")
            warm_box.setText("¡¡Atención!!")
            warm_box.setInformativeText("¿Estás seguro que deseas eliminar el script?")
            warm_box.setDetailedText("La eliminación de un script es una operación irreversible. Al eliminar un script"
                                     " éste será eliminado automáticamente de todos los usuarios del sistema y "
                                     "removido de todos los tags y grupos en el que esté. Además, si hay alumnos que "
                                     "tienen éste script, aplicado, será borrado y eliminado.")
            # Creamos los botones de aceptar y cancelar.
            warm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            warm_box.setDefaultButton(QMessageBox.Cancel)
            # Ejectuamos la interfaz y recogemos el resultado de la decisión
            seleccion = warm_box.exec_()
            if seleccion == QMessageBox.Ok:
                # Borramos al usuario
                # Tenemos que verificar si afecta o no a algún usuario el obrrado del script y mostrar acción a realizar
                exito = False
                lista_aplicados = self.controlador_scripts.obtener_aplicaciones_por_script(id_script)
                if len(lista_aplicados) != 0:
                    # Lllamamos a la interfaz para validar el borrado por parte del admin
                    self.window_borrar_script = IU_ADMIN_MOSTRAR_ALUMNO_SCRIPT_AFECTADO.AdminMostrarAlumnoScriptAfectado(lista_aplicados, id_script, self)
                    self.window_borrar_script.show()
                else:
                    # Nadie tiene el script aplicado, podemos borrarlo directamente
                    exito = self.controlador_scripts.borrar_script(id_script)
                    if exito is True:
                        print "Borrado ok"
                        info_box = QMessageBox()
                        info_box.setIcon(1)
                        info_box.setWindowTitle("Panel de administración")
                        info_box.setText("CORRECTO")
                        info_box.setInformativeText("El Script se ha borrado de forma satisfactoria del sistema")
                        info_box.exec_()
                        self.cargar_datos()
                    else:
                        print "Algo ha sucedido"

        else:
            # Error de seleccion
            error_box_1 = QMessageBox()
            error_box_1.setIcon(3)
            error_box_1.setWindowTitle("Panel de administración")
            error_box_1.setText("ERROR")
            error_box_1.setInformativeText("No has seleccionado nada")
            error_box_1.exec_()

    def cargar_datos(self):
        """
        Obtiene todos los scripts y los carga en la tabla correspondiente

        :return:
        """
        # Bloquemos las señales y vaciamos la tabla
        self.ventana.tScripts.blockSignals(True)
        # Modificar y setear el HEADER de la tabla.
        self.lista_scripts = self.controlador_scripts.obtener_todos_scripts()

        self.lista_scripts.generar_tabla(self.ventana.tScripts)

        # Liberamos las señales
        self.ventana.tScripts.blockSignals(False)

        if self.lista_scripts.tamano() != 0:
            # La tabla contiene elementos. Habilito los botones de modificar y eliminar
            self.ventana.bModificar.setEnabled(True)
            self.ventana.bEeliminar.setEnabled(True)
        else:
            # La tabla no contiene elementos, desactivo los botones
            self.ventana.bModificar.setEnabled(False)
            self.ventana.bEeliminar.setEnabled(False)

    def closeEvent(self, evnt):
        if self.quiero_cerrar:
            self.iu_admin_main.quiero_cerrar = True
            super(AdminScripts, self).closeEvent(evnt)
        else:
            evnt.ignore()
