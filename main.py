import PySimpleGUI as sg
from functions import make_archive

src_label = sg.Text('Select files to Compress')
src_input = sg.Input(key="src")
src_button = sg.FilesBrowse('Choose files')

des_label = sg.Text('Select destination folder')
des_input = sg.Input(key="des")
des_button = sg.FolderBrowse('Choose folder')

cmp_button = sg.Button('Compress')

output_message = sg.Text("", key="message", text_color="green", font=["helvetica", "20"])

window = sg.Window('Compress files', layout=[
    [src_label, src_input, src_button],
    [des_label, des_input, des_button],
    [cmp_button, output_message]
])

while True:
    event, values = window.read()
    files_path = values['Choose files'].split(";")
    folder_path = values['Choose folder']
    make_archive(filepaths=files_path, dir=folder_path)
    window["message"].update("Compress Successfully")


    match event:
        case sg.WINDOW_CLOSED:
            break

window.close()