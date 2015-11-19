# -*- coding: utf-8 -*-
__author__ = 'Rubén Mulero'

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from src.packControladoras import CAdminAnadirUsuario
from sys import argv
import re, random, string


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 565)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lNombre = QtWidgets.QLineEdit(self.groupBox)
        self.lNombre.setMaxLength(45)
        self.lNombre.setObjectName("lNombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lNombre)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lApellidos = QtWidgets.QLineEdit(self.groupBox)
        self.lApellidos.setMaxLength(45)
        self.lApellidos.setObjectName("lApellidos")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lApellidos)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lDni = QtWidgets.QLineEdit(self.groupBox)
        self.lDni.setMaxLength(10)
        self.lDni.setObjectName("lDni")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lDni)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lEmail = QtWidgets.QLineEdit(self.groupBox)
        self.lEmail.setMaxLength(60)
        self.lEmail.setObjectName("lEmail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lEmail)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cAutoGenerar = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.cAutoGenerar.setFont(font)
        self.cAutoGenerar.setObjectName("cAutoGenerar")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cAutoGenerar)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lContrasena = QtWidgets.QLineEdit(self.groupBox_2)
        self.lContrasena.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoPredictiveText)
        self.lContrasena.setMaxLength(45)
        self.lContrasena.setObjectName("lContrasena")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lContrasena)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lRepiteContrasena = QtWidgets.QLineEdit(self.groupBox_2)
        self.lRepiteContrasena.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoPredictiveText)
        self.lRepiteContrasena.setMaxLength(45)
        self.lRepiteContrasena.setObjectName("lRepiteContrasena")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lRepiteContrasena)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lUsuario = QtWidgets.QLineEdit(self.groupBox_2)
        self.lUsuario.setMaxLength(45)
        self.lUsuario.setObjectName("lUsuario")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lUsuario)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bAceptar = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-ok-apply.svg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAceptar.setIcon(icon)
        self.bAceptar.setObjectName("bAceptar")
        self.horizontalLayout.addWidget(self.bAceptar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bCancelar = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-remove.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.bCancelar.setIcon(icon1)
        self.bCancelar.setObjectName("bCancelar")
        self.horizontalLayout.addWidget(self.bCancelar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lNombre, self.lApellidos)
        Form.setTabOrder(self.lApellidos, self.lDni)
        Form.setTabOrder(self.lDni, self.lEmail)
        Form.setTabOrder(self.lEmail, self.lUsuario)
        Form.setTabOrder(self.lUsuario, self.cAutoGenerar)
        Form.setTabOrder(self.cAutoGenerar, self.lContrasena)
        Form.setTabOrder(self.lContrasena, self.lRepiteContrasena)
        Form.setTabOrder(self.lRepiteContrasena, self.bAceptar)
        Form.setTabOrder(self.bAceptar, self.bCancelar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Panel de administración"))
        self.groupBox.setTitle(_translate("Form", "Información personal del usuario"))
        self.label.setText(_translate("Form", "Nombre*:"))
        self.lNombre.setWhatsThis(_translate("Form", "Nombre del usuario a introducir."))
        self.label_2.setText(_translate("Form", "Apellidos*:"))
        self.lApellidos.setWhatsThis(_translate("Form", "Apellidos del usuario a introducir."))
        self.label_3.setText(_translate("Form", "DNI*:"))
        self.lDni.setWhatsThis(_translate("Form", "El Documento Nacional de Identidad del usuario a introducir."))
        self.label_4.setText(_translate("Form", "Email*:"))
        self.lEmail.setWhatsThis(_translate("Form",
                                            "El Email del usuario. Imprescidible para recibir cualquier tipo de aviso por parte del sistema"))
        self.groupBox_2.setTitle(_translate("Form", "Información de inicio de sesión"))
        self.label_5.setText(_translate("Form", "Método"))
        self.cAutoGenerar.setToolTip(
            _translate("Form", "¿Deseas generar la contraseña de forma automática o establecerla de manera manual?"))
        self.cAutoGenerar.setWhatsThis(_translate("Form",
                                                  "Permite decidir si se desea establecer la contrasña de forma automática o por ende, de forma manual.\n"
                                                  "\n"
                                                  "Al seleccionar ésta opción de deshabilitarán los campos de contraseña."))
        self.cAutoGenerar.setText(_translate("Form", "Auto-Generar contraseña"))
        self.label_6.setText(_translate("Form", "Contraseña*:"))
        self.lContrasena.setWhatsThis(_translate("Form", "Contraseña del usuario a introducir."))
        self.label_7.setText(_translate("Form", "Repite Contrseña*:"))
        self.lRepiteContrasena.setWhatsThis(_translate("Form",
                                                       "Repetición de la contraseña. Es importante para cercionarse de que ésta, ha sido correctamente introducida."))
        self.label_8.setText(_translate("Form", "Usuario*:"))
        self.lUsuario.setWhatsThis(_translate("Form",
                                              "El usuario del sistema. Esto junto con la contrasña son los requisitos para que un usuario pueda ser validado dentro del sistema."))
        self.bAceptar.setText(_translate("Form", "Aceptar"))
        self.bCancelar.setText(_translate("Form", "Cancelar"))


class AdminAnadirUsuario(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_usuario, p_lista_usuarios, p_iu_usuarios, parent=None):
        # Llamamos al constructor de la clase padre
        super(AdminAnadirUsuario, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        self.controlador_anadir_usuario = CAdminAnadirUsuario.CAdminAnadirUsuario()
        self.lista_usuarios = p_lista_usuarios
        self.usuario = p_usuario
        self.iu_usuarios = p_iu_usuarios

        # Configuro un valor por defecto para las contraseñas
        self.ventana.cAutoGenerar.setChecked(False)
        self.ventana.lContrasena.setEnabled(True)
        self.ventana.lRepiteContrasena.setEnabled(True)

        # descomentar ésto para que la contraseña no sea visible
        self.ventana.lContrasena.setEchoMode(QLineEdit.Password)
        self.ventana.lRepiteContrasena.setEchoMode(QLineEdit.Password)

        # Cargamos los datos si los hubiera
        self._cargar_datos()

        # Conectamos botones
        self.ventana.bCancelar.clicked.connect(self.close)
        self.ventana.bAceptar.clicked.connect(self.anadir_modificar_usuario)
        self.ventana.cAutoGenerar.clicked.connect(self.cambiar)

        # Configuramos la condición de cerrar
        self.quiero_cerrar = True

    def _cargar_datos(self):
        """
        Si estamos modificando un usuario. Carga los datos del mismo

        :return:
        """
        if self.usuario is not None:
            # Cagamos las ventnaas con sus valores
            self.ventana.lNombre.setText(self.usuario.nombre)
            self.ventana.lApellidos.setText(self.usuario.apellido)
            self.ventana.lDni.setText(self.usuario.dni)
            self.ventana.lEmail.setText(self.usuario.email)
            self.ventana.lUsuario.setText(self.usuario.usuario)
            self.ventana.lContrasena.setText(self.usuario.contrasena)
            self.ventana.lRepiteContrasena.setText(self.usuario.contrasena)

    def anadir_modificar_usuario(self):
        """
        Añade un nuevo usuario en el sistema o lo modifica

        :return:
        """
        exito = False
        # Aplicamos el filtrado de los campos
        resultado_filtrado = self._mascara_filtrado_datos()
        if resultado_filtrado is True:
            # Los datos introducidos son correctos.
            # Comprobamos el checkbox
            if self.ventana.cAutoGenerar.isChecked():
                # Auto-Generar Contraseña
                contrasena = ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _
                    in range(10))
                if self.usuario is not None:
                    exito = self.controlador_anadir_usuario.modificar_usuario(self.ventana.lNombre.text(),
                                                                              self.ventana.lApellidos.text(),
                                                                              self.ventana.lDni.text(),
                                                                              self.ventana.lEmail.text(),
                                                                              self.ventana.lUsuario.text(),
                                                                              contrasena,
                                                                              self.usuario.id_usuario,
                                                                              self.lista_usuarios)
                else:
                    exito = self.controlador_anadir_usuario.anadir_usuario(self.ventana.lNombre.text(),
                                                                           self.ventana.lApellidos.text(),
                                                                           self.ventana.lDni.text(),
                                                                           self.ventana.lEmail.text(),
                                                                           self.ventana.lUsuario.text(),
                                                                           contrasena,
                                                                           self.lista_usuarios)
            else:
                # Contraseña Manual
                if self.ventana.lContrasena.text() == self.ventana.lRepiteContrasena.text() and self.ventana.lContrasena != "":
                    # Añadimos
                    if self.usuario is not None:
                        exito = self.controlador_anadir_usuario.modificar_usuario(self.ventana.lNombre.text(),
                                                                              self.ventana.lApellidos.text(),
                                                                              self.ventana.lDni.text(),
                                                                              self.ventana.lEmail.text(),
                                                                              self.ventana.lUsuario.text(),
                                                                              self.ventana.lContrasena.text(),
                                                                              self.usuario.id_usuario,
                                                                              self.lista_usuarios)
                    else:
                        exito = self.controlador_anadir_usuario.anadir_usuario(self.ventana.lNombre.text(),
                                                                               self.ventana.lApellidos.text(),
                                                                               self.ventana.lDni.text(),
                                                                               self.ventana.lEmail.text(),
                                                                               self.ventana.lUsuario.text(),
                                                                               self.ventana.lContrasena.text(),
                                                                               self.lista_usuarios)
                else:
                    print "Las contraseñas no coinciden"
                    warm_box_2 = QMessageBox()
                    warm_box_2.setIcon(2)
                    warm_box_2.setWindowTitle("Panel de administración")
                    warm_box_2.setText("ADVERTENCIA")
                    warm_box_2.setInformativeText("Las contraseñas no coinciden, por favor introdúcelas bien")
                    warm_box_2.exec_()
                    self.ventana.lContrasena.setText("")
                    self.ventana.lRepiteContrasena.setText("")
        else:
            print "Existe algún error a la hora de borrar el alumno"
            warm_box = QMessageBox()
            warm_box.setIcon(2)
            warm_box.setWindowTitle("Panel de administración")
            warm_box.setText("ADVERTENCIA")
            warm_box.setInformativeText(resultado_filtrado)
            warm_box.exec_()


        # Coprobamos las operaciones finales
        if exito is True:
            # Ventana confirmación
            info_box = QMessageBox()
            info_box.setIcon(1)
            info_box.setWindowTitle("Panel de administración")
            info_box.setText("CORRECTO")
            info_box.setInformativeText("La operación se ha realizado satisfactoriamente")
            info_box.exec_()
            self.iu_usuarios.generar_tabla()
            self.close()
        elif exito is None:
            # El usuario ya existe
            warm_box_2 = QMessageBox()
            warm_box_2.setIcon(2)
            warm_box_2.setWindowTitle("Panel de administración")
            warm_box_2.setText("ADVERTENCIA")
            warm_box_2.setInformativeText("El usuario introducido, ya existe en el sistema.")
            warm_box_2.exec_()
        else:
            # Ventana error
            error_box = QMessageBox()
            error_box.setIcon(2)
            error_box.setWindowTitle("Panel de administración")
            error_box.setText("ERROR")
            error_box.setInformativeText("La operaación no se ha podido completar de forma correcta.")
            error_box.exec_()

    def cambiar(self):
        """
        Habilita o no los campos de contraseña dependiendo de si está o no activado el checkbox

        :return:
        """
        if self.ventana.cAutoGenerar.isChecked():
            # Deshabilitar
            self.ventana.lContrasena.setEnabled(False)
            self.ventana.lRepiteContrasena.setEnabled(False)
        else:
            self.ventana.lContrasena.setEnabled(True)
            self.ventana.lRepiteContrasena.setEnabled(True)

    def _mascara_filtrado_datos(self):
        """
        Revisa que los datos introducidos por el usuario son correctos.

        :return: True si todo ha ido bien
                Un texto de error si algo no ha salido bien
        """
        # Comprobamos el Dni
        patron_dni = re.compile("\d{8}[A-Z]$")
        if patron_dni.match(self.ventana.lDni.text()) and self.ventana.lDni.text() != "":
            print "dni ok"
            # Comprobamos el nombre
            patron_nombre = re.compile("[a-zA-Z]*$")
            if patron_nombre.match(self.ventana.lNombre.text()) and self.ventana.lNombre.text() != "":
                print "Nombre ok"
                patron_apellido = re.compile("[a-zA-Z]*\s[a-zA-Z]*$")
                if patron_apellido.match(self.ventana.lApellidos.text()) and self.ventana.lApellidos.text() != "":
                    print "apellido ok"
                    patron = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
                    if patron.match(self.ventana.lEmail.text()) and self.ventana.lEmail.text() != "":
                        print "Email ok"
                        patron_usuario = re.compile("[a-zA-Z0-9]*$")
                        if patron_usuario.match(self.ventana.lUsuario.text()) and self.ventana.lUsuario.text() != "":
                            print "ALL OK"
                            resultado = True
                        else:
                            resultado = "Usuario incorrecto"
                    else:
                        resultado = "Mail incorrecto"
                else:
                    resultado = "Apellido incorrecto"
            else:
                resultado = "Nombre incorrecto"
        else:
            resultado = "Dni incorrecto"

        return resultado

    def closeEvent(self, evnt):
        if self.quiero_cerrar:
            self.iu_usuarios.quiero_cerrar = True
            super(AdminAnadirUsuario, self).closeEvent(evnt)
        else:
            evnt.ignore()
