from pydoc import describe
import PySimpleGUI as sg
from PASSWORD import *

sg.theme("DarkBlack")

layout = [
    [sg.Text("Nome do serviço")],
    [sg.InputText(key= "-org-")],
    [sg.Text("Login utilizado")],
    [sg.InputText(key= "-login-")],
    [sg.Text("Quantidade de digitos"), sg.Radio("8", 1, default= True, key= "-R1-"),
    sg.Radio("12", 1,  key= "-R2-"),
    sg.Radio("16", 1, key= "-R3-")],
    [sg.OK(), sg.Exit()]
]

window = sg.Window("Gerador de senhas", layout)

user = getHost()
path_folder = (r"C:\Users\{usern}\Desktop").format( usern = user)

while True:
    event, values = window.read()
    print(event, values)
    

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    elif values["-R1-"] == True:

        password = Creat_pass(8)
        organization = values["-org-"]
        login = values["-login-"]
        file_checker = getTxt()

        txtfile = open(path_folder + "\passwords.txt", file_checker)

        with open(path_folder + "\passwords.txt" , file_checker) as f:
            f.write("{orga}\nLogin: {logintxt} \nSenha: {senhatxt}\n \n".format(orga = organization, senhatxt = password, logintxt = login))
        sg.Popup('Nova senha gerada!', keep_on_top=True)


    elif values["-R2-"] == True:

        password = Creat_pass(12)
        organization = values["-org-"]
        login = values["-login-"]

        txtfile = open(path_folder + "\passwords.txt", file_checker)

        with open(path_folder + "\passwords.txt" , file_checker) as f:
            f.write("{orga}\nLogin: {logintxt} \nSenha: {senhatxt}\n \n".format(orga = organization, senhatxt = password, logintxt = login))
        sg.Popup('Nova senha gerada!', keep_on_top=True)

    elif values["-R3-"] == True:

        password = Creat_pass(16)
        organization = values["-org-"]
        login = values["-login-"]

        txtfile = open(path_folder + "\passwords.txt", file_checker)

        with open(path_folder + "\passwords.txt" , file_checker) as f:
            f.write("{orga}\nLogin: {logintxt} \nSenha: {senhatxt}\n \n".format(orga = organization, senhatxt = password, logintxt = login))

        sg.Popup('Nova senha gerada!', keep_on_top=True)
