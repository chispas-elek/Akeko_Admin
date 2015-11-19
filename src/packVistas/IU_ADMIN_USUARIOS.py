# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QMessageBox
from src.packControladoras import CAdminUsuarios
from src.packModelo import Usuario
import IU_ADMIN_ANADIR_USUARIO


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1121, 803)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tUsuarios = QtWidgets.QTableWidget(Form)
        self.tUsuarios.setObjectName("tUsuarios")
        self.tUsuarios.setColumnCount(7)
        self.tUsuarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/im-msn.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tUsuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/im-user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tUsuarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/format-text-subscript.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tUsuarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/format-text-superscript.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tUsuarios.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/document-edit-decrypt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tUsuarios.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/mail-mark-read.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.tUsuarios.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/view-calendar-day.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.tUsuarios.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tUsuarios)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bAnadir = QtWidgets.QPushButton(Form)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-add-user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAnadir.setIcon(icon7)
        self.bAnadir.setObjectName("bAnadir")
        self.horizontalLayout.addWidget(self.bAnadir)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bModificar = QtWidgets.QPushButton(Form)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/user-properties.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bModificar.setIcon(icon8)
        self.bModificar.setObjectName("bModificar")
        self.horizontalLayout.addWidget(self.bModificar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bEeliminar = QtWidgets.QPushButton(Form)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-remove-user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEeliminar.setIcon(icon9)
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
        self.tUsuarios.setWhatsThis(_translate("Form", "Muestra la información de cada Usuario registrado en el sistema. El objetivo es proveer una vista completa de los Usuarios existentes y la información más importante para eliminar o modificar los datos contenidos."))
        item = self.tUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Identificador"))
        item = self.tUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Usuario"))
        item = self.tUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nombre"))
        item = self.tUsuarios.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Apellidos"))
        item = self.tUsuarios.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Dni"))
        item = self.tUsuarios.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Email"))
        item = self.tUsuarios.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Fecha alta"))
        self.bAnadir.setToolTip(_translate("Form", "Añadir un nuevo usuario"))
        self.bAnadir.setText(_translate("Form", "Añadir usuario"))
        self.bModificar.setToolTip(_translate("Form", "Modificar el Usuario actualmente seleccionado"))
        self.bModificar.setText(_translate("Form", "Modificar usuario"))
        self.bEeliminar.setToolTip(_translate("Form", "Eliminar el usuario actualmente seleccionado"))
        self.bEeliminar.setText(_translate("Form", "Eliminar usuario"))

class AdminUsuarios(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_iu_admin_main,  parent=None):
        # Llamamos al constructor de la clase padre
        super(AdminUsuarios, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        # Modificamos las propiedades de la tabla para que no pueda ser editable y solo se pueda seleccionar 1 fila
        self.ventana.tUsuarios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ventana.tUsuarios.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ventana.tUsuarios.setSelectionMode(QAbstractItemView.SingleSelection)
        # Ajustamos la tabla para que haga un fit correcto con el espacio que tiene el layout.
        self.ventana.tUsuarios.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Inicializamos variables
        self.lista_usuarios = None
        self.controladora_usuarios = CAdminUsuarios.CAdminUsuarios()
        self.iu_admin_main = p_iu_admin_main

        # Deshabilitamos los botones de eliminar y modificar
        self.ventana.bModificar.setEnabled(False)
        self.ventana.bEeliminar.setEnabled(False)

        # Cargamos la tabla de usuarios
        self.generar_tabla()


        # Conectamos los botones
        self.ventana.bEeliminar.clicked.connect(self.eliminar_usuario)
        self.ventana.bAnadir.clicked.connect(self.anadir_usuario)
        self.ventana.bModificar.clicked.connect(self.modificar_usuario)

        self.window_anadir_usuario = None
        self.window_modificar_usuario = None
        self.window_eliminar_usuario = None

        # Condición de cerrar la ventana
        self.quiero_cerrar = True

    def anadir_usuario(self):
        """
        Añade un nuevo usuario en el sistema
        """
        self.window_anadir_usuario = IU_ADMIN_ANADIR_USUARIO.AdminAnadirUsuario(None, self.lista_usuarios, self)
        self.quiero_cerrar = False
        self.window_anadir_usuario.show()

    def modificar_usuario(self):
        """
        Modificamos los datos del usuario actualmente seleccionado
        """
        # Comprobar primero si al menos se tiene un usuario seleccionado.
        usuario_seleccionado = self.ventana.tUsuarios.selectionModel().selectedRows()
        id_usuario = None
        # Este for está preparado para procesar varias selecciones, en nuestro caso sólo hace 1
        for index in sorted(usuario_seleccionado):
            row = index.row()  # Se obtiene el número de la línea
            id_usuario = int(index.sibling(row, 0).data())  # Se obtiene el dato de la columna 0.
        if id_usuario is not None:
            el_usuario = self.lista_usuarios.obtener_usuario(id_usuario)
            self.window_modificar_usuario = IU_ADMIN_ANADIR_USUARIO.AdminAnadirUsuario(el_usuario,
                                                                                       self.lista_usuarios, self)
            self.window_modificar_usuario.show()
        else:
            # Error de seleccion
            error_box_1 = QMessageBox()
            error_box_1.setIcon(3)
            error_box_1.setWindowTitle("Panel de administración")
            error_box_1.setText("ERROR")
            error_box_1.setInformativeText("No has seleccionado nada")
            error_box_1.exec_()

    def eliminar_usuario(self):
        """
        Dado un usuario, elimina dicho usuario del sistema de forma permanente

        """
        # Comprobar primero si al menos se tiene un usuario seleccionado.
        usuario_seleccionado = self.ventana.tUsuarios.selectionModel().selectedRows()
        id_usuario = None
        # Este for está preparado para procesar varias selecciones, en nuestro caso sólo hace 1
        for index in sorted(usuario_seleccionado):
            row = index.row()  # Se obtiene el número de la línea
            id_usuario = int(index.sibling(row, 0).data())  # Se obtiene el dato de la columna 0.

        if id_usuario is not None:
            # Preguntamos si desea hacer o no el borrado
            warm_box = QMessageBox()
            warm_box.setIcon(2)
            warm_box.setWindowTitle("Panel de administración")
            warm_box.setText("¡¡Atención!!")
            warm_box.setInformativeText("¿Estás seguro que deseas eliminar el usuario?")
            warm_box.setDetailedText("La eliminación del usuario es una operación irreversible. Se borrarán todos los "
                                     "grupos, tags y aplicaciones que tuviera.")
            # Creamos los botones de aceptar y cancelar.
            warm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            warm_box.setDefaultButton(QMessageBox.Cancel)
            # Ejectuamos la interfaz y recogemos el resultado de la decisión
            seleccion = warm_box.exec_()
            if seleccion == QMessageBox.Ok:
                # Borramos al usuario
                exito = self.controladora_usuarios.borrar_usuario(id_usuario)
                if exito is True:
                    # El usuario se ha borrado de forma satisfactoria
                    # Mostramos confirmación
                    info_box = QMessageBox()
                    info_box.setIcon(1)
                    info_box.setWindowTitle("Panel de administración")
                    info_box.setText("CORRECTO")
                    info_box.setInformativeText("El usuario ha sido eliminado del sistema")
                    info_box.exec_()
                else:
                    # Algo no ha ido bien
                    error_box = QMessageBox()
                    error_box.setIcon(3)
                    error_box.setWindowTitle("Panel de administración")
                    error_box.setText("ERROR")
                    error_box.setInformativeText("Algo ha ocurrido y el usuario no se ha eliminado como deberia")
                    error_box.exec_()
                # Regenerar la tabla
                self.generar_tabla()
        else:
            # Error de seleccion
            error_box_1 = QMessageBox()
            error_box_1.setIcon(3)
            error_box_1.setWindowTitle("Panel de administración")
            error_box_1.setText("ERROR")
            error_box_1.setInformativeText("No has seleccionado nada")
            error_box_1.exec_()


    def generar_tabla(self):
        """
        Genera una tabla a partir de las entradas existentes en el historial

        """
        # Bloquemos las señales y vaciamos la tabla
        self.ventana.tUsuarios.blockSignals(True)
        # Modificar y setear el HEADER de la tabla.

        self.lista_usuarios = self.controladora_usuarios.obtener_usuarios()
        self.lista_usuarios.generar_tabla(self.ventana.tUsuarios)

        # Liberamos las señales
        self.ventana.tUsuarios.blockSignals(False)

        if self.lista_usuarios.tamano() != 0:
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
            super(AdminUsuarios, self).closeEvent(evnt)
        else:
            evnt.ignore()