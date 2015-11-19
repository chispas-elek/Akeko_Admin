# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog, QMessageBox
import re
from src.packControladoras import CAdminAnadirScript
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 310)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lRuta = QtWidgets.QLineEdit(Form)
        self.lRuta.setMaxLength(250)
        self.lRuta.setObjectName("lRuta")
        self.horizontalLayout.addWidget(self.lRuta)
        self.bElegirRuta = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/network-connect.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bElegirRuta.setIcon(icon)
        self.bElegirRuta.setObjectName("bElegirRuta")
        self.horizontalLayout.addWidget(self.bElegirRuta)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lNombreBD = QtWidgets.QLineEdit(Form)
        self.lNombreBD.setMaxLength(20)
        self.lNombreBD.setObjectName("lNombreBD")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lNombreBD)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lDesc = QtWidgets.QLineEdit(Form)
        self.lDesc.setMaxLength(150)
        self.lDesc.setObjectName("lDesc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lDesc)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bAceptar = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-ok.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAceptar.setIcon(icon1)
        self.bAceptar.setObjectName("bAceptar")
        self.horizontalLayout_2.addWidget(self.bAceptar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.bCancelar = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCancelar.setIcon(icon2)
        self.bCancelar.setObjectName("bCancelar")
        self.horizontalLayout_2.addWidget(self.bCancelar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.label.setBuddy(self.lRuta)
        self.label_2.setBuddy(self.lNombreBD)
        self.label_3.setBuddy(self.lDesc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lRuta, self.bElegirRuta)
        Form.setTabOrder(self.bElegirRuta, self.lNombreBD)
        Form.setTabOrder(self.lNombreBD, self.lDesc)
        Form.setTabOrder(self.lDesc, self.bAceptar)
        Form.setTabOrder(self.bAceptar, self.bCancelar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Panel de administración"))
        self.label.setText(_translate("Form", "R&uta*:"))
        self.lRuta.setWhatsThis(_translate("Form", "La ruta completa donde se encuentra el script a introducir en la BD. Se puede introducir a mano o dejar que el botón rellene la casilla de manera automática"))
        self.bElegirRuta.setToolTip(_translate("Form", "Pulsa para elegir la ruta con el administrador de archivos del sistema."))
        self.bElegirRuta.setText(_translate("Form", "Elegir ruta"))
        self.label_2.setText(_translate("Form", "Nombre en &la BD*:"))
        self.lNombreBD.setWhatsThis(_translate("Form", "El nombre que debe tener el script en la base de datos. Es importante darle un nombre apropiado para después poder identificar el Script de manera correcta."))
        self.label_3.setText(_translate("Form", "Descripci&ón*:"))
        self.lDesc.setWhatsThis(_translate("Form", "Descripción del Script para mostrar al Usuario. Se recomienda ser explícito y muy claro a la hora de dar una descripción."))
        self.label_4.setText(_translate("Form", "¿Activado?"))
        self.bAceptar.setText(_translate("Form", "Aceptar"))
        self.bCancelar.setText(_translate("Form", "Cancelar"))

class AdminAnadirScript(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_script, p_lista_script, p_iu_admin_scripts, parent=None):
        # Llamamos al constructor de la clase padre
        super(AdminAnadirScript, self).__init__(parent)
        self.el_parent = parent
        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        # inicializar valores
        self.script = p_script
        self.lista_script = p_lista_script
        self.controlador_script = CAdminAnadirScript.CAdminAnadirScript()
        self.iu_admin_scripts = p_iu_admin_scripts

        # Cargar datos
        self._cargar_datos()

        # Conectamos botones
        self.ventana.bElegirRuta.clicked.connect(self.cargar_fichero)
        self.ventana.bAceptar.clicked.connect(self.anadir_modificar_script)
        self.ventana.bCancelar.clicked.connect(self.close)

    def _cargar_datos(self):
        """
        Em casp se estar , modificando un script. Carga los datos necesarios

        :return:
        """
        if self.script is not None:
            self.ventana.lRuta.setDisabled(True)
            self.ventana.bElegirRuta.setDisabled(True)
            self.ventana.lRuta.setText(self.script.ruta)
            self.ventana.lNombreBD.setText(self.script.nombre_s)
            self.ventana.lDesc.setText(self.script.descripcion)
            self.ventana.checkBox.setChecked(self.script.activo)


    def cargar_fichero(self):
        """
        Abre un diálogo de carga y permite introducir un fichero con extensión *.sh

        :return:
        """
        filename = QFileDialog.getOpenFileName(
            # self.el_parent, 'Open File', '', 'Images (*.png *.xpm *.jpg)',
            self.el_parent, 'Importar script', '', 'Archivo de script ejecutable (*.sh)',
            None, QFileDialog.DontUseNativeDialog)

        self.ventana.lRuta.setText(filename[0])

    def anadir_modificar_script(self):
        """
        Añade o modifica un Script en el sistema

        :return:
        """
        # Primero vamos a validar si los datos son correctos
        resultado = self._mascara_filtrado_datos()
        if resultado is True:
            if self.script is None:
                # Generamos un nuevo Script
                # Antes te proceder debemos comprobar que la ruta sea un archivo que se pueda abrir
                fichero_valido = self._validar_script(self.ventana.lRuta.text())
                if fichero_valido is True:
                    # Comprobar que no exista de antemano el nombre del script
                    ya_existe = self.lista_script.ya_existe(-1, self.ventana.lNombreBD.text())
                    if ya_existe is not True:
                        # Podemos insertar sin miedo
                        # todo seria necesario comprobar la ruta del script para saber si es duplicada?
                        exito = self.controlador_script.anadir_script(self.ventana.lRuta.text(),
                                                                      self.ventana.lNombreBD.text(),
                                                                      self.ventana.lDesc.text(),
                                                                      self.ventana.checkBox.isChecked())
                        if exito is True:
                            # ventana de confirmación
                            info_box = QMessageBox()
                            info_box.setIcon(1)
                            info_box.setWindowTitle("Panel de administración")
                            info_box.setText("INFORMACIÓN")
                            info_box.setInformativeText("El Script se ha creado correctamente")
                            info_box.exec_()
                            self.iu_admin_scripts.cargar_datos()
                            self.close()
                    else:
                        # EL nombre del script no está disponible
                        warm_box_2 = QMessageBox()
                        warm_box_2.setIcon(2)
                        warm_box_2.setWindowTitle("Panel de administración")
                        warm_box_2.setText("ADVERTENCIA")
                        warm_box_2.setInformativeText("El nombre del Script para la BD ya existe")
                        warm_box_2.exec_()
                else:
                    # Error
                    error_box = QMessageBox()
                    error_box.setIcon(3)
                    error_box.setWindowTitle("Panel de administración")
                    error_box.setText("ERROR")
                    error_box.setInformativeText("Parece que el fichero que has añadido no tiene mucha pinta de ser un "
                                                 "script en BashScripting. Revisa que esté correcto")
                    error_box.exec_()
            else:
                # Modificar el script actual
                # Validamos si el nombre existe o no.
                ya_existe = self.lista_script.ya_existe(self.script.id_script, self.ventana.lNombreBD.text())
                if ya_existe is not True:
                    # Actualizamos
                    exito = self.controlador_script.modificar_script(self.script.id_script,
                                                                     self.ventana.lNombreBD.text(),
                                                                     self.ventana.lDesc.text(),
                                                                     self.ventana.checkBox.isChecked())
                    if exito is True:
                        info_box_2 = QMessageBox()
                        info_box_2.setIcon(1)
                        info_box_2.setWindowTitle("Panel de administración")
                        info_box_2.setText("INFORMACIÓN")
                        info_box_2.setInformativeText("El Script se ha modificado correctamente")
                        info_box_2.exec_()
                        self.iu_admin_scripts.cargar_datos()
                        self.close()
                else:
                    # El nombre del script no está disponible
                    warm_box_3 = QMessageBox()
                    warm_box_3.setIcon(2)
                    warm_box_3.setWindowTitle("Panel de administración")
                    warm_box_3.setText("ADVERTENCIA")
                    warm_box_3.setInformativeText("El nombre del Script para la BD ya existe")
                    warm_box_3.exec_()
        else:
            warm_box = QMessageBox()
            warm_box.setIcon(2)
            warm_box.setWindowTitle("Panel de administración")
            warm_box.setText("ADVERTENCIA")
            warm_box.setInformativeText(resultado)
            warm_box.exec_()

    def _validar_script(self, p_filename):
        """
        Dada una ruta determinada, valida si el Script es válido o no

        :param p_filename: El path que contiene el Script a validar
        :return: True -> Script aparentemente correcto
                False -> Script incorrecto
        """
        resultado = False
        try:
            fichero = open(p_filename, 'r')
            # Obtengo la primera linea del fichero
            cabecera = fichero.readline()
            # Ponemos uan condición por la cabecera tenga al menos el SHABANG de /bin/bash
            if cabecera.lower() == "#!/bin/bash\n":
                resultado = True
        except (IOError, OSError) as e:
            print "Ha ocurrido un error al abrir el archivo: "
            print e

        return resultado

    def _mascara_filtrado_datos(self):
        """
        Revisa que los datos introducidos por el usuario son correctos.

        :return: True si todo ha ido bien
                Un texto de error si algo no ha salido bien
        """

        # Comprobamos el nombre de la bd
        patron_nombre_bd = re.compile("[a-zA-Z0-9]*$")
        if patron_nombre_bd.match(self.ventana.lNombreBD.text()) and self.ventana.lNombreBD.text() != "":
            print "Nombre en la BD ok"
            # Comprobamos que al menos la descripción tenga algún dato
            if self.ventana.lDesc.text() != "":
                print "Descripción ok"
                # Comprobamos que la ruta tenga elementos
                if self.ventana.lRuta.text() != "":
                    print "Todo Ok"
                    resultado = True
                else:
                    resultado = "La ruta del fichero está vacía"
            else:
                resultado = "Introduce al menos una descripción válida"
        else:
            resultado = "Nombre para la base de datos incorrecto"

        return resultado
