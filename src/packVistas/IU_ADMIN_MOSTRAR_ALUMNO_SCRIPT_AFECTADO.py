# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QTableWidgetItem, QMessageBox
from src.packControladoras import CAdminMostrarAlumnoScriptAfectado, CAdminScripts

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(920, 582)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.tAlumnosAfectados = QtWidgets.QTableWidget(Form)
        self.tAlumnosAfectados.setObjectName("tAlumnosAfectados")
        self.tAlumnosAfectados.setColumnCount(5)
        self.tAlumnosAfectados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/format-text-subscript.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tAlumnosAfectados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/format-text-superscript.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tAlumnosAfectados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/document-edit-decrypt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tAlumnosAfectados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/im-invisible-user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tAlumnosAfectados.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/view-calendar-day.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tAlumnosAfectados.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tAlumnosAfectados)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bConfirmar = QtWidgets.QPushButton(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-ok-apply.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bConfirmar.setIcon(icon5)
        self.bConfirmar.setObjectName("bConfirmar")
        self.horizontalLayout.addWidget(self.bConfirmar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bCancelar = QtWidgets.QPushButton(Form)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCancelar.setIcon(icon6)
        self.bCancelar.setObjectName("bCancelar")
        self.horizontalLayout.addWidget(self.bCancelar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Panel de administración"))
        self.label.setText(_translate("Form", "¡¡¡ATENCIÓN!!!"))
        self.label_2.setText(_translate("Form", "Los siguientes alumnos son afectados por la eliminación del Script."))
        self.tAlumnosAfectados.setWhatsThis(_translate("Form", "En ésta tabla se muestran aquellos alumnos que son afectados por la eliminación del script. Es imperativo revisar bien todo antes de proceder con el borrado."))
        item = self.tAlumnosAfectados.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre"))
        item = self.tAlumnosAfectados.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Apellidos"))
        item = self.tAlumnosAfectados.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Dni"))
        item = self.tAlumnosAfectados.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Profesor"))
        item = self.tAlumnosAfectados.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fecha Aplicación"))
        self.bConfirmar.setToolTip(_translate("Form", "Confirma la eliminación del Script."))
        self.bConfirmar.setText(_translate("Form", "Confirmar eliminación"))
        self.bCancelar.setWhatsThis(_translate("Form", "Cancela la acción."))
        self.bCancelar.setText(_translate("Form", "Cancelar"))

class AdminMostrarAlumnoScriptAfectado(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_lista_aplicacion_afectados, p_id_script, p_iu_admin_scripts, parent=None):
        # Llamamos al constructor de la clase padre
        super(AdminMostrarAlumnoScriptAfectado, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        # Modificamos las propiedades de la tabla para que no pueda ser editable y solo se pueda seleccionar 1 fila
        self.ventana.tAlumnosAfectados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ventana.tAlumnosAfectados.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ventana.tAlumnosAfectados.setSelectionMode(QAbstractItemView.SingleSelection)
        # Ajustamos la tabla para que haga un fit correcto con el espacio que tiene el layout.
        self.ventana.tAlumnosAfectados.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Inicializar valores
        self.id_script = p_id_script
        self.lista_aplicacion_afectados = p_lista_aplicacion_afectados
        self.controlador_scripts = CAdminScripts.CAdminScripts()
        self.controlador_admin_mostrar_alum_scrpt_afec = CAdminMostrarAlumnoScriptAfectado.CAdminMostrarAlumnoScriptAfectado()
        self.iu_admin_scripts = p_iu_admin_scripts

        # Cargamos los datos en la tabla
        self._cargar_datos()

        # Conectamos botones
        self.ventana.bCancelar.clicked.connect(self.close)
        self.ventana.bConfirmar.clicked.connect(self.borrar_script)

    def borrar_script(self):
        """
        El usuario acepta borrar

        :return:
        """
        # Ultima ventana de advertencia
        warm_box = QMessageBox()
        warm_box.setIcon(2)
        warm_box.setWindowTitle("Panel de administración")
        warm_box.setText("¡¡Atención!!")
        warm_box.setInformativeText("¿Estás seguro al 140% de querer hacer ésto?")
        warm_box.setDetailedText("Revisa bien todos los datos antes de proceder. Ésta operación NO SE PODRÁ"
                                     "DESHACER UNA VEZ REALIZADA")
        # Creamos los botones de aceptar y cancelar.
        warm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warm_box.setDefaultButton(QMessageBox.Cancel)
        # Ejectuamos la interfaz y recogemos el resultado de la decisión
        seleccion = warm_box.exec_()
        if seleccion == QMessageBox.Ok:
            exito = self.controlador_scripts.borrar_script(self.id_script)
            if exito is True:
                info_box = QMessageBox()
                info_box.setIcon(1)
                info_box.setWindowTitle("Panel de administración")
                info_box.setText("CORRECTO")
                info_box.setInformativeText("El Script ha sido completamente eliminado del sistema")
                info_box.exec_()
                self.iu_admin_scripts.cargar_datos()
                self.close()
            else:
                # Algo nada bueno ha sucedido
                error_box = QMessageBox()
                error_box.setIcon(1)
                error_box.setWindowTitle("Panel de administración")
                error_box.setText("ERROR")
                error_box.setInformativeText("Algo ha sucedido a la hora de borrar el script")
                error_box.exec_()

    def _cargar_datos(self):
        # Bloquemos las señales y vaciamos la tabla
        self.ventana.tAlumnosAfectados.blockSignals(True)

        self.ventana.tAlumnosAfectados.setRowCount(len(self.lista_aplicacion_afectados))
        for i in range(0, len(self.lista_aplicacion_afectados)):
            # Rellenamos la tabla
            afectado = self.lista_aplicacion_afectados[i]
            # Obtener nombre y apellido del afectado
            el_usuario = self.controlador_admin_mostrar_alum_scrpt_afec.obtener_datos_alumno(afectado['Dni'])
            newitem = QTableWidgetItem(el_usuario[0]['Nombre'])
            self.ventana.tAlumnosAfectados.setItem(i, 0, newitem)
            newitem = QTableWidgetItem(el_usuario[0]['Apellido'])
            self.ventana.tAlumnosAfectados.setItem(i, 1, newitem)
            newitem = QTableWidgetItem(el_usuario[0]['Dni'])
            self.ventana.tAlumnosAfectados.setItem(i, 2, newitem)
            # Obtenemos los datos del usuario
            el_usuario = self.controlador_admin_mostrar_alum_scrpt_afec.obtener_datos_usuario(afectado['IdUsuario'])
            newitem = QTableWidgetItem(el_usuario[0]['Nombre'] + " " + el_usuario[0]['Apellido'])
            self.ventana.tAlumnosAfectados.setItem(i, 3, newitem)
            newitem = QTableWidgetItem(afectado['FechaA'].strftime("%d-%m-%Y"))
            self.ventana.tAlumnosAfectados.setItem(i, 4, newitem)

        # Liberamos las señales
        self.ventana.tAlumnosAfectados.blockSignals(False)