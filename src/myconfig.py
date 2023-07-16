# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Modulo de configuraciones
"""
from decouple import config


class Config:
    """
    Se usa para configurar Flask
    """
    SECRET_KEY  = config('SECRET_KEY')
    SERVER_NAME = config('SERVER_NAME')

    # Datos de Google
    GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
    GOOGLE_LOGIN_URI = config('GOOGLE_LOGIN_URI')


class DevelopmentConfig(Config):
    """
    Ereda de Config y se configura en modo de dearrollo
    """
    DEBUG = True

default_config = Config

if config('FASE').lower() == 'desarrollo':
    default_config = DevelopmentConfig

