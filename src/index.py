#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Este es el programa principal o punto de entrada de la aplicación.
"""

from myconfig import default_config
from myapp import init_app

app = init_app(default_config)

if __name__ == '__main__':
    app.run()
