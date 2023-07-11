# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import Blueprint, request, redirect, render_template
from google.oauth2 import id_token
from google.auth.transport import requests

main = Blueprint('raiz', __name__, template_folder='templates')

CLIENT_ID="880330157243-dt16tsgb3famlqsp149kt986cp59j6j9.apps.googleusercontent.com"
GSUITE_DOMAIN_NAME="zapopan.tecmm.edu.mx"

@main.route('/')
def raiz():
    return redirect('/login')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        str_return="Valor por default"
        try:
            token = request.form.get('credential')
            g_csrf_token = request.form.get('g_csrf_token')
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

            # If auth request is from a G Suite domain:
            if idinfo['hd'] != GSUITE_DOMAIN_NAME:
                raise ValueError('Wrong hosted domain.')

            userid = idinfo['sub']
            email = idinfo['email']
            name = idinfo['name']
            picture = idinfo['picture']
            given_name = idinfo['given_name']
            family_name = idinfo['family_name']

            str_return=f"""
            User ID: {userid}
            Email: {email}
            Name: {name}
            Picture: {picture}
            Given name: {given_name}
            Family name: {family_name}
            """


        except ValueError:
            str_return='Value Error'
        return str_return
    elif request.method == 'GET':
        return render_template('login.html')
    else:
        return 'Not a valid request method for this route'

@main.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        print(request.form)
        return 'post'
    elif request.method == 'GET':
        return render_template('test.html')
    else:
        return 'Not a valid request method for this route'
