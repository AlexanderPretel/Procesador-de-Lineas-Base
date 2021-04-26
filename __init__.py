# -*- coding: utf-8 -*-
"""
/***************************************************************************
 processBaseLine
                                 A QGIS plugin
 Plugin que funciona como complemento al plugin Colector. Su función es procesar las líneas base de la información recolectada haciendo uso de RTKLIB tanto para convertir los archivos binarios creados a partir de la colección, como para realizar la corrección diferencial.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-04-18
        copyright            : (C) 2021 by Alexander Pretel Díaz
        email                : alexander.pretel@correounivalle.edu.co
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Alexander Pretel Díaz'
__date__ = '2021-04-18'
__copyright__ = '(C) 2021 by Alexander Pretel Díaz'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load processBaseLine class from file processBaseLine.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .process import processBaseLinePlugin
    return processBaseLinePlugin()
