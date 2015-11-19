# -*- encoding: utf-8 -*-

import sys
from os.path import dirname
from PyQt5.QtWidgets import QApplication
from src.packVistas import IU_ADMIN_MAIN

# Hacemos un appenr en el PYTHONPATH para que reconozca el sistema de imports de ésta app
sys.path.append(dirname(__file__))

# Lanzamos la pantalla principal del servidor
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = IU_ADMIN_MAIN.AdminMain()
    myapp.show()
    exit(app.exec_())
