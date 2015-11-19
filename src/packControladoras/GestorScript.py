# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


import subprocess as sub
from src.packGestorBD import MySQLConnector


class Singleton(type):
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance


class GestorScript(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def anadir_script(self, p_ruta, p_nombre_s, p_descripcion, p_sha, p_activado):
        """
        Añade un nuevo script en la BD

        :param p_ruta: El path que contiene dónde se encuentra ubicado el Script
        :param p_nombre: El nombre que se le ha dado al script
        :param p_descripcion: La descripción del Script
        :param p_sha: La suma de verificación SHA para introducir.
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """INSERT INTO Script(NombreScript,Descripcion,Activo,Ruta,SHA) VALUES
                    (%s,%s,%s,%s,%s);""", (p_nombre_s, p_descripcion, p_activado, p_ruta, p_sha)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def modificar_script(self, p_id_script, p_nombre_s, p_descripcion, p_activado):
        """
        Modifica los datos del script.

        :param p_id_script: El identificador del script
        :param p_nombre_s: El nuevo nombre del Script
        :param p_descripcion: La descripción del Script
        :param p_activado: Si el script está o no activado
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "Update Script set NombreScript=%s,Descripcion=%s,Activo=%s WHERE idScript=%s;", \
                   (p_nombre_s, p_descripcion, p_activado, p_id_script)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def borrar_script(self, p_id_script):
        """
        Dado el identificador de un Script. Borra del la BD el script

        :param p_id_script:
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Script WHERE IdScript=%s", (p_id_script, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_todos_scripts(self):
        """
        Obtiene todos los scripts existentes en el sistema

        :return: La lista con la información de todos los Scripts registrados en el sistema
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdScript,NombreScript,Descripcion,Activo,Ruta From Script;"
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_aplicaciones(self, p_id_usuario):
        """
        Dado el identificador del usuario. Obtenemos todas las aplicaciones que existan

        :param p_id_usuario: El identificador del usuario
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdScript,Dni,IdUsuario,IdGrupo,FechaA FROM Aplicacion WHERE IdUsuario=%s;", (p_id_usuario, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_aplicaciones_por_script(self, p_id_script):
        """
        Dado el identificador de un script. Obtenemos todos los grupos, profesores y alumnos afectados por un script

        :param p_id_script: El identificador de un script
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdScript,Dni,IdUsuario,IdGrupo,FechaA FROM Aplicacion WHERE IdScript=%s;", (p_id_script, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_alumnos_aplicacion_script(self, p_id_script):
        """
        Dado el identificador de un script. Obtenemos todas las aplicaciones de los alumnos afectados por dicho script

        :param p_id_script: El identificador de un script
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT DISTINCT Dni FROM Aplicacion WHERE IdScript=%s;", \
                   (p_id_script, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def eliminar_aplicaciones(self, p_id_usuario):
        """
        Dado un identificador de usuario. Borra todas las aplicaciones existentes

        :param p_id_usuario:
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Aplicacion WHERE IdUsuario=%s", (p_id_usuario, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def eliminar_aplicacion_unitaria(self, p_id_script, p_dni):
        """
        Borra una aplicación única en el sistema

        :param p_id_script:
        :param p_dni:
        :param p_id_usuario:
        :param p_id_grupo:
        :return: True -> Todo ha ido bien
                False -> Algo ha ocurrido
        """
        devolver = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Aplicacion WHERE IdScript=%s AND Dni=%s;", (p_id_script, p_dni)
        respuesta_bd = bd.execute(consulta)
        if respuesta_bd == 1:
            # Una vez borrada la intención. Borramos el script del alumno
            exito = self._execute_script(p_id_script, p_dni, False)
            if exito is True:
                devolver = True
        return devolver

    def comprobar_intencion(self, p_id_script, p_dni):
        """
        Dado el script y el alumno actual. Comprueba si le es necesario quitarle o no un script a cada aluumno.
        En caso afirmativo elimina el script. Si no, no hace nada.

        :param p_id_script: El identificador del script
        :param p_dni: El dni del alumno
        :return:
        """
        actualizar_bd = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdScript FROM Aplicacion WHERE IdScript=%s AND Dni=%s;", (p_id_script, p_dni)
        respuesta_bd = bd.execute(consulta)
        if len(respuesta_bd) != 0:
            # Aún hay más valores
            actualizar_bd = True
        else:
            # Ya no queda más intenciones por lo que debemos eliminar el script
            resultado = self._execute_script(p_id_script, p_dni, False)
            if resultado:
                # Al alumno se le ha revocado el script que tenia aplicado
                actualizar_bd = True
            else:
                # Ha ocurrido un error garrafal, raiseo exception y controlo la salida
                pass
        return actualizar_bd

    def _execute_script(self, p_id_script, p_dni, p_accion):
        """
        Aplicamos un script
        :param p_id_script: El identificador del Script
        :param p_dni: El Dni del alumno
        :param p_accion: True -> Ejecuta el Script añadiendo datos
                        False -> Ejecuta el Script eliminando datos
        :return: True o False dependiendo del éxito de la aplicación del script
        """
        correcto = False
        # Comprobar si la suma de verificación SHA-1 es correcta y en caso positivo continuar
        bd = MySQLConnector.MySQLConnector()
        consulta_1 = "SELECT Ruta,SHA FROM Script WHERE IdScript=%s;", (p_id_script,)
        respuesta_bd = bd.execute(consulta_1)
        if len(respuesta_bd) != 0:
            consulta_2 = "SELECT Email FROM Alumno WHERE Dni=%s;", (p_dni,)
            respuesta_bd_2 = bd.execute(consulta_2)
            if len(respuesta_bd_2) != 0:
                # Obtenemos el nombre de usuario del mail para usarlo como identificador en los servicios
                ident_alumno = respuesta_bd_2[0]['Email'].split("@")[0]
                # Obtenemos la Ruta del script
                p = sub.Popen(("shasum", respuesta_bd[0]['Ruta']), stdout=sub.PIPE, stderr=sub.PIPE)
                salidas_sha, errores_sha = p.communicate()
                if len(salidas_sha) != 0:
                    # Comprobamos los SHA de la BD con el del archivo
                    salidas = salidas_sha.split()
                    if respuesta_bd[0]['SHA'] == salidas[0]:
                        # Los SHA coinciden, podemos ejecutar el script
                        p = sub.Popen(("/bin/bash", respuesta_bd[0]['Ruta'], ident_alumno, str(p_accion)),
                                      stdout=sub.PIPE, stderr=sub.PIPE)
                        salidas, errores = p.communicate()
                        if len(salidas) != 0 and len(errores) == 0:
                            print salidas
                            salidas = salidas.split('\n', 2)
                            if salidas[0] == "borrado":
                                # Se ha hecho una eliminación
                                correcto = self._enviar_mail(respuesta_bd_2[0]['Email'], p_descripcion=salidas[1])
                            else:
                                # El script se ha aplicado correctamente. Por lo tanto, enviaremos un mail con los cambios
                                # hacemos un slipt del usuario y contraseña que nos deevuelve el script
                                correcto = self._enviar_mail(respuesta_bd_2[0]['Email'], salidas[0], salidas[1],
                                                             salidas[2])
                        else:
                            # El script no se ha podido aplicar bien, raise exception
                            print errores
                    else:
                        # Error, los SHA NO son iguales. Raise exception
                        print "El SHA no coincide con el de la BD"
                else:
                    # Error garrafal, raiseamos exception
                    print errores_sha

        return correcto

    def _enviar_mail(self, p_email_alumno, p_ident_alumno=None, p_contrasena=None, p_descripcion=None):
        """
        Contienen el texto que va a representar el cuerpo del Mail a enviar.

        :param p_ident_alumno: Identificador del alumno (Login)
        :param p_contrasena: Contraseña del alumno
        :param p_email_alumno: El mail del alumno a enviar
        :param p_descripcion: Descripción del script.
        :return: True o False dependiendo de si se ha enviado correctamente el mail
        """
        enviado = False
        if p_ident_alumno is None:
            # Se ha eliminado un alumno
            el_texto = """
                        Hola.

                        El acceso a tu usuario en: %s ha sido eliminado.

                        Ya no podrás loguearte más haciendo uso de tu usuario y contraseña.

                        Un saludo.


                        PD: Éste mail ha sido enviado de manera automática, por favor, no responda a ésta dirección.

                        """ % p_descripcion
        else:
            # Se ha añadido un alumno
            el_texto = """
                        Hola.

                        Se ha generado un acceso en: %s

                        Tus datos para poder acceder a éste servicio, son los siguientes:

                        --> Usuario: %s
                        --> Contraseña: %s

                        Un saludo.


                        PD: Éste mail ha sido enviado de manera automática, por favor, no responda a ésta dirección.

                        """ % (p_descripcion, p_ident_alumno, p_contrasena)

        # Enviamos el mail
        p = sub.Popen(("/bin/bash", "./scripts/sent_mail.sh", el_texto, p_email_alumno),
                      stdout=sub.PIPE, stderr=sub.PIPE)
        salidas_mail, errores_mail = p.communicate()
        if salidas_mail == "ok\n" and len(errores_mail) == 0:
            # Send OK
            enviado = True

        return enviado
