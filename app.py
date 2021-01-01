#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:40:23 2020

@author: ashish
"""
from flask import Flask, render_template
from tic_tac_toe import tic_tac_toe
from ping_ping import ping_pong
#from hangman import hangman

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')
    






if __name__=="__main__": 
    app.run(debug='False')