# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import Blueprint, request, redirect, render_template

main = Blueprint('raiz', __name__, template_folder='templates')

@main.route('/')
def raiz():
    return redirect('/login')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        return 'post'
    elif request.method == 'GET':
        return render_template('login.html')
    else:
        return 'Not a valid request method for this route'

