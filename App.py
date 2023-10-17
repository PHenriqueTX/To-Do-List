import tkinter
import sys
import PySimpleGUI as sg
import os

#Função de leitura das tarefas no arquivo
def read_tasks():
    tasks = []
    if os.path.exists("saved_tasks.txt"):
        with open("saved_tasks.txt","r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

#Função para escrever as tarefas no arquivo
def write_tasks():
    with open("saved_tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

#Layout/Estrutura da Janela inicial
layout = [
    [sg.Text("Lista de Tarefas")],
    [sg.Listbox([], size=(40, 10), key="-LIST-")],
    [sg.Button("Nova Tarefa"),sg.Button("Editar tarefa"),sg.Button("Excluir Tarefa"),sg.Button("Sair")]
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

    # Função do botão "Nova Tarefa"
    if event == "Nova Tarefa":
        # Defina o layout da janela de tarefa
        task_layout = [
            [sg.Multiline('', size=(40, 10), key="task")],
            [sg.Button("Salvar"), sg.Button("Excluir")]
        ]

        #  ---------------- Crie a janela de tarefa------------------
        task_window = sg.Window("Nova Tarefa", task_layout)

        while True:
            event_task, values_task = task_window.read()

            # Se o usuário fechar a janela de tarefa, saia do loop interno
            if event_task == sg.WIN_CLOSED or event_task == "Cancelar":
                break

            # Se o usuário clicar em "Salvar", adicione a tarefa à lista e saia
            if event_task == "Salvar":
                task_text = values_task["task"]
                tasks.append(task_text)
                task_window.close()
                task_display = [f"Tarefa {i + 1}: {task}" for i, task in enumerate(tasks)]
                window["-LIST-"].update(values=task_display)
                break

        task_window.close()

# Feche a janela principal
window.close()

#Função do botão "Editar Tarefa"
if event=="Editar Tarefa":
    selected_task_index=values["-LIST-"][0]
    if selected_task_index :
        selected_task_index = int(selected_task_index[0])
        task_layout= [
            [sg.Multiline(tasks[selected_task_index],size=(40,10), key="task")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]
        task_window=sg.Window("Editar Tarefa", task_layout)

        while True:
            event_task, values_tarefa=task_window.read()

            # Se o usuário fechar a janela de tarefa, saia do loop interno
            if event_task == sg.WIN_CLOSED or event_task == "Cancelar":
                break
            
            #"Salvar" atualaiza na lista
            if event_task == "Salvar":
                task_text=values_task["task"]
                tasks[selected_task_index]=task_text
                task_window.close()
                task_display = [f"Tarefa {i + 1}: {task}" for i, task in enumerate(tasks)]
                window["-LIST-"].update(values=task_display)
                break

        task_window.close()


#Adição da função Excluir Tarefa
if event=="Excluir Tarefa":
    selected_task_index=values["-LIST-"][0]
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        tasks.pop(selected_task_index)
        task_display = [f"Tarefa {i + 1}: {task}" for i, task in enumerate(tasks)]
        window["-LIST-"].update(values=task_display)

window.close()