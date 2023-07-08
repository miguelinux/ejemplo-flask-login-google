# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa de inicialización de la aplicación Flask.
"""

from flask import Flask

# Rutas
from .rutas import raiz
from .rutas import auth

app = Flask(__name__)

def init_app(config):
    """
    Inicializa la aplicación de Flask
    """
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(raiz.main, url_prefix='/')
    app.register_blueprint(auth.main, url_prefix='/auth')

    return app
