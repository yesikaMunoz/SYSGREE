# Importar flask y otros metodos
from flask import Blueprint, render_template

menut = Blueprint("menut", __name__)

@menut.route("/menu")
def menu():
    return render_template("menus/menu.html")

@menut.route("/Entradas")
def Entradas():
    return render_template("menus/Entradas.html")

@menut.route("/Adicionales")
def Adicionales():
    return render_template("menus/Adicionales.html")

@menut.route("/bebidas")
def bebidas():
    return render_template("menus/bebidas.html")

@menut.route("/Infantil")
def Infantil():
    return render_template("menus/Infantil.html")

@menut.route("/Jugos")
def Jugos():
    return render_template("menus/Jugos.html")

@menut.route("/robalo")
def robalo():
    return render_template("menus/robalo.html")

@menut.route("/salmon")
def salmon():
    return render_template("menus/salmon.html")

@menut.route("/Truchas")
def Truchas():
    return render_template("menus/Truchas.html")

@menut.route("/Variedade")
def Variedade():
    return render_template("menus/Variedades.html")

@menut.route("/Variedades2")
def Variedades2():
    return render_template("menus/Variedades2.html")
