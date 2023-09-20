import tkinter
import sys
import PySimpleGUI as sg

#Layout/Estrutura da Janela inicial
layout = [
    [sg.Text("Lista de Tarefas")],
    [sg.Listbox([], size=(40, 10), key="-LIST-")],
    [sg.Button("Nova Tarefa"), sg.Button("Sair")]
]
#Criar a janela
window = sg.Window("Gerenciador de Tarefas", layout)

#Lista para armazenar tarefa
tasks = []

#Captura de eventos
while True:
    event, values = window.read()

    # Se o usuário fechar a janela principal, saia do loop
    if event == sg.WIN_CLOSED or event == "Sair":
        break

    # Se o usuário clicar no botão "Nova Tarefa", abra a nova janela de tarefa
    if event == "Nova Tarefa":
        # Defina o layout da janela de tarefa
        task_layout = [
            [sg.Multiline('', size=(40, 10), key="task")],
            [sg.Button("Salvar"), sg.Button("Excluir")]
        ]

        # Crie a janela de tarefa
        task_window = sg.Window("Nova Tarefa", task_layout)

        while True:
            event, values = task_window.read()

            # Se o usuário fechar a janela de tarefa, saia do loop interno
            if event == sg.WIN_CLOSED:
                break

            # Se o usuário clicar em "Salvar", adicione a tarefa à lista e saia
            if event == "Salvar":
                task_text = values["task"]
                tasks.append(task_text)
                task_window.close()
                window["-LIST-"].update(values=tasks)
                break

            # Se o usuário clicar em "Excluir", saia da janela de tarefa
            if event == "Excluir":
                task_window.close()
# Feche a janela principal
window.close()
