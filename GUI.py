import PySimpleGUI as sg


sg.theme('DarkBlue16')  
pw = ""
b64Img = b'iVBORw0KGgoAAAANSUhEUgAAAC8AAAAtCAYAAAA+7zKnAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAACxMAAAsTAQCanBgAAANpSURBVGhDzZlbSBVBGMd3SzO60wUigoqoh4goiiCIkkKiIBCV5Gh0ewgCK3qLKILo8hZIV+glo7weRUqyMIp8K8wKioiEgiyoh8IyUbxsv29nk3M8xzyXmfH84M/MN0fc/8x+Mzs76zrjSFVNeAXFLfQ8Qu9DxUWDlGMy3uZXUbxW0TC/0As03CFvKKuzJJRPNRor5sPhRqd/cEBGeTOa4Tc6zmPUh0aaj8dXFHl32vr7erqMm2d0Z1HcQIVIzHYj4QpqQImYH8kQajNqHuOTKVrRHFSGWsjnAUqfUdImUX5OCCqmOIaWoVxMN0ca14Ex8w0NkhHOPlSB6c8S6CZp89zqbHQB3UZLguYY+vqHsiiWojd+gwFSGfn96DgqRS10YL40xuLJfJL/rzVVIknF/KKgFGRkm+nATBXaRUfOr0aNVbX+ymIVHeaFXMdz7lTXhCcGsRV0mRcKPMe5yh2wtuVwydd5lDIJp/otY7MFbVTVuJydNiXnVHdPLwPjviI+ylL5RP0UDddO6yEl5p9S2aRibRzG8OWgPirpmpe0WavqWinHWHFQN4aYN5Gj8n8r6ECeCs2gc8KOJAfV04F1KtSPSfPCdHSfDixXoV5MmxdkNXtIBxaoUB82zAuLUVN1dZ3W69kyL6zxXHdhUNeCTfPtqFNV9WDL/Ee0kweXvHtqw4b572gbxuUEQCumzf9GOzD+QYV6MWlejjkKMC4HSEYQ8+xktSO5vQfjj1RoBjHfpqpaOYLx2qBuDNkSz6XcixLdz29F/9tCn3G9gdOOm+16jneN+BIdeat+ioZrp7efDyoJwwXPUZxQUQzXGY9DoeJC/q4um7rk/QHM31Q/R5OueZ0Tth6ViXFb6DIvr3mljHBC5+q60GH+JcrHuKSIVVIx/ykohQ60HePyQcA6yZt3HZl855F8jsnD+DdpjoXFRh31TfJDA5g+n5eV5BkdPKhaosmk1SYeLJ3ObkyuVKFeTI+8HP/dRevRSXQPdSFJqV4kncrMkQ+WzgIk86McfUHyTeoPuohSRTr/0tq5IndhNsUG9O9roHzVky1JMiP/DlWJGJgOa+bjkeCElVfHGlRJkreHdhX5jUKmmv+BZLtRSX60lozy+phJ5ntQE6pED0iLMZ/Y421evorLxBXDjRhO4kntOH8BhCoR5A1uBiEAAAAASUVORK5CYII='
path =r"C:\\Users\\rober\\PycharmProjects\\Password-Generator\\lock.png"

col = [[sg.Button("", image_data=b64Img, button_color=(sg.theme_background_color(), sg.theme_background_color()),
                  border_width=0, key='exitgen', tooltip="Exits the password generator")]]


generatorly = [[sg.Column(col, justification="right")],

             [sg.Text('Password Generator', pad=(0, 40), font="SegoeUI 35")],

             [sg.Text('Click on generate for a password!', font="SegoeUI 16")],

             [sg.Image(path),
              sg.InputText(justification="center", text_color="black",
                           disabled=True, font="SegoeUI 16", size=(16, 10), key="generatedPW"),
              sg.Button("Copy", tooltip="Copies the password to clipboard", key="copy",
                         border_width=0, font="SegoeUI 13")],

             [sg.Button('Generate', key="gen", border_width=0, font="SegoeUI 13")],

             [sg.Button("2", button_color=("#1c44ac", "#1c44ac"), border_width=0, key="btn2")]]

# Create the Window

genWindow = sg.Window('Password Generator', generatorly,size=(640, 480),
                      element_justification="center", keep_on_top=True,
                      no_titlebar=True, grab_anywhere=True, ttk_theme="DarkBlue16")


