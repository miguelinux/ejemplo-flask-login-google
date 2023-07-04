#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

from myconfig import config
from myapp import init_app

configuration = config['development']
app = init_app(configuration)

if __name__ == '__main__':
    app.run()
