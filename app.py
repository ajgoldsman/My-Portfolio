# -*- coding: utf-8 -*-
"""
@author: ajgoldsman
"""

from flask import Flask, render_template, request


server = Flask(__name__)
@server.route("/")
def compile():
    return render_template('index.html')


if __name__ == '__main__':
    server.run(debug=True, use_reloader=False, host='0.0.0.0')
