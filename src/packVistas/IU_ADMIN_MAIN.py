# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import IU_ADMIN_SCRIPTS, IU_ADMIN_USUARIOS
from sys import argv

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(748, 382)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bGestionarUsuarios = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/im-user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bGestionarUsuarios.setIcon(icon)
        self.bGestionarUsuarios.setObjectName("bGestionarUsuarios")
        self.horizontalLayout.addWidget(self.bGestionarUsuarios)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.bGestionarScripts = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/irc-operator.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bGestionarScripts.setIcon(icon1)
        self.bGestionarScripts.setObjectName("bGestionarScripts")
        self.horizontalLayout_2.addWidget(self.bGestionarScripts)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Panel de administración"))
        self.label.setText(_translate("Form", "Panel de administración"))
        self.bGestionarUsuarios.setText(_translate("Form", "Gestionar Usuarios del sistema"))
        self.bGestionarScripts.setText(_translate("Form", "Gestionar Scripts del sistema"))


class AdminMain(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, parent=None):
        # Llamamos al constructor de la clase padre
        super(AdminMain, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        # Conectamos botones
        self.ventana.bGestionarScripts.clicked.connect(self.gestionar_script)
        self.ventana.bGestionarUsuarios.clicked.connect(self.gestionar_usuario)

        # Inicializar interfaces
        self.window_admin_script = None
        self.window_admin_usuario = None

        # Condición de cerrar ventana
        self.quiero_cerrar = True

    def gestionar_script(self):
        if self.window_admin_script is None:
            self.window_admin_script = IU_ADMIN_SCRIPTS.AdminScripts(self)
        self.quiero_cerrar = False
        self.window_admin_script.show()

    def gestionar_usuario(self):
        if self.window_admin_usuario is None:
            self.window_admin_usuario = IU_ADMIN_USUARIOS.AdminUsuarios(self)
        self.quiero_cerrar = False
        self.window_admin_usuario.show()

    def closeEvent(self, evnt):
        if self.quiero_cerrar:
            super(AdminMain, self).closeEvent(evnt)
        else:
            evnt.ignore()
